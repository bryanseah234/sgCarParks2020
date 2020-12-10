import math
from flask import Flask, render_template, request, redirect
from copy import copy
# Task 1.1
# Write your code here
carpark_data = []
def store():
    with open("hdb-carpark-information.csv", 'r') as f:
        f.readline()
        for line in f.readlines():
            line_nobreak = line.strip('\n')
            line_nocomma = line_nobreak.split(',')
            d = {}
            d['car_park_no'] = line_nocomma[0]
            d['address'] = line_nocomma[1]
            d['x_coord'] = line_nocomma[2]
            d['y_coord'] = line_nocomma[3]
            d['car_park_type'] = line_nocomma[4]
            d['type_of_parking_system'] = line_nocomma[5]
            d['short_term_parking'] = line_nocomma[6]
            d['free_parking'] = line_nocomma[7]
            d['night_parking'] = line_nocomma[8]
            d['car_park_decks'] = line_nocomma[9]
            d['gantry_height'] = line_nocomma[10]
            d['car_park_basement']  = line_nocomma[11]
            carpark_data.append(d)
    return carpark_data
#print(store())
# Task 1.2
# Write your code here
carparks = store()
#print(carparks[11])
counter_SC = []
counter_MSC = []
for i in carparks:
    if i["car_park_type"] == "SURFACE CAR PARK":
        counter_SC.append(i["car_park_type"])
    if i["car_park_type"] == "MULTI-STOREY CAR PARK":
        counter_MSC.append(i["car_park_type"])
total_number_of_surface = len(counter_SC)
total_number_of_multi = len(counter_MSC)
#print(total_number_of_surface)
#print(total_number_of_multi)
# Task 1.3
# Write your code here
carparks = store()
#print(carparks[:11])
def calculate(x1,y1,x0,y0):
    import math
    distance = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    return distance

def input_coords(x,y):
    input_x = float(x)
    input_y = float(y)
    distances = []
    #print(carparks[0]['x_coord'])
    for i in carparks:
        carpark_x = float(i['x_coord'])
        #print(type(float(carpark_x)))
        carpark_y = float(i['y_coord'])
        #print(float(i['y_coord']))
        distance = calculate(input_x,input_y,carpark_x,carpark_y)
        distances.append(distance)
    counter = 0
    for distance in distances:
        carparks[counter]['distance'] = distance
        counter += 1
    #print(carparks[0:11])
    return carparks

def sortByDistance(x,y):
    input_coords(x,y)
    #print(type(carparks))
    #print(len(carparks))    
    for i in range(0,len(carparks)): #2nd to last elements
        pop = carparks.pop(i)
        #print(type(pop))
        #print(pop)
        pop_distance = pop["distance"]
        #print(pop_distance)
        found = False
        for j in range(0,i): #first to i-1 elements
            this_distance = carparks[j]["distance"]
            #print(this_distance)
            if not found and pop_distance < this_distance:
                carparks.insert(j, pop)
                found = True
        if not found:
            carparks.insert(i, pop)
    #print(carparks[:3])
    return carparks
# Task 1.4
# Write your code here
def nearestCarpark(x_coord, y_coord):
    sorted_carparks = sortByDistance(x_coord, y_coord)
    nearest = sorted_carparks[0]
    return nearest["car_park_no"], nearest['address']
# Task 1.5
# Write your code here

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
   	return render_template('index.html')
#index.html should have buttons, that redirect to "/search" page

@app.route('/search', methods=['GET'])
def search():
	print(request.args)
	# import pdb; pdb.set_trace()
	# if 'xcoords' in request.args.get("xcoords") and 'ycoords' in request.args.get("ycoords"):
		# print(request.args)
	xcoords = float(request.args.get("xcoords"))
	ycoords = float(request.args.get("ycoords"))
	number, address = nearestCarpark(xcoords, ycoords)
	return render_template('search.html', xcoords=xcoords, ycoords=ycoords, number=number, address=address)
# #search.html should display x, y, nearest where appropriate

# @app.route('/')
# def root():
#     return render_template('index.html')

# @app.route('/search')
# def search():
#     if 'x' in request.args and 'y' in request.args:
#         x = float(request.args['x'])
#         y = float(request.args['y'])
#         cp_number, cp_address = nearestCarpark(x, y)
#         # cp_name = nearest_cp['car_park_no']
#         return render_template('search.html', x=x, y=y, cp_number=cp_number, cp_address=cp_address)

if __name__ == '__main__':
    app.run("0.0.0.0",debug=False, use_reloader=True)
