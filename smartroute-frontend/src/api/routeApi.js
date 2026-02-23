import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const optimizeCoordinates = async (points) => {
  const payload = points.map(p => ({
    lat: p.lat,
    lng: p.lng
  }));

  const res = await axios.post(`${BASE_URL}/optimize-coordinates`, payload);
  return res.data;
};