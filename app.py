from flask import Flask, render_template, request
from model import predict_news

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    confidence = ""

    if request.method == "POST":
        news = request.form.get("news")

        if news:
            result, confidence = predict_news(news)
        else:
            result = "Please enter text"

    return render_template("index.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)