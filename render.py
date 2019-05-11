from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def local():
    pass


def get_page():
    return render_template("map.html")
    # return "Hello"

if __name__ == "__main__":
    app.run(debug=True)