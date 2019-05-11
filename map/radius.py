from map.unchanged import *


class Circle:
    def __init__(self, coords, entrances=0, exits=0):
        self.coords = coords
        self.entrances = entrances
        self.exits = exits

    def get_district(self):
        if BRONX[0][0] <= self.coords[0] <= BRONX[1][0] and BRONX[0][1] <= self.coords[1] <= BRONX[1][1]:
            return BRONX_AREA

        elif MANHATTAN[0][0] <= self.coords[0] <= MANHATTAN[1][0] and MANHATTAN[0][1] <= self.coords[1] <= MANHATTAN[1][1]:
            return MANHATTAN_AREA

        elif BROOKLYN[0][0] <= self.coords[0] <= BROOKLYN[1][0] and BROOKLYN[0][1] <= self.coords[1] <= BROOKLYN[1][1]:
            return BROOKLYN_AREA

        elif QUEENS[0][0] <= self.coords[0] <= QUEENS[1][0] and QUEENS[0][1] <= self.coords[1] <= QUEENS[1][1]:
            return QUEENS_AREA
        else:
            return BRONX_AREA

    def abs_of_people(self):
        return abs(self.entrances - self.exits)

    def count_radius(self):
        for_one_km = int(self.abs_of_people() // self.get_district())
        coef = 10 ** (-len(str(for_one_km)) + 1)
        return int(for_one_km * coef) * 10


if __name__ == "__main__":
    circ = Circle([40.759901, -73.984139], 6041196, 37111525)
    print(circ.get_district())
    # print(circ.area)
    print(circ.abs_of_people())
    print(circ.count_radius())
    # print(circ.radius)
