from setuptools import setup, find_packages

setup(
    name='devops_toolkit_cli',
    version='0.1',
    packages=find_packages(),
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'devops-cli=cli.main:main',
        ],
    },
)

