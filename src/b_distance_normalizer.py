##################################################################################################################

__author__ = "Boris Martinez Castillo"
__version__ = "1.0.1"
__maintainer__ = "Boris Martinez Castillo"
__email__ = "boris.vfx@outlook.com"

##################################################################################################################


#IMPORTS
import nuke
import nukescripts
import random
import math


NODEA =  nuke.thisNode().input(0)
NODEB =  nuke.thisNode().input(1)


#DEFINITIONS      

def calculate_distance_between_two_points(a,b):

    distance = math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1],2) + math.pow(a[2]-b[2],2))

    return distance  


def calculate_distances_iteratively(camera,axis):

    first = int(nuke.Root().knob('first_frame').getValue())
    last = int(nuke.Root().knob('last_frame').getValue())+1
    frame = first
    
    distances = []
    

    while frame < last:
        
        translate_a = camera['translate'].valueAt(frame)
        translate_b = axis['translate'].valueAt(frame)

        temp_distance = calculate_distance_between_two_points(translate_a,translate_b)
        distances.append(temp_distance)

        frame += 1

    return distances


def normalize_values(ls):
    maxvalue = max(ls)
    normalize_values = []
    for i in ls:
        temp = i / maxvalue
        normalize_values.append(temp)

    return normalize_values

def genereate_curve(ls):

	first = int(nuke.Root().knob('first_frame').getValue())
    last = int(nuke.Root().knob('last_frame').getValue())+1
    frame = first
	count = 0

    while frame < last:
    	nuke.thisNode()['multiplier'].setValueAt(ls[count],frame)
    	count +=1
    	frame +=1


def main_function():
	genereate_curve(normalize_values(calculate_distances_iteratively(NODEA,NODEB)))


if __name__ == "__main__":
    main_function()    








