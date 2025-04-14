# 🛒 99BooksStore E-Commerce Automation (Selenium)

⚠️ **WARNING:**  
The website `https://www.99booksstore.com` does **not exist anymore** as of the time this script was created.  
However, if the website comes back online in the future with the same structure, this script should work as expected.

---

## 📜 Description

This project is an **end-to-end automation test script** for an e-commerce platform `99booksstore.com` using **Selenium WebDriver** in Python.

It simulates a full customer journey:
- Searching and selecting books
- Adding them to the cart
- Applying a coupon code
- Logging in
- Proceeding to checkout
- Selecting a payment option
- Placing the order

All test results are logged in a **HTML report (`test_results.html`)**.

---

## 📁 Files Included

- `automation_script.py` - The main Selenium test script.
- `testdata.json` - Contains test input like book names, email, password, and coupon code.
- `test_results.html` - Auto-generated report of test execution.
- `README.md` - This file.

---

## 📦 Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your Chrome version)
- Selenium

### Install Selenium:

```bash
pip install selenium

## ▶️ How to Run

1. Make sure all dependencies are installed:
   ```bash
   pip install selenium
