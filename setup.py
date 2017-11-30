# -*- coding: utf-8 -*-
import os
from setuptools import setup


setup(
    name='edx-custom-registration-form',
    version='1.0',
    description='Custom registration form extension apps for Open edX',
    packages=['reg_form_ext'],
    install_requires=[
        'Django',
    ],
)
