import pytest


def test_selenium(launch_browser,closing_browser):
    launch_browser
    print("do TC")
    closing_browser
