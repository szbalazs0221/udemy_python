from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()

# venv) C:\Users\baszabo\PycharmProjects\udemy_python_bootcamp>set FLASK_APP=flask_experimenting.py
#
# (venv) C:\Users\baszabo\PycharmProjects\udemy_python_bootcamp>flask run
#  * Serving Flask app "flask_experimenting"
#  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
