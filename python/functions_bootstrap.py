"""Tiny helper to load a Python file as a module by path.

Used by the test suite so exercises live in plain files without
needing to be part of an installed package.
"""

import importlib.util
import sys
from pathlib import Path


def load_module(name: str, path: str):
    """Load a Python file at `path` as a module named `name`."""
    file_path = Path(path).resolve()
    if not file_path.exists():
        raise FileNotFoundError(file_path)

    spec = importlib.util.spec_from_file_location(name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
