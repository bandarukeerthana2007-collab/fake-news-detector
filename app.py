from flask import Flask, render_template, request
from model import predict_news
from newspaper import Article

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    confidence = ""

    if request.method == "POST":
        news = request.form.get("news")
        url = request.form.get("url")

        # If URL is provided
        if url:
            try:
                article = Article(url)
                article.download()
                article.parse()
                news = article.text
            except:
                result = "Invalid URL"

        # If text exists
        if news:
            result, confidence = predict_news(news)
            history.append((news[:50], result))

    return render_template("index.html", result=result, confidence=confidence, history=history)

if __name__ == "__main__":
    app.run(debug=True)