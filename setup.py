from distutils.core import setup

setup(
    name='square',
    version='0.1.0',
    author='Fran Aguila',
    author_email='francescaaguila@gmail.com',
    packages=['square'],
    scripts=['square/utils.py'],
    url='https://github.ubc.ca/fhaguila/DSCI_524-square-python',
    license='LICENSE.txt',
    description='Get the area of a square',
    long_description=open('README.txt').read(),
    install_requires=[],
)
