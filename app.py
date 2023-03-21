from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from operator import add

app = Flask(__name__)

app.config['SECRET_KEY'] = "iloverollerderby12"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
     html = """
    <html>
        <body>
            <h1>Welcome to the Home Page</h1>
            <p>This is my app. Let me show you around.</p>
            <a href='/hello'>Go to hello page</a>
        </body>
    </html>
            """
     return render_template('home.html')

@app.route('/old-home-page')
def redirect_to_home():
    """Redirects to new home page"""
    flash("That paged has moved. Let me redirect you to our new home page.")
    return redirect('/')

MOVIES = {'While You were Sleeping', "You Can't Take it with You", "Mr. Smith Goes to Washington"}

@app.route('/movies')
def show_movies():
    """show list of all movies"""
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movie():
    new_movie = request.form['title']
    if new_movie in MOVIES: 
        flash('That movie is already in the list.', 'error')
    else:
        MOVIES.add(new_movie)
        flash("Added Movie to List!", 'success')
    return redirect('/movies')

@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/form2')
def show_form_2():
    return render_template("form_2.html")

COMPLIMENTS = ["cool", "clever", "tenacious", "brilliant", "phenomenal"]

@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)

@app.route('/greet2')
def get_greeting_2():
    username = request.args["username"]
    wants_compliments = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, wants_compliments=wants_compliments, compliments=nice_things)


@app.route('/lucky')
def lucky_number():
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg="You are so LUCKY!!")

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)

@app.route("/hello")
def say_hello():    
# this is a decorator
    """Shows hello page"""
    return render_template("hello.html")



@app.route("/goodbye")
def say_bye():
    return "GOOD BYE!!!"

@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1> <p> Sorting by: {sort} </p>"

# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You made a post request"

# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "You made a GET request"
    
@app.route('/add-comment')
def add_comment_form():
    return """
        <h1>Add Comment</h1>
        <form method="POST">
            <input type='text' placeholder='comment'name='comment'/>
            <input type='text' placeholder='username'name='username'/>
            <button>Submit</button>
        </form>
    """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    print(request.form)
    return f"""
    <h1>SAVED YOUR COMMENT WITH TEXT OF {comment}</h1>
    """
    
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"

POSTS = {
    1: "I like roller derby",
    2: "jamming is my favorite",
    3: "I am byzantine",
    4: "BOTAS is this weekend"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found.")
    return f"<h1>{post}</h1>"

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for {post_id} from the subreddit {subreddit}</h1>"


