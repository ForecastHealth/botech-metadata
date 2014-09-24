# -*- coding: utf-8 -*-

import pytest
from iso3166 import countries


def check_lookup(alpha2, matching_keys, missing_keys):
    for k in matching_keys:
        assert countries[k].alpha2 == alpha2
        assert countries.get(k).alpha2 == alpha2
        assert k in countries

    for k in missing_keys:
        with pytest.raises(KeyError):
            countries.get(k)

        with pytest.raises(KeyError):
            countries[k]

        assert countries.get(k, None) == None


def test_alpha2():
    check_lookup("US", ["us", "US"], ["zz"])


def test_alpha3():
    check_lookup("US", ["usa", "USA"], ["zzz"])


def test_name():
    check_lookup("US", ["united states", "United STates"], ["zzzzz"])


def test_numeric():
    check_lookup("US", [840, "840"], [111, "111"])


def test_data():
    assert len(list(countries)) > 0

    for country in countries:
        assert len(country.alpha2) == 2
        assert country.alpha2.upper() == country.alpha2

        assert len(country.alpha3) == 3
        assert country.alpha3.upper() == country.alpha3

        assert len(country.numeric) == 3
        assert country.numeric == ("%03d" % int(country.numeric))