import {
  MapContainer,
  TileLayer,
  Polyline,
  Marker,
  Popup,
  LayersControl,
  useMapEvents
} from "react-leaflet";
import { useEffect } from "react";

/* ================================
   MAP CLICK HANDLER
================================ */
function MapClickHandler({ setPoints }) {
  useMapEvents({
    async click(e) {
      const { lat, lng } = e.latlng;

      try {
        const res = await fetch(
          `http://127.0.0.1:8000/geocode?lat=${lat}&lng=${lng}`
        );

        const data = await res.json();

        const newPoint = {
          lat,
          lng,
          label:
            data?.name ||
            `Location ${lat.toFixed(4)}, ${lng.toFixed(4)}`
        };

        setPoints(prev => [...prev, newPoint]);

      } catch (error) {
        console.error("Reverse geocoding failed:", error);

        setPoints(prev => [
          ...prev,
          {
            lat,
            lng,
            label: `Location ${lat.toFixed(4)}, ${lng.toFixed(4)}`
          }
        ]);
      }
    }
  });

  return null;
}

/* ================================
   MAIN MAP COMPONENT
================================ */
const MapView = ({ points, setPoints, route }) => {
  return (
    <MapContainer
      center={[10.5276, 76.2144]} // Thrissur center
      zoom={12}
      style={{ height: "100%", width: "100%" }}
    >
      {/* 🌍 BASE MAP SWITCHER */}
      <LayersControl position="topright">
        <LayersControl.BaseLayer checked name="Street">
          <TileLayer
            attribution="© OpenStreetMap contributors"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
        </LayersControl.BaseLayer>

        <LayersControl.BaseLayer name="Satellite">
          <TileLayer
            attribution="Tiles © Esri"
            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
          />
        </LayersControl.BaseLayer>
      </LayersControl>

      {/* 🖱 CLICK HANDLER */}
      <MapClickHandler setPoints={setPoints} />

      {/* 📍 MARKERS */}
      {points.map((p, i) => (
        <Marker key={i} position={[p.lat, p.lng]}>
          <Popup>
            <strong>Stop {i + 1}</strong>
            <br />
            {p.label}
          </Popup>
        </Marker>
      ))}

      {/* 🛣 ROUTE LINE */}
      {route.length > 0 && (
        <Polyline
          positions={route}
          pathOptions={{
            color: "#2563eb",
            weight: 5
          }}
        />
      )}
    </MapContainer>
  );
};

export default MapView;