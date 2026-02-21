# 🚀 SmartRoute -- Intelligent Route Optimization System

SmartRoute is a full-stack route optimization platform that computes the
most efficient travel path between multiple stops using real-world road
network data.

The system leverages graph theory, shortest-path algorithms, and
Traveling Salesman Problem (TSP) optimization techniques to generate
optimized routes with segment-level distance breakdown and professional
visualization.

------------------------------------------------------------------------

## 📌 Project Highlights

-   🗺 Interactive map-based stop selection\
-   🔎 Location search with geocoding\
-   📍 Real road-network routing using OSMnx\
-   ⚡ TSP-based multi-stop optimization\
-   📊 Segment-wise distance calculation\
-   🧭 Advanced timeline route visualization\
-   🔁 State persistence across pages\
-   🧹 Smart clear & stop deletion functionality

------------------------------------------------------------------------

## 🏗️ System Architecture

``` mermaid
flowchart TD
    A[React Frontend - Leaflet Map] --> B[FastAPI Backend]
    B --> C[Graph Service - OSMnx]
    C --> D[NetworkX Road Graph]
    B --> E[TSP Optimization Engine]
    E --> F[Distance Matrix Builder]
    F --> G[Nearest Neighbor Algorithm]
    G --> H[2-Opt Optimization]
    H --> B
    B --> A
```

------------------------------------------------------------------------

## 🧠 Algorithms Used

### 🔹 Shortest Path

-   Implemented using `networkx.shortest_path`
-   Edge weight: road length (meters)

### 🔹 Traveling Salesman Problem (TSP)

1.  Nearest Neighbor (Initial solution)
2.  2-Opt Optimization (Route refinement)

### 🔹 Distance Matrix

-   Pairwise shortest path distance calculation
-   Cached for performance optimization

------------------------------------------------------------------------

## 🛠️ Tech Stack

### Frontend

-   React (Vite)
-   React Router
-   Leaflet.js
-   Axios

### Backend

-   FastAPI
-   OSMnx
-   NetworkX
-   NumPy
-   Pydantic

### Version Control

-   Git
-   GitHub

------------------------------------------------------------------------

## 📂 Project Structure

    Route-Optimiser/
    │
    ├── frontend/
    │   ├── src/
    │   │   ├── components/
    │   │   ├── pages/
    │   │   ├── hooks/
    │   │   └── api/
    │
    ├── backend/
    │   ├── app/
    │   │   ├── services/
    │   │   ├── main.py
    │
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

``` bash
git clone https://github.com/Arjun-P-Manoj/Route-Optimiser.git
cd Route-Optimiser
```

### 2️⃣ Backend Setup

``` bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs at:

http://127.0.0.1:8000

### 3️⃣ Frontend Setup

``` bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

http://localhost:5173

------------------------------------------------------------------------

## 📡 API Endpoint Example

### POST /optimize-coordinates

Request:

``` json
[
  {"lat": 10.52, "lng": 76.21},
  {"lat": 10.54, "lng": 76.23}
]
```

Response:

``` json
{
  "optimized_order": [0, 1],
  "total_distance_km": 12.45,
  "segment_distances": [12.45],
  "route": [...]
}
```

------------------------------------------------------------------------

## ✨ Key Improvements

-   Global route state management
-   Real backend-calculated segment distances
-   Professional timeline UI
-   Stop deletion support
-   Large graph file handling with .gitignore

------------------------------------------------------------------------

## 📈 Future Enhancements

-   Estimated travel time calculation
-   Traffic-aware routing
-   Cloud deployment (Docker + AWS)
-   User authentication & saved routes

------------------------------------------------------------------------

## 👨‍💻 Author

**Arjun P Manoj**\
Final Year B.Tech Computer Science\
GitHub: https://github.com/Arjun-P-Manoj

------------------------------------------------------------------------

## 📄 License

Developed for academic and research purposes.
