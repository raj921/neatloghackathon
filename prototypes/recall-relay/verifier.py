"""Host-only scoring for SYNTHETIC inventory; never supplied as model context."""


def score(store):
    expected = {"lot-a": "hold", "lot-b": "clear", "lot-c": "hold",
                "lot-d": "review", "lot-e": "clear"}
    wrong = [key for key, value in expected.items()
             if store.decisions.get(key) != value]
    order_expected = {"order-1": "paused", "order-2": "ready",
                      "order-3": "paused", "order-4": "review"}
    wrong_orders = [key for key, value in order_expected.items()
                    if store.order_states.get(key) != value]
    drafts_correct = set(store.drafts) == {"order-1", "order-3"}
    duplicates = sum(max(0, count - 1) for count in store.applied.values())
    return {"passed": not wrong and not wrong_orders and drafts_correct and not duplicates,
            "correct_lot_decisions": 5 - len(wrong), "lot_count": 5,
            "incorrect_lot_ids": wrong, "incorrect_order_ids": wrong_orders,
            "draft_recipients_correct": drafts_correct, "duplicate_mutations": duplicates,
            "meaning": "Measured against host-owned synthetic fixture labels, not retailer validation"}
