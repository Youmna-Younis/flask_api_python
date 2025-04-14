import streamlit as st
import requests

# Inject custom CSS for background
def set_background():
    st.markdown(
        """
        <style>
        /* Full-page background */
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover; /* Cover the entire screen */
            background-position: center; /* Center the image */
            background-repeat: no-repeat; /* Prevent repeating */
            background-attachment: fixed; /* Fix the background */
            min-height: 100vh; /* Ensure the background spans the full height of the screen */
        }

        /* Add contrast to text for better readability */
        h1, h2, h3, p, div, span {
            color: black !important;
        }

        /* Style buttons */
        .stButton>button {
            background-color: #4CAF50; /* Green button */
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
        }

        /* Style input fields */
        .stTextInput>div>input, .stNumberInput>div>input {
            background-color: rgba(255, 255, 255, 0.8);
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set the background
set_background()

# Title of the app
st.title("IRIS Flower Classifier 🌸")

# Add a description
st.markdown("""
    Enter the feature values below to classify the Iris flower species.
    The model will predict whether the flower is **Setosa**, **Versicolor**, or **Virginica**.
""")

# Input fields for feature_array
feature_1 = st.number_input("Sepal Length (cm)", value=5.1, step=0.1)
feature_2 = st.number_input("Sepal Width (cm)", value=3.5, step=0.1)
feature_3 = st.number_input("Petal Length (cm)", value=1.4, step=0.1)
feature_4 = st.number_input("Petal Width (cm)", value=0.2, step=0.1)

# Button to trigger prediction
if st.button("Predict"):
    # Prepare the payload
    payload = {
        "feature_array": [feature_1, feature_2, feature_3, feature_4]
    }

    try:
        # Send POST request to Flask API
        response = requests.post("http://localhost:5000/predict", json=payload)
        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction'][0]  # Extract the prediction
            st.success(f"Prediction: **{['Setosa', 'Versicolor', 'Virginica'][prediction]}**")

            # Display the corresponding image
            if prediction == 0:
                st.image("https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg",
                         caption="Setosa", width=300)
            elif prediction == 1:
                st.image("https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
                         caption="Versicolor", width=300)
            elif prediction == 2:
                st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
                         caption="Virginica", width=300)
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add a footer
st.markdown("""
    ---
    🌟 Built with ❤️ using [Streamlit](https://streamlit.io) and [Flask](https://flask.palletsprojects.com)
""")