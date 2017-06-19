import os
from distutils.core import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='pdict', 
    version='1.0',
    packages=['pdict'],
    package_dir={'pdict' : '.'}, 
    author='Richard Penman',
    author_email='richard.penman@gmail.com',
    description='pdict has a dictionary like interface and a sqlite backend',
    long_description=read('README.rst'),
    url='https://bitbucket.org/richardpenman/pdict',
    license='lgpl',
)
