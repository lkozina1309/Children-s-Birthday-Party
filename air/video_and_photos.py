# This script is used for aerial video recording and taking images, in this case for children's birthday party
# The drone will takeoff, go to exact point, record a video and take photos during rotation and come back to starting point autonomously  
# Useful for automatic video recording and photographing


# import the libraries
from __future__ import print_function
import os
import numpy as np
import math
import sys
import rospy
import picamera
import mavros
import threading
import time
import mavros_msgs
from mavros import command
from std_msgs.msg import String
from mavros_msgs import srv
from geometry_msgs.msg import Twist, TwistStamped
from mavros_msgs.srv import SetMode, CommandTOL, CommandBool
from mavros_msgs.msg import State
from mavros_msgs.srv import *


class Drone:
    
    def __init__(self):
        self.rate = 1
        self.connected = False

    def connect(self, node: str, rate: int):
        rospy.init_node(node, anonymous=True)
        self.rate = rospy.Rate(rate)
        self.connected = True
        rospy.loginfo("Connected...")

    def arm(self):
        print("Arming...")
        rospy.wait_for_service('/mavros/cmd/arming')
        try:
            armService = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)
            armService(True)
        except rospy.ServiceException as e:
            print ("Service arm call failed: %s" %e)	
 
    def takeoff(self):
	print("Takeoff ...")
        rospy.wait_for_service('/mavros/cmd/takeoff')
        try:
		takeoffService = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
		response = takeoffService(altitude = 10, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)             # change the altitude if you want different
		rospy.loginfo(response)
        except rospy.ServiceException as e:
            print ("Service takeoff call failed: %s"%e)

    def move(self, x, y):
	pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)
	vel = TwistStamped()
	vel.twist.linear.x= x;
	vel.twist.linear.y= y;
	pub.publish(vel);	
	time.sleep(5)		
    
    def rotate(self,z):
       vel = TwistStamped()
       vel.twist.rotate.z = z 
       time.sleep(600)

    def land(self):
	print("Landing... ")
	rospy.wait_for_service('/mavros/cmd/land')
	try:
		landService = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
		response = landService(altitude = 0, latitude = 0, longitude = 0, min_pitch = 0, yaw = 0)
		rospy.loginfo(response)
	except rospy.ServiceException as e:
		print ("service land call failed: %s. The vehicle cannot land "%e) 
			
def main(args):
	camera = PiCamera()
	camera.resolution = (640, 480)
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(640, 480))
	v=Drone()
	v.connect("drone",rate=10)           # connecting
	time.sleep(3)
	rospy.wait_for_service('/mavros/set_mode')
	change_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
	response = change_mode(custom_mode="GUIDED")                    #setting mode to GUIDED
	print("Mode set to GUIDED")
	time.sleep(3)
	v.arm()                                           # arming the motors
	time.sleep(3)
	v.takeoff()                                      # takeoff to 10 meters
	time.sleep(3)
    	camera.start_recording('my_video.h264')         #start recording
    	camera.wait_recording(200)
	camera.stop_recording()
	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		image = frame.array
    		rawCapture.truncate(0)
    		for i in range(80):
        		camera.start_preview()
        		time.sleep(2)
        		camera.capture('image%s.jpg' %i)
        		time.sleep(5)
        	break

	vel = [[0, 0], [-5, 0], [0, -5]]                # change the values if they are different from your starting point and point of rotation
	i = 0
	while i < len (vel):
		x = vel [i] [0]
		y = vel [i] [1]
		v.move(x, y)
		i = i+1
    	v.rotate(0.2)                                  # change if you want different rotational speed
    	vel = [[0, 0], [0, 5], [5, 0]]
	i = 0
	while i < len (vel):
		x = vel [i] [0]
		y = vel [i] [1]
		v.move(x, y)
		i = i+1	
    	v.land()
	time.sleep(10)
	
if __name__ == "__main__":
	main(sys.argv)
