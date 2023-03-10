"""First introduction to pytest."""
from types import MappingProxyType

# import models
# import pydantic
# import pytest

# example data to create Europa Satellite
BASE_DATA = MappingProxyType(
    {
        "id": 5,
        "planetId": 5,
        "name": "Europa",
        "gm": 3202.739,
        "radius": 1560.8,
        "density": 3.013,
        "magnitude": 5.29,
        "albedo": 0.67,
    }
)


class TestSatelliteInit:
    """Tests for basic operations with Satellite."""

    def test_base_case(self):
        """Ensure the base case is parsable."""
        # You might start by loading in the base data like this
        # europa = models.Satellite(**BASE_DATA)

        # Add some sensible asserts here

    def test_round_trip(self):
        """Ensure data can be round-tripped to/from dict."""
        # Here round-tripped means converted to and from a dict, and the two
        # dicts are identical (check equality).
        # Hint: Satellite.dict(by_alias=True) generates output.

    def test_missing_optional_fields(self):
        """
        Test optional data filled in.

        Ensure if the optional fields of Satellite (have default values)
        are missing the data are still parsable.
        """
        # Hint: be sure to copy BASE_DATA so you can modify them, like this:
        # data = dict(BASE_DATA)  # then modify data as a normal dict.

    def test_read_from_file(self):
        """Ensure data can be read from a file using Satellite.parse_file."""
        # Hint: First save the data to a json file using json module and
        # one of pytest's temp file fixtures:
        # https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html


class TestSatelliteFieldTypes:
    """Tests for field type coercion."""

    def test_id_float(self):
        """Ensure when the id field is a float it is coerced to an int."""

    def test_id_str(self):
        """Ensure when the id field is a string it is coerced to an int."""

    def test_string_radius_raises(self):
        """Ensure a string radius (eg 'bob') raises a ValidationError."""
        # Hint: import ValidationError from pydantic and use pytest.raises

    def test_negative_albedo_raises(self):
        """Ensure a negative albedo raises a ValidationError."""

    def test_many_radii(self, radius):
        """Test many different radii work for creating a Satellite object."""
        # Hint: you need to parametrize this test with several values > 0.
        # see: https://docs.pytest.org/en/6.2.x/parametrize.html
