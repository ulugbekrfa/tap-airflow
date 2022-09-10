#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-airflow",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["airflow"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "apache-airflow-client == 2.3.0",
        "backoff == 1.8.0",
        "ciso8601 == 2.2.0",
        "jsonschema == 2.6.0",
        "python-dateutil == 2.8.2",
        "pytz == 2022.2.1",
        "simplejson == 3.11.1",
        "singer-python == 5.12.2",
        "six == 1.16.0",
        "urllib3 == 1.26.12"
    ],
    entry_points="""
    [console_scripts]
    tap-airflow=airflow:main
    """,
    packages=["airflow"],
    package_data={
        "schemas": ["airflow/schemas/*.json"]
    },
    include_package_data=True,
)
