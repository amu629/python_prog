#!/usr/bin/python

import webbrowser as web

u=raw_input('Enter anything you want to search')
web.open_new('https://www.google.com/search?q='+u)
