import openai
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ✅ Step 1: Set Your API Key
openai.api_key = "You Open AI Key"

# ✅ Step 2: Define the AI Prompt
def generate_pinterest_caption(product_description):
    prompt = f"Write a 150-character Pinterest caption for {product_description} with trending keywords and hashtags."
   
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# ✅ Step 3: Generate Captions
product_list = [
    "Vending Machine Business Plan Template",
    "Vending Machine Location Tracker Spreadsheet",
    "Digital Guide: How to Start a Profitable Vending Business",
    "Vending Machine Contract Agreement"
]

captions = [generate_pinterest_caption(product) for product in product_list]

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Path to your downloaded JSON credentials file
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "C:/Users/smp/Python/pinterest-posts-454916-2835656c1b6f.json", scope
)

# Authenticate and connect to Google Sheets
client = gspread.authorize(creds)

# Open the Google Sheet (replace with your actual sheet name)
spreadsheet = client.open("Pinterest API Post")  # Use your actual spreadsheet name
worksheet = spreadsheet.get_worksheet(0)  # Select the first worksheet

# ✅ Step 5: Save Captions to Google Sheets
# Insert data in the first row: "Product" and "Pinterest Caption"
worksheet.append_row(["Product", "Pinterest Caption"])

# Insert each product and its caption to the Google Sheet
for product, caption in zip(product_list, captions):
    worksheet.append_row([product, caption])

print("Captions generated and saved to Google Sheets!")