#!/usr/bin/python3
"""
Module that handles the initialization of the models package.
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
