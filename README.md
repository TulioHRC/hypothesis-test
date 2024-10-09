# hypothesis-test

Testing hypothesis python library, for property-based testing.

### How to run it?

Installing requirements:

```bash
pip install pytest
pip install hypothesis
```

Running the tests:

```bash
pytest test.py
```

### Parallel test running (pytest feature)

To run all test files in parallel you can use:

```bash
pip install pytest-xdist
pytest -n auto -v
```
