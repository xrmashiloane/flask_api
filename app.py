from flask import Flask, jsonify, request
import os
import psutil
import json

app = Flask(__name__)



@app.route('/utilisation', methods=['GET'])
def utilisation():
    load = psutil.getloadavg()
    #Represent load in percentage 
    load_percent = [load / psutil.cpu_count() * 100 for load in psutil.getloadavg() ]
    disk = psutil.disk_usage('/')
    #Convert bytes to GB
    free = disk[2] / (1024 * 1024 * 1024)

    return jsonify(
                cpu=f"Average Load  is {load}",
                percentage=f"Load Percentacge {load_percent}",
                free =f"Available Disk {free:.2f}GB"
            )

@app.route('/value', methods=['GET', 'POST'])
def value():
    if request.method == 'GET':
        with app.open_resource('static/tech_assess.json') as f:
            data = json.load(f)
        value = data['tech']['return_value']
        return jsonify(
            value=f"{value}"
        )
    if request.method == 'POST':

            update = request.get_json()

            with app.open_resource('static/tech_assess.json', 'r') as f:
                data = json.load(f)  

            data['tech']['return_value'] = update['return_value']         

            with open(os.path.join(app.root_path, 'static/tech_assess.json'), 'w') as f:
                data = json.dump(data, f)

            with app.open_resource('static/tech_assess.json', 'r') as f:
                data = json.load(f)  

            value = data['tech']['return_value']

            return jsonify(
                new_value=f"{value}"
            )  
    
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)