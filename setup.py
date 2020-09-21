from setuptools import find_packages, setup

setup(
    name='flaskr',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
