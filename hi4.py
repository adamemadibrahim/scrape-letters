import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get business type from the business page
def get_business_type(url):
    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the business type using the given selector
        business_type_element = soup.find('a', {'data-index-link': 'true'})
        
        # Return the business type if found, otherwise return None
        if business_type_element:
            business_type = business_type_element.get_text(strip=True)
            print(f"Extracted business type: {business_type} from {url}")
            return business_type
        else:
            print(f"No business type found for {url}")
            return None
    except Exception as e:
        print(f"Error while scraping {url}: {e}")
        return None

# Load the CSV file containing the business links
file_path = 'T_GROUP.csv'
data = pd.read_csv(file_path)

# Initialize a list to store business types
business_types = []

# Loop through each row to process the 'Business Link'
for index, row in data.iterrows():
    business_link = row['Business Link']
    if isinstance(business_link, str):  # Ensure the link is a string
        print(f"Processing business link: {business_link}")
        business_type = get_business_type(business_link)
        business_types.append(business_type)
    else:
        business_types.append(None)

# Add the business type column to the dataframe
data['Business Type'] = business_types

# Save the updated dataframe to a new CSV file
output_file_path = 'T_GROUP_with_business_type.csv'
data.to_csv(output_file_path, index=False)

output_file_path
