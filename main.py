import ollama
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/translate", methods=["POST"])
def translate():
    content = request.json['content']
    outlang = request.json['outLang']
    result = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': f'Translate in {outlang} this: "{content}". The return type should be in JSON format with'
                       ' the key "content" and the value the translated text. You must define whether the text is'
                       ' explicit or not and the language of the text. Example: {"content": the translation, '
                       '"explicit": if the text seems explicit (true/false), "inLang": language you detected (ja), '
                       '"outLang": given outlang (fr)}. Type your response as a JSON and don\'t write anything '
                       'else.',
        },
    ])
    print(result['message']['content'])
    return result['message']['content']


if __name__ == '__main__':
    app.run(debug=True)
