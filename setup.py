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
            'bioext  @ https://github.com/FynnFreyer/BioExt/archive/bd9f4c8d1298651943be6b9679385f1829b4a65d.zip#sha256=1d4232556e010a5c5de94617fd006ee1bc2e56513b13f92d16c99a01898169d3',
            'hppy >= 0.9.9',
            'tornado >= 4.3',
            'hivclustering @ https://github.com/FynnFreyer/hivclustering/archive/23279699bc4a680ae293037c5730867ade3fc540.zip#sha256=f8258a184a760534a5a72333567049a0aa96aeb3e9fc26299dd40158c89a4e7f',
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
