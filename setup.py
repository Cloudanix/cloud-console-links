import setuptools

with open("README.md") as fh:
    long_description = fh.read()

# version of the module
__version__ = "1.0.25"


setuptools.setup(
    # Here is the module name.
    name="cloudconsolelink",
    # version of the module
    version=__version__,
    # Name of Maintainer
    maintainer="Cloudanix",
    # Maintainer Email address
    maintainer_email="ganesh@cloudanix.com",
    # Small Description about module
    description="Generate console links for cloud resources",
    long_description=long_description,
    # Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
    # Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Cloudanix/cloud-console-links",
    license="apache2",
    install_requires=[],
    packages=setuptools.find_packages(exclude=["tests*"]),
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
