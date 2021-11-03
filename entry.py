from dataclasses import dataclass


@dataclass(repr=True)
class Entry:
    callsign: str
    name: str
    date: str
    time: str
    mode: str
    band: str
    country: str
    state: str
    city: str
    coordinates: list  # possibly change to tuple
    talk_group: str
    other: str
    tags: list
