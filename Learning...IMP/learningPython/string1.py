import string

x = string.ascii_letters
print(x)
print(string.ascii_uppercase)
print('{},{},{}'.format("a",x,"b"))

# 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))