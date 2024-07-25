const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const ollama = require('ollama');

const app = express();
app.use(cors());

const jsonParser = bodyParser.json();

app.post('/api/translate', jsonParser, async (req, res) => {
    try {
        const { content, outLang } = req.body;
        const translation = await ollama.default.chat({
            model: "mistral",
            messages: [{
                role: "user",
                content: `Translate in ${outLang} this: "${content}". The return type should be in JSON format with the key "content" 
                and the value the translated text. You must define whether the text is explicit or not and the language of the text. 
                Example: {"content": the translation, "explicit": if the text seems explicit (true/false), "inLang": language you detected (ja), 
                "outLang": given outlang (fr)}. Type your response as a JSON and don\'t write anything else.`
            }],
        })
        // extract json from the response
        const json = JSON.parse(translation.message.content);
        console.log(json);
        res.json(json);
    } catch (error) {
        console.log(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(5001,() => {
    console.log('Server is running on port 5001');
    console.log('http://localhost:5001');
});