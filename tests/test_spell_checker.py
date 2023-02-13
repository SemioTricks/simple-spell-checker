import pytest

from simple_spell_checker import SpellChecker

cities = [
    "Kyiv",
    "Kharkiv",
    "Odesa",
    "Dnipro",
    "Donetsk",
    "Zaporizhzhia",
    "Lviv",
    "Kryvyi Rih",
    "Mykolaiv",
    "Luhansk",
    "Vinnytsia",
    "Simferopol",
    "Chernihiv",
    "Kherson",
    "Poltava",
    "Khmelnytskyi",
    "Cherkasy",
    "Chernivtsi",
    "Zhytomyr",
    "Sumy",
    "Rivne",
    "Ivano-Frankivsk",
    "Ternopil",
    "Kropyvnytskyi",
    "Lutsk",
    "Uzhhorod",
]


def test_correct_word():
    spell_checker = SpellChecker(max_corrections_relative=0.5)
    spell_checker.add_words(cities)

    R = spell_checker.correction("Kharkiv")
    assert len(R) == 1
    assert len(R[0]["corrections"]) == 0
    assert R[0]["word"] == "Kharkiv"


def test_non_correct_words():
    spell_checker = SpellChecker(max_corrections_relative=0.5)
    spell_checker.add_words(cities)

    R = spell_checker.correction("odessa")
    assert len(R) == 1
    assert len(R[0]["corrections"]) == 2
    assert R[0]["word"] == "Odesa"

    R = spell_checker.correction("Hmelnitskiy", max_corrections_relative=0.5)
    assert len(R[0]["corrections"]) == 4
    assert R[0]["word"] == "Khmelnytskyi"


def test_unknown_word():
    spell_checker = SpellChecker(max_corrections_relative=0.5)
    spell_checker.add_words(cities)

    R = spell_checker.correction("new-york")
    assert len(R) == 0


def test_incorrect_type():
    spell_checker = SpellChecker(max_corrections_relative=0.5)
    with pytest.raises(TypeError):
        spell_checker.add_words(["one", "two", 3])


def test_incorrect_value():
    spell_checker = SpellChecker(max_corrections_relative=0.5)
    with pytest.raises(ValueError):
        spell_checker.add_words(["one", "two", ""])
