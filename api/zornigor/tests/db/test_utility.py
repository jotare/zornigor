from unittest.mock import Mock

import pytest

from zornigor.db.utility import get_database, set_database


def test_get_unset_utility():
    assert get_database() is None


def test_get_unset_utility_strict():
    with pytest.raises(ValueError):
        get_database(strict=True)


def test_set_utility():
    db = Mock()
    set_database(db)
    assert get_database() == db


def test_set_utility_twice():
    db = Mock()
    set_database(db)
    assert get_database() == db

    with pytest.raises(ValueError):
        set_database(db)


def test_set_utility_twice_force():
    db1 = Mock()
    set_database(db1)
    assert get_database() == db1

    db2 = Mock()
    set_database(db2, force=True)
    assert get_database() == db2
