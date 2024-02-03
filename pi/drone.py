from flask import Flask, request
from flask_cors import CORS
import subprocess
import  requests
from simulator import idle
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
sense.low_light = True

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'


#Give a unique ID for the drone
#===================================================================
myID = "D1"
#===================================================================

# Get initial longitude and latitude the drone
#===================================================================
current_longitude = 13.233290
current_latitude = 55.715810
#===================================================================

drone_info = {'id': myID,
                'longitude': current_longitude,
                'latitude': current_latitude,
                'status': 'idle'
            }

# Fill in the IP address of server, and send the initial location of the drone to the SERVER
#===================================================================
SERVER="http://10.0.76.20:5001/drone"
with requests.Session() as session:
    resp = session.post(SERVER, json=drone_info)
    sense.set_pixels(idle)
#===================================================================

@app.route('/', methods=['POST'])
def main():
    coords = request.json
    # Get current longitude and latitude of the drone 
    #===================================================================
    current_longitude = coords['current'][0]
    current_latitude = coords['current'][1]
    #===================================================================
    from_coord = coords['from']
    to_coord = coords['to']
    subprocess.Popen(["python3", "simulator.py", '--clong', str(current_longitude), '--clat', str(current_latitude),
                                                 '--flong', str(from_coord[0]), '--flat', str(from_coord[1]),
                                                 '--tlong', str(to_coord[0]), '--tlat', str(to_coord[1]),
                                                 '--id', myID
                    ])
    return 'New route received'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
