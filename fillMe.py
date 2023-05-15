import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the URL of the webpage you want to fill out
url = "https://slubillikens.com/sb_output.aspx?form=13"

driver = webdriver.Chrome()
driver.get(url)

# Define the data to fill in
data = {
    "First Name": "John",
    "Last Name": "Doe",
    "Email": "johndoe@example.com",
    # Add more fields and values as needed
}

# Iterate through the data dictionary
for field_name, value in data.items():
    # Find the label element associated with the field
    label_element = driver.find_element(By.XPATH, f"//label[contains(text(), '{field_name}')]")
    input_id = label_element.get_attribute("for")
    
    # Find the input field by ID
    input_field = driver.find_element(By.ID, input_id)
    
    # Fill in the input field with the value
    input_field.send_keys(value)

input('Close me')
driver.quit()
