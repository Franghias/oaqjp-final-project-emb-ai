"""Flask app for detecting emotions from input using AI Watson NLP."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detecting():
    """Return 5 emotion scores and the dominant one if receive correct text, else output invalid"""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Error Handling in case failing
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return f"""
            For the given statement, the system response is \'anger\': {response['anger']}
            , \'disgust\': {response['disgust']}
            , \'fear\': {response['fear']}
            , \'fear\': {response['fear']}
            , \'joy\': {response['joy']}
            , \'sadness\': {response['sadness']}.
            The dominant emotion is {response['dominant_emotion']}
            """

@app.route("/")
def render_index_page():
    """Render for the main index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
