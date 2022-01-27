from typing import List

from Xlib.protocol.structs import Segment

class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination

class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return ' -> '.join(stops)
    @property
    def departure_point(self):
        return self.segments[0].departure

    @departure_point.setter
    def departure_point(self, var):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=var, destination=dest)


flight = Flight([Segment('GLA', 'LHR')])
print(flight)
flight.departure_point = "Eddingsburg"
print(flight)

