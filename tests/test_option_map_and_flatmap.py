import pytest

from pyffect import Some, NONE


# Test the `Some` class and methods
def test_some_map():
    some_value = Some(5)

    # Test that `map` transforms the value
    result = some_value.map(lambda x: x * 2)
    assert result.is_defined
    assert result.value == 10


def test_some_map_none():
    none_value = NONE()

    # Test that `map` on `NONE` returns `NONE`
    result = none_value.map(lambda x: x * 2)
    assert result.is_empty


def test_some_flatMap():
    some_value = Some(5)

    # Test that `flatMap` transforms the value and returns a new Option
    result = some_value.flat_map(lambda x: Some(x * 3))
    assert result.is_defined
    assert result.value == 15


def test_some_flatMap_none():
    none_value = NONE()

    # Test that `flatMap` on `NONE` returns `NONE`
    result = none_value.flat_map(lambda x: Some(x * 3))
    assert result.is_empty


# Test the `NONE` class and methods
def test_none_map():
    none_value = NONE()

    # Test that `map` on `NONE` returns `NONE`
    result = none_value.map(lambda x: x * 2)
    assert result.is_empty


def test_none_flatMap():
    none_value = NONE()

    # Test that `flatMap` on `NONE` returns `NONE`
    result = none_value.flat_map(lambda x: Some(x * 2))
    assert result.is_empty


