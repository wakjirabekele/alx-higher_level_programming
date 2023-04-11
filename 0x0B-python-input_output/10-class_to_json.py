#!/usr/bin/python3
# 10-class_to_json.py
# wakjira Bekele <wakjirabekele2018@gmial.com>
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
