import pytest


def test_total_divisible_by_5(input_total):
    assert input_total % 5 == 0


def test_total_divisible_by_10(input_total):
    assert input_total % 10 == 0


def test_total_divisible_by_8(input_total):
    assert input_total % 8 == 0
