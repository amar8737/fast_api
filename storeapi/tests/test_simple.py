def test_simple():
    assert 1 + 1 == 2


def test_dict_contains_key():
    my_dict = {"key1": "value1", "key2": "value2"}

    expected = {
        "key1": "value1",
    }
    assert expected.items() <= my_dict.items()
