#!/bin/bash

# then run the app
python -m unittest discover -s ./Student_system -p "test_Student.py"

python -m unittest discover -s ./Inventory_system -p "test_Inventory.py"
