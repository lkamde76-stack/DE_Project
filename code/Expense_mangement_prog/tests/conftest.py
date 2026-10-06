import os
import sys

project_root = os.path.join(os.path.dirname(__file__),'..')
sys.path.insert(0,project_root)
print("System path",sys.path)
print("___root_path__",project_root)