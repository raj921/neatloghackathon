"""Download the pinned official release as data; never launch the external app."""
import hashlib
import shutil
import urllib.request
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ZIP_SHA='0573c46a7049c4def8a55a78edf6fe6202cae2ea6c8475da8cfc819408455ae9'
ASAR_SHA='fe9b4c89660ac3f1291707746f76b9b5850edda368a5e0250055687ab02ec767'
archive=ROOT/'.local/research/bruno-4.2.1.zip'
artifact=ROOT/'.local/research/bruno-4.2.1/app.asar'
def digest(path):
    with path.open('rb') as stream: return hashlib.file_digest(stream,'sha256').hexdigest()
if artifact.exists() and digest(artifact)==ASAR_SHA:
    print('Pinned reference already verified.')
else:
    archive.parent.mkdir(parents=True,exist_ok=True)
    if not archive.exists():
        temporary=archive.with_suffix('.download')
        with urllib.request.urlopen('https://github.com/usebruno/bruno/releases/download/v4.2.1/bruno_4.2.1_arm64_mac.zip',timeout=90) as source, temporary.open('wb') as output:
            shutil.copyfileobj(source,output)
        temporary.replace(archive)
    if digest(archive)!=ZIP_SHA: raise SystemExit('Reference ZIP digest differs. Remove it and investigate; no extraction performed.')
    artifact.parent.mkdir(parents=True,exist_ok=True)
    temporary=artifact.with_suffix('.extracting')
    with zipfile.ZipFile(archive) as z, z.open('Bruno.app/Contents/Resources/app.asar') as source, temporary.open('wb') as output:
        shutil.copyfileobj(source,output)
    if digest(temporary)!=ASAR_SHA:
        temporary.unlink();raise SystemExit('Reference ASAR digest differs; rejected.')
    temporary.replace(artifact)
    print('Pinned reference extracted and verified. The app was not launched.')
