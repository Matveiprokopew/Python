from tello import * 
drone=Tello(port=8890,ip="192.168.10.1")
drone.takeoff()
drone.land()