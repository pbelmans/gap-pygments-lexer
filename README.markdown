About
-----

An implementation of a lexer for the GAP language, to be used in the Pygments highlighting system. See

* [gap-system.org](http://gap-system.org)
* [pygments.org](http://pygments.org)

Installation
------------

Assuming you already have Pygments installed (otherwise a simple `sudo easy_install Pygments` should suffice, or look at the other options at [pygments.org/docs/installation](http://pygments.org/docs/installation/)), in order to install the GAPLexer package you only need to

1. `git clone git://github.com/pbelmans/gap-pygments-lexer.git` or download and extract the archive GitHub automatically creates at [this project's Downloads page](https://github.com/pbelmans/gap-pygments-lexer/downloads)
1. `cd gap-pygments-lexer`
1. `sudo python setup.py install`


Remarks
-------

The list of functions and classes was automatically generated from [GAP's documentation](http://www.gap-system.org/Manuals/doc/htm/ref/chapters.htm), so if functions or classes aren't documented these will not be highlighted.

Thanks
------

The code is based on several of the already existing mathematical lexers from Pygments, as listed in `pygments.lexers.math`. For the list of builtin classes, functions and procedures I am greatly indebted to Wim Thys and his commandline skills.
