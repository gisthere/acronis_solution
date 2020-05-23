from collections.abc import MutableMapping
from dataclasses import dataclass
from typing import Optional, Any, Hashable, Dict


@dataclass
class _CacheEntry:
    """
    Entry of cache represented by doubly linked list.
    """
    prev: Optional['_CacheEntry']
    next: Optional['_CacheEntry']
    key: Hashable
    value: Any


class LRUCache(MutableMapping):
    """
    Least recently used cache implementation.
    """
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError('Capacity should be positive.')

        self._capacity = capacity

        self._cache = {}  # type: Dict[Hashable, _CacheEntry]
        self._head = None  # type: Optional[_CacheEntry]
        self._tail = None  # type: Optional[_CacheEntry]

    def __setitem__(self, key, value):
        cache_entry = self._cache.get(key)
        if cache_entry:
            cache_entry.value = value
            self._move_to_front(cache_entry)
            return

        if self._is_capacity_exceeded():
            self._remove_from_tail()

        cache_entry = _CacheEntry(prev=None, next=None, key=key, value=value)
        self._append_to_front(cache_entry)

    def __delitem__(self, key):
        cache_entry = self._cache[key]
        self._remove(cache_entry)

    def __getitem__(self, key):
        cache_entry = self._cache[key]
        self._move_to_front(cache_entry)
        return cache_entry.value

    def __len__(self):
        return len(self._cache)

    def __iter__(self):
        cache_entry = self._head
        while cache_entry:
            yield cache_entry.key, cache_entry.value
            cache_entry = cache_entry.next

    def _move_to_front(self, cache_entry):
        if cache_entry == self._head:
            return

        if cache_entry == self._tail:
            self._tail = cache_entry.prev
            self._tail.next = None
        else:
            cache_entry.next.prev = cache_entry.prev

        cache_entry.prev.next = cache_entry.next

        cache_entry.prev = None
        cache_entry.next = self._head
        self._head.prev = cache_entry
        self._head = cache_entry

    def _is_capacity_exceeded(self):
        return len(self._cache) >= self._capacity

    def _remove_from_tail(self):
        assert len(self._cache) > 0

        cache_entry = self._tail

        if cache_entry == self._head:
            self._head = None
            self._tail = None
        else:
            cache_entry.prev.next = None
            self._tail = cache_entry.prev

        del self._cache[cache_entry.key]

    def _remove(self, cache_entry):
        if cache_entry == self._head:
            self._head = cache_entry.next
            self._head.prev = None

        if cache_entry == self._tail:
            self._tail = cache_entry.prev
            self._tail.next = None

        if cache_entry != self._head and cache_entry != self._tail:
            cache_entry.prev.next = cache_entry.next

        cache_entry.prev = None
        cache_entry.next = None
        del self._cache[cache_entry.key]

    def _append_to_front(self, cache_entry):
        if len(self._cache) == 0:
            self._head = cache_entry
            self._tail = self._head
        else:
            self._head.prev = cache_entry
            cache_entry.next = self._head
            self._head = cache_entry

        self._cache[cache_entry.key] = cache_entry
