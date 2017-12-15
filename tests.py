"""Add tests for the program here.
1. Declare a test function,
2. then call it from all_tests.

You can upgrade to a module called 'nose' later."""
from storyteller_base import Location, Direction, add_location, game_map, start_location


def test_env():
    import os
    assert hasattr(os, 'path'), 'Basic import error on os'


def test_create_objects():
    s = Location('a place',)
    north = Direction('go north', s)
    assert isinstance(north.destination, Location)


def test_add_location():
    desc = "The pond is very wet."
    add_location(start_location, 'jump', desc, "Swim to shore")
    assert desc in game_map
    new_loc = game_map[desc]
    assert "Swim to shore" in new_loc.exits


def all_tests():
    test_env()
    test_create_objects()
    test_add_location()
    print("All tests pass")


if __name__ == '__main__':
    all_tests()
