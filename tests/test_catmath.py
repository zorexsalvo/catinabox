from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(1) == 5


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(-1) == -5


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2

def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2000) is True


def test__is_cat_leap_year__year_mod_4_not_equal_0():
    assert catmath.is_cat_leap_year(1757) is False


def test__is_cat_leap_year__year_mod_100_not_equal_0():
    assert catmath.is_cat_leap_year(2004) is True


def test__is_cat_leap_year__year_mod_400_not_equal_0():
    assert catmath.is_cat_leap_year(1900) is False
