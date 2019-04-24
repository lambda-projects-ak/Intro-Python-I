"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE

# waypoints.append(dict(lat=30, lon=-100, name='yet another place'))

new_location = {
    "lat": 43,
    "lon": -124,
    "name": "a fourth place"
}

waypoints.append(new_location)

# for i in waypoints:
#     print(i)


# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE


# waypoints[0]["lon"] = -130
# waypoints[0]["name"] = "not a real place"

found = next(wp for wp in waypoints if wp['name'] == 'a place')
if found is not None:
    found['lon'] = -130
    found['name'] = 'not a real place'

# print(waypoints[0])

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for item in waypoints:
    # print(item.values())
    for key, value in item.items():
        print(f'{key}: {value}')
        # print(v)


for d in waypoints:
    for key in d:
        print(d[key])

# for x in y
# for item in collection
