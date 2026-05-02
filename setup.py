from pathlib import Path

import setuptools


ROOT = Path(__file__).parent


def read_text(path: str, *, required: bool = True) -> str:
    file_path = ROOT / path
    if not file_path.exists():
        if required:
            raise FileNotFoundError(file_path)
        return ""
    return file_path.read_text(encoding="utf-8")


def read_requirements(path: str) -> list[str]:
    lines = []
    for line in read_text(path, required=False).splitlines():
        requirement = line.strip()
        if requirement and not requirement.startswith("#"):
            lines.append(requirement)
    return lines


package_info: dict[str, object] = {}
exec(read_text("cloudconsolelink/__init__.py"), package_info)
long_description = read_text("README.md")
install_requires = read_requirements("requirements.txt")
dev_requirements = read_requirements("requirements-dev.txt")


setuptools.setup(
    # Here is the module name.
    name="cloudconsolelink",
    # version of the module
    version=str(package_info["__version__"]),
    # Name of Maintainer
    maintainer="Cloudanix",
    # Maintainer Email address
    maintainer_email="support@cloudanix.com",
    # Small Description about module
    description="Generate console links for cloud resources",
    long_description=long_description,
    # Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
    # Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Cloudanix/cloud-console-links",
    license="Apache-2.0",
    install_requires=install_requires,
    packages=setuptools.find_packages(exclude=["tests*"]),
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": dev_requirements,
    },
)
