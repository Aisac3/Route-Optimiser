import { useNavigate } from "react-router-dom";

const RouteDetails = ({
  points = [],
  optimizedOrder = [],
  segmentDistances = [],
  distance = 0,
}) => {
  const navigate = useNavigate();

  // If no route calculated
  if (!optimizedOrder.length) {
    return (
      <div style={{ padding: "60px", textAlign: "center" }}>
        <h2>No Route Data Available</h2>
        <button
          onClick={() => navigate("/")}
          style={{
            marginTop: "20px",
            padding: "10px 20px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          Go Back to Map
        </button>
      </div>
    );
  }

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #f8fafc, #e2e8f0)",
        padding: "50px 20px",
      }}
    >
      <div style={{ maxWidth: "900px", margin: "0 auto" }}>
        {/* Header */}
        <div
          style={{
            marginBottom: "50px",
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <div>
            <h1 style={{ margin: 0, fontSize: "32px", fontWeight: "700" }}>
              Route Overview
            </h1>
            <p style={{ color: "#64748b", marginTop: "6px", fontSize: "16px" }}>
              Total Distance: <strong>{distance} km</strong>
            </p>
          </div>

          <button
            onClick={() => navigate("/")}
            style={{
              padding: "12px 20px",
              background: "#2563eb",
              color: "white",
              border: "none",
              borderRadius: "10px",
              cursor: "pointer",
              fontWeight: "600",
              boxShadow: "0 6px 15px rgba(37,99,235,0.3)",
            }}
          >
            ← Back to Map
          </button>
        </div>

        {/* Timeline Card */}
        <div
          style={{
            background: "white",
            borderRadius: "20px",
            padding: "50px",
            boxShadow: "0 25px 60px rgba(0,0,0,0.08)",
            position: "relative",
          }}
        >
          {/* Vertical Line */}
          <div
            style={{
              position: "absolute",
              left: "34px",
              top: "50px",
              bottom: "50px",
              width: "4px",
              background: "#e2e8f0",
              borderRadius: "2px",
            }}
          />

          {optimizedOrder.map((index, i) => (
            <div
              key={i}
              style={{
                position: "relative",
                paddingLeft: "90px",
                marginBottom: i === optimizedOrder.length - 1 ? "0" : "50px",
              }}
            >
              {/* Circle Indicator */}
              <div
                style={{
                  position: "absolute",
                  left: "18px",
                  top: "0",
                  width: "34px",
                  height: "34px",
                  borderRadius: "50%",
                  background:
                    i === 0
                      ? "#16a34a"
                      : i === optimizedOrder.length - 1
                        ? "#dc2626"
                        : "#2563eb",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: "white",
                  fontSize: "14px",
                  fontWeight: "bold",
                  boxShadow: "0 6px 15px rgba(0,0,0,0.15)",
                }}
              >
                {i + 1}
              </div>

              {/* Stop Name */}
              <div
                style={{
                  fontSize: "20px",
                  fontWeight: "600",
                  marginBottom: "8px",
                }}
              >
                {points[index]?.label}
              </div>

              {/* Segment Distance */}
              {i < segmentDistances.length && (
                <div
                  style={{
                    fontSize: "15px",
                    color: "#64748b",
                  }}
                >
                  Distance to next stop:{" "}
                  <strong>{segmentDistances[i]} km</strong>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RouteDetails;
