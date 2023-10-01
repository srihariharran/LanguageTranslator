from flask import Flask,render_template,jsonify,request
from googletrans import Translator
import json


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get-language-code",methods=["POST"])
def getLanguageCode():
    with open('languageCodes.json', 'r') as f:
        languageCodes = json.load(f)
        f.close()
    return jsonify(languageCodes)


@app.route("/translate",methods=["POST"])
def translate():
    text_to_translate=request.form["text"]
    code=request.form["code"]
    translator = Translator()
    translated_text = translator.translate(text_to_translate,dest=code)
    return str(translated_text.text)



@app.route("/get-translate")
def get_translate():
    text_to_translate=request.args.get("text")
    code=request.args.get("code")
    translator = Translator()
    translated_text = translator.translate(text_to_translate,dest=code)
    return str(translated_text.text)
    

if __name__ == "__main__":
   app.run()