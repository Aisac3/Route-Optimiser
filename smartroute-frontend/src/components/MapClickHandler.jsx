import { useMapEvents } from "react-leaflet";
import axios from "axios";

const MapClickHandler = ({ setPoints }) => {
  useMapEvents({
    async click(e) {
      const { lat, lng } = e.latlng;

      try {
        const res = await axios.get(
          `http://127.0.0.1:8000/geocode?lat=${lat}&lng=${lng}`
        );

        const newPoint = {
          lat,
          lng,
          label: res.data?.name || `Location ${lat.toFixed(3)}, ${lng.toFixed(3)}`
        };

        setPoints(prev => [...prev, newPoint]);
      } catch (err) {
        console.error("Reverse geocode failed");

        const newPoint = {
          lat,
          lng,
          label: `Location ${lat.toFixed(3)}, ${lng.toFixed(3)}`
        };

        setPoints(prev => [...prev, newPoint]);
      }
    }
  });

  return null;
};

export default MapClickHandler;