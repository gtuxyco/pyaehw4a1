import pyaehw4a1
import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='pyaehw4a1',
    version=pyaehw4a1.__version__,
    description='Python interface for Hisense AEH-W4A1 module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bannhead/pyaehw4a1',
    author='Davide Varricchio',
    author_email='davide.varricchio@gmail.com',
    license='Apache 2.0',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Home Automation",
    ],
)

