#!/bin/bash

VIRTUAL_ENV_PATH=".venv"

echo "Setup the Jupyter notebook environment"
if [ ! -d .venv  ]; then
	echo "- Install virtual env"
	python3 -m venv ${VIRTUAL_ENV_PATH}
else
	echo "- Use the existing virtual environment (${VIRTUAL_ENV_PATH})"
fi

echo "- Activate virtual environment"
source ${VIRTUAL_ENV_PATH}/bin/activate

echo "- Install require packages"
pip install -q --upgrade jupyter ipykernel

echo "- Launch Jupyter notebook"
jupyter notebook && deactivate

exit 0

