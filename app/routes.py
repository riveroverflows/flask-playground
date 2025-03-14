from app import app


@app.route("/")
def home():
    return "Hello from Flask app package!"
