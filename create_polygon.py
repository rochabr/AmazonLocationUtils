import json
import boto3
import math

def create_geofence(longitude, latitude):  
    #creates inverted polygon
    coordinates = create_polygon(longitude, latitude)
    location_coordinates.append(create_coordinate_structure(coordinates, identifier))        

    batch_put_geofence(location_coordinates)

#creates polygon
def create_polygon(longitude, latitude, radius=0.0008, vertices=6):
    center = (longitude,latitude)

    angle = 0
    angle -= (math.pi/vertices)
    
    coord_list = [[center[0] + radius * math.sin((2*math.pi/vertices) * i - angle), center[1] + radius * math.cos((2*math.pi/vertices) * i - angle)] for i in range(vertices)]
    coord_list.append(coord_list[0])
    
    return coord_list
    
#formats amazon location geofence
def create_coordinate_structure(coordinates, identifier):
    coordinates.reverse()
    return {
	    'GeofenceId': identifier,
		'Geometry': {
		'Polygon': [coordinates]
		}
	}

#creates geofence on amazon location
def batch_put_geofence(geofences, identifier='geofence_id'):
    location = boto3.client('location')
    geofence_collection = 'COLLECTION_NAME' 
    
    response = location.batch_put_geofence(
				CollectionName=geofence_collection,
				Entries=geofences)
	
    print(response)
    
    


