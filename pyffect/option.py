
import warnings
from typing import Callable, Generic, Optional, final


from pyffect._types import T


class Option(Generic[T]):

    def __init__(self, value: T, *, _force: bool = False) -> None:
        if not _force:
            raise TypeError(
                'Cannot directly initialize, '
                'please either Some or NONE'
            )
        self._value = value
        self._type = type(self)

    @property
    def is_empty(self) -> bool:
        """The preferred property to check if the value is empty (None)."""
        return self._value is None

    @property
    def isEmpty(self) -> bool:
        """Deprecated. Use `is_empty` instead."""
        warnings.warn(
            "`isEmpty` is deprecated, use `is_empty` instead.",
            category=DeprecationWarning,
            stacklevel=2
        )
        return self.is_empty  # Alias to the new property

    @property
    def is_defined(self) -> bool:
        """The preferred property to check if the value is defined (not None)."""
        return self._value is not None

    @property
    def isDefined(self) -> bool:
        """Deprecated. Use `is_defined` instead."""
        warnings.warn(
            "`isDefined` is deprecated, use `is_defined` instead.",
            category=DeprecationWarning,
            stacklevel=2
        )
        return self.is_defined  # Alias to the new property

    @property
    def value(self) -> T:
        """The value of the option."""
        if self._value is None:
            raise ValueError('Value is NONE.')
        else:
            return self._value

    def get_or_else(self, value: T) -> T:
        """Return the value if defined, else return the provided default value."""
        if self._value is not None:
            return self._value
        else:
            return value

    def getOrElse(self, value: T) -> T:
        """Deprecated. Use `get_or_else` instead."""
        warnings.warn(
            "`getOrElse` is deprecated, use `get_or_else` instead.",
            category=DeprecationWarning,
            stacklevel=2
        )
        return self.get_or_else(value)  # Alias to the new method

    @classmethod
    def of(cls, val: Optional[T]) -> 'Option[T]':
        """Creates an Option from the given value."""
        return NONE() if val is None else Some(val)

    @classmethod
    def fromValue(cls, val: Optional[T]) -> 'Option[T]':
        warnings.warn(
            "`fromValue` is deprecated, use `of` instead.",
            category=DeprecationWarning,
            stacklevel=2
        )
        return NONE() if val is None else Some(val)

    def bind(self, bindable: Callable[[T], T]) -> 'Option[T]':
        """Applies a function to the value inside the option, if it is defined (not None). Returns a new Option containing the result, or NONE if the option is empty."""
        if self._value is not None:
            return self.of(bindable(self._value))
        return NONE()

    def map(self, f: Callable[[T], T]) -> 'Option[T]':
        """Transforms the value inside the Option using function `f`, and returns a new Option with the transformed value."""
        if self._value is not None:
            return self.of(f(self._value))
        return NONE()

    def flat_map(self, f: Callable[[T], 'Option[T]']) -> 'Option[T]':
        """Transforms the value inside the Option using function `f`, which must return an Option. Flattens the result."""
        if self._value is not None:
            return f(self._value)
        return NONE()

    def __eq__(self, other: T):  # type: ignore
        return isinstance(other, self._type) and self._value == other._value

@final
class NONE(Option):  # type: ignore

    def __init__(self) -> None:
        super().__init__(None, _force=True)

@final
class Some(Option[T]):
    def __init__(self, value: T) -> None:
        super().__init__(value, _force=True)
