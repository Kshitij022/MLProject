from setuptools import find_packages, setup

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Kshitij',
    author_email = 'kshitij9839@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)