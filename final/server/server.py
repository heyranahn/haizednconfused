#Must accept a path /hello with a parameter for 'name'
#Return value must be a dictionary with the key 'hello' and the value of the name url parameter
#Server should listen on port 5000

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return {"hello": name}

@app.route('/movies/<int:movies_id>')
@db
def search_title(descr, c=None):
    results = []
    parm = "%{}%".format(descr)
    SELECT_QUERY = " SELECT * FROM movies WHERE title like ? LIMIT 5 "
    result = c.execute(SELECT_QUERY, (parm,))
    for movie in result:
        results.append(movie)
    return results

    