Spotify Music Trends Dashboard
==============================

Overview
--------
This project is an interactive dashboard built with Streamlit and Plotly that visualizes how key audio features of popular Spotify songs have changed over time (2010-2019). Users can explore trends in song features such as valence (musical positivity), tempo (beats per minute), and energy.

Dataset
-------
- Source: Kaggle Spotify dataset (top10s.csv)
- Contains audio features and metadata for Spotify’s top songs from 2010 to 2019.
- Stored in the `data/` folder.

Features
--------
- Sidebar dropdown to select audio features: valence, tempo, energy.
- Line chart showing average feature values per year.
- Interactive and visually appealing Plotly charts embedded in Streamlit.

Requirements
------------
- Python 3.12+
- pandas
- plotly
- streamlit

Setup Instructions
------------------
1. Clone or download this repository.
2. Navigate to the project folder in terminal.
3. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate       # On Linux/macOS
   venv\Scripts\activate          # On Windows
