import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="The Skyfall Conundrum",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

st.title('the skyfall condrum')
 
# Load the trained model
with open("random_forest_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to make predictions
def predict_alien_type(features):
    prediction = model.predict(features.reshape(1, -1))
    return prediction[0]

# Streamlit app
# st.title("Alien Type Predictor")

# User input section
st.sidebar.header("User Input")
island_size = st.sidebar.slider("Island Size", 0.0, 100.0, 500.0)
terrain_type = st.sidebar.selectbox("Terrain Type", ["Coastal", "Desert", "Forested","Mountainous", "Plains", "Swamp","Tundra","Urban settlements", "Other"])
distance_from_mainland = st.sidebar.slider("Distance from Mainland", 0.0, 500.0, 800.0)
avg_temperature = st.sidebar.slider("Avg Temperature", -50.0, 60.0, 0.0)
avg_humidity = st.sidebar.slider("Avg Humidity", 0.0, 100.0, 50.0)
unexplain_sounds_count = st.sidebar.selectbox("Unexplain Sounds Count", ["High", "Low", "Moderate","Other"])
ph_change = st.sidebar.slider("pH Change", -5.0, 10.0, 7.0)

# Create a feature vector based on user input
features = pd.DataFrame({
    "Island Size": [island_size],
    "Terrain Type": [terrain_type],
    "Distance from Mainland": [distance_from_mainland],
    "Avg Temperature": [avg_temperature],
    "Avg Humidity": [avg_humidity],
    "Unexplain Sounds Count": [unexplain_sounds_count],
    "pH Change": [ph_change]
})

# Map categorical variables to numerical values
# Update this mapping based on your model preprocessing
terrain_mapping = {"Coastal": 0, "Desert": 1, "Forested": 2,"Mountainous": 3, "Plains": 4, "Swamp": 5,"Tundra": 6, "Urban settlements": 7, "Other": 8}
sounds_mapping = {"High": 0, "Low": 1, "Moderate": 2,"Other": 3}

features["Terrain Type"] = features["Terrain Type"].map(terrain_mapping)
features["Unexplain Sounds Count"] = features["Unexplain Sounds Count"].map(sounds_mapping)

# Prediction
if st.sidebar.button("Predict Alien Type"):
    prediction = predict_alien_type(features.values)
    # st.success(f"The predicted alien type is: {prediction}")

    alien_type_mapping = { 0: "Banshee",1: "Chupacabra", 2: "Jersey Devil", 3: "Mothman", 4: "Ropen", 5: "Sasquatch", 6: "Thunderbird", 7: "Wendigo", 8: "Yeti"}  
    prediction_str = alien_type_mapping.get(prediction, "Unknown")
    st.success(f"The predicted alien type is: {prediction_str}")