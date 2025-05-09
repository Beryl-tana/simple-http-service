#!/bin/bash

# Check for Python 3 and virtualenv
python3 --version || exit 1
virtualenv --version || exit 1

# Set up virtual environment
python3 -m venv venv && source venv/bin/activate

# Install requirments
pip install -r requirments.txt

# Launch the service
nohup python app.py > service.log 2>&1 &
