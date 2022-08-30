from flask import Flask, request, jsonify, render_template
from datetime import datetime

from init import app, db, Occupancy
import maths

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

@app.route('/sample', methods=['GET'])
def sample():
    day = maths.getDay()
    return render_template("graph.html", template_folder='templates', lower=[2,3,4,5,4,3,2], times=day)

@app.route('/graphs', methods=['GET'])
def graphs():
    todayData = Occupancy.query.filter(Occupancy.date == datetime.now().date()).all()
    times = []
    lower = []
    for i in todayData:
        times.append(maths.formatTime(i.hour, i.minute))
        lower.append(i.lower)
    return render_template("graph.html", template_folder='templates', lower=lower, times=times)

if __name__ == '__main__':
    app.run()
