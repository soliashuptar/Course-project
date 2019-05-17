import runner
from flask import Flask, render_template, request, redirect, url_for
import sys

sys.path.append("..")


app = Flask(__name__, template_folder='templates', static_folder='vendor')


@app.route("/")
def index():
    """
    Function renders home page
    :return: html
    """
    return render_template('home_page.html')


@app.route("/uptodatemap", methods=["GET", "POST"])  # Function which is implemented only if user ask for up-to-date map
def up_to_date_map():
    """
    Function for generating a new up-to-date map
    :return: html/ function
    """
    if request.method == "POST":
        day = request.form.get('day')
        print(day)
        runner.main(day)
        return redirect(url_for("generated_map"))

    return redirect(url_for("index"))


@app.route("/generatedmap", methods=["GET", "POST"])  # Function is always implemented
def generated_map():
    """
    Function which renders a map
    :return: html
    """
    return render_template("my_map.html")


if __name__ == "__main__":
    app.run(debug=True)
