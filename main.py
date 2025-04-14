from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.common.keys import Keys
import time

# Load configuration from the JSON file
with open('testdata.json', 'r') as file:
    testdata = json.load(file)

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

# Create an HTML log file
html_log = open('test_results.html', 'w')
html_log.write("<html><head><title>Test Results</title></head><body>")
html_log.write("<h1>Test Results</h1>")
html_log.write("<table border='1'><tr><th>Step</th><th>Status</th></tr>")

def log_result(step, status, error_message=""):
    print(f"{step}: {status}")
    color = "green" if status == "pass" else "red"
    if status == "fail":
        html_log.write(f"<tr><td>{step}</td><td style='color:{color}'>{status} - {error_message}</td></tr>")
    else:
        html_log.write(f"<tr><td>{step}</td><td style='color:{color}'>{status}</td></tr>")

# Open the website
try:
    driver.get(testdata['website'])
    driver.maximize_window()
    log_result("Website opened", "pass")
except Exception as e:
    log_result("Website opened", "fail", str(e))

# Search the book and press enter
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Find Book Name']").send_keys(testdata['search_terms'][0] + Keys.ENTER)
    time.sleep(3)
    log_result("Search first book", "pass")
except Exception as e:
    log_result("Search first book", "fail", str(e))

# Click on the book link
try:
    driver.find_element(By.XPATH, "//a[contains(text(),'How to Win Friends And Influence People (Paperback')]").click()
    time.sleep(3)
    log_result("Click first book link", "pass")
except Exception as e:
    log_result("Click first book link", "fail", str(e))

# Make the quantity of the book 2
try:
    driver.find_element(By.XPATH, "//em[@class='plus pd-plus']").click()
    time.sleep(3)
    log_result("Increase quantity of first book", "pass")
except Exception as e:
    log_result("Increase quantity of first book", "fail", str(e))

# Click on add to cart button
try:
    driver.find_element(By.XPATH, "//a[@class='tg-btn tg-active tg-btn-lg d-block']").click()
    time.sleep(3)
    log_result("Add first book to cart", "pass")
except Exception as e:
    log_result("Add first book to cart", "fail", str(e))

# Search the second book and press enter
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Find Book Name']").send_keys(testdata['search_terms'][1] + Keys.ENTER)
    time.sleep(3)
    log_result("Search second book", "pass")
except Exception as e:
    log_result("Search second book", "fail", str(e))

# Click on the second book link using CSS selector
try:
    driver.find_element(By.CSS_SELECTOR, "div[class='tg-booktitle'] h3 a").click()
    time.sleep(3)
    log_result("Click second book link", "pass")
except Exception as e:
    log_result("Click second book link", "fail", str(e))

# Make the quantity of the second book 3
try:
    driver.find_element(By.XPATH, "//em[@class='plus pd-plus']").click()
    driver.find_element(By.XPATH, "//em[@class='plus pd-plus']").click()
    time.sleep(3)
    log_result("Increase quantity of second book", "pass")
except Exception as e:
    log_result("Increase quantity of second book", "fail", str(e))

# Add the second book to cart
try:
    driver.find_element(By.XPATH, "//a[@class='tg-btn tg-active tg-btn-lg d-block']").click()
    time.sleep(3)
    log_result("Add second book to cart", "pass")
except Exception as e:
    log_result("Add second book to cart", "fail", str(e))

# Search the third book and press enter
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Find Book Name']").send_keys(testdata['search_terms'][2] + Keys.ENTER)
    time.sleep(3)
    log_result("Search third book", "pass")
except Exception as e:
    log_result("Search third book", "fail", str(e))

# Click on the third book link
try:
    driver.find_element(By.XPATH, "//a[contains(text(),'The Rudest Book Ever (Paperback) - Shwetabh Gangwar')]").click()
    time.sleep(3)
    log_result("Click third book link", "pass")
except Exception as e:
    log_result("Click third book link", "fail", str(e))

# Add the third book to cart
try:
    driver.find_element(By.XPATH, "//a[@class='tg-btn tg-active tg-btn-lg d-block']").click()
    time.sleep(3)
    log_result("Add third book to cart", "pass")
except Exception as e:
    log_result("Add third book to cart", "fail", str(e))

# Click on the cart button
try:
    driver.find_element(By.XPATH, "//button[@id='tg-minicart']//i[@class='icon-cart']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='tg-minicart']//i[@class='icon-cart']").click()
    time.sleep(2)
    log_result("Click cart button", "pass")
except Exception as e:
    log_result("Click cart button", "fail", str(e))

# Click on the view cart button
try:
    driver.find_element(By.XPATH, "//a[normalize-space()='View Cart']").click()
    time.sleep(3)
    log_result("View cart", "pass")
except Exception as e:
    log_result("View cart", "fail", str(e))

# Apply coupon code
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Coupon Code']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Coupon Code']").send_keys(testdata['coupon_code'])
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@class='btn btcart']").click()
    time.sleep(3)
    log_result("Apply coupon", "pass")
except Exception as e:
    log_result("Apply coupon", "fail", str(e))

# Proceed to checkout
try:
    driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to checkout']").click()
    time.sleep(3)
    log_result("Proceed to checkout", "pass")
except Exception as e:
    log_result("Proceed to checkout", "fail", str(e))

# Enter email
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(testdata['email'])
    time.sleep(1)
    log_result("Enter email", "pass")
except Exception as e:
    log_result("Enter email", "fail", str(e))

# Enter password
try:
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(testdata['password'])
    time.sleep(1)
    log_result("Enter password", "pass")
except Exception as e:
    log_result("Enter password", "fail", str(e))

# Log in
try:
    driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()
    time.sleep(1)
    log_result("Log in", "pass")
except Exception as e:
    log_result("Log in", "fail", str(e))

# After login, click again on cart button
try:
    driver.find_element(By.XPATH, "//button[@id='tg-minicart']//i[@class='icon-cart']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[normalize-space()='View Cart']").click()
    time.sleep(2)
    log_result("Click cart button after login", "pass")
except Exception as e:
    log_result("Click cart button after login", "fail", str(e))

# Proceed to pay
try:
    driver.find_element(By.XPATH, "//a[normalize-space()='Proceed to checkout']").click()
    time.sleep(2)
    log_result("Proceed to pay", "pass")
except Exception as e:
    log_result("Proceed to pay", "fail", str(e))

# Select radio button for payment type
try:
    driver.find_element(By.CSS_SELECTOR, "label[for='type_prepaid']").click()
    time.sleep(2)
    log_result("Select prepaid radio button", "pass")
except Exception as e:
    log_result("Select prepaid radio button", "fail", str(e))

# Place order
try:
    driver.find_element(By.XPATH, "//button[@id='place-order']").click()
    time.sleep(2)
    log_result("Place order", "pass")
except Exception as e:
    log_result("Place order", "fail", str(e))

# Close the HTML log file
html_log.write("</table></body></html>")
html_log.close()

# Close the browser
driver.quit()