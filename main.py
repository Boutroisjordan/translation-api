import flask, ollama

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/llama3', methods=['GET'])
def llama():
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': 'Translate in englsih this and response in json: 向いているものはありません',
        },
    ])
    print(response['message']['content'])
    return response['message']['content']


@app.route('/translate', methods=['POST'])
def translate():
    content = flask.request.json['content']
    outlang = flask.request.json['outLang']
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': f'Translate in {outlang} this: "{content}". The return type should be in JSON format with'
                       ' the key "content" and the value the translated text. You must define whether the text is'
                       ' explicit or not and the language of the text. Example: {"content": the translation, '
                       '"explicit": if the text seems explicit (true/false), "inLang": language you detected (ja), '
                       '"outLang": given outlang (fr)}. Type your response as a JSON and don\'t write anything else.',
        },
    ])
    print(response['message']['content'])
    return response['message']['content']


@app.route('/lang', methods=['GET'])
def getlang():
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': 'Give me the langage of the next sentence juste respond in JSON format "language": the name of '
                       'the language and "code": two first letter of langage or diminutif (like en for english or fr '
                       'for french) : 向いているものはありません',
        },
    ])
    print(response['message']['content'])
    return response['message']['content']


@app.route('/explicit', methods=['GET'])
def explicit():
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': 'Is the next text explicit content or bad wors, response only by true false et the type of '
                       'explicit content all in a json:  Stupid mother fucker, suck my big dick and kill ur self',
        },
    ])
    print(response['message']['content'])
    return response['message']['content']


app.run()
