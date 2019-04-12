from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib
import os
import sys

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of anthill-gaming requires Python {}.{}, but you're trying to
install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install anthill-gaming
This will install the latest version of anthill-gaming which works on your
version of Python.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)

# Warn if we are installing over top of an existing installation. This can
# cause issues where files that were deleted from a more recent anthill-gaming
# are still present in site-packages.
overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "anthill", "gaming"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


EXCLUDE_FROM_PACKAGES = [

]

setup(
    name='anthill.gaming',
    version='0.0.1a1',
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    url='https://github.com/0x55AAh/anthill_gaming',
    author='woland',
    author_email='wofkin@gmail.com',
    description='',
    long_description=read('README.rst'),
    license='BSD',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    scripts=[],
    entry_points={'console_scripts': [

    ]},
    namespace_packages=['anthill'],
    install_requires=[
        'anthill.framework',
        'anthill.platform',
        'anthill.admin',
        'anthill.apigw',
        'anthill.backup',
        'anthill.bot',
        'anthill.config',
        'anthill.discovery',
        'anthill.dlc',
        'anthill.environment',
        'anthill.event',
        'anthill.exec',
        'anthill.game-master',
        'anthill.game-controller',
        'anthill.leaderboard',
        'anthill.login',
        'anthill.media',
        'anthill.message',
        'anthill.moderation',
        'anthill.blog',
        'anthill.profile',
        'anthill.promo',
        'anthill.report',
        'anthill.social',
        'anthill.store',
    ],
    extras_require={

    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Anthill',
        'Framework :: Tornado',
        'Framework :: Tornado :: 5',
        'Framework :: Tornado :: 5.0',
        'Framework :: Tornado :: 5.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        # 'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={

    },
)

if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
You have just installed anthill-gaming over top of an existing
installation, without removing it first. Because of this,
your install may now include extraneous files from a
previous version that have since been removed from
anthill-gaming. This is known to cause a variety of problems.
You should manually remove the %(existing_path)s
directory and re-install anthill-gaming.
""" % {"existing_path": existing_path})
