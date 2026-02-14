from setuptools import setup, find_packages

setup(
    name="safe_route_av",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "networkx",
        "ray[rllib]",
        "gymnasium",
        "pyyaml"
    ],
)
