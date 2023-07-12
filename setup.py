from setuptools import setup
import numpy

# everything you would need to run your module to run your code goes in here
# import numpy as np ... etc


# write some kind of script to install any requirements to run our package

# once you run your setup script, the expectation is to be able to run the package


def get_requires():
    reqs = []
    for line in open("requirements.txt", "r").readlines():
        reqs.append(line)
    return reqs


setup(
    name="planet-guts",
    description="a triple threat code",
    author="",
    author_email="",
    include_package_data=True,
    zip_safe=False,
    keywords="Live Love Laugh",
    install_requires=get_requires(),
)