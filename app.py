#!/usr/bin/env python3

from bottle import get, post, redirect, request, route, run, static_file, template

_baseurl = '/'
_words = []
_words.append("Hello")
_words.append("World")
_words.append("Foo")
_words.append("Bar")


# ------------------------------------------
''' Static Files'''
@route( '/static/:path#.+#', name='static' ) # supply a path for js and css files
def static( path ):
    return static_file( path, root='static' )


# ------------------------------------------
''' Create '''
@get( _baseurl + 'create' ) # Give a form for the user to work with
def present_create():
    return template('create.html') # template searches for a /views folder

@post( _baseurl ) # Gets redirected from create.html
def create_object():

    _words.append( request.POST.get('word') )

    return redirect( _baseurl )


''' Retreive '''
@get( _baseurl ) # (static route)
def present_all_objects():
    return template( 'index.html', words = _words )


''' Update '''
@get( _baseurl + '<identifier>' ) # (dynamic route)
def get_object( identifier = "none" ):
    return template( 'edit.html', word = identifier )

@post( _baseurl + '<identifier>' ) # Gets redirected from edit.html
def post_object( identifier = "none" ):

    _words.remove( identifier )
    _words.append( request.POST.get('word') )

    return redirect( _baseurl )


''' Delete '''
# " Web browsers can't seem to send methods PUT and DELETE. 
#   They only send GET and POST "...?! so @delete() and @put() won't work?!
@post( _baseurl  + 'delete/'+ '<identifier>' )
def delete_object( identifier = "" ):

    _words.remove( identifier )

    return redirect( _baseurl )

# ---------------------------------------------------
run( host='localhost', port=8080, debug=True, reloader=True )
