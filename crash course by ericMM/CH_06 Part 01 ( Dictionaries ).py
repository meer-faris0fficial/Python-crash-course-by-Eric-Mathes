# A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# adding elements in the dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_coordinates'] = 0
alien_0['y_coordinates'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print(f"the color of the alien is {alien_0['color']}")
print(f"your point is {alien_0['points']}")

# position of the alien with speed
alien_0 = {'x_position' : 0, 'y_position' : 25 ,'speed' : 'medium'}
print(f"original positon {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_icrement = 1
elif alien_0['speed'] == 'medium':
    x_icrement = 2
else:
    x_icrement = 3
alien_0['x_position'] = alien_0['x_position'] + x_icrement
print(f"new position : {alien_0['x_position']}")

# Removing Key-Value Pairs
alien_0 = {'x_position' : 0, 'y_position' : 25 ,'speed' : 'medium'}
del alien_0['speed']
print(alien_0)

# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.') # if there is no value like point it will give output as a no point value assigned
print(point_value)




