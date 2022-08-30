from flask import Flask, request, jsonify
from datetime import datetime

from init import app, db, Occupancy

@app.route('/submit', methods=['POST'])
def submission():
    time = datetime.now()
    weekday = time.weekday()
    date = time.date()
    hour = time.hour
    minute = time.minute
    data = request.get_json()
    print(f"\nData from {weekday}, {date} at {hour}:{minute}")
    print("Lower Fitness Center occupant count: " + data['lower'])
    print("Upper Fitness Center occupant count: " + data['upper'])
    print("Aquatics Center occupant count: " + data['aquatics'] + "\n")
    occupancy = Occupancy(time, date, hour, minute, weekday, data['lower'], data['upper'], data['aquatics'])
    db.session.add(occupancy)
    db.session.commit()
    return "Data recieved.", 200, {'Content-Type': 'application/json'}

app.run()
