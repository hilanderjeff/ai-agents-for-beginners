from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("API_KEY")
debug_mode = os.getenv("DEBUG")

print(api_key)     # 123456
print(debug_mode)  # True