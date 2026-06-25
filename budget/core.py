"""Core functions for the budget CLI app."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


Transaction = Dict[str, Any]


def add_transaction(transactions: List[Transaction], transaction: Transaction) -> List[Transaction]:
    """Add a transaction to the list and return the updated list."""
    transactions.append(transaction)
    return transactions


def get_balance(transactions: List[Transaction]) -> float:
    """Return the balance calculated from transactions."""
    pass


def filter_by_category(transactions: List[Transaction], category: str) -> List[Transaction]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(csv_path: Path) -> List[Transaction]:
    """Load transactions from a CSV file."""
    pass


def monthly_summary(transactions: List[Transaction]) -> Dict[str, Dict[str, int]]:
    """Return monthly income, expense, and net totals."""
    pass

