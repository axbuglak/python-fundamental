from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

sourceFiles = ["nogil.pyx"]

ext_modules = [Extension("nogil", sourceFiles)]

setup(
    name='google-drive-bot',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)