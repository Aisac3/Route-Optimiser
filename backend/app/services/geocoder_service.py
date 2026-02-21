from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from app.config import DISTRICT_NAME


class GeocoderService:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="smart_route_app")

    # 🔎 Forward Geocoding (Search by name)
    def geocode_location(self, place_name: str):
        try:
            query = f"{place_name}, {DISTRICT_NAME}"

            locations = self.geolocator.geocode(
                query,
                exactly_one=False,
                limit=5
            )

            if not locations:
                return None

            results = []
            for loc in locations:
                results.append({
                    "lat": loc.latitude,
                    "lng": loc.longitude,
                    "name": loc.address
                })

            return results

        except GeocoderTimedOut:
            return None

    # 📍 Reverse Geocoding (Click on map)
    def reverse_geocode(self, lat: float, lng: float):
        try:
            location = self.geolocator.reverse((lat, lng))

            if not location:
                return None

            return {
                "lat": lat,
                "lng": lng,
                "name": location.address
            }

        except GeocoderTimedOut:
            return None


geocoder_service = GeocoderService()