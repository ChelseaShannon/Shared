import os

def set_iconcache():
    # HOUDINI_TEMP_DIR should have been set to fast previously, if it exists
    houdiniTemp = os.environ['HOUDINI_TEMP_DIR']
    user = os.environ['USER']
    houdiniHome = os.environ['HIH']
    houdiniDirName = houdiniHome.split("/")[-1]
    iconsPathLocal = os.path.join(houdiniTemp,user,houdiniDirName,"Icons")

    # Check if local icons cache exists
    if (not os.path.exists(iconsPathLocal)):
        os.makedirs(iconsPathLocal)

    # Remove old symlink if it exists
    userIconDir = os.path.join(houdiniHome, 'config', 'Icons')
    if os.path.islink(userIconDir):
        os.remove(userIconDir)

    # Set the cache dir env var
    os.environ['HOUDINI_ICON_CACHE_DIR'] = iconsPathLocal
