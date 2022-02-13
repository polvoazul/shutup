import warnings
ORIGINAL_WARN = warnings.warn 
from shutup import *
import shutup


def are_warnings_working():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        warnings.warn("TEST")
        return len(w) == 1


def test_version():
    assert shutup.__version__

class TestWarnings():
    def setup_method(self, method):
        unmute_warnings()

    def test_mute_warnings(self):
        with mute_warnings:
            assert are_warnings_muted()
            assert not are_warnings_working()
        assert not are_warnings_muted()
        assert are_warnings_working()
        mute_warnings()
        assert not are_warnings_working()
        with unmute_warnings:
            assert not are_warnings_muted()
            assert are_warnings_working()

    def test_ctx_manager_respect_previous_state(self):
        mute_warnings()
        assert are_warnings_muted()
        with mute_warnings:
            assert are_warnings_muted()
        assert are_warnings_muted()
