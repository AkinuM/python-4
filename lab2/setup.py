from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="serializer3",
    version="1.2",
    description="library for python serialization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkinuM/python-4/tree/master/lab2",
    author="Akinshev Dmitriy",
    author_email="avia65461323@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["serializers/json", "serializers/src", "serializers/toml", "serializers/yaml"],
    include_package_data=True
)
