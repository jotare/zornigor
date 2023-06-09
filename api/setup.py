from typing import List

from setuptools import find_packages, setup

VERSION = open("VERSION").read().strip()


def read_requirements(path: str) -> List[str]:
    with open(path) as reqs:
        return [line.strip() for line in reqs]


setup(
    name="zornigor",
    version=VERSION,
    author="jotare",
    license="AGPLv3",
    install_requires=read_requirements("requirements.txt"),
    test_require=read_requirements("requirements-test.txt"),
    packages=find_packages(include=["zornigor"]),
    entry_points={
        "console_scripts": [
            "zornigor-api = zornigor.run:run",
            "zornigor-dev-api = zornigor.run:run_dev",
        ]
    },
)
