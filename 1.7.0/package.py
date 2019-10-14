# -*- coding: utf-8 -*-

name = 'houdini_startup'

version = '1.7.0'

uuid = 'db59683f-fa57-46af-8896-f893a27f20ad'

authors = [
    'jaideepk',
    'sotirisb'
]

description = 'Houdini Startup Scripts'

private_build_requires = [
    'cmake-2.8',
    'AL_CMakeLibALPythonLibs-3',
    'houdini'
]

requires = [
    '~houdini',
    'AL_pylib_houdini-1.17+'
]

variants = [
    ['python-2.7', 'houdini-16'],
    ['python-2.7', 'houdini-17']
]

def commands():
    prependenv('PATH', '{root}/bin')

timestamp = 1524713679

vcs = 'github'

changelog = 'commi...'

release_message = 'Fixing pyc issue'

revision = \
    {'branch': 'master',
     'commit': '5dd058ed2f3bb41aa2b50a31cb4e5e839235fc3f',
     'fetch_url': 'http://github.al.com.au/rnd/houdini_startup',
     'push_url': 'http://github.al.com.au/rnd/houdini_startup',
     'tracking_branch': 'origin/master'}

config_version = 0
