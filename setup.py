from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requires = [
    'pandas==1.3.4',
    'pandas-stubs==1.2.0.39',  # for linting purposes nvim
]

testing = [
    'pytest==6.2.4',
    'pytest-cov==2.12.1',
]

linting_requires = ['pylint==2.4.4']

setup(
    name='Advent of code',
    version='0.0.1',
    install_requires=requires,
    testing_requires=testing,
    extras_require={'linting': linting_requires},
    description='For Fun!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
)
