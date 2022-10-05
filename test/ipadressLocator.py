import geocoder as geo

ip_adress = geo.ip('me')
print(ip_adress)

ip = geo.ip('192.xxx.xxx.x')
print(ip.city)

print(ip.latlng)

info = geo.google('Turkey')
print(info.geojson)
print(info.osm)
print(info.wkt)