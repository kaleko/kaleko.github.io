#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Kaleko'
SITENAME = 'David Kaleko'
SITETITLE = 'David Kaleko'
SITESUBTITLE = "Data Scientist, Ph.D."


THEME = 'mytheme'
THEME_STATIC_DIR = 'mytheme/static'
PATH = 'content'
#STATIC_PATHS = [ 'mail','js', 'css', 'fonts']
STATIC_PATHS = [ 'images', 'CNAME' ]
#add images back in above
# EXTRA_PATH_METADATA = {
#     'static/images/portfolio': {'path': 'images/portfolio'},
#     }
TIMEZONE = 'America/Chicago'

DEFAULT_PAGINATION = 5

DEFAULT_LANG = 'en'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'

SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'contact_me.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DIRECT_TEMPLATES = ['index']

GOOGLE_ANALYTICS = 'UA-71585052-2'

# Top Menu Links
NAVLINKS = (
	('#page-top', 'Home'),
	('#about', 'About'),
        ('#blog', 'Blog'),
	('#contact', 'Contact')
)


#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],

	['Message', 'textarea', 'message', 'Please enter a message.']
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

#MARKUP = ('md', 'ipynb')
#PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['ipynb']
