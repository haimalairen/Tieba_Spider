# -*- coding: utf-8 -*-

BOT_NAME = 'tieba'

SPIDER_MODULES = ['tieba.spiders']
NEWSPIDER_MODULE = 'tieba.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'tieba.pipelines.TiebaPipeline': 300,
}

LOG_LEVEL = 'WARNING'
#LOG_LEVEL = 'INFO'

COMMANDS_MODULE = 'tieba.commands'

COOKIES_ENABLED = False

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'tieba.middlewares.IPMiddleware': 10,
}
