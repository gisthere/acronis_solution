from lrucache import LRUCache


def test_adding_single_item_to_empty_cache():
    lru_cache = LRUCache(capacity=10)
    lru_cache[10] = 5
    assert list(lru_cache) == [(10, 5)]


def test_adding_multiple_items_to_empty_cache():
    lru_cache = LRUCache(capacity=10)
    lru_cache[20] = 5
    lru_cache[40] = 7
    assert list(lru_cache) == [(40, 7), (20, 5)]


def test_adding_single_item_to_full_cache():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 5
    lru_cache[40] = 7
    lru_cache[50] = 9
    assert list(lru_cache) == [(50, 9), (40, 7), (20, 5)]


def test_adding_multiple_items_to_full_cache():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 5
    lru_cache[40] = 7
    lru_cache[50] = 9
    lru_cache[60] = 11
    assert list(lru_cache) == [(60, 11), (50, 9), (40, 7)]


def test_getting_first_item_1():
    lru_cache = LRUCache(capacity=2)
    lru_cache[20] = 7
    lru_cache[40] = 9
    assert lru_cache[40] == 9
    assert list(lru_cache) == [(40, 9), (20, 7)]


def test_getting_first_item_2():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    assert lru_cache[40] == 9
    assert list(lru_cache) == [(40, 9), (20, 7), (10, 5)]


def test_getting_middle_item():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    assert lru_cache[20] == 7
    assert list(lru_cache) == [(20, 7), (40, 9), (10, 5)]


def test_getting_last_item_1():
    lru_cache = LRUCache(capacity=2)
    lru_cache[10] = 5
    lru_cache[40] = 9
    assert lru_cache[10] == 5
    assert list(lru_cache) == [(10, 5), (40, 9)]


def test_getting_last_item_2():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    assert lru_cache[10] == 5
    assert list(lru_cache) == [(10, 5), (40, 9), (20, 7)]


def test_getting_last_item_twice():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    assert lru_cache[10] == 5
    assert lru_cache[20] == 7
    assert list(lru_cache) == [(20, 7), (10, 5), (40, 9)]


def test_removing_item_from_cache():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    del lru_cache[10]
    assert list(lru_cache) == [(40, 9), (20, 7)]


def test_add_item_after_removing():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    del lru_cache[10]
    lru_cache[50] = 11
    assert list(lru_cache) == [(50, 11), (40, 9), (20, 7)]


def test_add_multiple_items_after_removing():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    del lru_cache[10]
    lru_cache[50] = 11
    lru_cache[60] = 13
    assert list(lru_cache) == [(60, 13), (50, 11), (40, 9)]


def test_updating_item():
    lru_cache = LRUCache(capacity=3)
    lru_cache[10] = 5
    lru_cache[20] = 7
    lru_cache[40] = 9
    lru_cache[20] = 10
    assert list(lru_cache) == [(20, 10), (40, 9), (10, 5)]
