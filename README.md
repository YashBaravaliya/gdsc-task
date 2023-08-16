# Recommendation System Project

This repository contains a recommendation system project implemented using various datasets. The system is designed to provide personalized recommendations based on user preferences.

## Running the Recommendation System

To run the recommendation system and launch the accompanying web app, follow these steps:

1. **Preprocessing Data and Model Creation:**
   - Open `main.ipynb` in a Jupyter Notebook environment or Jupyter Lab.
   - Run the notebook cells to preprocess the datasets and create a `.pickle` file containing the preprocessed data and model.

2. **Setting Up Dependencies:**
   - Open a terminal in the project directory.
   - Install the required Python packages by running the following command:
   
     ```
     pip install -r requirements.txt
     ```

3. **Launching the Web App:**
   - After the installation is complete, run the following command to launch the web app:
   
     ```
     streamlit run app.py
     ```
   
   - A new browser window should automatically open, displaying the web app interface.

## App Usage

The web app provides an intuitive user interface for interacting with the recommendation system. Users can input their preferences and receive personalized recommendations based on the pre-trained model.

- Select preferences such as categories, ratings, or any other relevant filters.
- Click on the "Get Recommendations" button to see the top recommendations based on the provided preferences.
- Explore the recommended items and their details.
- Enjoy exploring the recommendations tailored just for you!

Please note that the recommendation model was trained on the provided datasets and may not be fully optimized for all scenarios. Feel free to experiment with different preferences and provide feedback for improvements.

## Datasets

The `data` folder contains various datasets used for training and testing the recommendation system. Each dataset provides valuable insights to enhance the system's recommendations.

## Contributing

If you find any issues or would like to contribute to the project, feel free to open an issue or submit a pull request. Your contributions are greatly appreciated!

## Contact

For any questions or inquiries, please contact [Yash Baravaliya](yashbaravaliya206@gmail.com).
