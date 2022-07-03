#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 21:54:42 2022

@author: ahmad_izzuddin
"""

import flask
from flask import request
from newspaper import Article
import nltk
nltk.download('punkt')



app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Text Summariser</h1><p>This site is a prototype API for text summariser</p>" 

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404  

@app.route('/api/v1/ts/summarise', methods=['GET'])
def api_main():
    
    query_parameters = request.args
    url = query_parameters.get('targetUrl')
    
    out_text = summarise(url)
    
    
    return out_text


def summarise(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    return article.summary

app.run()
