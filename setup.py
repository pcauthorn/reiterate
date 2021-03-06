import os
import pathlib

import pkg_resources
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [str(requirement).strip() for requirement in pkg_resources.parse_requirements(requirements_txt)
                        if not str(requirement).strip().startswith('#')]
print(find_packages('src'))
setup(
    name='devcache',
    version='1.0.2',
    author='Patrick Cauthorn',
    author_email='patrick.cauthorn@gmail.com',
    description='Provides caching decorator to help speedup development',
    license='MIT',
    url='https://github.com/pcauthorn/devcache',
    install_requires=install_requires,
    package_dir={'': str('src')},
    packages=find_packages('src'),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
