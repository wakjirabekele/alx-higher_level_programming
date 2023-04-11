#!/usr/bin/python3
# 8-load_from_json_file.py
# wakjira Bekele <wakjirabekele2018@gmial.com>
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
