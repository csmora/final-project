"""
A Flask application for anlyzing the emotions expressed in user-provided text 
using the Watson NLP service. It provides an endpoint to receive text and
returns the dominant emotion with a corresponding score.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sentiment_analyzer():
    """
    This function performs sentiment analysis for given arguments

    Args:
        arg: Description of text to analyze

    Returns:
        If NLP api is successful it returns response string
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    # dominant_emotion = response['dominant_emotion']
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return result

@app.route("/")
def render_index_page():
    """
        This function returns index.html using built in render_template function
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
