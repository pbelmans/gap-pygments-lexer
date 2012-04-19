""" 
A GAP lexer for Pygments
""" 
from setuptools import setup 

entry_points = """ 
[pygments.lexers]
gaplexer = gaplexer:gaplexer.GAPLexer
""" 

setup( 
    name         = 'gaplexer', 
    version      = '1.0', 
    description  = __doc__, 
    author       = "Pieter Belmans", 
    packages     = ['gaplexer'], 
    entry_points = entry_points 
) 
