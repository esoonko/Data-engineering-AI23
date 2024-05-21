#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install dbt
pip freeze > requirements.txt
 
