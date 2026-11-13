Job Scraper

11.11.2024

Prologue:
Hello! Thank you for taking the time to check out my project. For months, my homeland of Manipur, India has been in a state of turmoil. (https://www.nytimes.com/2024/09/11/world/asia/india-manipur-conflict.html) People have passed away, families have been misplaced from their homes, children are unable to attend school, and breadwinners cannot provide for their loved ones. This program was intended to help those affected by the violence by streamlining job listings that are curated for them based on level of education. 

This is a Python-based automation tool that scrapes job listings from specified websites, filters jobs based on education requirements, and sends email notifications for new job postings. This tool is designed to run on a daily schedule, either locally or via AWS Lambda.

---

Features

- Web Scraping: Scrapes job postings from a predefined job listing website.
- Job Comparison: Compares current job postings with previous ones to extracct only new postings.
- Job Filtering: Uses OpenAI to filter jobs based on education requirements (college degree or not).
- Email Notifications: Sends an email with the filtered job listings.
- Daily Scheduling: The program can be scheduled to run daily using Python's scheduling libraries or AWS Lambda.

---

Table of Contents

- Installation
- Configuration
- Usage
- Project Structure
- Environment Variables
- Contributing
- License

---

Installation

Follow the steps below to set up the project locally:

1. Clone the repository**:
   ```bash
   git clone https://github.com/your-username/job-scraper-notifier.git
   cd job-scraper-notifier
2. Install (using pip install) all requirements in the requirements.txt file. Note: Ensure you have Python 3.7+ installed.

---

Configuration

Create a .env file in the root directory to store sensitive information like your email credentials and OpenAI API key.
Example .env file:
   TO_EMAIL=your_recipient_email@example.com
   FROM_EMAIL=your_sending_email@example.com
   EMAIL_PASSWORD=your_sending_email_password
   OPENAI_API_KEY=your_openai_api_key

Web Scraping Source:
The program currently scrapes job listings from Sarkari Naukri. You can change the URL in scrape.py to scrape from a different site if needed.

---

Usage

Run the main program:
python src/main.py
This will trigger the job scraping process, compare with previous results, filter jobs, and send an email with the filtered results.

Scheduling:
Local Scheduling: The program uses the repeater.py module to run daily at a specified time.
Example: Run at 10:31 AM every day:
schedule_job(check_new_jobs, "10:31")
AWS Lambda Scheduling: For serverless execution, deploy the program using AWS Lambda. Set up an EventBridge rule to trigger the lambda_handler function daily.

---

Project Structure

job-scraper-notifier/
   ├── README.md                  # Project documentation
   ├── .env                       # Environment variables (not included in the repository)
   ├── requirements.txt           # Python dependencies
   ├── src/                       # Source files
   │   ├── main.py                # Main program that runs the job scraper and notifier
   │   ├── emailer.py             # Sends email notifications using Gmail SMTP
   │   ├── compare.py             # Compares current job listings with previous ones
   │   ├── openai_filter.py       # Uses OpenAI to filter jobs based on education level
   │   ├── repeater.py            # Schedules job checking function
   │   └── scrape.py              # Web scraping logic to fetch job postings

---

OpenAI API Usage

OpenAI API Key:
Sign up for an OpenAI account to get your API key if you haven’t already.
Add OPENAI_API_KEY to your .env file to enable job filtering using OpenAI’s GPT model, and add money to your balance to enable usage. It is important to note that 

---

Licensing

Look at license.txt



## Interactive workbench (2026-11-13)

Run `python serve_demo.py`, then open <http://127.0.0.1:8000>. See [QUICKSTART.md](QUICKSTART.md) for core commands, tests, provenance and remaining requirements.
