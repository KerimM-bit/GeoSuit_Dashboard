# Geospatial Suitability Analysis Dashboard


An interactive **geospatial decision-support dashboard** for evaluating summer pasture suitability using terrain constraints and vegetation indicators (NDVI).

The dashboard is designed to **communicate spatial insights clearly** to both technical and non-technical users, focusing on interpretation rather than raw processing ( Click the link below to see the dashboard via streamlit).
---
https://geosuitdashboard-pasture-suitability.streamlit.app 
---

## 🎯 Project Objective

This project aims to:
- Identify areas suitable for **summer pasture** in mountainous regions
- Provide **clear spatial context** using elevation data
- Validate suitability results using **NDVI (vegetation condition)**
- Present results through a **lightweight, interactive dashboard**

All heavy geospatial processing is performed **offline**.  
The dashboard focuses on **analysis, comparison, and interpretation**.

---

## 🧭 Dashboard Structure

The Streamlit application is organized into three analysis modes:

### 1️⃣ Regional Context & Criteria
Provides an overview of the **Karabakh region’s physical environment**, including:
- Elevation distribution
- Key terrain-based suitability constraints

This section answers:
> *Under what physical conditions is suitability evaluated?*

---

### 2️⃣ Single District Overview
Allows users to explore suitability results for individual districts.

Features:
- Suitability map (static, precomputed)
- Area-based comparison (Suitable vs Unsuitable)
- Summary metrics (total area, suitable area, percentage)

This section answers:
> *How suitable is a specific district for summer pasture?*

---

### 3️⃣ Suitability vs Vegetation Condition (NDVI)
Links suitability outputs with **mean NDVI values** to support validation.

Features:
- NDVI comparison between Suitable and Unsuitable areas
- Area vs NDVI relationship
- Automatically generated interpretive insight
- Optional spatial map showing NDVI–suitability relationship

This section answers:
> *Do suitable areas show better vegetation condition?*

---

## 🗺️ Suitability Criteria (Summary)

Suitability was evaluated using the following terrain-based constraints:

- **Elevation:** 1400–3000 m  
- **Slope:** < 20°  
- **Aspect:** North-facing slopes preferred  
- **Vegetation:** NDVI used for validation

These criteria reflect **known summer pasture characteristics** in mountainous regions and were applied consistently across all districts.

---

## 📊 Data Sources & Processing

- **DEM-derived layers:** Elevation, slope, aspect
- **Satellite data:** Sentinel-2 NDVI
- **Spatial analysis:** Polygon-based suitability classification
- **Validation:** Zonal statistics of NDVI by suitability class

> ⚠️ Note:  
> All raster processing, spatial modeling, and zonal statistics were performed **offline** using GIS and remote sensing tools.  
> The dashboard does **not** process rasters dynamically.

## 🚀 Technologies Used

- **Python**
- **Streamlit** – interactive dashboard
- **Pandas** – data handling
- **Plotly** – interactive charts
- **GIS / Remote Sensing tools** (offline processing)

---

## 👤 Author

**Karim Mirzayev**  
GIS & Remote Sensing Specialist  

This project was developed as part of applied geospatial analytics work, combining **GIS modeling**, **remote sensing validation**, and **decision-oriented visualization**.

---

## 📌 Disclaimer

This dashboard is intended for **exploratory analysis and decision support**.  
Results depend on input data quality, spatial resolution, and chosen criteria.

