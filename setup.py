#!/usr/bin/env python3

import os
import gzip
from setuptools import setup

def gunzip_file(zip_file, out_file):
    ''' unzips files'''
    with gzip.open(zip_file, 'rb') as f_in:
        with open(out_file, 'wb') as f_out:
            f_out.writelines(f_in)

def setup_package():
    ''' setup declaration '''

    # Unzip LANL files
    resource_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'hivtrace/rsrc')
    lanl_zip = os.path.join(resource_dir, 'LANL.FASTA.gz')
    lanl_tn93output_zip = os.path.join(resource_dir, 'LANL.TN93OUTPUT.csv.gz')
    lanl_outfile = os.path.join(resource_dir, 'LANL.FASTA')
    lanl_tn93output_outfile = os.path.join(resource_dir, 'LANL.TN93OUTPUT.csv')

    gunzip_file(lanl_zip, lanl_outfile)
    gunzip_file(lanl_tn93output_zip, lanl_tn93output_outfile)

    setup(
        name='hivtrace',
        version='0.6.3',
        description='HIV-TRACE',
        author='Joel Wertheim, Sergei Pond, and Steven Weaver',
        author_email='sweaver@temple.edu',
        url='http://www.hivtrace.org',
        packages=['hivtrace'],
        package_data={
            'hivtrace': [
                'rsrc/LANL.FASTA.gz',
                'rsrc/LANL.TN93OUTPUT.csv.gz',
                'web/templates/results.html',
                'web/static/*.js',
                'web/static/*.css',
                'web/static/workers/*.js',
                'web/static/css/*.css',
                'web/static/fonts/*'
                ]
            },
        install_requires=[
            'biopython >= 1.58',
            'bioext @ https://github.com/FynnFreyer/BioExt/archive/c58951c3d57e714ae09d7abc450124bf3c7bbbae.zip#sha256=0baf4a91766dacd6b30dcf9a9ce85e989baa38f34c5589c6011a82a814052f31',
            'hppy >= 0.9.9',
            'tornado >= 4.3',
            'hivclustering @ https://github.com/FynnFreyer/hivclustering/archive/5477e7208d2ca8e65e4d0bd083a82f81deb0abda.zip#sha256=c2ea8cb45d17dbc1e778415c9877c3140fd954215b3cd595d9a64a881e46ac00',
            ],
        entry_points={
            'console_scripts': [
                'hivtrace = hivtrace.hivtrace:main',
                'hivtrace_strip_drams = hivtrace.strip_drams:main',
                'hivtrace_viz = hivtrace.hivtraceviz:main',
            ]
        },
        tests_require=[
            'nose'
        ]

    )

# Unzip LANL

if __name__ == '__main__':
    setup_package()

# Non-Python/non-PyPI plugin dependencies:
# tn93
