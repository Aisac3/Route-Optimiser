import Sidebar from "../components/Sidebar";
import MapView from "../components/MapView";

const Home = ({
  points,
  setPoints,
  route,
  distance,
  loading,
  optimize,
  optimizedOrder,
  segmentDistances,
  clearAll,
  removePoint,
}) => {
  return (
    <div style={{ display: "flex", height: "100vh", background: "#f8fafc" }}>
      <Sidebar
        optimize={() => optimize(points)}
        points={points}
        distance={distance}
        loading={loading}
        clearPoints={clearAll}
        optimizedOrder={optimizedOrder}
        segmentDistances={segmentDistances}
        setPoints={setPoints}
        removePoint={removePoint}
      />

      <div style={{ flex: 1 }}>
        <MapView points={points} setPoints={setPoints} route={route} />
      </div>
    </div>
  );
};

export default Home;