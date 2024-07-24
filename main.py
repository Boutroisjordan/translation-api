import flask, ollama

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
   return "<h1>Annuaire Internet</h1><p>Ce site est le prototype d’une API mettant à disposition des données sur les employés d’une entreprise.</p>"

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

@app.route('/lang', methods=['GET'])
def getLang():
  response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Give me the langage of the next sentence juste respond in JSON format "language": the name of the language and "code": two first letter of langage or diminutif (like en for english or fr for french) : 向いているものはありません',
  },
  ])
  print(response['message']['content'])
  return response['message']['content']


@app.route('/explicit', methods=['GET'])
def explicit():
  response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Is the next text explicit content or bad wors, response only by true false et the type of explicit content all in a json:  Stupid mother fucker, suck my big dick and kill ur self',
  },
  ])
  print(response['message']['content'])
  return response['message']['content']


app.run()