import math
import requests
import argparse
import pygame
from sense_hat import SenseHat

# Initialize the player, only need once
pygame.mixer.init()

sense = SenseHat()
sense.clear()
sense.low_light = True

s = (0, 0, 0) # Black
b = (66, 255, 233) # Blue
r = (255, 66, 66) # Red
v = (255, 255, 255) # White
w = (255, 102, 0) # Orange

dot1 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, w, w, s, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot2 = [
    s, s, s, s, s, s, s, s,
    s, s, s, w, w, w, s, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot3 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, w, w, s, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot4 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, w, w, s, s,
    s, s, w, s, s, w, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot5 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, w, w, s, s,
    s, w, w, s, s, w, w, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot6 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, w, w, s, s,
    s, w, w, s, s, w, s, s,
    s, w, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot7 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, w, w, s, s,
    s, w, w, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot8 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, w, s, s, s,
    s, w, w, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot9 = [
    s, s, s, s, s, s, s, s,
    s, s, w, w, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot10 = [
    s, s, s, s, s, s, s, s,
    s, s, w, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, s, w, s, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot11 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, s, w, w, s, s, s, s,
    s, s, s, s, s, s, s, s
]
dot12 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, s, w, w, w, s, s, s,
    s, s, s, s, s, s, s, s
]
dot13 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, w, s, s, s, s, s,
    s, s, w, w, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot14 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, w, s, s, s, s, s, s,
    s, w, w, s, s, w, s, s,
    s, s, w, w, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot15 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, w, w, s, s, w, w, s,
    s, s, w, w, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot16 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, w, s,
    s, s, w, s, s, w, w, s,
    s, s, w, w, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot17 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, w, w, s,
    s, s, w, w, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot18 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, w, w, s,
    s, s, s, w, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot19 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, w, w, s, s,
    s, s, s, s, s, s, s, s
]
dot20 = [
    s, s, s, s, s, s, s, s,
    s, s, s, s, s, w, s, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, s, w, s,
    s, s, s, s, s, w, w, s,
    s, s, s, s, s, w, s, s,
    s, s, s, s, s, s, s, s
]
busyFrames = [
    dot1,
    dot2,
    dot3,
    dot4,
    dot5,
    dot6,
    dot7,
    dot8,
    dot9,
    dot10,
    dot11,
    dot12,
    dot13,
    dot14,
    dot15,
    dot16,
    dot17,
    dot18,
    dot19,
    dot20,
]

loadPackage1 = [
    s, s, s, s, s, s, s, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, v, v, v, v, v, s,
    s, s, s, s, s, s, s, s
]
loadPackage2 = [
    s, s, s, b, b, s, s, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, v, v, v, v, v, s,
    s, s, s, s, s, s, s, s
]
loadPackage3 = [
    s, s, s, b, b, s, s, s,
    s, v, s, b, b, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, v, v, v, v, v, s,
    s, s, s, s, s, s, s, s
]
loadPackage4 = [
    s, s, s, s, s, s, s, s,
    s, v, s, b, b, s, v, s,
    s, v, s, b, b, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, v, v, v, v, v, s,
    s, s, s, s, s, s, s, s
]
loadPackage5 = [
    s, s, s, s, s, s, s, s,
    s, v, s, s, s, s, v, s,
    s, v, s, b, b, s, v, s,
    s, v, s, b, b, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, v, v, v, v, v, s,
    s, s, s, s, s, s, s, s
]
loadPackage6 = [
    s, s, s, s, s, s, s, s,
    s, v, s, s, s, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, s, b, b, s, v, s,
    s, v, s, b, b, s, v, s,
    s, v, s, s, s, s, v, s,
    s, v, v, v, v, v, v, s,
    s, s, s, s, s, s, s, s
]
loadPackageFrames = [
    loadPackage1,
    loadPackage2,
    loadPackage3,
    loadPackage4,
    loadPackage5,
    loadPackage6,
    loadPackage6,
    loadPackage6
]

idle = [
    b, b, b, b, b, b, b, b,
    b, s, s, s, s, s, s, b,
    s, b, s, s, s, s, b, s,
    s, s, b, s, s, b, s, s,
    s, s, b, s, s, b, s, s,
    s, b, s, s, s, s, b, s,
    b, s, s, s, s, s, s, b,
    b, b, b, b, b, b, b, b
]

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
        drone_info = {
            'id': id,
            'longitude': drone_coords[0],
            'latitude': drone_coords[1],
            'status': status
        }
        resp = session.post(SERVER_URL, json=drone_info)

def distance(_fr, _to):
    _dist = ((_to[0] - _fr[0])**2 + (_to[1] - _fr[1])**2)*10**6
    return _dist

def startSound(file):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def run(id, current_coords, from_coords, to_coords, SERVER_URL):
    drone_coords = current_coords

    # Move from current_coodrs to from_coords
    d_long, d_la =  getMovement(drone_coords, from_coords)
    loopAmount = 0.0
    startSound("../pygame-music/coin.wav")
    while pygame.mixer.music.get_busy() == True:
        continue
    startSound("../pygame-music/space-odyssey.mp3")
    while distance(drone_coords, from_coords) > 0.0002:
        drone_coords = moveDrone(drone_coords, d_long, d_la)
        send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='busy')

        sense.set_pixels(busyFrames[int(loopAmount // 1) % len(busyFrames)])
        loopAmount += 0.5

    # package arrived to currier
    send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='waiting')
    startSound("../pygame-music/doorbell-1.wav")
    # wait for human intercation
    loopAmount = 0.0
    exit_loop = False
    while not exit_loop:
        for key in sense.stick.get_events():
            if key.direction == "middle":
                startSound("../pygame-music/coin.wav")
                sense.clear()
                exit_loop = True
                while pygame.mixer.music.get_busy() == True:
                    continue
                break
        sense.set_pixels(loadPackageFrames[int(loopAmount // 1) % len(loadPackageFrames)])
        loopAmount += 0.5

    # Move from from_coodrs to to_coords
    d_long, d_la =  getMovement(drone_coords, to_coords)
    loopAmount = 0.0
    startSound("../pygame-music/space-odyssey.mp3")
    while distance(drone_coords, to_coords) > 0.0002:
        drone_coords = moveDrone(drone_coords, d_long, d_la)
        send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='busy')

        sense.set_pixels(busyFrames[int(loopAmount // 1) % len(busyFrames)])
        loopAmount += 0.5
    
    # package arrived to destination
    send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='waiting')
    startSound("../pygame-music/doorbell.mp3")
    # wait for human intercation
    loopAmount = 0.0
    exit_loop = False
    sense.clear()
    sense.stick.get_events() ## needs this or it wont work for some unknown reason O_O
    while not exit_loop:
        for key in sense.stick.get_events():
            if key.direction == "middle":
                startSound("../pygame-music/coin.wav")
                sense.clear()
                exit_loop = True
                while pygame.mixer.music.get_busy() == True:
                    continue
                break
        sense.set_pixels(loadPackageFrames[::-1][int(loopAmount // 1) % len(loadPackageFrames)])
        loopAmount += 0.5
        
    # Stop and update status to database
    send_location(SERVER_URL, id=id, drone_coords=drone_coords, status='idle')
    sense.set_pixels(idle)
    
    return drone_coords[0], drone_coords[1]
   
if __name__ == "__main__":
    # Fill in the IP address of server, in order to location of the drone to the SERVER
    #===================================================================
    SERVER_URL = "http://10.0.76.20:5001/drone"
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