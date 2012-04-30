""" 
A GAP lexer for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'GAPLexer', 
    version      = '1.1', 
    description  = __doc__, 
    author       = "Pieter Belmans", 
    install_requires=['pygments'],
    packages     = ['gaplexer'], 
    entry_points = '''
    [pygments.lexers]
    GAPLexer = gaplexer:GAPLexer
    '''
) 
