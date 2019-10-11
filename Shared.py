https://github.al.com.au/gist/manuelk/9892a5b96a540a0872b2a7575a78f654

import os, sys
from functools import partial
import time
import hou
from hutil.Qt.QtCore import *


<?xml version="1.0" encoding="UTF-8"?>
<pythonPanelDocument>
  <!-- This file contains definitions of Python interfaces and the
 interfaces menu.  It should not be hand-edited when it is being
 used by the application.  Note, that two definitions of the
 same interface or of the interfaces menu are not allowed
 in a single file. -->
  <interface name="version_explorer" label="Version Explorer" icon="OBJ_light_point" help_url="">
    <script><![CDATA[########################################################################
# The 'hutil.Qt' is for internal-use only.
# It is a wrapper module that enables the sample code below to work with
# either a Qt4 or Qt5 environment for backwards-compatibility.
#
# When developing your own Python Panel, import directly from PySide2
# or PyQt5 instead of from 'hutil.Qt'.
########################################################################
#from hutil.Qt import QtWidgets
from AL.versionexplorer.applicationhoudini import application
from AL.libs.nucleus import application as nucleusApp
def onCreateInterface():
    nucleusConfiguration = application.VersionExplorerHoudini()
    app = nucleusApp.Application(nucleusConfiguration)
    app.runEvent('Nucleus.Application.ApplicationStartedEvent')
    return app.mainWindow()
]]></script>
    <includeInToolbarMenu menu_position="1001" create_separator="false"/>
    <includeInPaneTabMenu menu_position="1001" create_separator="false"/>
  </interface>
</pythonPanelDocument>
