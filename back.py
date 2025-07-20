import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env into environment

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)  # use your api key here

model = genai.GenerativeModel('gemini-1.5-flash')


commands = {
    # Entertainment
    "open youtube": ["https://www.youtube.com", "Opening YouTube"],
    "open netflix": ["https://www.netflix.com", "Opening Netflix"],
    "open spotify": ["https://open.spotify.com", "Opening Spotify"],
    "open amazon prime": ["https://www.primevideo.com", "Opening Amazon Prime Video"],

    # Google baba
    "open google": ["https://www.google.com", "Opening Google"],
    "open gmail": ["https://mail.google.com", "Opening Gmail"],
    "open google drive": ["https://drive.google.com", "Opening Google Drive"],
    "open google maps": ["https://maps.google.com", "Opening Google Maps"],
    "open google photos": ["https://photos.google.com", "Opening Google Photos"],

    # AI & Developer Tools
    "open chatgpt": ["https://chatgpt.com", "Opening ChatGPT"],
    "open bard": ["https://bard.google.com", "Opening Bard AI"],
    "open hugging face": ["https://huggingface.co", "Opening Hugging Face"],
    "open github": ["https://github.com", "Opening GitHub"],
    "open stackoverflow": ["https://stackoverflow.com", "Opening StackOverflow"],

    # Social Media
    "open tiktok": ["https://www.tiktok.com", "Opening TikTok"],
    "open facebook": ["https://facebook.com", "Opening Facebook"],
    "open instagram": ["https://www.instagram.com", "Opening Instagram"],
    "open twitter": ["https://twitter.com", "Opening Twitter"],
    "open reddit": ["https://www.reddit.com", "Opening Reddit"],
    "open linkedin": ["https://www.linkedin.com", "Opening LinkedIn"],
    "open pinterest": ["https://www.pinterest.com", "Opening Pinterest"],
    "open snapchat": ["https://www.snapchat.com", "Opening Snapchat"],

    # News
    "open bbc news": ["https://www.bbc.com/news", "Opening BBC News"],
    "open cnn": ["https://www.cnn.com", "Opening CNN News"],
    "open wikipedia": ["https://www.wikipedia.org", "Opening Wikipedia"],
    "open quora": ["https://www.quora.com", "Opening Quora"],

    # Shopping
    "open amazon": ["https://www.amazon.com", "Opening Amazon"],
    "open ebay": ["https://www.ebay.com", "Opening eBay"],
    "open aliexpress": ["https://www.aliexpress.com", "Opening AliExpress"],

    # Nepali sites
    "open ekantipur": ["https://ekantipur.com", "Opening eKantipur News"],
    "open onlinekhabar": ["https://www.onlinekhabar.com", "Opening OnlineKhabar News"],
    "open ratopati": ["https://www.ratopati.com", "Opening Ratopati News"],
    "open setopati": ["https://setopati.com", "Opening Setopati News"],
    "open my republica": ["https://myrepublica.nagariknetwork.com", "Opening MyRepublica"],
    "open nepal telecom": ["https://www.ntc.net.np", "Opening Nepal Telecom"],
    "open nid": ["https://www.nidmc.gov.np", "Opening National ID portal"],
    "open loksewa": ["https://psc.gov.np", "Opening Lok Sewa Aayog"],
    "open tu": ["https://tribhuvan-university.edu.np", "Opening Tribhuvan University"],
    "open see examination board": ["https://www.see.gov.np", "Opening SEE Examination Board"],

    # Mero
    "open my website": ["https://prasoonkandel.netlify.app", "Opening your website"],

    # Identity
    "your name": [None, "I am a simple Voice assistant made by Prasoon Kandel."],
    "who are you": [None, "I am a simple Voice assistant made by Prasoon Kandel."],
    "your creator": [None, "This Voice Assistant is created by Prasoon Kandel. Visit his website: https://prasoonkandel.netlify.app/"],
    "the creator": [None, "This Voice Assistant is created by Prasoon Kandel. Visit his website: https://prasoonkandel.netlify.app/"],
    "made you": [None, "This Voice Assistant is created by Prasoon Kandel. Visit his website: https://prasoonkandel.netlify.app/"],
    "you creator": [None, "This Voice Assistant is created by Prasoon Kandel. Visit his website: https://prasoonkandel.netlify.app/"],

    # Exit
    "bye": ["bye", "Bye, have a nice day!"]
}


# ✅ Single answer() handles both


def answer(command: str):
    for key in commands:
        if key in command:
            url, message = commands[key]
            if callable(message):
                message = message()
            return url, message
    try:
        response = model.generate_content(command)
        return None, str(response.text)
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None, "Sorry, I couldn't process that."
