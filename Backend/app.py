from flask import Flask
from flask_cors import CORS
from routes import tempo, ground, weather, forecast, alerts


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message": "NASA Air Quality API running"}


if __name__ == '__main__':
    app.run(debug=True)