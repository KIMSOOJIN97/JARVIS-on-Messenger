import os

import re
import requests

import config
from templates.generic import *
from templates.text import TextTemplate

NEWS_API_KEY = os.environ.get('NEWS_API_KEY', config.NEWS_API_KEY)


def process(input, entities=None):
    output = {}
    try : 
        country=entities['country'][0]['value']
        country="Korea"
        r=requests.get("http://news.naver.com/"+country.capitalize())
        news_data=r.json
        output['input']=input
        output['output']='Headline news in ' + country.capitalize()  + '\n' + news_data['data']['children'][HEADLINE_NUM]['data']['title']
        output['success']  = True
    except:
        output['success']=False
     
    return output
process(input)
