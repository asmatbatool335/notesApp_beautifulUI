#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f init_db.py ]; then python init_db.py; fi
