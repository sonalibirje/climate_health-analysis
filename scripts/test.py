from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Retrieve API Key
API_KEY = os.getenv("API_KEY")

# Debugging: Print API Key
print(f"Using API Key: {API_KEY}")











