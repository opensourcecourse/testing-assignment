"""
Task for learning pytest marks and a few command line arguments.
"""
import time

import pytest


def test_mark_xfail():
    """Mark this test as expected to fail."""
    assert 0


def test_mark_skip():
    """Mark this test as skipped."""
    assert 0


def test_mark_long_running():
    """Apply a 'long_running' mark to this test."""
    time.sleep(10)
    assert 1
