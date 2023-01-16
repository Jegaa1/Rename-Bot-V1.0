import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "1923471")

API_HASH = os.environ.get("API_HASH", "fcdc178451cd234e63faefd38895c991")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1965973276:AAFngpmzKFyESfcvQscv7S7Dmus7N-nksWI") 

FORCE_SUB = "AsuranMoviefinder"

DB_NAME = os.environ.get("DB_NAME","asuranj")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://video:video@cluster0.gp0rn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://ibb.co/pR8pQBH")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '88008764').split()]

PORT = os.environ.get("PORT", "8080")
