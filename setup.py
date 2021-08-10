#!/usr/bin/env python

from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'avendesora-export',
    version = '0.0.0',
    author = 'Ken Kundert',
    author_email = 'avendesora-export@nurdletech.com',
    description = 'Exports Avendesora accounts to satellite hosts',
    long_description = readme,
    long_description_content_type = 'text/x-rst',
    url = 'https://github.com/kenkundert/avendesora-export',
    download_url = 'https://github.com/kenkundert/avendesora-export/tarball/master',
    license = 'GPLv3+',
    scripts = 'avendesora-export'.split(),
    install_requires = [
        'appdirs',
        'arrow',
        'avendesora>=1.21',
        'docopt',
        'inform>=1.25',
        'nestedtext>=3.0',
        'shlib',
        'python-gnupg>=0.4.4',
            # Be careful.  There's a package called 'gnupg' that's an 
            # incompatible fork of 'python-gnupg'.  If both are installed, the 
            # user will probably have compatibility issues.
    ],
    python_requires='>=3.6',
    keywords = 'avendesora export'.split(),
    classifiers = [
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
)
