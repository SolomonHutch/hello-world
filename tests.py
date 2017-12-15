"""Add tests for the program here.
1. Declare a test function,
2. then call it from all_tests.

You can upgrade to a module called 'nose' later."""


def test_env():
    import os
    assert hasattr(os, 'path'), 'Basic import error on os'


def all_tests():
    test_env()

if __name__ == '__main__':
    all_tests()