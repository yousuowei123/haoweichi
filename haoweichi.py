# !/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: c_tob -*-
import requests
from bs4 import BeautifulSoup


def get_page_source(url):
	pass


def parse_page_source(html):
	pass


def main():
	url = 'http://www.haoweichi.com/Index/random'
	html = get_page_source(url)
	results = parse_page_source(html)


if __name__ == "__main__":
	main()