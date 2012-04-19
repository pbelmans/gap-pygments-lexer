import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
     this, do_insertions
from pygments.token import Error, Punctuation, Literal, Token, \
     Text, Comment, Operator, Keyword, Name, String, Number, Generic

__all__ = ['GAPLexer']

class GAPLexer(RegexLexer):
    name = 'GAP'
    aliases = ['gap']
    filenames = ['*.gap']
    mimetypes = ['text/x-gap']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\'', String, 'string_squote'),
            (r'\"', String, 'string_dquote'),

            include('comments'),
            include('delimiters'),
            include('numbers'),
            include('keywords'),
            include('operators'),
            include('statements'),

            include('identifiers'), # if all else fails it must be an identifier
        ],
        'comments': [
            (r'#.*$', Comment.Single),
        ],
        'delimiters': [
            (r'~|!.|!\[|\.|\.\.|->|,|;|!\{|\[|\]|\{|\}|\(|\)|:', Punctuation),
        ],
        'identifiers': [ # 4.6
            (r'Print', Name.Builtin),

            # TODO this is not the complete implementation I ignore identifiers with escaped characters (who uses those?!)
            (r'[A-Za-z_0-9]*[A-Za-z_]+[A-Za-z_0-9]*', Name),
        ],
        'keywords': [ # 4.15
            (r'and|do|elif|else|end|fi'
             r'for|function|if|in|local|mod'
             r'not|od|or|repeat|return|then'
             r'until|while|quit|QUIT|break|rec'
             r'continue',
             Keyword.Reserved),
        ],
        'numbers': [
            (r'[-]?[0-9]+(?:e[0-9]+)?', Number),
        ],
        'operators': [
            (r'=|<>|<|<=|>|>=|in', Operator), # comparisons
            (r'\+|-|\*|/|mod|\^', Operator),  # arithmetic operators
            (r'not|and|or', Operator),        # logical operators
        ],
        'statements': [ # 4.13
            (r':=', Operator),                # assignment
            # the others are keywords and are already covered
        ],
        'string_squote': [
            (r'[^\']*\'', String, '#pop'),
        ],
        'string_dquote': [
            (r'[^\"]*\"', String, '#pop'),
        ],
    }

