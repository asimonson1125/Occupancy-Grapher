from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# Allow all domain names to cross domain
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/submit', methods=['POST'])
def submission():
    time = datetime.now()
    weekday = time.weekday()
    date = time.date()
    hour = time.hour
    minute = time.minute
    timeinfo = {'weekday': weekday, 'date': date, 'hour': hour, 'minute': minute}
    data = request.get_json()
    print("Data from {weekday}, {date} at {hour}:{minute}".format(**timeinfo))
    print("Lower Fitness Center occupant count: " + data['lower'])
    print("Upper Fitness Center occupant count: " + data['upper'])
    print("Aquatics Center occupant count: " + data['aquatics'])
    return "Data recieved.", 200, {'Content-Type': 'application/json'}


app.run()
