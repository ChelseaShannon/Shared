# -*- coding: utf-8 -*-

uuid = '930faa04-f15e-44e4-a3bd-637006520793'

name = 'houdini'

version = '18.0.253'

description = \
    """
    Houdini combines  superior performance and dramatic, new ease-of-use functionality to deliver a powerful and accessible 3D animation experience to CG professionals everywhere.
    """

authors = ['sidefx']

private_build_requires = ['cmake-3']

requires = [
    'CentOS-7.4+<8',
    'python-2.7',
    'Qt_vfx-5.12',
    'houdiniDevKit-18.0.253',
    '~libxml2-2.8.0',
    '~zlib-1.2.7+<2',
    '~PyQt-4.7.3+<6'
]

def commands():
    setenv('LD_LIBRARY_PATH', '$HOUDINI_LOCATION/dsolib:$LD_LIBRARY_PATH')
    setenv('PATH', '$HOUDINI_LOCATION/bin:$HOUDINI_LOCATION/houdini/sbin:$PATH')
    
    setenv('HOUDINI_PYTHON_BIN', '$REZ_PYTHON_ROOT/bin/python')
    setenv('HOUDINI_PYTHON_LIB', '$REZ_PYTHON_ROOT/lib/libpython2.7.so')
    
    
    setenv('HOUDINI_USE_HFS_PYTHON', '1')
    setenv('HOUDINI_PATH', '&')
    setenv('HOUDINI_DSO_PATH', '@/dso_^:@/dso')
    setenv('HOUDINI_SCRIPT_PATH', '@/scripts')
    setenv('HOUDINI_UI_ICON_PATH', '@/^')
    setenv('HOUDINI_TOOLBAR_PATH', '@/^')
    setenv('HOUDINI_SCRIPT_LICENSE', 'hbatch')
    setenv('SESI_LMHOST', 'lic-houdini')
    setenv('CMAKE_MODULE_PATH', '{root}/cmake;$CMAKE_MODULE_PATH')
    setenv('PYTHON_EXE', '$HOUDINI_LOCATION/bin/hython')
    setenv('HYTHON_EXE', '$HOUDINI_LOCATION/bin/hython')
    setenv('HOUDINI_GLSL_PATH', '.;@/glsl')
    setenv('HOUDINI_LICENSE_VERSION', '17.0')
    
    # Ideally we would like to remove these, as they get reset by houdini_setup anyway, but we need them before a Houdini
    # environment is initialised
    setenv('HB', '$HOUDINI_LOCATION/bin')
    setenv('HOUDINI_MAJOR_RELEASE', '18')
    setenv('HOUDINI_MINOR_RELEASE', '0')
    setenv('HOUDINI_BUILD_VERSION', '253')
    setenv('HIH', '$HOME/houdini$HOUDINI_MAJOR_RELEASE.$HOUDINI_MINOR_RELEASE')
    
    # temp workaround for Qt-5.12.4 be removed see FX-291 & https://bugreports.qt.io/browse/QTBUG-77826
    setenv('QT_XCB_TABLET_LEGACY_COORDINATES', '')

def post_commands():
    setenv('HOUDINI_OTLSCAN_PATH', '$HOUDINI_OTLSCAN_PATH:@/otls')
    appendenv('HOUDINI_OTLS_PATH', '$HIH/otls')

timestamp = 1570747012

vcs = 'github'

changelog = 'commi...'

release_message = ''

revision = \
    {'branch': 'master',
     'commit': 'f5b8b0a50ceb3e28c43b0caacf8643850ac8e8a3',
     'fetch_url': 'https://github.al.com.au/rnd/rezExternalPackages',
     'push_url': 'https://github.al.com.au/rnd/rezExternalPackages',
     'tracking_branch': 'origin/master'}

external = 'true'

format_version = 2
