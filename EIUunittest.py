"""
MAT 2170: support functions for unit testing
"""

def assertEquals(expected, yours):
    if expected != yours:
        message = 'unit testing: expected ' + \
                  str(expected) + ", but instead got " + \
                  str(yours)
        raise AssertionError(message)


def assertTrue(received):
    if not received:
        message = 'unit testing: expected True, but got False'
        raise AssertionError(message)


def assertFalse(received):
    if received:
        message = 'unit testing: expected False, but got True'
        raise AssertionError(message)