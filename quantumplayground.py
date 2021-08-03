# y0ka1
# July 18th, 2021

''' This program sets some rules for vectors and uses numpy to do some linear algebra mathematics '''

import thewalrus
import numpy as np
import altair as alt
import pandas as pd
import math

# Defining some gates
I = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
SX = ((1/math.sqrt(2))*np.array([[1+1j,1-1j],[1+1j,-1-1j]]))
RX = ((1/math.sqrt(2))*np.array([[1,0-1j],[0-1j,1]]))
Y = np.array([[0,0-1j],[0+1j,0]])
Z = np.array([[1,0],[0,-1]])
H = ((1/math.sqrt(2))*np.array([[1,1],[1,-1]]))
S = np.array([[1,0],[0,0-1j]])
bell = np.array([[0.5+0.5j,-0.5-0.5j],[-0.5-0.5j,0.5+0.5j]])
