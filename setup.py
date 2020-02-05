from setuptools import setup

setup(
    name='test_setup',
    packages=['test_setup'],
    include_package_data=True,
    install_requires=[
        "pandas",
        "jupyter"
    ]
)
