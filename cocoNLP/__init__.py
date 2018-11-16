#                      _   _ _     ____  
#   ___ ___   ___ ___ | \ | | |   |  _ \ 
#  / __/ _ \ / __/ _ \|  \| | |   | |_) |
# | (_| (_) | (_| (_) | |\  | |___|  __/ 
#  \___\___/ \___\___/|_| \_|_____|_|    
                                        
                                    
# -*- coding: utf-8 -*-

"""
cocoNLP module
~~~~~~~~~~~~~
Usage:
    >>> from cocoNLP import rake
    >>> r = rake.Rake() # With language as English
    >>> r = Rake(ranking_metric=Metric.<ranking_metric>)
:copyright: (c) 2018 by Yang Yang.
:license: MIT, see LICENSE for more details.
"""

from .rake import Metric, Rake