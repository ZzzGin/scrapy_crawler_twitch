# main.py

__author__ = 'Jing Qi-SU'

"""
This is the entrance of this spider project.

Maintenance history:
- 3/24/2018 ver 1.0:
    file created
"""


from scrapy.cmdline import execute

import sys
import os
import time

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'twitchdb'])

