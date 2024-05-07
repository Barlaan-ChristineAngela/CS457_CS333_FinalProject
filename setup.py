from setuptools import setup, find_packages

setup(
    name='your-package',
    version='1.0',
    packages=find_packages(exclude=['tests', 'tests.*']) + ['thinc'],
)
