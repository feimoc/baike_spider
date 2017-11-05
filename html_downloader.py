# -*- coding: UTF-8 -*-
import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        print(response)
        if response.getcode() != 200:
            return None

        return response.read()
