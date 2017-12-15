"""Add tests for the program here.
1. Declare a test function,
2. then call it from all_tests.

You can upgrade to a module called 'nose' later."""
from storyteller_base import Location, Direction, add_location, game_map


def test_env():
    import os
    assert hasattr(os, 'path'), 'Basic import error on os'


def test_create_objects():
    s = Location('a place', 'a test')
    north = Direction('go north', s)
    assert isinstance(north.destination, Location)


def test_add_location():
    add_location(game_map['start'], 'jump', 'pond', "It's very wet.", "Swim to shore")
    assert 'pond' in game_map
    assert "Swim to shore" in game_map['pond'].exits


def all_tests():
    test_env()
    test_create_objects()
    test_add_location()


if __name__ == '__main__':
    all_tests()
    print("All tests pass")