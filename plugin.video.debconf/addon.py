from xbmcswift2 import Plugin
from resources.lib.debconf.scraper import get_videos, get_years, get_events, get_formats


plugin = Plugin()


@plugin.route('/')
def main_menu():
	items = [
		{'label': 'Years', 'path': plugin.url_for('show_years')},
	]
	return items

@plugin.route('/years/')
def show_years():
    years = get_years()

    items = [{
        'label': year['name'],
        'path': plugin.url_for('show_year_info', url=year['url']),
    } for year in years]

    sorted_items = sorted(items, key=lambda item: item['label'])
    return sorted_items

@plugin.route('/year/<url>/')
def show_year_info(url):
	events = get_events(url)
	items = [{
        'label': event['name'],
        'path': plugin.url_for('show_event_info', url=event['url']),
    } for event in events]

	sorted_items = sorted(items, key=lambda item: item['label'])
	return sorted_items
    
@plugin.route('/event/<url>/')
def show_event_info(url):
	formats = get_formats(url)
	items = [{
		'label': format['name'],
		'path': plugin.url_for('show_format_info', url=format['url']),
		} for format in formats]

	sorted_items = sorted(items, key=lambda item: item['label'])
	return sorted_items

@plugin.route('/format/<url>/')
def show_format_info(url):
	videos = get_videos(url)
	items = [{
		'label': video['name'],
		'path': video['url'],
		'is_playable': True,
		} for video in videos]

	sorted_items = sorted(items, key=lambda item: item['label'])
	return sorted_items

@plugin.route('/hack/')
def show_deconf2013():
	videos = get_videos('http://meetings-archive.debian.net/pub/debian-meetings/2013/debconf13/high/')
	items = [{
		'label': video['name'],
		'path': video['url'],
		'is_playable': True,
		} for video in videos]

	sorted_items = sorted(items, key=lambda item: item['label'])
	return sorted_items

if __name__ == '__main__':
    plugin.run()
