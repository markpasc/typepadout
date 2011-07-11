from setuptools import setup

setup(
    name='typepadout',
    version='1.0',
    packages=[],
    include_package_data=True,
    scripts=['bin/typepadout'],

    requires=['termtool', 'typepad'],
    install_requires=['termtool', 'typepad'],
)
