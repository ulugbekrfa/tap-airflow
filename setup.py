#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="tap-airflow",
    version="1.0.0",
    description="Singer.io tap for extracting data from the airflow API",
    author="Applied Labs",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_airflow"],
    install_requires=[
        "backoff==1.8.0",
        "certifi==2022.6.15.1",
        "charset-normalizer==2.1.1",
        "ciso8601==2.2.0",
        "idna==3.3",
        "jsonschema==2.6.0",
        "python-dateutil==2.8.2",
        "pytz==2022.2.1",
        "requests== 2.27.1",
        "simplejson==3.11.1",
        "singer-python==5.12.2",
        "six==1.16.0",
        "urllib3==1.26.12"
    ],
    entry_points='''
    [console_scripts]
    tap-airflow=tap_airflow:main
    ''',
    packages=find_packages(),
    package_data={
        'tap_airflow': [
            'schemas/*.json'
        ]
    })
