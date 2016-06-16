#!/usr/bin/env python

import collectd
import urllib2

class URLChecker(object):

    def __init__(self):
        self.urls = []
    
    def init(self):
        collectd.info('init url check plugin')

    def config(self, conf):
        urls = []
        for node in conf.children:
            key = node.key.lower()
            val = str(node.values[0])
            
            if key == "url":
                urls.append(val)
            else:
                collectd.warning('%s plugin: Unknown config key: %s.' % (self.plugin_name, node.key))
    
    def check_url(self, url):
        response = urllib2.urlopen(url, timeout=3)
        code = response.getcode()
        if(code >= 200 and code < 400):
            values = [1]
        else:
            valuse = [0]

        metric = collectd.Values()
        metric.plugin = 'collect_url_check'
        metric.type = 'gauge'
        metric.values = values
        metric.dispatch()
            
    def read(self):
        for url in self.urls:
            check_url(url) 
    
    
if __name__ == '__main__':
    pass

else:
    url_checker = URLChecker()
    collectd.register_init(url_checker.init)
    collectd.register_config(url_checker.config)
    collectd.register_read(url_checker.read)
