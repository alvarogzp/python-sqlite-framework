from setuptools import setup, find_packages

from sqlite_framework import project_info

setup(
    name=project_info.name,

    use_scm_version=True,

    description=project_info.description,

    url=project_info.url,

    author=project_info.author_name,
    author_email=project_info.author_email,

    license=project_info.license_name,

    packages=find_packages(exclude=["sqlite_framework_test*"]),

    setup_requires=[
        'setuptools_scm'
    ],

    install_requires=[
        'sqlite3',
    ],

    python_requires='>=3',
)
