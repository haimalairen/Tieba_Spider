# -*- coding: utf-8 -*-
from scrapy.cmdline import execute

import sys
import os

if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    execute(["scrapy", "run", "梦幻五开", "menghuan", "-p", "1", "2"])