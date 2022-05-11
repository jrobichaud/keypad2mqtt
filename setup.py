#!/usr/bin/env python

from distutils.core import setup

setup(name='keypad2mqtt',
      version='1.0',
      description='Send keys F1-F16 to mqtt',
      author='Jules Robichaud-Gagnon',
      author_email='j.robichaudg@gmail.com',
      url='https://github.com/jrobichaud/keypad2mqtt/',
      py_modules=['keypad2mqtt'],
      install_requires=["paho-mqtt", "evdev"],
     )
