from setuptools import setup, Extension

setup(name="tkinter",
      description="Python interface to Tcl/Tk",
      version="1.0.0",
      ext_modules = [
        Extension("_tkinter", ["_tkinter.c", "tkappinit.c"],
                  define_macros=[("WITH_APPINIT", 1), ("TCL_WITH_EXTERNAL_TOMMATH", 1)],
                  include_dirs=["@INCLUDE@/internal", "@INCLUDE@/tcl", "@INCLUDE@/tk"],
                  libraries=["tcl8.6"],
                  library_dirs=["/usr", "/usr/local"])
      ]
)
