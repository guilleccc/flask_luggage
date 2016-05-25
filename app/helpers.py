import config
from datetime import datetime
import json
import string
import os

def currentyear():
    return datetime.now().year


def locations(selected_locations):
    try:
        selected_locations = json.loads(selected_locations) if selected_locations else dict()
    except ValueError, e:
        return selected_locations if selected_locations else ''

    locations_filtered = {key: value for key, value in selected_locations.iteritems() if value}
    keys = []

    if locations_filtered:
        keys = locations_filtered.keys()
        keys.sort(key=string.lower)

    return ' '.join(keys)


def is_production():
    return config.PRODUCTION in os.getenv('FLAKS_CONFIGURATION', '')