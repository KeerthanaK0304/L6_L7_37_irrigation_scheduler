
import math


def parse_zone(text):
    if not isinstance(text, str):
        return None

    if text.count(':') != 1:
        return None

    name, area = text.split(':')

    name = name.strip()

    if not name:
        return None

    try:
        area = float(area)
    except ValueError:
        return None

    if not math.isfinite(area) or area < 0:
        return None

    return name.title(), area


def moisture_average(readings_csv):
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        return None

    try:
        values = [int(r.strip()) for r in readings_csv.split(',')]

        if any(v < 0 for v in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError, ZeroDivisionError):
        return None


def water_needed(text):
    if not isinstance(text, str):
        return None

    if text.count('|') != 1:
        return None

    plot, rain = text.split('|')

    try:
        plot = float(plot)
        rain = float(rain)
    except ValueError:
        return None

    if not math.isfinite(plot) or not math.isfinite(rain):
        return None

    if plot < 0 or rain < 0:
        return None

    need = plot * 5 - rain

    return max(need, 0)


def main():
    print("==== Running parse_zone ====")
    user_input = input("Enter zone:area in m2 (e.g. north:120): ")
    result = parse_zone(user_input)
    print("Zone and Area:", result)

    print("\n==== Running moisture_average ====")
    user_input = input("Enter moisture readings as CSV (e.g. 40,35,50): ")
    result = moisture_average(user_input)
    print("Average Moisture:", result)

    print("\n==== Running water_needed ====")
    user_input = input("Enter area|rainfall (e.g. 120|8): ")
    result = water_needed(user_input)
    print("Water Needed:", result)


if __name__ == "__main__":
    main()
