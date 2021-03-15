class Street:
    def __init__(self, start, end, name, duration):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.duration = int(duration)


class Car:
    def __init__(self, street_count, path):
        self.street_count = street_count
        self.path = path


class StreetSystem:
    def __init__(self, simulation_time, intersection_count, street_count, car_count, points, streets, cars):
        self.simulation_time = simulation_time
        self.intersection_count = intersection_count
        self.street_count = street_count
        self.car_count = car_count
        self.points = points
        self.streets = streets
        self.cars = cars
