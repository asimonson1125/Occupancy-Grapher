from flask import request, render_template, redirect
from datetime import datetime, timedelta

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
    return "<h1>home</h1>"

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

if __name__ == '__main__':
    app.run()
