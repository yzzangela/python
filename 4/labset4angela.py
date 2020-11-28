city_state = ["Detroit|MI", "Philadelphia|PA", "Hollywood|CA", "Oakland|CA", "Boston|MA", "Atlanta|GA", "Phoenix|AZ", "Birmingham|AL", "Houston|TX", "Tampa|FL"]
cali = city_state[3:5]
us_cities = []
for i in city_state:
    city,state=i.split("|")
    us_cities.append(city)
for j in us_cities:
    