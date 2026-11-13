"""Sample script to verify Python environment and HTTP requests."""

import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """Return a greeting string for the given name."""
    greeting = f"Hello, {who_to_greet}"
    return greeting


print(greet("World"))

r = requests.get("https://www.python.org", timeout=10)
print(r.status_code)
print(r.headers)
