from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='FinanceAPI',
    version=version,
    description='Script to extract data against Yahoo! Finance India',
    author='Nar Kumar Chhantyal',
    author_email='neokya@gmail.com',
    url='https://github.com/neokya/FinanceAPI',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)