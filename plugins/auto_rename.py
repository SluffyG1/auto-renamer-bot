from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from helper.database import db
import time
import queue

# Create a queue to hold the files to be processed
file_queue = queue.Queue(maxsize=5)

# Your existing code here

# Inside the handler for file uploads
@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def auto_rename_files(client, message):
    # Your existing code here

    # Add the file to the queue instead of processing it directly
    file_id = message.document.file_id
    file_name = message.document.file_name
    file_queue.put((file_name, file_id))

    # Process the files in the queue
    while not file_queue.empty():
        file_name, file_id = file_queue.get()

        # Check whether the file is already being renamed or has been renamed recently
        if file_id in renaming_operations:
            elapsed_time = (datetime.now() - renaming_operations[file_id]).seconds
            if elapsed_time < 10:
                print("File is being ignored as it is currently being renamed or was renamed recently.")
                continue  # Skip the file if it's being ignored

        # Mark the file as currently being renamed
        renaming_operations[file_id] = datetime.now()

        # Your existing code to process the file here

        # Remove the entry from renaming_operations after successful renaming
        del renaming_operations[file_id]

# Your existing code here

# Start the main thread
if __name__ == "__main__":
    app.run()

@Client.on_message(filters.private & filters.command("autorename"))
async def auto_rename_command(client, message):
    user_id = message.from_user.id

    
    format_template = message.text.split("/autorename", 1)[1].strip()

    
    await db.set_format_template(user_id, format_template)

    await message.reply_text("**Auto Rename Format Updated Successfully! ✅**")

@Client.on_message(filters.private & filters.command("setmedia"))
async def set_media_command(client, message):
    user_id = message.from_user.id    
    media_type = message.text.split("/setmedia", 1)[1].strip().lower()

    
    await db.set_media_preference(user_id, media_type)

    await message.reply_text(f"**Media Preference Set To :** {media_type} ✅")
