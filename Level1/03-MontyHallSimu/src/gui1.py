import time
import streamlit as st
import pandas as pd
import numpy as np
from main import simulate_game

# Set page configuration
st.set_page_config(page_title="Monty Hall Simulation", layout="wide")

# Add a header image (Replace with a suitable URL or local image)
st.image('images/1.jpg', width=300)

# Title and description with improved fonts and colors
st.title("Monty Hall Problem Simulation 🏆🚪")
st.markdown(
    """
    ### Welcome to the Monty Hall Simulation!

    The **Monty Hall Problem** is a famous probability puzzle that originated from a game show called *Let's Make a Deal*. In the game, there are 3 doors:

    - Behind one door is a car (the prize).
    - Behind the other two doors are goats (no prize).

    You pick one door, then the host (Monty Hall) opens another door that has a goat behind it. Monty then offers you the chance to switch to the remaining door. 

    The question is: **Is it better to stick with your original choice, or should you switch?**

    This simulation will show you how your chances of winning change based on whether you switch doors or not. We will run multiple simulations to see the results.

    **Let's see if switching doors really gives you a higher chance of winning!**
    """
)

# User input with styled text
num_games = st.number_input("Enter the number of simulations to run:", min_value=1, max_value=100000, value=1000, step=500)

# Layout setup
col1, col2 = st.columns(2)
col1.subheader("Win Percentage Without Switching")
col2.subheader("Win Percentage With Switching")

# Initialize progress bar and placeholders
progress_bar = st.progress(0)
chart_placeholder1 = col1.empty()
chart_placeholder2 = col2.empty()

# Running simulation
wins_no_switch = 0
wins_switch = 0
progress_interval = max(1, num_games // 100)  # Update progress bar at intervals

data_no_switch = []
data_switch = []
indices = []

for i in range(1, num_games + 1):
    num_wins_without_switching, num_wins_with_switching = simulate_game(1)
    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching
    
    win_rate_no_switch = wins_no_switch / i
    win_rate_switch = wins_switch / i
    
    data_no_switch.append(win_rate_no_switch)
    data_switch.append(win_rate_switch)
    indices.append(i)
    
    if i % progress_interval == 0 or i == num_games:
        progress_bar.progress(i / num_games)
        
        df_no_switch = pd.DataFrame({
            "Simulations": indices,
            "Win Rate": data_no_switch
        })
        df_switch = pd.DataFrame({
            "Simulations": indices,
            "Win Rate": data_switch
        })
        
        chart_placeholder1.line_chart(df_no_switch.set_index("Simulations"))
        chart_placeholder2.line_chart(df_switch.set_index("Simulations"))

# Final results with custom styling
st.subheader("Final Results 🎉")
st.write(f"**Win percentage without switching:** {wins_no_switch / num_games:.2%}", unsafe_allow_html=True)
st.write(f"**Win percentage with switching:** {wins_switch / num_games:.2%}", unsafe_allow_html=True)

# Add additional styling and background color
st.markdown("""
    <style>
        .css-1v3fvcr {
            background-color: #f4f4f4;
        }
        .css-ffhzg2 {
            color: #ff6347; 
            font-weight: bold;
        }
        h1, h2, h3, h4 {
            color: #0066cc;
        }
        .stProgress {
            background-color: #ffa500;
        }
    </style>
""", unsafe_allow_html=True)
