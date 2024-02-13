import re
from unittest import TestCase, skipIf, expectedFailure

from main import summarize, get_dict, SOME_NUMBER, multiply


class TestSummarize(TestCase):
    def test_2_positive_number(self):
        x1 = 10
        x2 = 20
        expected = 30
        res = summarize(x1, x2)
        # assert res == expected
        self.assertEqual(res, expected)

    def test_2_negative_number(self):
        x1 = -10
        x2 = -20
        expected = -30
        res = summarize(x1, x2)
        self.assertEqual(res, expected)

    def test_failed(self):
        x1 = 10
        x2 = 34
        expected = 45
        res = summarize(x1, x2)
        # assert res > expected
        self.assertGreater(res, expected)

    def test_error(self):
        x1 = 20
        x2 = "35"
        res = summarize(x1, x2)
        expected = 55
        self.assertEqual(res, expected)


class TestSomething(TestCase):
    def test_key_in(self):
        dict1 = get_dict()
        key1 = "name"
        self.assertIn(key1, dict1)

    def test_dict_value(self):
        value1 = "Ivan"
        dict1 = get_dict()
        value = dict1.get("name")
        self.assertEqual(value, value1)
        self.assertIn(value1, dict1.values())

    @skipIf(SOME_NUMBER > 35, "Too big value")
    def test_regex(self):
        date = "12-02-2024"
        date1 = "12.02.2024"
        pattern = r"\d{2}-\d{2}-\d{4}"
        self.assertRegex(date, pattern)
        self.assertNotRegex(date1, pattern)

    @expectedFailure
    def test_expected_failure(self):
        x1 = 10
        x2 = 30
        expected = 41
        res = summarize(x1, x2)
        self.assertEqual(res, expected)

    def test_not_equal(self):
        x1 = 10
        x2 = 30
        expected = 41
        res = summarize(x1, x2)
        self.assertNotEqual(res, expected)


import pytest


class TestWithPytest:
    def test_2_positive_numbers(self):
        x1 = 10
        x2 = 20
        expected = 30
        res = summarize(x1, x2)
        assert res == expected

    @pytest.mark.skipif(SOME_NUMBER > 35, reason='Too big value')
    def test_regex(self):
        date = "12-02-2024"
        date1 = "12.02.2024"
        pattern = r"\d{2}-\d{2}-\d{4}"
        res = re.match(pattern, date1)
        assert res

    @pytest.mark.xfail
    def test_failed(self):
        x1 = 10
        x2 = 20
        res = multiply(x1, x2)
        expected = 210
        assert res == expected

    @pytest.mark.parametrize(
        "x,y,expected",
        [
            (1, 2, 3),
            (-10, 4, -6),
            (-100, 1234, 1134),
            (63, 34, 97)
        ]
    )
    def test_parametrized(self, x, y, expected):
        res = summarize(x, y)
        assert res == expected
