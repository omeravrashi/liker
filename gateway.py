from __future__ import print_function
from flask import Flask, request, g
import time
app = Flask(__name__)

@app.route('/')
def hi():
    g.fn = str(time.time()) + ".txt"
    with open(g.fn,'w') as f:
        print ("Request headers", request.headers, file=f)
    return 'oh hai'

@app.route('/foo')
def foo():
    return 'foo'

@app.before_request
def before():
    pass


@app.after_request
def after(response):
    fn = g.get('fn', None)
    if fn:
        with open(fn,'a') as f:
            print ("Printing response", file=f)
            print (response.status, file=f)
            print (response.headers, file=f)
            print (response.get_data(), file=f)
    return response

if __name__ == '__main__':
    app.run(debug=True)