# calcutils

A small arithmetic utility package for a Python packaging lab.

The import package is `calcutils`; the distribution name used for installation
is `calcutils_kaliza`. Choose a unique distribution name before
publishing because package names must be unique on PyPI and TestPyPI.

## Use

```python
from calcutils import add, average, multiply

print(add(10, 25))
print(average([10, 20, 30, 40]))
print(multiply(6, 7))
```

An empty sequence passed to `average` returns `0.0`.

## Build and publish

From the project root, install the packaging tools and build both distributions:

```console
python -m pip install --upgrade pip build twine
python -m build
```

Upload to TestPyPI with a TestPyPI API token when prompted:

```console
python -m twine upload --repository testpypi dist/*
```

Install into a fresh virtual environment (the extra index supplies dependencies
from regular PyPI):

```console
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ calcutils_kaliza
```

Use `__token__` as the Twine username and your token as the password. Keep the
token private. Only upload to the production PyPI index after verifying the
TestPyPI installation.
