import typing
import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # Disables pygame support prompt
map_options = {'схема': 'map', 'спутник': 'sat', 'гибрид': 'sat,skl'}
EXIT_SUCCESS = 0
