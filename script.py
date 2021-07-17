import os
import re
from typing import List
from scripts import Script

path = os.path.join(os.getcwd(), 'scripts')
module_paths: List[str] = []
for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
        file = os.path.join(dirname, filename)
        module_paths.append(file)

module_paths = [m for m in module_paths if re.match(r'.*\.py$', m)]
module_paths = [m for m in module_paths if not m.__contains__('__pycache__')]
module_paths = [m for m in module_paths if m != __file__]
module_paths = [m.replace(path, '') for m in module_paths]
module_paths = [m.replace(os.path.sep, '.') for m in module_paths]
module_paths = [m.replace('.__init__.py', '') for m in module_paths]
module_paths = [re.sub(r'^\.', '', m) for m in module_paths]
module_paths = [re.sub(r'\.py$', '', m) for m in module_paths]
module_paths = [m for m in module_paths if m != '']
module_paths = [f"scripts.{m}" for m in module_paths]

if __name__ == '__main__':
    for m in module_paths:
        __import__(m)
    Script.start()
