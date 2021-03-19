from setuptools import setup, find_packages
from ngspicejson.config import VERSION


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='ngspice-json-cli',
    version=VERSION,
    packages=find_packages(),
    author='devkingsejong',
    author_email='devkingsejong@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
    ],
    keywords='ngspice python cli json tool bash circuit simulate',
    url='https://github.com/devkingsejong/ngspice-json-cli',
    description='Print NGSPICE result as JSON',
)
