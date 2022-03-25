from flask import Flask, send_from_directory


app = Flask(__name__)

# address.com/index
# always a slash at the beginning of the PATH (end of the address)
# the slash at the beginning of the path at the end of the address is ALWAYS hidden
# WHY: There IS A DIFFFERENCE  between:
# /Foo  - give me the file foo in the root folder
# /Foo/ - gve me the listing of things in the foo folder
# index/foo

@app.route("/")
def index():
    return send_from_directory(".","index.html")

@app.route("/0")
def danger():
    return send_from_directory(".","bootstrap.html")

@app.route("/1")
def startertemp():
    return send_from_directory(".","index_startertemp.html")

@app.route("/2")
def table():
    return send_from_directory(".","index_table.html")