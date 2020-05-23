from unittest.mock import Mock

from decorator import lru_cache


def test_call_only_args():
    mock = Mock()
    f = lru_cache()(mock)
    f(1, 2, 3)
    mock.assert_called_with(1, 2, 3)


def test_call_only_kwargs():
    mock = Mock()
    f = lru_cache()(mock)
    f(a=1, b=2, c=3)
    mock.assert_called_with(a=1, b=2, c=3)


def test_call_arg_and_kwargs():
    mock = Mock()
    f = lru_cache()(mock)
    f(1, 2, 3, a=1, b=2, c=3)
    mock.assert_called_with(1, 2, 3, a=1, b=2, c=3)


def test_no_args_and_kwargs():
    mock = Mock()
    f = lru_cache()(mock)
    f()
    mock.assert_called_with()
