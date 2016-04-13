from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname' : "Steveboi"} # fake user
  posts = [ # Fake array of fake posts for fakers
    {
      'author' : {'nickname' : 'Bohn'},
      'body' : "A borkborkbork"
    },
    {
      'author' : {'nickname' : 'Jovi'},
      'body' : "I yam a real porson"
    }
  ]
  return render_template('index.html',
                         title='Home',
                         appname="0xDEADBEEF",
                         user=user,
                         posts=posts)
