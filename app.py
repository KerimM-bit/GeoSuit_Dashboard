


import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title="Pasture Suitability Dashboard",
    layout="wide"
)

st.title("Geospatial Suitability Analysis Dashboard")

# ------------------------
# Load data
# ------------------------
@st.cache_data
def load_data():
    df_main = pd.read_excel("data/suit_binary.xlsx")
    df_ndvi = pd.read_excel("data/Suitability_pasture_ha.xlsx")
    return df_main, df_ndvi

df_main, df_ndvi = load_data()

# ------------------------
# Sidebar
# ------------------------
st.sidebar.header("Analysis Controls")

analysis_mode = st.sidebar.radio(
    "Analysis mode",
    [
        "Regional context & criteria",
        "Single district overview",
        "Suitability vs NDVI"
    ]
)


# ------------------------
# Helper plot
# ------------------------
def plot_binary_bar(df, title):
    fig = px.bar(
        df_main,
        x="suitability",
        y="area_ha",
        color="suitability",
        title=title,
        color_discrete_map={
            "Suitable": "#2ecc71",
            "Unsuitable": "#e74c3c"
        }
    )
    fig.update_layout(showlegend=False)
    return fig

# ========================
# MODE 1 — Single district
# ========================
# ========================
# MODE 0 — Regional context
# ========================
if analysis_mode == "Regional context & criteria":

    st.subheader("Qarabagh region — physical context")

    col1, col2 = st.columns([1.3, 1])

    # ---- Elevation map ----
    with col1:
        st.markdown("### Elevation overview")
        st.image(
            "maps/elev_qarabagh_suit.jpg",
            use_column_width=True
        )

    # ---- Minimal criteria explanation ----
    with col2:
        st.markdown("### Suitability criteria (summary)")

        st.markdown(
            """
            - **Elevation:** 1400–3000 m  
            - **Slope:** < 20°  
            - **Aspect:** North (N) and North -East (NE) -> facing preferred  
            - **Vegetation:** NDVI-based validation
            """
        )

        st.markdown(
            """
            These criteria reflect **known summer pasture conditions**
            in mountainous regions and are used consistently across districts.
            """
        )

        # Optional small highlight
        st.info(
            "This dashboard visualizes precomputed suitability results "
            "based on terrain and vegetation characteristics."
        )

elif analysis_mode == "Single district overview":

    district = st.sidebar.selectbox(
        "Select district",
        sorted(df_main["district"].unique())
    )

    df_d = df_main[df_main["district"] == district]

    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.subheader(f"{district} — Suitability Map")
        img = Image.open(f"maps/{district.lower()}.jpg")
        st.image(img, use_column_width=True)

    with col2:
        st.subheader("Suitability distribution (ha)")
        st.plotly_chart(
            plot_binary_bar(df_d, f"{district} suitability"),
            use_container_width=True
        )

        total_area = df_d["area_ha"].sum()
        suitable_area = df_d[df_d["suitability"] == "Suitable"]["area_ha"].sum()
        pct = suitable_area / total_area * 100 if total_area > 0 else 0

        st.metric("Total area (ha)", f"{total_area:,.0f}")
        st.metric("Suitable area (ha)", f"{suitable_area:,.0f}")
        st.metric("Suitable (%)", f"{pct:.1f}%")

# ========================
# MODE 2 — Comparison
# ========================
else:
    st.subheader("Suitability vs Vegetation Condition (NDVI)")

    district = st.selectbox(
        "Select district",
        sorted(df_ndvi["district"].unique())
    )

    df_d = df_ndvi[df_ndvi["district"] == district]

    # --------------------
    # Tabs
    # --------------------
    tab1, tab2 = st.tabs(["📊 Analytics", "🗺️ Map view"])

    # ====================
    # TAB 1 — Analytics
    # ====================
    with tab1:
        col1, col2 = st.columns(2)

        # NDVI by suitability
        with col1:
            fig_ndvi = px.bar(
                df_d,
                x="suitability",
                y="ndvi_mean",
                color="suitability",
               # text_auto=".2f",
                title=f"{district} — Mean NDVI by suitability",
                color_discrete_map={
                    "Suitable": "#2ecc71",
                    "Unsuitable": "#e74c3c"
                }
            )
            fig_ndvi.update_layout(
                showlegend=False,
                yaxis_title="Mean NDVI"
            )
            st.plotly_chart(fig_ndvi, use_container_width=True)

        # NDVI vs area
        with col2:
            fig_area = px.scatter(
                df_d,
                x="ndvi_mean",
                y="area_ha",
                size="area_ha",
                color="suitability",
                title=f"{district} — NDVI vs area",
                color_discrete_map={
                    "Suitable": "#2ecc71",
                    "Unsuitable": "#e74c3c"
                }
            )
            fig_area.update_layout(
                xaxis_title="Mean NDVI",
                yaxis_title="Area (ha)"
            )
            st.plotly_chart(fig_area, use_container_width=True)

        # Auto insight
        ndvi_s = df_d[df_d["suitability"] == "Suitable"]["ndvi_mean"].values[0]
        ndvi_u = df_d[df_d["suitability"] == "Unsuitable"]["ndvi_mean"].values[0]
        diff = ndvi_s - ndvi_u

        st.markdown(
            f"""
            ### 🔍 Insight
            In **{district}**, areas classified as **Suitable** show a **higher mean NDVI**
            ({ndvi_s:.2f}) compared to **Unsuitable** areas ({ndvi_u:.2f}).

            **NDVI difference:** `{diff:.2f}`
            """
        )

    # ====================
    # TAB 2 — Map view
    # ====================
    with tab2:
        st.markdown("### NDVI – Suitability spatial relationship")

        map_path = f"maps/{district.lower()}_ndvi_suit.jpg"

        try:
            st.image(map_path, use_column_width=True)
        except:
            st.warning("Map image not found. Please check file name or path.")




