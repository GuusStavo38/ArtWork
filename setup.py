#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='ArtWork',
    # Follow the semantic versioning rules for your versioning. In short this means:
    # version='X.Y.Z' where:
    #   X = Major version. Increase this number if backwards incompatible changes are introduced.
    #   Y = Minor version. Increase this number if new features are added.
    #   Z = Patch version. Increase this number for every other (small) change.
    # You can find more information here:
    # https://www.python.org/dev/peps/pep-0440/#semantic-versioning
    #
    # If you want to test a package but not release it, then you can use development releases.
    # These are very useful (and recommended) if you make a small change while testing on a
    # remote machine for example. The development version works as follows:
    # version='X.Y.Z.devN' where:
    #   X,Y,Z are the same as earlier and are the UPCOMING release version
    #   N is an increasing number for every change.
    # For example, a pre-release for version 3.2.2 would be 3.2.2.dev1
    # Note that 3.2.2.dev1 < 3.2.2
    version='0.0.1',
    description='ArtWork is a package designed to scrape data from Catawiki and use this data for analytics and trading',
    author='guusvheijningen',
    author_email='gvanheijningen@crunchanalytics.be',
    url='https://github.com/GuusStavo38/ArtWork',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # For all version comparisons, look here:
        # https://www.python.org/dev/peps/pep-0440/#version-specifiers
    ],
    extras_require={
        # [OPTIONAL]
        # Sometimes you have dependencies that are not always required. If you for example need
        # flask for a webserver, but don't always need the webserver, you can add this here.
        # The example below installs flask along with the package if we run
        # $ pip3 install demo[webserver]
    },
    scripts=[
        # [OPTIONAL]
        # If you need executable scripts for your application, then you should place them in
        # the scripts/ folder and add them to this list here. You MUST add one of the following
        # lines as first line of your script in order to make it work:
        # #!/usr/bin/env python3
        # #!/usr/bin/python3
        # The first one is uses the local python3 and is recommended if you run your script in
        # virtual environments. The second one always uses the global python3 interpreter.
    ]
)
