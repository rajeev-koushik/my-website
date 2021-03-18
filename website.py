from flask import Flask, render_template
my_site = Flask(__name__)

@my_site.route('/')
def home():
    return render_template("home.html")

@my_site.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    my_site.run(debug=True)