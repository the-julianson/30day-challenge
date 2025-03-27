def count_fruits(fruits: list[str]) -> dict[str, int]:
    # if not fruits:
    #     return {}
    # no needed, collection of fruits already initializes to empty dict
    
    collection_of_fruits: dict[str, int] = {}
    for fruit in fruits:
        # if not fruit in collection_of_fruits:
        #     collection_of_fruits[fruit] = 0
        # collection_of_fruits[fruit] += 1
        # The line below is more readable and concise
        collection_of_fruits[fruit] = collection_of_fruits.get(fruit, 0) + 1

    
    return collection_of_fruits


def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}
    assert count_fruits(["apple"] * 1000 + ["banana"] * 1000 + ["cherry"] * 1000) == {"apple": 1000, "banana": 1000, "cherry": 1000}
    print("All tests passed!")


if __name__ == "__main__":
    main()
