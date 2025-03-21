from flask import Flask

from routes import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(debug=True)
