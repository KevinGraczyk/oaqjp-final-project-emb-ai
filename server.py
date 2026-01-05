"""Executing this function initiates the application of emotion
detection """
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    This function will get the text to analyze from the request arguments,
    process it and return a formatted string.
    """
    #retrive text to analyze from request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # pass the text to the emotion_detector and store the response
    response = emotion_detector(text_to_analyze)

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
