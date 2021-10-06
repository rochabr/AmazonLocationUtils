import json
import boto3
import math

def create_geofence(longitude, latitude):    
    coordinates = create_polygon(longitude, latitude)
    location_coordinates.append(create_coordinate_structure(coordinates, identifier))        

    batch_put_geofence(location_coordinates)
        
def create_polygon(longitude, latitude):
    center = (longitude,latitude)
    radius = 0.0008
    
    n = 6
    
    angle = 0
    angle -= (math.pi/n)
    
    coord_list = [[center[0] + radius * math.sin((2*math.pi/n) * i - angle), center[1] + radius * math.cos((2*math.pi/n) * i - angle)] for i in range(n)]
    coord_list.append(coord_list[0])
    
    return coord_list
    

def create_coordinate_structure(coordinates, identifier):
    coordinates.reverse()
    return {
	    'GeofenceId': identifier,
		'Geometry': {
		'Polygon': [coordinates]
		}
	}
	

    
def batch_put_geofence(geofences):
    location = boto3.client('location')
    geofence_collection = 'COLLECTION_NAME' 
    
    response = location.batch_put_geofence(
				CollectionName=geofence_collection,
				Entries=geofences)
	
    print(response)
    
    


