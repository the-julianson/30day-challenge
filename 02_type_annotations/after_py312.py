"""
Since Python 3.12 the syntax for generics has been improved. This is a version of the solution using the new syntax.
Based on a solution provided by Stefan Hilker.
"""

from collections.abc import Callable, Iterable, Sized


def filter_odd_numbers(numbers: Iterable[int]) -> list[int]:
    """Filters odd numbers from a sequence of numbers."""
    result: list[int] = [num for num in numbers if num % 2 == 0]
    return result


def square_numbers(numbers: Iterable[int | float]) -> list[float]:
    """Square numbers in a sequence."""
    result: list[float] = [num**2 for num in numbers]
    return result


def count_elements(words: Iterable[Sized]) -> list[int]:
    """Counts the number of elements in an iterable of words."""
    result: list[int] = [len(word) for word in words]
    return result


type FilterFunc[T] = Callable[[T], T]
type ProcessFunc[T, V] = Callable[[T], V]


def process_data[T, V](
    data: T,
    filter_func: FilterFunc[T] | None = None,
    process_func: ProcessFunc[T, V] | None = None,
) -> T | V:
    """Applies filter_func and process_func on a data sequence."""
    if filter_func:
        data = filter_func(data)
    if process_func:
        return process_func(data)
    return data


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = process_data(numbers, filter_odd_numbers, process_func=square_numbers)
    print(result)

    words = ["apple", "banana", "cherry"]
    result2 = process_data(words, process_func=count_elements)
    print(result2)


if __name__ == "__main__":
    main()
