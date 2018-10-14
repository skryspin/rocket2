#!/usr/bin/env bash
set -euxo pipefail
pipenv run pycodestyle .
pipenv run pydocstyle .
pipenv run markdownlint .
pipenv run pytest tests/
