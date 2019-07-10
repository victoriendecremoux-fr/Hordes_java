import time as tm
import random as rd
import os
import pickle as pk
import Individu as ind
from tkinter import *

jean = ind.Individu(20,5,6,80,True)
marie = ind.Individu(20,5,6,120,False)

bebe = ind.enfant(jean,marie)
