import sys
import subprocess


def test_get_user_name():
    # Simulate user input
    sample_input = "5\n 0 1\n 1 2\n 2 3"
    result = subprocess.run(
        "python",
        "../../cs412_mingraphcoloring.exact.py",
        input=sample_input,
        text=True,
        capture_output=True,
    )
    answer = result.stdout

    assert answer == "whatedver"
