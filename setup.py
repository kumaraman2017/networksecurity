from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirements = []
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line and line != '-e .':
                    requirements.append(line)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirements

setup(
    name='networksecurity',
    version='0.1.0',
    author='Aman Kumar',
    author_email='kumar.amann126@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
