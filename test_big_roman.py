import pytest
from funciones_romanos import de_arabigo_a_romano, de_romano_a_arabigo, to_groups, to_roman_tuples

@pytest.mark.parametrize(
    "number, roman_number",
    [
        (4000, "IV•"),
        (4000000, "IV••"),
        (4004000, "IV••IV•"),
        (4004004, "IV••IV•IV"),
        (3004004, "MMMIV•IV"),
        (3124568, "MMMCXXIV•DLXVIII"),
        (4000004, "IV••IV"),
        (int(6.024E23), "DCII•••••••CCCXCIX••••••CMXCIX•••••CMXCIX••••CMXCIX•••CMXCI••DCXI•CCCXCII")
    ]
)
def test_to_roman(number, roman_number):
    assert de_arabigo_a_romano(number) == roman_number

@pytest.mark.parametrize(
    "number, groups",
    [(4000, [4, 0]),
    (4000000, [4, 0, 0]),
    (4004000, [4, 4, 0]),
    (4004004, [4, 4, 4]),
    (3004004, [3004, 4]),
    (3124568, [3124, 568]),
    (int(6.024E23), [602, 399, 999, 999, 999, 991, 611, 392])]
)
def test_to_groups(number, groups):
    assert to_groups(number) == groups


@pytest.mark.parametrize(
    "roman_number, number",
    [
        ("IV•", 4000),
        ("IV••", 4000000),
        ("IV••IV•", 4004000),
        ("IV••IV•IV", 4004004),
        ("MMMIV•IV", 3004004),
        ("MMMCXXIV•DLXVIII", 3124568),
        ("IV••IV", 4000004),
        ("DCII•••••••CCCXCIX••••••CMXCIX•••••CMXCIX••••CMXCIX•••CMXCI••DCXI•CCCXCII", int(6.024E23))
    ]
)
def test_to_arabic(roman_number, number):
    assert de_romano_a_arabigo(roman_number) == number

@pytest.mark.parametrize(
    "roman_number, lista_romans",
    [
        ("IV•", [("IV", 1)]),
        ("IV••", [("IV", 2)]),
        ("IV••IV•", [("IV", 2), ("IV", 1)]),
        ("IV••IV•IV", [("IV", 2), ("IV", 1), ("IV", 0)]),
        ("MMMIV•IV", [("MMMIV", 1), ("IV", 0)]),
        ("MMMCXXIV•DLXVIII", [("MMMCXXIV", 1), ("DLXVIII", 0)]),
        ("IV••IV", [("IV", 2), ("IV", 0)]),
        #("DCII•••••••CCCXCIX••••••CMXCIX•••••CMXCIX••••CMXCIX•••CMXCI••DCXI•CCCXCII", int(6.024E23))
    ]
)
def test_to_roman_tuples(roman_number, lista_romans):
    assert to_roman_tuples(roman_number) == lista_romans