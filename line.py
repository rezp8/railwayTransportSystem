class Line:
    def __init__(self, name, origin, destination, station_count, stations):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.station_count = station_count
        self.stations = stations 
    def __str__(self):
        return (f"Line '{self.name}' from {self.origin} to {self.destination}, "
                f"stations: {self.station_count}, list: {', '.join(self.stations)}")