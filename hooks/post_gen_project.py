#!/usr/bin/env python
from __future__ import unicode_literals, absolute_import, print_function

import os
import shutil
from collections import OrderedDict
from cookiecutter.prompt import read_user_yes_no

try:
    input = raw_input
except NameError:
    pass

components = OrderedDict()

components['awsconfig'] = {
    'question': '\nInclude AWS configuration variable declarations? ',
    'hint': '  Include AWS access and secret key variables ',
    'filename': 'variables.tf',
    'append': '\n// Variables for AWS Provider\nvariable "aws_access_key" {}\nvariable "aws_secret_key" {}\nvariable "aws_region" {}'
}

def configure_role():
    print('\n\nMODULE CONFIGURATION:\n=====================')
    if read_user_yes_no(components['awsconfig']['question'], 'Yes'):
        if 'fiename' in action:
            if 'append' in action:
                with open(action['filename'], 'a') as f:
                    f.write(action['append'])
