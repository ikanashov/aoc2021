#!/bin/bash

# Parse first command line argument or check all
if [ -n "$1" ]
then
  CHECK=$1/$1.py
else
  CHECK=day1/day1.py
fi

flake8 "${CHECK}"
pylint "${CHECK}"
pycodestyle "${CHECK}"
mypy "${CHECK}"

