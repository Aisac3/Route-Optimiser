import { Routes, Route } from "react-router-dom";
import { useState } from "react";
import Home from "./pages/Home";
import RouteDetails from "./pages/RouteDetails";
import { useRouteOptimization } from "./hooks/useRouteOptimization";

function App() {
  const [points, setPoints] = useState([]);

  const {
    route,
    distance,
    loading,
    optimize,
    optimizedOrder,
    segmentDistances,
    reset,
  } = useRouteOptimization();

  const clearAll = () => {
    setPoints([]);
    reset();
  };

  const removePoint = (index) => {
    setPoints((prev) => prev.filter((_, i) => i !== index));
  };

  return (
    <Routes>
      <Route
        path="/"
        element={
          <Home
            points={points}
            setPoints={setPoints}
            route={route}
            distance={distance}
            loading={loading}
            optimize={optimize}
            optimizedOrder={optimizedOrder}
            segmentDistances={segmentDistances}
            clearAll={clearAll}
            removePoint={removePoint}
          />
        }
      />

      <Route
        path="/details"
        element={
          <RouteDetails
            points={points}
            optimizedOrder={optimizedOrder}
            segmentDistances={segmentDistances}
            distance={distance}
          />
        }
      />
    </Routes>
  );
}

export default App;