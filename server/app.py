from flask import request, render_template, redirect, Response
from datetime import datetime
from sqlalchemy import cast, between
import pandas as pd
import json

from init import app, Occupancy, submit, est
import maths


@app.route('/submit', methods=['POST'])
def submission():
    data = request.get_json()
    submit(data)
    return "Data recieved.", 200, {'Content-Type': 'application/json'}

@app.route('/sample', methods=['GET'])
def sample():
    day = maths.getDay()
    return render_template("graph.html", template_folder='templates', lower=[2,3,4,5,4,3,2], times=day)

@app.route('/')
def home():
    return redirect('/graphs')

@app.route('/graphs', methods=['GET'])
def graphs():
    date = request.args.get('date')
    if date == None or date == '':
        return redirect(f'/graphs?date={datetime.now(est).date()}')
    todayData = Occupancy.query.filter(Occupancy.date == date).all()
    todayData.sort()
    if len(todayData) == 0:
        return render_template('graph.html', alert="No Data For Today!")
    times = maths.getDay()
    lower = []
    upper = []
    aquatics = []
    i = 0
    formatted = maths.format24Time(todayData[0].hour, todayData[0].minute)
    while(formatted != times[i]):
        i += 1
        if(i == len(times)):
            break
        lower.append(0)
        upper.append(0)
        aquatics.append(0)
    for i in todayData:
        lower.append(i.lower)
        upper.append(i.upper)
        aquatics.append(i.aquatics)
    combo = maths.getCombo(lower, upper)
    return render_template("graph.html", template_folder='templates', lower=lower, upper=upper, combo=combo,  aquatics=aquatics, times=times)

# def getDataset():
#     start = request.args.get('start')
#     end = request.args.get('end')
    
#     if start == None or start == '':
#         start = datetime.now(est).date()
#     if end == None or end == '':
#         end = datetime.now(est).date()
#    data = Occupancy.query.filter(between(cast(Occupancy.date, Date), start_date, end_date)).all()

@app.route('/download-the-kitchen-sink')
def downloadingEverything():
    data = Occupancy.query.all()
    keys = data[0].to_json().keys()
    out = ','.join(keys)
    for datapoint in data:
        out += "\n"
        for key in keys:
            out += str(datapoint.__getattribute__(key)) + ","
        out = out[:-1]
    response = Response(out, mimetype="text/csv", direct_passthrough=True)
    response.headers.set('Content-Disposition', 'attachment', filename=f"occupyRIT-{datetime.now(est).date()}")
    return response
        
        
if __name__ == '__main__':
    app.run()
