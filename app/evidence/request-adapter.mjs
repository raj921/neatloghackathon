// Bruno-compatible experimental adapter. Finite scope: see accompanying proof.
//
// MIT License
//
// Copyright (c) 2022 Anoop M D, Anusree P S and Contributors
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
function adapter(request, options = {}) {
  const cloneDeep = (o) => {
    if (Array.isArray(o)) return o.map(cloneDeep);
    if (o && typeof o === 'object') {
      const r = {};
      for (const k of Object.keys(o)) r[k] = cloneDeep(o[k]);
      return r;
    }
    return o;
  };
  const get = (obj, path) => {
    if (obj == null) return undefined;
    if (Object.prototype.hasOwnProperty.call(obj, path)) return obj[path];
    const parts = String(path).split('.');
    let cur = obj;
    for (const p of parts) {
      if (cur == null) return undefined;
      cur = cur[p];
    }
    return cur;
  };
  const replace = (str, obj, visited = new Set(), results = new Map()) => {
    let resultStr = str;
    let matchFound = true;
    while (matchFound) {
      const patternRegex = /\{\{([^}]+)\}\}/g;
      matchFound = false;
      resultStr = resultStr.replace(patternRegex, (match, placeholder) => {
        let replacement = get(obj, placeholder);
        if (typeof replacement === 'object' && replacement !== null) {
          replacement = JSON.stringify(replacement);
        }
        if (results.has(match)) return results.get(match);
        if (patternRegex.test(replacement) && !visited.has(match)) {
          visited.add(match);
          const result = replace(replacement, obj, visited, results);
          results.set(match, result);
          matchFound = true;
          return result;
        }
        visited.add(match);
        const result = replacement !== undefined ? replacement : match;
        results.set(match, result);
        matchFound = true;
        return result;
      });
    }
    return resultStr;
  };
  const interpolate = (str, obj) => {
    if (!str || typeof str !== 'string') return str;
    if (!obj || typeof obj !== 'object') return str;
    return replace(str, obj);
  };

  const envVariables = cloneDeep(options.envVars || {});
  const runtimeVariables = options.runtimeVariables || {};
  const processEnvVars = options.processEnvVars || {};
  const promptVariables = options.promptVariables || {};
  const secretVariables = options.secretVariables || {};

  const globalEnvironmentVariables = request?.globalEnvironmentVariables || {};
  const oauth2CredentialVariables = request?.oauth2CredentialVariables || {};
  const collectionVariables = request?.collectionVariables || {};
  const folderVariables = request?.folderVariables || {};
  const requestVariables = request?.requestVariables || {};
  const iterationData = request?.runnerIterationDetails?.iterationData || {};

  for (const key of Object.keys(envVariables)) {
    envVariables[key] = interpolate(envVariables[key], { process: { env: {} } });
  }

  const _interpolate = (str) => {
    if (!str || !str.length || typeof str !== 'string') return str;
    const combinedVars = {
      ...globalEnvironmentVariables,
      ...collectionVariables,
      ...envVariables,
      ...folderVariables,
      ...requestVariables,
      ...oauth2CredentialVariables,
      ...runtimeVariables,
      ...promptVariables,
      ...iterationData,
      process: { env: { ...processEnvVars } },
      ...secretVariables
    };
    return interpolate(str, combinedVars);
  };

  request.url = _interpolate(request.url);
  const isGrpcRequest = request.mode === 'grpc';

  if (request.headers) {
    for (const key of Object.keys(request.headers)) {
      const value = request.headers[key];
      delete request.headers[key];
      request.headers[_interpolate(key)] = _interpolate(value);
    }
  }
  if (request.apiKeyHeaderName) {
    request.apiKeyHeaderName = _interpolate(request.apiKeyHeaderName);
  }

  const getContentType = (headers = {}) => {
    let contentType = '';
    for (const key of Object.keys(headers)) {
      if (key && key.toLowerCase() === 'content-type') contentType = headers[key];
    }
    return contentType;
  };
  const contentType = getContentType(request.headers);
  const isGraphqlRequest = request.mode === 'graphql';

  if (isGrpcRequest && request.body) {
    const jsonDoc = JSON.stringify(request.body);
    const parsed = _interpolate(jsonDoc);
    request.body = JSON.parse(parsed);
  }
  const isWsRequest = request.mode === 'ws';
  if (isWsRequest && request.body && request.body.ws && Array.isArray(request.body.ws)) {
    request.body.ws.forEach((message) => {
      if (message && message.content) {
        message.content = _interpolate(message.content);
      }
    });
  }

  if (isGraphqlRequest && request.data && typeof request.data === 'object') {
    request.data.query = _interpolate(request.data.query);
    request.data.variables = _interpolate(request.data.variables);
  }

  if (typeof contentType === 'string' && !isGraphqlRequest) {
    if (contentType.includes('json')) {
      if (typeof request.data === 'string') {
        if (request.data.length) {
          request.data = _interpolate(request.data);
        }
      } else if (typeof request.data === 'object' && request.data !== null) {
        try {
          const jsonDoc = JSON.stringify(request.data);
          const parsed = _interpolate(jsonDoc);
          request.data = JSON.parse(parsed);
        } catch (err) {}
      }
    } else if (contentType === 'application/x-www-form-urlencoded') {
      if (request.data && Array.isArray(request.data)) {
        request.data = request.data.map((d) => ({ ...d, value: _interpolate(d?.value) }));
      }
    } else if (contentType.startsWith('multipart/')) {
      if (request?.data && typeof request.data === 'string') {
        request.data = _interpolate(request.data);
      } else if (Array.isArray(request?.data)) {
        try {
          request.data = request?.data?.map((d) => ({
            ...d,
            value: Array.isArray(d?.value) ? d.value.map((v) => _interpolate(v)) : _interpolate(d?.value)
          }));
        } catch (err) {}
      }
    } else {
      request.data = _interpolate(request.data);
    }
  }

  if (request.proxy) {
    request.proxy.protocol = _interpolate(request.proxy.protocol);
    request.proxy.hostname = _interpolate(request.proxy.hostname);
    request.proxy.port = _interpolate(request.proxy.port);
    if (request.proxy.auth) {
      request.proxy.auth.username = _interpolate(request.proxy.auth.username);
      request.proxy.auth.password = _interpolate(request.proxy.auth.password);
    }
  }

  if (request.basicAuth) {
    const username = _interpolate(request.basicAuth.username) || '';
    const password = _interpolate(request.basicAuth.password) || '';
    request.headers['Authorization'] = `Basic ${Buffer.from(`${username}:${password}`).toString('base64')}`;
    delete request.basicAuth;
  }

  if (request?.auth) delete request.auth;

  return request;
}

export { adapter };
