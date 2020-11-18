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


@app.route('/movies/bytitle/<str:title>')

#@app.route('/')
#def index():
    #return 'Index Page\n'


#@app.route('/dictionary')
#def dictionary():
    #return {"key": "value"}

#@app.route('/user/<username>')
#def show_user_profile(username):
    # show the user profile for that user
    #return 'User %s' % escape(username)
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
    # show the post with the given id, the id is an integer
    #return 'Post %d' % post_id
#@app.route('/path/<path:subpath>')
#def show_subpath(subpath):
    # show the subpath after /path/
    #return 'Subpath %s' % escape(subpath)


