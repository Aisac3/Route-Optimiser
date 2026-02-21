# 🚀 Road Network Based Multi-Stop Route Optimization System

A full-stack route optimization system that computes near-optimal routes across multiple stops (20–50) using real OpenStreetMap road network data and heuristic graph algorithms.

---

## 📌 Project Overview

This project implements a district-level road network routing and multi-destination optimization engine.

Unlike systems that rely on paid APIs (e.g., Google Maps), this solution:

- Uses OpenStreetMap (OSM) road data
- Builds a local weighted graph
- Computes shortest paths using A* algorithm
- Solves the Traveling Salesman Problem (TSP)
- Refines solution using 2-Opt heuristic
- Visualizes optimized route using React + Leaflet

---

## 🧠 Core Features

- ✅ Real road-network based routing
- ✅ A* shortest path computation
- ✅ Distance matrix generation
- ✅ Nearest Neighbor TSP
- ✅ 2-Opt optimization refinement
- ✅ Full route reconstruction
- ✅ FastAPI backend
- ✅ React + Leaflet interactive map
- ✅ Optimized route visualization
- ✅ Total distance calculation

---

## 🏗️ System Architecture
User → React Frontend → FastAPI Backend
↓
OSM Road Graph
↓
A* Shortest Path Engine
↓
Distance Matrix
↓
TSP (NN + 2-Opt)
↓
Full Route Reconstruction
↓
Optimized Map Display


---

## 🛠️ Tech Stack

### Backend
- Python 3.x
- FastAPI
- OSMnx
- NetworkX
- NumPy
- Uvicorn

### Frontend
- React
- Leaflet
- React-Leaflet
- Axios

### Data Source
- OpenStreetMap (OSM)

---

## 📂 Project Structure
route-optimizer/
│
├── backend/
│ ├── app.py
│ ├── optimizer.py
│ ├── tsp_nn.py
│ ├── tsp_2opt.py
│ ├── ernakulam_drive.graphml
│
├── frontend/
│ ├── src/
│ └── package.json
│
└── README.md


---

# ⚙️ Setup Instructions

---

## 🔹 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd route-optimizer


2️⃣ Backend Setup
Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

Install Dependencies

pip install osmnx networkx numpy fastapi uvicorn scikit-learn

Run Backend Server

cd backend
uvicorn app:app --reload

Backend runs at:
http://127.0.0.1:8000

Swagger API docs:
http://127.0.0.1:8000/docs

3️⃣ Frontend Setup

cd frontend
npm install
npm start

Frontend runs at:http://localhost:3000

🧮 Algorithms Used
1️⃣ A* Shortest Path

Used to compute real road distances between stops.

2️⃣ Distance Matrix

Stores pairwise shortest path distances.

3️⃣ Nearest Neighbor (Greedy Heuristic)

Generates initial TSP solution.

Time Complexity: O(n²)

4️⃣ 2-Opt Optimization

Refines route by removing crossing edges.

Time Complexity: O(n³)

📊 Example Output

Optimized visiting order

Total road distance (meters/km)

Blue polyline visualization on map