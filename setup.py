from setuptools import setup, find_packages

setup(
    name='twelfe',
    version=0.2,
    description=('A simple ELF file parser'),
    author='G-Nils',
    url='https://github.com/G-Nils/twelfe',
    packages=["twelfe"],
    python_requires='>=3.5.0',
    install_requires=['argparse'],
)
