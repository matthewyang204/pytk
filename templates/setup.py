from setuptools import setup, Extension
import platform

if platform.system() == "Windows":
      print("Windows Python installs already include tkinter, no need to install")
      exit(1)

try:
      import tkinter

      print("Tkinter is already installed, no need to install")
      exit(1)
except ImportError:
      print("Tkinter not already installed, installing...")

setup(name="tkinter",
      description="Python interface to Tcl/Tk",
      version="1.0.0",
      ext_modules = [
        Extension("_tkinter", ["_tkinter.c", "tkappinit.c"],
                  define_macros=[("WITH_APPINIT", 1), ("TCL_WITH_EXTERNAL_TOMMATH", 1)],
                  include_dirs=["@INCLUDE@/internal", "@INCLUDE@/tcl", "@INCLUDE@/tk"],
                  libraries=["tcl8.6", "tk8.6"],
                  library_dirs=["/usr", "/usr/local", "/opt/tcl-tk"])
      ]
)

print("done")
