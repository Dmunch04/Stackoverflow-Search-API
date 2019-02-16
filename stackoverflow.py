import sys
import json
from stackapi import StackAPI
if sys.version < '3':
    from urllib2 import urlopen
    from urllib import quote as urlquote
else:
    from urllib.request import urlopen
    from urllib.parse import quote as urlquote

URL_SEARCH = 'https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=activity&q={0}&site=stackoverflow'

class StackOverflow (object):
  def __init__ (self, title, sender, tags, url, answers, answered):
    self.title = title
    self.sender = sender
    self.tags = tags
    self.url = url
    self.answers = answers
    self.answered = answered

  def __str__ (self):
    return '%s: %s: [%d] (%d - %d (%d))' % (self.title, self.sender, self. tags, self.url, self.answers, self.answered)

def get_search_json (url):
  raw = urlopen(url).read()
  #raw = open('raw.json', 'r')
  raw2 = str(raw, 'unicode')
  jsonData = json.loads(raw2)
  raw.close()

  return jsonData

def parse_search_json (json):
  results = []

  for result in json['items']:
    search = StackOverflow(str(result['title']), str(result['owner']['display_name']), str(result['tags']), str(result['link']), int(result['answer_count']), str(result['is_answered']))

    results.append(search)

  return results[0]

def search (search):
  json = get_search_json(URL_SEARCH.format(urlquote(search)))
  return parse_search_json(json)
