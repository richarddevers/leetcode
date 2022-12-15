def reverse_string(input: str):
    return input[::-1]


def test_reverse_string() -> None:
    data = "abc"
    expected = "cba"

    result = reverse_string(
        input=data,
    )

    assert result == expected
