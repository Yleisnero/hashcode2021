import streets_parser

if __name__ == '__main__':
    input_file = "f.txt"
    street_system = streets_parser.read_input(input_file)

    intersections = []
    for i in range(street_system.intersection_count):
        incoming_streets = []
        for s in street_system.streets:
            if s.end == i:
                incoming_streets.append(s)
        intersections.append(incoming_streets)

    output_file = open("1_output_f.txt", "w")
    output_file.write(f"{street_system.intersection_count}\n")
    inter_count = 0
    for inter in intersections:
        # ID
        output_file.write(f"{inter_count}\n")
        inter_count += 1
        # Number of streets
        output_file.write(f"{len(inter)}\n")
        # Green lights
        for street in inter:
            # give every street one second
            output_file.write(f"{street.name} 1\n")
