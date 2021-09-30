import pytest

from pyffect import Some, NONE, Option


def test_option():
    assert Some(7).isDefined is True
    assert Some(7).isEmpty is False
    assert NONE().isDefined is False
    assert NONE().isEmpty is True
    assert Some(6).value == 6
    with pytest.raises(ValueError):
        assert NONE().value

    assert Some(6).getOrElse(5) == 6
    assert NONE().getOrElse(5) == 5
    assert NONE().getOrElse(None) is None
    assert NONE() == NONE()
    assert NONE() != Some(6)
    assert Some(5) != Some(6)
    assert Some(5) == Some(5)
    assert Option.fromValue(5).isDefined
    assert Option.fromValue(None).isEmpty


