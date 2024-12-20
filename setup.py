from setuptools import find_packages, setup

setup(
    name="linear-python",
    version="0.2.2",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
        "strawberry-graphql>=0.138.0",
        "pydantic>=2.0.0",
        "typing-extensions>=4.5.0",
    ],
    author="Jourdan Bul-lalayao",
    description="A Python client for the Linear API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jpbullalayao/linear-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
