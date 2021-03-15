import models


def read_input(input_file):
    file = open(input_file, "r")
    first_line = file.readline()

    first_line = first_line.split()
    sim_time = int(first_line[0])
    intersect_count = int(first_line[1])
    street_count = int(first_line[2])
    car_count = int(first_line[3])
    points = int(first_line[4])

    streets = []
    for i in range(street_count):
        street = file.readline()
        street = street.split()
        streets.append(models.Street(street[0], street[1], street[2], street[3]))

    cars = []
    for i in range(car_count):
        car = file.readline()
        car = car.split()
        path = []
        street_count = int(car[0])
        for y in range(street_count):
            path.append(car[y + 1])
        cars.append(models.Car(street_count, path))

    for s in streets:
        print(s.__dict__)

    for c in cars:
        print(c.__dict__)

    return models.StreetSystem(sim_time, intersect_count, street_count, car_count, points, streets, cars)
