"""Tests for budget.core."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    transactions = []
    transaction = {
        "date": "2026-06-25",
        "type": "expense",
        "category": "Food",
        "description": "Lunch",
        "amount": -12000,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 1

