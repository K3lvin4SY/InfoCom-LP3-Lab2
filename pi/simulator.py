import math
import requests
import argparse

def getMovement(src, dst):
    speed = 0.00001
    dst_x, dst_y = dst
    x, y = src
    direction = math.sqrt((dst_x - x)**2 + (dst_y - y)**2)
    longitude_move = speed * ((dst_x - x) / direction )
    latitude_move = speed * ((dst_y - y) / direction )
    return longitude_move, latitude_move

def moveDrone(src, d_long, d_la):
    x, y = src
    x = x + d_long
    y = y + d_la        
    return (x, y)

def send_location(SERVER_URL, id, drone_coords, status):
    with requests.Session() as session:
        drone_info = {'id': id,
                      'longitude': drone_coords[0],
                      'latitude': drone_coords[1],
                       'status': status
                    }
        resp = session.post(SERVER_URL, json=drone_info)

def distance(_fr, _to):
    _dist = ((_to[0] - _fr[0])**2 + (_to[1] - _fr[1])**2)*10**6
    return _dist
        
def run(id, current_coords, from_coords, to_coords, SERVER_URL):
    drone_coords = current_coords

    # Move from current_coodrs to from_coords
    d_long, d_la =  getMovement(drone_coords, from_coords)
    while distance(drone_coords, from_coords) > 0.0002:
        drone_coords = moveDrone(drone_coords, d_long, d_la)
        send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='busy')

    # Move from from_coodrs to to_coords
    d_long, d_la =  getMovement(drone_coords, to_coords)
    while distance(drone_coords, to_coords) > 0.0002:
        drone_coords = moveDrone(drone_coords, d_long, d_la)
        send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='busy')
    
    # Stop and update status to database
    send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='idle')
    
    return drone_coords[0], drone_coords[1]
   
if __name__ == "__main__":
    # Fill in the IP address of server, in order to location of the drone to the SERVER
    #===================================================================
    SERVER_URL = "http://10.0.76.19:5001/drone"
    #===================================================================

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    parser.add_argument("--id", help ='drones ID' ,type=str)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print("Get New Task!")

    drone_long, drone_lat = run(args.id ,current_coords, from_coords, to_coords, SERVER_URL)
    # drone_long and drone_lat is the final location when drlivery is completed, find a way save the value, and use it for the initial coordinates of next delivery
    #=============================================================================