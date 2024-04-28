# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
  stations = {}
  with open(filename) as new_file:
    for line in new_file:
      parts = line.split(';')
      if parts[0] == "Longitude":
        continue
      stations[parts[3]] = (float(parts[0]), float(parts[1]))
  return stations

def distance(stations: dict, station1: str, station2: str):
  x_km = (stations[station1][0] - stations[station2][0]) * 55.26
  y_km = (stations[station1][1] - stations[station2][1]) * 111.2
  dist_km = math.sqrt(x_km**2 + y_km**2)
  return dist_km

def greatest_distance(stations: dict):
  greatest = ()
  dist = 0
  max_dist = 0
  st1 = ""
  st2 = ""

  for station1 in stations:
    for station2 in stations:
      if station1 != station2:
        dist = distance(stations, station1, station2)
        if dist > max_dist:
          max_dist = dist
          st1 = station1
          st2 = station2
  greatest = (st1, st2, max_dist)
  return greatest

if __name__ == "__main__":
  print(get_station_data("stations1.csv"))
  stations = get_station_data('stations1.csv')
  d = distance(stations, "Designmuseo", "Hietalahdentori")
  print(d)
  d = distance(stations, "Viiskulma", "Kaivopuisto")
  print(d)
  stations = get_station_data('stations1.csv')
  station1, station2, greatest = greatest_distance(stations)
  print(station1, station2, greatest)