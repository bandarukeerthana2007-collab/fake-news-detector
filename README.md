#  Fake News Detector

##  About the Project

This project is a web-based application that helps users identify whether a news article is real or fake.
The user can either enter the news text directly or provide a news URL, and the system will analyze it and give a prediction.

This project demonstrates how basic Machine Learning can be applied to solve real-world problems like fake news detection.

---

##  Features

* Detects whether news is **Fake or Real**
* Accepts both **text input and URL input**
* Displays **confidence percentage**
* Shows **history of checked news**
* Modern and clean user interface
* Responsive design for different devices

---

## Technologies Used

* Python (Flask)
* HTML, CSS
* Scikit-learn (Machine Learning)
* Newspaper3k (for extracting news from URLs)

---

##  How It Works

1. User enters news text or provides a URL
2. If URL is given, the system extracts the article content
3. The text is processed using a machine learning model
4. The system predicts whether the news is real or fake
5. The result is displayed along with a confidence score

---

##  Project Structure

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
   pip install flask scikit-learn newspaper3k
4. Run the application:
   python app.py
5. Open browser and go to:
   http://127.0.0.1:5000/

---

##  Future Improvements

* Improve accuracy using a larger dataset
* Add user authentication
* Deploy the project online
* Enhance UI/UX further

---

##  Conclusion

This project is a simple implementation of a fake news detection system using machine learning. It provides a user-friendly interface and demonstrates how AI can be used to identify misleading information.

---

##  Author

Keerthana Bandaru
