import { useNavigate } from "react-router-dom";
import { useState } from "react";
import axios from "axios";

const Sidebar = ({
  optimize,
  points,
  distance,
  loading,
  clearPoints,
  optimizedOrder,
  segmentDistances,
  setPoints,
  removePoint, // ✅ add this
}) => {
  const navigate = useNavigate(); // ✅ INSIDE COMPONENT

  const [search, setSearch] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const handleSearch = async (value) => {
    setSearch(value);

    if (value.length < 3) {
      setSuggestions([]);
      return;
    }

    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/geocode?place=${value}`,
      );

      if (Array.isArray(res.data)) {
        setSuggestions(res.data);
      } else {
        setSuggestions([]);
      }
    } catch (err) {
      console.error(err);
      setSuggestions([]);
    }
  };

  const handleSelect = (place) => {
    const newPoint = {
      lat: place.lat,
      lng: place.lng,
      label: place.name,
    };

    setPoints((prev) => [...prev, newPoint]);
    setSearch("");
    setSuggestions([]);
  };

  return (
    <div
      style={{
        width: "340px",
        padding: "24px",
        background: "#ffffff",
        boxShadow: "2px 0 10px rgba(0,0,0,0.08)",
        overflowY: "auto",
      }}
    >
      <h2>🚀 SmartRoute</h2>

      <div style={{ marginTop: "20px", position: "relative" }}>
        <input
          type="text"
          value={search}
          placeholder="Search place (e.g., KSRTC)"
          onChange={(e) => handleSearch(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            borderRadius: "8px",
            border: "1px solid #ddd",
          }}
        />

        {suggestions.length > 0 && (
          <div
            style={{
              position: "absolute",
              top: "45px",
              left: 0,
              right: 0,
              background: "#ffffff",
              border: "1px solid #ddd",
              borderRadius: "8px",
              maxHeight: "200px",
              overflowY: "auto",
              zIndex: 1000,
            }}
          >
            {suggestions.map((s, i) => (
              <div
                key={i}
                onClick={() => handleSelect(s)}
                style={{
                  padding: "8px",
                  cursor: "pointer",
                  borderBottom: "1px solid #eee",
                }}
              >
                {s.name}
              </div>
            ))}
          </div>
        )}
      </div>

      <h4 style={{ marginTop: "20px" }}>Selected Stops</h4>

      <div style={{ marginTop: "10px" }}>
        {points.map((p, i) => (
          <div
            key={i}
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "8px 10px",
              background: "#f1f5f9",
              borderRadius: "8px",
              marginBottom: "6px",
            }}
          >
            <span style={{ fontSize: "14px" }}>
              {i + 1}. {p.label}
            </span>

            <button
              onClick={() => removePoint(i)}
              style={{
                background: "transparent",
                border: "none",
                color: "#ef4444",
                cursor: "pointer",
                fontWeight: "bold",
                fontSize: "16px",
              }}
            >
              ✕
            </button>
          </div>
        ))}
      </div>

      <button
        onClick={() => optimize(points)}
        disabled={points.length < 2}
        style={{
          width: "100%",
          padding: "12px",
          marginTop: "20px",
          background: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "8px",
        }}
      >
        {loading ? "Optimizing..." : "Optimize Route"}
      </button>

      <button
        onClick={clearPoints}
        style={{
          width: "100%",
          padding: "12px",
          marginTop: "10px",
          background: "#ef4444",
          color: "white",
          border: "none",
          borderRadius: "8px",
        }}
      >
        Clear Points
      </button>

      {distance && (
        <div
          style={{
            marginTop: "20px",
            padding: "12px",
            background: "#f3f4f6",
            borderRadius: "8px",
          }}
        >
          <strong>Total Distance:</strong> {distance} km
        </div>
      )}

      {optimizedOrder.length > 0 && (
        <div
          style={{
            marginTop: "20px",
            padding: "12px",
            background: "#e0f2fe",
            borderRadius: "8px",
          }}
        >
          <strong>Optimized Order:</strong>
          <p>
            {optimizedOrder.map((i, idx) => (
              <span key={idx}>
                {points[i]?.label}
                {idx !== optimizedOrder.length - 1 && " → "}
              </span>
            ))}
          </p>
        </div>
      )}

      <button
        onClick={() =>
          navigate("/details", {
            state: {
              points,
              optimizedOrder,
              segmentDistances,
              distance,
            },
          })
        }
        disabled={!distance}
        style={{
          width: "100%",
          padding: "12px",
          marginTop: "10px",
          background: "#0f172a",
          color: "white",
          border: "none",
          borderRadius: "8px",
          fontWeight: "600",
        }}
      >
        Advanced Route Details
      </button>
    </div>
  );
};

export default Sidebar;
