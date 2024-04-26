# Generate a code to regularly backup critical data (such as bookings, passenger details, and payment records) to ensure data safety and create a Python script to schedule this process every 2 hours and synchronize data between different locations.

import schedule
import time
import shutil

def backup_data():
    # Define the source and destination directories for backup
    source_directory = '/path/to/source/directory'
    destination_directory = '/path/to/destination/directory'

    # Perform the backup by copying the files from source to destination
    shutil.copytree(source_directory, destination_directory)

# Schedule the backup process to run every 2 hours
schedule.every(2).hours.do(backup_data)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)





