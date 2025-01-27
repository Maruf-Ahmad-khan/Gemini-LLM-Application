import streamlit as st
import pickle
import numpy as np


class ElectricCarPricePredictor:
    def __init__(self, model_path):
        """
        Initializes the predictor class by loading the pre-trained model.
        :param model_path: Path to the saved pickle file containing the pre-trained model.
        """
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        """
        Loads the pre-trained model from the specified path.
        :return: Loaded model object.
        """
        try:
            with open(self.model_path, "rb") as file:
                model = pickle.load(file)
            return model
        except FileNotFoundError:
            st.error("Model file not found. Please check the file path.")
            raise
        except Exception as e:
            st.error(f"Error loading model: {e}")
            raise

    def predict_price(self, features):
        """
        Predicts the price of an electric car based on input features.
        :param features: A numpy array of input features.
        :return: Predicted price of the car.
        """
        try:
            return self.model.predict(features)[0]
        except Exception as e:
            st.error(f"Prediction error: {e}")
            raise


class ElectricCarPriceApp:
    def __init__(self, predictor):
        """
        Initializes the Streamlit app with a given predictor instance.
        :param predictor: An instance of ElectricCarPricePredictor.
        """
        self.predictor = predictor

    def render_header(self):
        """Renders the header section of the app."""
        st.title("Electric Car Price Prediction")
        st.header("Input Car Features")

    def get_user_inputs(self):
        """
        Gets user inputs for car features using Streamlit widgets.
        :return: A numpy array of input features.
        """
        engine_size = st.number_input("Engine Size (in cc)", min_value=500, max_value=10000, value=2000)
        curb_weight = st.number_input("Curb Weight (in kg)", min_value=500, max_value=3000, value=1500)
        horsepower = st.number_input("Horsepower", min_value=50, max_value=1000, value=300)
        city_mpg = st.number_input("City MPG", min_value=5, max_value=100, value=30)
        highway_mpg = st.number_input("Highway MPG", min_value=5, max_value=100, value=40)

        # Prepare the input data as a 2D array for prediction
        return np.array([[engine_size, curb_weight, horsepower, city_mpg, highway_mpg]])

    def render_prediction(self, features):
        """
        Renders the predicted price on the Streamlit interface.
        :param features: A numpy array of input features for prediction.
        """
        if st.button("Predict Price"):
            try:
                # Predict the price using the predictor
                predicted_price = self.predictor.predict_price(features)
                st.success(f"The predicted price of the electric car is: ${predicted_price:,.2f}")
            except Exception as e:
                st.error(f"Failed to generate prediction: {e}")

    def run(self):
        """Runs the Streamlit app."""
        self.render_header()
        features = self.get_user_inputs()
        self.render_prediction(features)


# Main execution
if __name__ == "__main__":
    # Path to the model file
    MODEL_PATH = r"C:\Users\mk744\Downloads\Car price\lr_model_wout.pkl"

    # Initialize the predictor
    predictor = ElectricCarPricePredictor(MODEL_PATH)

    # Initialize and run the app
    app = ElectricCarPriceApp(predictor)
    app.run()
