from setuptools import setup, find_packages

setup(
    name='twelfe',
    version=0.1,
    description=('A simple ELF file parser'),
    author='G-Nils',
    url='https://github.com/G-Nils/twelfe',
    packages=find_packages(),
    # packages=["twelfe"],
    python_requires='>=3.5.0',
    install_requires=['argparse'],
)
