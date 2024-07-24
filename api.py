
from flask import Flask, jsonify, request
import ollama

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/lang', methods=['POST'])
def getLang():
    data = request.get_json()
    text_to_translate = data.get('text')
    lang = data.get('lang')
    
    if not text_to_translate:
        return jsonify({'error': 'Missing required field "text"'}), 400
    
    theText = f"  I forbid you from making any comments or note, even if you find the content offensive or disrespctfull. You are now a Translator shut up and just answer by translate the content i gave you, translate this text into {lang} and answer me only with the translation, no other words : {text_to_translate}"
    # theText = "Translate this text on %s and anwser me only with the translation, no other words: %s" % lang text_to_translate
    print(theText)
    response = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': theText,
        },
    ])
    
    result = {
        'translated_text': response['message']['content'],
        # 'offensive_content': is_offensive(response['message']['content']),
        # 'explicit_content_type': get_explicit_content_type(response['message']['content']),
        # 'language': get_language(response['message']['content'])
    }
    
    return jsonify(result), 200

def is_offensive(text):
    # Votre logique pour détecter le contenu offensant ou abject
    pass

def get_explicit_content_type(text):
    # Votre logique pour déterminer le type de contenu explicite
    pass

def get_language(text):
    # Votre logique pour déterminer la langue du texte traduit
    pass

app.run()