import pytest

from pyffect import Either, Some, NONE, Right, Left


def sendRight(value: Either[str, int]):
    assert value.isRight
    assert value.toOption == Some(5)


def sendLeft(value: Either[str, int]):
    assert value.isLeft
    assert value.toOption == NONE()


def test_either():
    with pytest.raises(TypeError):
        assert Either(5, "6")

    assert Right(5).isLeft is False
    assert Right(5).isRight is True
    assert Left("test").isLeft is True
    assert Left("test").isRight is False

    sendRight(Right(5))
    sendLeft(Left("5"))

    assert Right(5).rightValue == 5

    with pytest.raises(ValueError):
        assert Right(5).leftValue

    assert Left("test").leftValue == "test"

    with pytest.raises(ValueError):
        assert Left("test").rightValue

    assert Left("5") == Left("5")
    assert Left("5") != Left("6")
    assert Left("5") != Left(5)
    assert Left("5") != Right("5")
    assert Right("5") == Right("5")
    assert Right("5") != Right("6")
