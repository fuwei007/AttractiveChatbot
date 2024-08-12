from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Replace 'your-openai-api-key' with your actual OpenAI API key
openai.api_key = ''


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    message = data['message']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the GPT-4 turbo model
            messages=[
                {"role": "system", "content": "You are a helpful restaurant assistant. The restaurant sale fried rice, the price is $12.99"},
                {"role": "user", "content": message}
            ],
            max_tokens=150,
            temperature=0.7
        )

        chat_response = response.choices[0].message['content'].strip()
        return jsonify({'response': chat_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
