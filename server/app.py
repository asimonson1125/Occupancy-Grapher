from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
# Allow all domain names to cross domain
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/submit', methods=['POST'])
def submission():
    data = request.get_json()
    print("Lower Fitness Center occupant count: " + data['lower'])
    print("Upper Fitness Center occupant count: " + data['upper'])
    print("Aquatics Center occupant count: " + data['aquatics'])
    return "Data recieved.", 200, {'Content-Type': 'application/json'}


app.run()
