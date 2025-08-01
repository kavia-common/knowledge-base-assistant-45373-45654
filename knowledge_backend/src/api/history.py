"""In-memory storage for query history and helper functions."""

from typing import List, Optional
from threading import Lock
from datetime import datetime
from .main import QueryHistoryItem

# Singleton pattern for history storage
class HistoryStore:
    """Thread-safe in-memory query/answer history store."""
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._history = []
        return cls._instance

    # PUBLIC_INTERFACE
    def get_history(self) -> List[QueryHistoryItem]:
        """Returns all history items in most-recent-first order."""
        return list(reversed(self._history))

    # PUBLIC_INTERFACE
    def add_entry(self, question: str, answer: str) -> QueryHistoryItem:
        """Add a new history entry."""
        item = QueryHistoryItem(
            question=question,
            answer=answer,
            timestamp=datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        )
        self._history.append(item)
        return item

    # PUBLIC_INTERFACE
    def search_history(self, query: Optional[str] = None) -> List[QueryHistoryItem]:
        """Search for history entries containing the query text."""
        if query is None or query.strip() == "":
            return self.get_history()
        q_lower = query.lower()
        return [h for h in self.get_history() if q_lower in h.question.lower() or q_lower in h.answer.lower()]

    # PUBLIC_INTERFACE
    def delete_entry(self, timestamp: str) -> bool:
        """Remove an entry by exact timestamp (returns True if deleted, False if not found)."""
        for i, h in enumerate(self._history):
            if h.timestamp == timestamp:
                del self._history[i]
                return True
        return False

    # PUBLIC_INTERFACE
    def clear(self):
        """Remove all history."""
        self._history.clear()


# Single global store
history_store = HistoryStore()
