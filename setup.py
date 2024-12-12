from setuptools import find_packages, setup

setup(
    name="linear-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "linear=linear_cli.commands:cli",
        ],
    },
)
