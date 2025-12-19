"""Flask server for emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyze input text and return detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid Text! Please try again"
    response = emotion_detector(text_to_analyze)

    return response

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
