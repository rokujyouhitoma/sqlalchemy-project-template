def test_import():
    from settings import (default, test)
    assert default
    assert test
