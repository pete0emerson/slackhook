import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "slackhook",
    version = "0.1.0",
    author = "Pete Emerson",
    author_email = "pete@theemersons.org",
    description = ("A Slack module and CLI"),
    license = "MIT",
    keywords = "slack module API",
    url = "https://github.com/pete0emerson/slackhook",
    scripts=['bin/slackhook'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
    ],
)
