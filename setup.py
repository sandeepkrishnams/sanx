from setuptools import find_packages, setup

setup(
    name="sanx",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.13",
    install_requires=[], 
    author="Your Name",
    description="A minimal example server for testing purposes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sandeepkrishnams/sanx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
