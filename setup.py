from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except IOError as e:
    print(e)

test_requirements = [
    'tox',
]
