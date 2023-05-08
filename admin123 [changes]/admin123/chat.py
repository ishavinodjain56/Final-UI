from flask import Flask, jsonify, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Create a new chat bot named "Bot"
bot = ChatBot('Bot')

# Train the bot using the English corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# Define a route for the API endpoint
@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    # Get the user's message from the POST request
    user_message = request.json['message']

    # Get a response from the chat bot
    bot_response = bot.get_response(user_message)

    # Return the response as a JSON object
    return jsonify({'message': str(bot_response)})

if __name__ == '__main__':
    app.run(debug=True)
