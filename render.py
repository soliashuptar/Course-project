import sys
sys.path.append("..")
from data.info_ADT import Info
# sys.path.append("..")
from flask import Flask, render_template, request, redirect, url_for
# from data.info_ADT import Info

from data.get_new_file import get_last
app = Flask(__name__, template_folder='templates', static_folder='vendor')
# app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index():
    return render_template('home_page.html')


@app.route("/uptodatemap", methods=["GET", "POST"])
def up_to_date_map():
    if request.method == "POST":
        day = request.form.get('day')
        print(day)
        txt_data = Info(day, "http://web.mta.info/developers/" + get_last()[0])
        csv_data = Info("data/Stations.csv")
        data = txt_data + csv_data
        data.write('data.txt')

        return redirect(url_for("generated_map"))

    return render_template("my_map.html")


@app.route("/generatedmap", methods=["GET", "POST"])
def generated_map():

    return render_template("my_map.html")


if __name__ == "__main__":
    app.run(debug=True)
