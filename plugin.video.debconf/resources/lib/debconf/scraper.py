'''
    debconf.scraper
    ~~~~~~~~~~~~~~~~~~~~~

    This module contains some functions which do the website scraping for the
    API module. You shouldn't have to use this module directly.
'''
import re
from urllib2 import urlopen
from urlparse import urljoin
from bs4 import BeautifulSoup as BS


BASE_URL = 'http://meetings-archive.debian.net/pub/debian-meetings/'
def _url(path):
    '''Returns a full url for the given path'''            
    return urljoin(BASE_URL, path)


def get(url):
    '''Performs a GET request for the given url and returns the response'''
    conn = urlopen(url)
    resp = conn.read()
    conn.close()
    return resp


def _html(url):
    '''Downloads the resource at the given url and parses via BeautifulSoup'''
    return BS(get(url))


def get_years():
	'''Returns a list of subjects for the website. Each subject is a dict with
	keys of 'name' and 'url'.
	'''
	url = _url('')
	html = _html(url)
	subjs = html.find_all('a', text=re.compile("2.*"))
	items = []
	for s in subjs:
		href = s.attrs['href']
		items.append({
			'name':href,
			'url': _url(href)
			})
	return items

def get_events(url):
	'''Returns a list of subjects for the website. Each subject is a dict with
	keys of 'name' and 'url'.
	'''
	html = _html(url)
	subjs = html.find_all('a')
	subjs = subjs[4:]
	items = []
	for s in subjs:
		href = url + s.attrs['href']
		items.append({
			'name':s.text,
			'url': _url(href)
			})
	return items

def get_formats(url):
	'''Returns a list of subjects for the website. Each subject is a dict with
	keys of 'name' and 'url'.
	'''
	html = _html(url)
	subjs = html.find_all('a')
	subjs = subjs[4:]
	items = []
	for s in subjs:
		href = url + s.attrs['href']
		items.append({
			'name':s.text,
			'url': _url(href)
			})
	return items

def get_videos(url):
	'''Returns a list of subjects for the website. Each subject is a dict with
	keys of 'name' and 'url'.
	'''
	html = _html(url)
	subjs = html.find_all('a', text=re.compile(".*\.(webm|ogv|mpeg)"))
	items = []
	for s in subjs:
		href = url + s.attrs['href']
		items.append({
			'name':s.text,
			'url': _url(href)
			})
	return items
