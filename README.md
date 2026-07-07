# GeoGuardAI: Intelligent Route Resilience Terminal

GeoGuardAI is an AI-powered geospatial platform designed to transform raw satellite imagery into a "self-healing," resilient urban road network. Moving beyond static mapping, our platform acts as a "digital doctor" for urban infrastructure, diagnosing network vulnerabilities before disaster strikes.

## 🚀 Mission
Disasters don't wait for clear skies, but traditional mapping systems do. GeoGuardAI bridges the gap between raw LISS-IV/Cartosat satellite data and actionable emergency response, enabling urban planners to visualize road bottlenecks, simulate disaster scenarios, and optimize emergency transit paths in real-time.

## 🏗️ Architecture
Our pipeline follows an end-to-end geospatial intelligence workflow:
1. **Perception Layer:** Sliding-window inference using occlusion-aware FPN/SegFormer models to extract road networks under tree canopy and shadow cover.
2. **Topology Layer:** Graph skeletonization and MST-based healing to bridge fragmented road masks into a fully routable network graph.
3. **Intelligence Layer:** Betweenness-centrality and disaster-simulation math to identify critical "Gatekeeper Nodes."
4. **Application Layer:** Interactive GIS dashboard for explainable decision support.

## 🛠️ Tech Stack
* **AI/ML:** PyTorch, Albumentations, OpenCV, Rasterio/GDAL.
* **Graph Logic:** NetworkX, OSMnx.
* **Backend:** FastAPI, PostgreSQL, PostGIS.
* **Frontend:** React.js, Tailwind CSS, Leaflet.js.
* **DevOps:** Docker, Nginx.

## 🏁 Development Roadmap
* **Week 1:** Foundation, Data Ingestion, and Environment Setup.
* **Week 2:** Core Engineering (Model Training & Graph Construction).
* **Week 3:** Integration (Self-Healing Loop & API Integration).
* **Week 4:** Visualization, Documentation, and Final Pitch Deck Polish.

## ⚙️ Setup Instructions
```bash
# 1. Clone the repository
git clone [https://github.com/your-org/GeoGuardAI.git](https://github.com/your-org/GeoGuardAI.git)
cd GeoGuardAI

# 2. Setup Backend/AI Environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Setup Frontend
cd frontend
npm install
npm run dev
