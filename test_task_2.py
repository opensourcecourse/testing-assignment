"""Task for learning pytest fixtures and marks."""
import models

# Mutable Global state is evil, don't try this at home.
UGLY_STATE = {"setup": False, "teardown": False}


def planets():
    """A fixture which returns a list of planets once per session."""
    # Hint: use load_data from models to, well, load the data.


def jupiter():
    """A fixture which returns a new instance of jupiter for each use."""
    # Hint: use the load data function in models, find jupiter, return
    # a copy. Ensure the scope parameter is set right in the fixture
    # decorator. You can use `deepcopy` from the copy module or the copy
    # method on the Satellite instance.


def satellite():
    """A parametrized fixture which returns each moon for all planets."""
    # Hint: https://docs.pytest.org/en/6.2.x/fixture.html#parametrizing-fixtures


def setup_teardown_fixture():
    """
    A function scoped fixture which does setup and teardown.

    For setup set UGLY_STATE['setup'] = True and for teardown set
    UGLY_STATE['setup'] = True. Yield 42 as the value for this fixture.
    """


class TestPlanetsFixture:
    """Tests for the planets fixture."""

    def test_planet_length_and_type(self, planets):
        """Ensure a sequence of 9 is returned."""
        assert len(planets) == 9
        for planet in planets:
            assert isinstance(planet, models.Planet)


class TestJupiterFixture:
    """Tests for the jupiter fixture."""

    def test_modify(self, jupiter):
        """
        Tests that a new jupiter is returned each time.

        If this is not the case, downstream tests will fail.
        """
        jupiter.name = "not_jupiter_any_more"

    def test_is_jupiter(self, jupiter):
        """Ensure the fixture returns jupiter."""
        assert jupiter.name.lower() == "jupiter"


class TestSatelliteFixture:
    """Tests for the moon fixture, which should be parametrized."""

    found_satellites = []

    def test_single_moon(self, satellite):
        """Ensure a single moon was returned."""
        assert isinstance(satellite, models.Satellite)
        self.found_satellites.append(satellite)

    def teardown_class(self):
        """Ensure all satellites were found."""
        planets = models.load_data()
        moon_count = sum([len(x.satellites) for x in planets])
        assert len(self.found_satellites) == moon_count


class TestSetupTearDownFixture:
    """Tests to ensure the setting up and tearing down worked."""

    def setup_class(self):
        """Ensure fixture setup hasn't yet run."""
        assert not UGLY_STATE["setup"]
        assert not UGLY_STATE["teardown"]

    def test_fixture_values(self, setup_teardown_fixture):
        """Ensure requested value is returned."""
        assert UGLY_STATE["setup"]
        assert setup_teardown_fixture == 42
        assert not UGLY_STATE["teardown"]

    def teardown_class(self):
        """Ensure teardown flag was switched."""
        assert UGLY_STATE["setup"]
        assert UGLY_STATE["teardown"]
