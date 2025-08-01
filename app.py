import pandas as pd
import plotly.express as px
import streamlit as st

# Load data with latin1 encoding to avoid UnicodeDecodeError
df = pd.read_csv("data/top10s.csv", encoding='latin1')

# Clean column names: strip spaces, lowercase, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Debug: print columns before renaming
print("Columns after cleaning:", df.columns.tolist())

# Rename columns only if they exist
rename_dict = {}
if 'bpm' in df.columns:
    rename_dict['bpm'] = 'tempo'
if 'valence_' in df.columns:
    rename_dict['valence_'] = 'valence'
if 'nrgy' in df.columns:
    rename_dict['nrgy'] = 'energy'

df.rename(columns=rename_dict, inplace=True)

# Debug: print columns after renaming
print("Columns after renaming:", df.columns.tolist())

# Sidebar controls with friendly names mapped to actual columns
st.sidebar.title("🎧 Spotify Trends Explorer")

feature_map = {
    'Valence': 'val',
    'Tempo': 'tempo',
    'Energy': 'energy'
}

choice = st.sidebar.selectbox("Choose a feature to explore:", list(feature_map.keys()))
feature = feature_map[choice]

# Check if selected feature exists in dataframe
if feature not in df.columns:
    st.error(f"Feature '{feature}' not found in data columns: {df.columns.tolist()}")
else:
    # Compute averages grouped by year
    avg_features = df.groupby('year')[[feature]].mean().reset_index()

    # Main view
    st.title("📊 Spotify Music Trends (2010–2019)")
    st.write(f"How has **{choice}** changed over time?")

    fig = px.line(avg_features, x='year', y=feature,
                  title=f"Average {choice} by Year",
                  markers=True, template="plotly_dark")

    st.plotly_chart(fig)
