# Demo `pytest`

A few simple demos to display basic `pytest` concepts.

## Getting started

Install `pytest`:

    $ python3 -m venv venv
    $ . ./venv/bin/activate
    $ (venv) pip install pytest

Run tests:

    $ (venv) pytest
    $ (venv) pytest test_demo1.py
    $ (venv) pytest test_demo1.py::test_add
