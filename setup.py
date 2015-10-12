try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(name='aiotkinter',
      author='montag451',
      author_email='montag451 at laposte.net',
      maintainer='montag451',
      maintainer_email='montag451 at laposte.net',
      url='https://github.com/montag451/aiotkinter',
      description='An asyncio API for the Tkinter event loop',
      long_description=open('README.rst').read(),
      version='0.2',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3'],
      py_modules=['aiotkinter'])
