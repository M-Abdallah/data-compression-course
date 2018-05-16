#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mohamed
"""

import numpy as np

import arithmaticEncoder

seq = 'acba'

encode = arithmaticEncoder.arrithmaticEncode( seq )

code = encode.encode()

print( code )
