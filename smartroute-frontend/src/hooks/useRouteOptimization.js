import { useState } from "react";
import { optimizeCoordinates } from "../api/routeApi";

export const useRouteOptimization = () => {
  const [route, setRoute] = useState([]);
  const [distance, setDistance] = useState(null);
  const [loading, setLoading] = useState(false);
  const [optimizedOrder, setOptimizedOrder] = useState([]);
  const [segmentDistances, setSegmentDistances] = useState([]);

  const optimize = async (points) => {
    if (points.length < 2) {
      alert("Select at least 2 points");
      return;
    }

    setLoading(true);

    try {
      const data = await optimizeCoordinates(points);

      // Convert route to leaflet format
      const coords = data.route.map((p) => [p.lat, p.lng]);

      setRoute(coords);
      setDistance(data.total_distance_km);
      setOptimizedOrder(data.optimized_order);

      // ✅ Use REAL segment distances from backend
      setSegmentDistances(data.segment_distances || []);

      setLoading(false);

      return data;
    } catch (err) {
      console.error(err);
      alert("Route calculation failed");
      setLoading(false);
    }
  };

  // Reset everything
  const reset = () => {
    setRoute([]);
    setDistance(null);
    setOptimizedOrder([]);
    setSegmentDistances([]);
  };

  return {
    route,
    distance,
    loading,
    optimize,
    optimizedOrder,
    segmentDistances,
    reset,
  };
};
