import logging

from telegram import Update

from telegram.ext import CallbackContext, Updater, CommandHandler

from urllib.parse import quote

# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the handler for the file command

def file_handler(update: Update, context: CallbackContext) -> None:

    file = update.message.document  # Get the file from the message

    file_id = file.file_id  # Get the file ID

    file_access_count = get_file_access_count(file_id)  # Get the current access count for the file

    access_link = generate_access_link(file_id)  # Generate the access link for the file

    # Send the access link and access count as a reply to the user

    reply_text = f"Access Link: {access_link}\nAccess Count: {file_access_count}"

    update.message.reply_text(reply_text)

    # Increment the access count for the file

    increment_file_access_count(file_id)

# Function to generate the access link for the file

def generate_access_link(file_id: str) -> str:

    base_url = "https://example.com/access/"

    encoded_file_id = quote(file_id)  # URL-encode the file ID

    access_link = base_url + encoded_file_id

    return access_link

# Function to get the current access count for the file

def get_file_access_count(file_id: str) -> int:

    # Implement your logic to retrieve the access count for the file

    # Here, you can use a database or any storage mechanism to store and retrieve the access count

    # For simplicity, let's assume a dictionary to store the access counts for each file ID

    file_access_counts = {"file_id1": 0, "file_id2": 0}  # Replace with your actual data

    return file_access_counts.get(file_id, 0)

# Function to increment the access count for the file

def increment_file_access_count(file_id: str) -> None:

    # Implement your logic to increment the access count for the file

    # Here, you can use a database or any storage mechanism to update the access count

    # For simplicity, let's assume a dictionary to store the access counts for each file ID

    file_access_counts = {"file_id1": 0, "file_id2": 0}  # Replace with your actual data

    file_access_counts[file_id] = file_access_counts.get(file_id, 0) + 1

def main() -> None:

    # Create the Telegram Updater and dispatcher

    updater = Updater("6242918828:AAHH0M0GZC4rjF57bZIvbFMMaOCSSs0ZsHw")

    dispatcher = updater.dispatcher

    # Add the file handler command

    dispatcher.add_handler(CommandHandler("file", file_handler))

    # Start the bot

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':

    main()

