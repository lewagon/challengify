
from setuptools import setup, find_packages

import os

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name="challengify",
      version="0.3.0",
      description="Le Wagon challenge generator tool",
      packages=find_packages(),
      install_requires=requirements,
      scripts=[os.path.join("scripts", "challengify")])
