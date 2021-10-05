def create_polygon(longitude, latitude):
    center = (longitude,latitude)
    radius = 0.0008
    
    n = 6
    
    angle = 0
    angle -= (math.pi/n)
    
    coord_list = [[center[0] + radius * math.sin((2*math.pi/n) * i - angle), center[1] + radius * math.cos((2*math.pi/n) * i - angle)] for i in range(n)]
    coord_list.append(coord_list[0])
    
    return coord_list