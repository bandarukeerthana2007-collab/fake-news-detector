# Fake News Detector

##  About the Project

This project is a simple web application that helps users check whether a piece of news is real or fake.
The user just needs to enter the news text, and the system will analyze it and give a prediction.

The main idea behind this project is to show how basic Machine Learning can be used in real-world problems like detecting fake news.

---

##  What This Project Does

* Takes news text as input
* Analyzes the content using a machine learning model
* Predicts whether the news is **Real** or **Fake**
* Displays the result along with a confidence score

---

##  Technologies Used

* Python (Flask)
* HTML, CSS
* Scikit-learn (Machine Learning)

---

##  How It Works

When the user enters some news text:

1. The text is processed using a vectorizer
2. The trained model analyzes the text
3. The system predicts whether it is real or fake
4. The result is shown on the screen

---

## Project Structure

fake-news-detector/

* app.py → main application
* model.py → machine learning logic
* templates/ → HTML files
* static/ → images and styling

---

##  How to Run

1. Download or clone the project
2. Open the folder in VS Code
3. Install required libraries:
   pip install flask scikit-learn
4. Run the app:
   python app.py
5. Open your browser and go to:
   http://127.0.0.1:5000/

---

##  Future Improvements

* Add URL-based news checking
* Improve accuracy using a larger dataset
* Deploy the project online
* Add history of checked news

---

##  Conclusion

This project is a basic implementation of a fake news detection system using machine learning. It shows how technology can be used to solve real-world problems in a simple and effective way.

---

##  Author

Keerthana Bandaru