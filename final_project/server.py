from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    answer = translator.english_to_french(textToTranslate)
    return answer

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    answer = translator.french_to_english(textToTranslate)
    return answer

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    #app.run(debug=True) 
    app.run(host="0.0.0.0", port=8080)
