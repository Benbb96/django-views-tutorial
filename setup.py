"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-views-tutorial',
    version='0.1.0',
    description='Function and class-based Django view repository.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/django-views-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='Django Views Tutorial',
    packages=find_packages(),
    install_requires=['Django',
                      'python-dotenv'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run = djangotutoial/__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/django-views-tutorial/issues',
        'Source': 'https://github.com/hackersandslackers/django-views-tutorial/',
    },
)
