
from hypothesis import given, strategies as st
from irrigation_scheduler import (
    parse_zone,
    moisture_average,
    water_needed
)


# Test 1: parse_zone should not crash for unexpected inputs
@given(st.text() | st.none())
def test_parse_zone_no_crash(s):
    try:
        parse_zone(s)
    except (ValueError, TypeError, AttributeError):
        assert False, f"parse_zone crashed with input: {s!r}"


# Test 2: moisture_average should not crash for unexpected inputs
@given(st.text() | st.none())
def test_moisture_average_no_crash(s):
    try:
        moisture_average(s)
    except (ValueError, TypeError, AttributeError, ZeroDivisionError):
        assert False, f"moisture_average crashed with input: {s!r}"


# Test 3: water_needed should not crash for unexpected inputs
@given(st.text() | st.none())
def test_water_needed_no_crash(s):
    try:
        water_needed(s)
    except (ValueError, TypeError, AttributeError):
        assert False, f"water_needed crashed with input: {s!r}"


# Test 4: Valid moisture readings should have correct averages
@given(st.lists(st.integers(min_value=0), min_size=1))
def test_moisture_average_correct(readings):
    csv = ",".join(map(str, readings))
    expected = sum(readings) // len(readings)

    assert moisture_average(csv) == expected
