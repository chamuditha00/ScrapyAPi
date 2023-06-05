import subprocess
import time

# Function to run the scraping script
def run_scraping_script():
    try:
        subprocess.run(["python", "scrapy.py"])
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

# Run the scraping script initially
run_scraping_script()

# Flag to track execution status
is_running = False

# Run the Flask application
subprocess.Popen(["python", "flaskapi.py"])

while True:
    # Check if the scraping script is already running
    if not is_running:
        # Set the flag to indicate that the scraping script is running
        is_running = True
        
        # Run the scraping script
        run_scraping_script()
        
        # Reset the flag after the scraping script is finished
        is_running = False

    # Wait for 24 hours
    time.sleep(24*60*60)
    print("started")