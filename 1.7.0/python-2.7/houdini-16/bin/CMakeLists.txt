CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

add_custom_target (recompile
    ALL
    COMMENT "Compiling python/pyc for  bin ..."
    COMMAND python -m compileall bin
)
set(source_files 
    common.py
    common.pyc
)

install(FILES ${source_files} DESTINATION bin)

rez_install_files(
  houdinifx
  DESTINATION bin
  EXECUTABLE
)

rez_install_files(
  hescape
  DESTINATION bin
  EXECUTABLE
)

rez_install_files(
  hmaster
  DESTINATION bin
  EXECUTABLE
)

rez_install_files(
  houdini
  DESTINATION bin
  EXECUTABLE
)

