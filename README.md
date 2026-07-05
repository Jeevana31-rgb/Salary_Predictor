# Salary Predictor

A machine learning web application that predicts a user's salary based on input parameters. The application features a predictive backend built using Python and a lightweight web interface powered by Flask.

## 🚀 Features
* **Machine Learning Pipeline:** Complete data preprocessing and model training scripts.
* **Web Interface:** Interactive frontend built with HTML templates to input details and view results.
* **Serialized Model:** Pre-trained and saved model file for instant production predictions.

## 📁 Project Structure
The repository contains the following core files and directories:
* `templates/` - Contains the HTML user interface files for the Flask application.
* `Salary_Data.csv` - The historical dataset containing experience metrics and corresponding salary figures.
* `train_model.py` - The automation script to preprocess data, train, and test the machine learning model.
* `salary_model.pkl` - The optimized, serialized model file ready for inference deployment.
* `app.py` - The primary Flask application handling request routing and model rendering.

## 🛠️ Installation & Setup

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd Salary_Data_Predictor
```

### 2. Install Required Dependencies
Ensure you have Python installed, then install the necessary libraries:
```bash
pip install flask numpy pandas scikit-learn
```

### 3. Train the Model (Optional)
If you want to regenerate or re-optimize the serialized model file, run:
```bash
python train_model.py
```

### 4. Run the Flask Web App
Start your local server with the primary application script:
```bash
python app.py
```

### 5. Access the Web UI
Open your preferred web browser and navigate to the local address outputted by the terminal:
```text
http://127.0.0
```

## 🧠 Technologies Used
* **Backend Framework:** Flask
* **Data Processing & Analytics:** Pandas, NumPy
* **Machine Learning Engine:** Scikit-Learn
*
