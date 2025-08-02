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

    # === Add this block below ===

    # Let user select year for top artists/songs
    years = df['year'].sort_values().unique()
    selected_year = st.sidebar.selectbox("Select year for top artists/songs:", years)

    # Filter data by selected year
    df_year = df[df['year'] == selected_year]

    st.header(f"Top Spotify Trends for {selected_year}")

    # Top Artists
    if 'artist' in df_year.columns:
        top_artists = df_year['artist'].value_counts().head(10)
        st.subheader("Top 10 Artists")
        for artist, count in top_artists.items():
            st.write(f"{artist} — {count} songs")

    # Top Genres (if available)
    if 'genre' in df_year.columns:
        top_genres = df_year['genre'].value_counts().head(10)
        st.subheader("Top 10 Genres")
        for genre, count in top_genres.items():
            st.write(f"{genre} — {count} songs")
    else:
        st.info("Genre data not available in dataset.")

    # Top Songs
    if 'track_name' in df_year.columns:
        top_songs = df_year['track_name'].value_counts().head(10)
        st.subheader("Top 10 Songs")
        for song, count in top_songs.items():
            st.write(f"{song} — {count} occurrences")

