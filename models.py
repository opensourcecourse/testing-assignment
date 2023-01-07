"""Pydantic Models for testing module."""
from __future__ import annotations

import json
from functools import cache
from pathlib import Path

from pydantic import BaseModel, Field


def to_camel(snake_str):
    """Function to convert snake_case to camelCase."""
    first, *others = snake_str.split("_")
    return "".join([first.lower(), *map(str.title, others)])


class CamelModel(BaseModel):
    """
    A model which converts to/from camelCase.

    This allows models to be defined in snake_case but ingest json data
    which uses camelCase.
    """

    class Config:
        """Configuration for model."""

        alias_generator = to_camel
        allow_population_by_field_name = True


class Planet(CamelModel):
    """A model for a planet (or former planet)."""

    id: int
    name: str
    mass: float
    diameter: float
    density: float
    gravity: float
    escape_velocity: float
    rotation_period: float
    length_of_day: float
    distance_from_sun: float
    perihelion: float
    aphelion: float
    orbital_period: float
    orbital_velocity: float
    orbital_inclination: float
    orbital_eccentricity: float
    obliquity_to_orbit: float
    mean_temperature: float
    surface_pressure: float | None
    number_of_moons: int
    has_ring_system: bool
    has_global_magnetic_field: bool
    satellites: list[Satellite] = []


class Satellite(CamelModel):
    """A model for satellites of planets."""

    id: int
    planet_id: int
    name: str
    gm: float
    radius: float = Field(ge=0)
    density: float | None = None
    magnitude: float | None = None
    albedo: float | None = Field(ge=0, le=2.0, default=None)
    # Note albedo is geometric albedo; it can be gt 1 (shorturl.at/akv07)


@cache
def load_data(data_path):
    """Load the data into pydantic models."""
    planet_path = data_path / "planets.json"
    satellite_path = data_path / "satellites.json"
    with planet_path.open("r") as fi:
        planet_data = json.load(fi)
        planets = [Planet(**x) for x in planet_data]
    with satellite_path.open("r") as fi:
        satellite_data = json.load(fi)
        satellites = [Satellite(**x) for x in satellite_data]
    planet_dict = {x.id: x for x in planets}
    for satellite in satellites:
        planet_dict[satellite.planet_id].satellites.append(satellite)
    return planets


if __name__ == "__main__":
    # test that models can ingest data.
    data_path = Path(__file__).absolute().parent / "data"
    planets = load_data(data_path)
