#coding=UTF-8
import os
from os import environ as env
import bottle
application = bottle.default_app()
from bottle import default_app, request, route, response, run, error, redirect, abort, static_file, template
from sys import argv

bottle.debug(True)



nofn = {'jón': '0402982541',
        'steinn': '0510853652',
        'alfreð': '0101932201',
        'ásgeir': '2010789426'}


@route('/')
def index():
    return template('main.tpl', names=nofn, title = None, kt = 0)
@route('/<id>')
def kt(id):
    if id == '0402982541' or id == '0510853652' or id == '0101932201' or id == '2010789426':
        return template('page1.tpl', kt=id, title='Kennitala')
    else:
        abort(404)
#@route('/<ii>')
@error(404)
def villa(error):
    return template('villa.tpl')
@route('/static/<skra:path>')
def static_skrar(skra):
    return static_file(skra, root='./public/')


bottle.run(host='0.0.0.0', port=argv[1])
#run(host='localhost', port=8000, degbug=True)
