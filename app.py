import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.title("My first Streamlit App")

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load data set
data =pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")


# Load the dataset
data = sns.load_dataset("penguins").dropna()  # Drop missing values for cleaner plots

# Streamlit App Title
st.title("Interactive Streamlit Scatter Chart")

# Sidebar for filtering options
st.sidebar.header('Filter the Options')

# Category selection dropdown
species_options = ['All'] + list(data['species'].unique())  # Add "All" option
selected_category = st.sidebar.selectbox('Select Category', options=species_options)

# Filter the dataset based on selection
if selected_category != 'All':
    filtered_data = data[data['species'] == selected_category]
else:
    filtered_data = data  # Show full dataset if "All" is selected

# Streamlit Scatter Chart
st.subheader("Streamlit Scatter Plot")
st.scatter_chart(filtered_data, x='flipper_length_mm', y='body_mass_g', color='species')

# Seaborn Scatter Plot
st.subheader("Seaborn Scatter Plot")

# Select a numerical column for the histogram
hist_col = st.sidebar.selectbox("Select Column for Histogram", ["body_mass_g", "flipper_length_mm", "bill_length_mm"])

# Create histogram
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.histplot(data=filtered_data, x=hist_col, hue="species", kde=True, palette="deep", bins=20, ax=ax2)
st.pyplot(fig2)

# Create a matplotlib figure
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=filtered_data, x='flipper_length_mm', y='body_mass_g', hue='species', style='sex', palette='viridis', s=100, ax=ax)

# Display the seaborn chart
st.pyplot(fig)

# Add descriptive text
st.write("This interactive scatter chart allows you to filter penguin species and visualize their body mass against flipper length.")

    





