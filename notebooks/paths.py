"""
Adds source code folder to PYTHONPATH, so imports can be made from notebooks.
"""

import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[1] / 'src'))
