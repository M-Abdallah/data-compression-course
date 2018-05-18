#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mohamed
"""

import numpy as np

import arithmaticEncoder
import arithmaticDecoder

seq = 'aabbccddabcdabcd'

encode = arithmaticEncoder.arrithmaticEncode( seq )

code = encode.encode()

# print( code, int(encode.m), encode.letters, encode.cdf)


decode = arithmaticDecoder.arithmaticDecoder( code, 8, encode.letters, encode.cdf )

decoded = decode.decode()
print( 'final', decoded)
