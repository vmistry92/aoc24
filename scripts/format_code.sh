#!/bin/bash

pipenv run ruff check aoc24 tests --fix
pipenv run ruff format aoc24 tests
