from pyffect import Some, NONE


def test_bind_with_some_option():
    """Test bind with a Some option."""

    def bindable(value: str) -> str:
        return value.upper()

    # Create a Some option
    some_option = Some("hello")

    # Use bind and test that the result is Some("HELLO")
    result = some_option.bind(bindable)

    assert isinstance(result, Some)
    assert result.value == "HELLO"


def test_bind_with_none_option():
    """Test bind with a NONE option."""

    def bindable(value: str) -> str:
        return value.upper()

    # Create a NONE option
    none_option = NONE()

    # Use bind and test that the result is NONE()
    result = none_option.bind(bindable)

    assert isinstance(result, NONE)
