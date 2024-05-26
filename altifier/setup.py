# setup.py

from setuptools import setup, find_packages

setup(
    name="altifier",
    version="0.1.0",
    packages=find_packages(),
    description="library to convert text to alty text",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="restriction policy happend",
    author_email="zaksteryt@gmail.com",
    url="https://github.com/sirscripter/altifier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
