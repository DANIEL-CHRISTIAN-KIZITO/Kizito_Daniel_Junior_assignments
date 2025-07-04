#Config.py    
TWITTER_API = {
    'api_key': 'YOUR_TWITTER_API_KEY',
    'api_secret': 'YOUR_TWITTER_API_SECRET',
    'access_token': 'YOUR_ACCESS_TOKEN',
    'access_token_secret': 'YOUR_ACCESS_SECRET'
}

OPENAI_API_KEY = 'your-openai-api-key'
POST_TIMES = ['09:00', '13:00', '18:00']  # Optimal posting times
USER_INTERESTS = ['AI', 'Python', 'Tech Trends']

#Content_generator.py
import openai
import random
from config import OPENAI_API_KEY, USER_INTERESTS

openai.api_key = OPENAI_API_KEY

def generate_post():
    interest = random.choice(USER_INTERESTS)
    prompt = f"Write a short engaging tweet about {interest} that's under 280 characters."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content'].strip()
