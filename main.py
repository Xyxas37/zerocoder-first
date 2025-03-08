from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_word():
       return render_template("DZ40.html")

if __name__ == "__main__":
    app.run()

