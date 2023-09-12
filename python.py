import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import json


# Use pandas to read the CSV file and extract the URLs.
# Extract the country code and ASIN from each row.
# Load the CSV file


df = pd.read_csv('amazon_urls.csv')

# Loop through rows to scrape data
for index, row in df.iterrows():
    country_code = row['CountryCode']
    asin = row['ASIN']
    
    # Construct the Amazon product URL
    url = f"https://www.amazon.{country_code}/dp/{asin}"
    
    # Continue with scraping steps...


# Loop through each URL obtained from the CSV.
# Use try-except to handle exceptions (e.g., 404 errors).
# Use Selenium or BeautifulSoup to visit the Amazon product page.
# Extract the required details.

# Initialize a Selenium WebDriver (you may need to specify the path to your webdriver executable)
driver = webdriver.Chrome()

for index, row in df.iterrows():
    try:
        country_code = row['CountryCode']
        asin = row['ASIN']
        url = f"https://www.amazon.{country_code}/dp/{asin}"
        
        # Visit the Amazon product page
        driver.get(url)
        
        # Use driver to find and extract product details
        product_title = driver.find_element_by_id('productTitle').text
        product_image_url = driver.find_element_by_id('landingImage').get_attribute('src')
        product_price = driver.find_element_by_id('priceblock_ourprice').text
        
        # Extract product details (you may need to locate the element)
        product_details_element = driver.find_element_by_id('productDescription')
        product_details = product_details_element.text
        
        # Print or store the data as needed
        print(f"Product Title: {product_title}")
        print(f"Product Image URL: {product_image_url}")
        print(f"Price of the Product: {product_price}")
        print(f"Product Details: {product_details}")
        
    except NoSuchElementException:
        print(f"{url} not available (404 error)")
    except Exception as e:
        print(f"An error occurred for {url}: {str(e)}")

# Close the Selenium WebDriver when done
driver.quit()




for index, row in df.iterrows():
    try:
        country_code = row['CountryCode']
        asin = row['ASIN']
        url = f"https://www.amazon.{country_code}/dp/{asin}"
        
        # Send a request to the Amazon product page
        response = requests.get(url)
        if response.status_code == 404:
            print(f"{url} not available (404 error)")
            continue
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract product details
        product_title = soup.find(id='productTitle').get_text(strip=True)
        product_image_url = soup.find(id='landingImage')['src']
        product_price = soup.find(id='priceblock_ourprice').get_text(strip=True)
        
        # Extract product details (you may need to locate the element)
        product_details_element = soup.find(id='productDescription')
        product_details = product_details_element.get_text(strip=True)
        
        # Print or store the data as needed
        print(f"Product Title: {product_title}")
        print(f"Product Image URL: {product_image_url}")
        print(f"Price of the Product: {product_price}")
        print(f"Product Details: {product_details}")
        
    except Exception as e:
        print(f"An error occurred for {url}: {str(e)}")



# Create a list of dictionaries to store the scraped data.
# Append the data for each product to this list.
# After scraping all URLs, convert the list of dictionaries to JSON and save it to a file.

# Create a list to store the scraped data
product_data_list = []

# Inside the scraping loop, append data to the list
product_data_list.append({
    'Product Title': product_title,
    'Product Image URL': product_image_url,
    'Price of the Product': product_price,
    'Product Details': product_details
})

# After scraping all URLs, convert the list to JSON
with open('amazon_products.json', 'w', encoding='utf-8') as json_file:
    json.dump(product_data_list, json_file, ensure_ascii=False, indent=4)


# You can measure the time it took to scrape 100 URLs using the time library.
import time

start_time = time.time()

# Your scraping code here

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time} seconds")

  
