from __future__ import print_function

import ctypes as c
import subprocess
from time import sleep
from bitstring import BitArray
from sys import platform as _platform
from ftdi import *

open_ex_by_name(b'USB-Blaster')
