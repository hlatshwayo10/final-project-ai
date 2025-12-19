from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        empty_response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        return "Invalid Text! Please try again"
    response = emotion_detector(text_to_analyze)

    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5001)