from flask import request, render_template
from datetime import datetime

from init import app, Occupancy, submit
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

@app.route('/graphs', methods=['GET'])
def graphs():
    todayData = Occupancy.query.filter(Occupancy.date == datetime.now().date()).all()
    times = []
    lower = []
    upper = []
    aquatics = []
    for i in todayData:
        times.append(maths.formatTime(i.hour, i.minute))
        lower.append(i.lower)
        upper.append(i.upper)
        aquatics.append(i.aquatics)
    combo = maths.getCombo(lower, upper)
    return render_template("graph.html", template_folder='templates', lower=lower, upper=upper, combo=combo,  aquatics=aquatics, times=times)

if __name__ == '__main__':
    maths.startScheduler()
    app.run()
