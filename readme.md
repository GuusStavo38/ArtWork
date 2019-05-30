![Alt text](https://www.crunchanalytics.be/uploads/use-cases/CRUNCH_LOGO_RGB-2.png)

# ArtWork

<<< ADD DESCRIPTION >>>

## Installing / Getting started

### Initial Configuration

You need to configure access to the private repository of Crunch. 
Follow [this guide](https://crunchanalytics.atlassian.net/wiki/spaces/STT/pages/562200577/User+guide+for+the+private+PyPI) to get started.

### Installation

You can install the project using pip. 
The package is only supports Python3.5 and up.

```shell
$ pip3 install ArtWork
```

## Developing

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone git@github.com:GuusStavo38/ArtWork.git
cd ArtWork
python3 -m venv venv
source venv/bin/activate
pip3 install -e .
```

This clones the repository and installs all the required dependencies for development
in a virtual environment.

Always create a new branch when you make a change to your project. 
It's considered bad practice to push directly to master, because then there is
no way to ensure that master is always stable.

### Building / testing

Tests and builds are automatically run by Jenkins. 
Everytime you push a change to master or a pull request, Jenkins will be notified and 
run the tests for you.

It is of course also possible to run the tests locally.
That is what we will cover in this section. 
To make sure that the tests run for everyone, we use `tox`. 
This is a python framework that makes sure you have the correct build dependencies
and runs every test stage in a separate virtual environment. 
Make sure you have tox installed before continuing.

```shell
pip3 install tox
```

The following command runs mypy, pylint and pytest in sequence.

```shell
# Use the python version that you use on your system!
# If you use python3.5, then use py35. 
tox -e py36
```

> Important! For now, Jenkins only has support for python3.5. So if you want to 
rely on the functionality provided by Jenkins, then your code must be compatible
with python3.5.

### Deploying / Publishing

#### Publish development version

In a lot of cases, before you want to build a new version to PyPI, you want to test what you just created.
PyPI has support for _pre-releases_, which are development releases right before a new final release.
Please head to the 
[manual on PyPI on confluence](https://crunchanalytics.atlassian.net/wiki/spaces/STT/pages/562200577/User+guide+for+the+private+PyPI) 
for more information.

#### Publish final version
When everything works as expected you can instruct Jenkins to build a final version by creating a git tag.
Make sure that your setup.py file contains the same version as your git tag!
Keep the versioning practices in mind:
* Major version for backwards incompatible changes
* Minor version for new features
* Patch version for small changes and bug fixes

Release a new version by creating a tag and pushing it to bitbucket.
Jenkins will automatically detect this and build the package.
```shell
git tag <VERSION>
git push --tags
```

## Links

- Project homepage: https://github.com/GuusStavo38/ArtWork
- Repository: git@github.com:GuusStavo38/ArtWork.git


## Licensing

Copyright (C) Crunch Analytics, bvba - All Rights Reserved \
Unauthorized copying of this project, via any medium is strictly prohibited \
Proprietary and confidential \
Maintained by guusvheijningen <gvanheijningen@crunchanalytics.be>, 2018
