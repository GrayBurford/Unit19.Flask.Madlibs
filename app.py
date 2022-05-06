from flask import Flask, request, render_template
from random import randint, choice, sample
from stories import story, grays_story, tinas_story

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def home_page_form():
    prompts = story.prompts # list of terms
    template = story.template # String of text to fill {values}

    return render_template("madlibs.html", prompts = prompts, template = template)

@app.route("/story")
def render_story():
    story_text = story.generate(request.args)
    return render_template("story.html", text = story_text)