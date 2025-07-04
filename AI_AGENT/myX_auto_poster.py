import tweepy
import datetime
import os
import socket
import time

#Step 1: Wait for internet connection (up to 2 mins)
# This function checks if the internet connection is available by trying to connect to Twitter's API.
def is_connected():
    try:
        socket.create_connection(("api.twitter.com", 443), timeout=5)
        return True
    except OSError:
        return False

for _ in range(120):  # check every second for 2 minutes
    if is_connected():
        break
    time.sleep(1)
else:
    print("❌ Internet not available. Tweet not sent.")
    exit()

#Step 2: Skip if already posted today

today = datetime.datetime.now().strftime("%Y-%m-%d")
weekday = datetime.datetime.now().strftime("%A")

log_file = "last_posted.txt"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        last_date = f.read().strip()
    if last_date == today:
        print("✅ Already posted today. Skipping.")
        exit()

#Step 3: Select today's quote 

quotes = {
    "Monday Motivation": "Start your week with a positive mindset! #MondayMotivation",
    "Tuesday Tips": "Did you know that consistency is key to success? #TuesdayTips",
    "Wednesday Wisdom": "Keep pushing forward, you're halfway through the week! #WednesdayWisdom",
    "Thursday Thoughts": "Reflect on your progress and set new goals! #ThursdayThoughts",
    "Friday Fun": "It's almost the weekend! What are your plans? #FridayFun",
    "Saturday Vibes": "Take a break and enjoy some leisure time! #SaturdayVibes",
    "Sunday Reflections": "Prepare for the week ahead and set your intentions! #SundayReflections"
}

quote = quotes.get(weekday, "Stay inspired.")

#Step 4: Twitter API credentials 

API_KEY = 'rW2MaRgHMlRHT5iNEPmWt7VLN'
API_SECRET_KEY = 'N2YDLHiUCsIkdUymzgFHKrKLazoEm50fWGZOpqSu3vyGBUxSB8'
ACCESS_TOKEN = '1046443484268429313-CAFBdmNKmzfBCRUEu0aZqJJKTbbSen'
ACCESS_TOKEN_SECRET = 'umowecj2zBfXUuerb8t7amCeuetkNBaqIosSMtgtCaBzx'


#Step 5: Post the tweet using Twitter API v2

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

try:
    response = client.create_tweet(text=quote)
    print(f"✅ Posted: {quote}")
    with open(log_file, "w") as f:
        f.write(today)
except Exception as e:
    print(f"❌ Failed to post tweet: {e}")