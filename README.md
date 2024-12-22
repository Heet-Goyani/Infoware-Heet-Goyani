Amazon Best Sellers Scraper

This project is an internship assignment to develop a Python web scraper using Selenium. The scraper extracts information from Amazon's Best Sellers section and stores it in a CSV file. It includes authentication, robust error handling, and structured data storage.

Overview

The scraper performs the following tasks:

Authentication: Logs into Amazon using valid credentials.

Category-Based Scraping: Scrapes data from multiple categories (e.g., Kitchen, Electronics, Shoes, etc.).

Product Details Extraction: Captures key details such as name, price, discount, rating, and more.

Data Storage: Saves the scraped data into a CSV file.

Error Handling: Handles issues like timeouts, missing data, and navigation errors.

Compliance: Operates responsibly to avoid violating Amazon's terms of service.

Libraries and Tools

The script uses the following libraries:

Selenium: For browser automation and scraping dynamic content.

webdriver-manager: To manage ChromeDriver installation.

time: To introduce delays and manage scraping intervals.

csv: For saving the scraped data in CSV format.

json: For potential future enhancements to save data in JSON format.

Setup Instructions

1. Install Required Libraries

Run the following command to install necessary libraries:

pip install selenium webdriver-manager

2. Download ChromeDriver

The webdriver-manager library automatically handles the installation of ChromeDriver. Ensure you have Google Chrome installed on your system.

3. Set Up Amazon Credentials

Replace the placeholders in the script (email and password) with your Amazon login credentials:

email = "your-email@example.com"
password = "your-password"

Script Functionality

1. Login to Amazon

Navigates to the Amazon login page.

Authenticates using the provided email and password.

2. Navigate to Best Sellers Pages

Visits the URLs for selected categories, such as Kitchen, Shoes, Electronics, etc.

3. Scrape Product Data

Extracts the following details for each product:

Category: The category of the product.

Product Name: The name of the product.

Product Price: The listed price.

Sale Discount: Placeholder, as discounts are not currently implemented.

Best Seller Rating: Customer ratings for the product.

Ship From: Placeholder, not implemented in the script.

Sold By: Placeholder, not implemented in the script.

Product Description: Placeholder, not implemented in the script.

Images: Placeholder, not implemented in the script.

4. Store Data in CSV

Saves the scraped data to a CSV file named amazon_best_sellers.csv.

5. Error Handling

Includes robust handling for timeouts, missing elements, and navigation errors.

Usage

Run the script:

python script_name.py

The scraper will:

Log into Amazon.

Navigate through the specified categories.

Extract and save product details to amazon_best_sellers.csv.

The CSV file will be created in the same directory as the script.

Key Notes

1. Respectful Scraping

Introduces delays between page navigations to avoid overwhelming Amazon's servers.

Limits the number of pages scraped per category to stay within ethical boundaries.

2. CAPTCHA or 2FA Challenges

Manual intervention may be required if CAPTCHA or two-factor authentication is encountered.

3. Data Compliance

Ensure responsible usage of the data scraped and adhere to Amazon's terms of service.

Future Enhancements

Implement extraction of additional fields such as discounts, shipping details, and product descriptions.

Add support for scraping images and saving URLs in the CSV.

Handle CAPTCHA challenges programmatically if possible.

Conclusion

This Python script automates Amazon Best Sellers data extraction, ensuring efficiency and accuracy. It provides a foundation for further development and enhancement to meet specific data collection requirements.