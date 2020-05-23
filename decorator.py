import functools

from lrucache import LRUCache


def _make_key(args, kwargs):
    key = args
    if kwargs:
        for item in kwargs.items():
            key += item
    return hash(key)


def lru_cache(capacity=10):
    if capacity < 1:
        raise ValueError('Capacity should be positive.')

    def _inner(func):
        cache = LRUCache(capacity=capacity)

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            key = _make_key(args, kwargs)
            try:
                return cache[key]
            except KeyError:
                result = func(*args, **kwargs)
                cache[key] = func(*args, **kwargs)
                return result

        return _wrapper

    return _inner
