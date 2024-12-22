import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the webdriver
browser = webdriver.Chrome(executable_path='/path/to/chromedriver')

def amazon_sign_in(user_email, user_password):
    # Open Amazon login page
    browser.get("https://www.amazon.in/ap/signin")
    
    # Fill in login details
    browser.find_element(By.ID, 'ap_email').send_keys(user_email)
    browser.find_element(By.ID, 'continue').click()
    browser.find_element(By.ID, 'ap_password').send_keys(user_password)
    browser.find_element(By.ID, 'signInSubmit').click()

def extract_bestsellers(section_url):
    browser.get(section_url)
    time.sleep(3)  # Wait for the page to load

    product_list = []
    try:
        while True:
            # Wait for products to load
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".zg-item-immersion"))
            )

            # Extract product information
            items = browser.find_elements(By.CSS_SELECTOR, '.zg-item-immersion')
            for item in items:
                try:
                    product_name = item.find_element(By.CSS_SELECTOR, '.p13n-sc-truncate').text
                    product_price = item.find_element(By.CSS_SELECTOR, '.p13n-sc-price').text
                    product_rating = item.find_element(By.CSS_SELECTOR, '.a-icon-alt').text
                    product_discount = item.find_element(By.CSS_SELECTOR, '.p13n-sc-price-discount').text
                    
                    # Ensure discount > 50%
                    if product_discount:
                        discount_value = int(product_discount.strip('%'))
                        if discount_value <= 50:
                            continue

                    # Store product data
                    product_list.append({
                        'product_name': product_name,
                        'product_price': product_price,
                        'product_rating': product_rating,
                        'product_discount': product_discount,
                        'category_url': section_url
                    })
                except Exception as error:
                    print(f"Error extracting product: {error}")
            
            # Try to go to the next page
            next_page = browser.find_element(By.CSS_SELECTOR, '.zg_pagination a.zg_page')
            if next_page:
                next_page.click()
                time.sleep(3)
            else:
                break  # End loop if no more pages

    except Exception as error:
        print(f"Error during extraction: {error}")
    
    return product_list

def main():
    # Log into Amazon
    email = "your_amazon_username"
    password = "your_amazon_password"
    amazon_sign_in(email, password)

    category_links = [
        "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0",
        "https://www.amazon.in/gp/bestsellers/shoes/ref=zg_bs_nav_shoes_0",
        "https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0",
        "https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0"
        # Add 6 more categories as needed
    ]

    all_items = []
    for section_url in category_links:
        items = extract_bestsellers(section_url)
        all_items.extend(items)
    
    # Store the data in CSV format
    data_frame = pd.DataFrame(all_items)
    data_frame.to_csv('amazon_bestsellers.csv', index=False)

if __name__ == "__main__":
    main()
