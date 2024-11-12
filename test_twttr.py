from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_shorten_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_uppercase():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_shorten_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"

def test_shorten_with_numbers_and_punctuation():
    assert shorten("H3LL0, W0RLD!") == "H3LL0, W0RLD!"
    assert shorten("twttr123!") == "twttr123!"

def test_shorten_with_spaces():
    assert shorten("   ") == "   "

def test_shorten_empty_string():
    assert shorten("") == ""
