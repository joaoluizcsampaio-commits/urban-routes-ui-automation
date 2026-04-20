# Urban Routes UI Test Automation

This project contains automated UI tests for the Urban Routes web application,
focusing on validating real user flows and interface behavior using browser automation.

---

## Technologies Used

- Python
- Selenium
- Pytest
- Page Object Model (POM)

---

## How to Run the Project

1. Clone the repository:

git clone https://github.com/joaoluizcsampaio-commits/urban-routes-ui-automation.git
cd urban-routes-ui-automation

2. Install dependencies:

pip install -r requirements.txt

3. Run the tests:

pytest

---

## What Was Tested

- Route setup: entering origin and destination addresses and initiating the ride request
- Tariff selection: selecting the Comfort plan and validating the active card state
- Phone number input: filling in the phone field and confirming via SMS code
- Payment method: adding a credit card and validating it as the selected payment method
- Driver message: entering a comment and verifying it was correctly saved
- Extra options: enabling the blanket and handkerchiefs toggle and validating its checked state
- Ice cream order: adding 2 units via counter and asserting the correct amount
- Order flow: triggering the taxi request and confirming the order popup appears
- Driver info display: waiting for driver assignment and validating name, rating, and photo are shown

---

## Project Purpose

This project was developed as part of a QA engineering bootcamp.

It demonstrates practical skills in:

- UI test automation
- Test structure using Page Object Model (POM)
- Writing automated test scenarios with Pytest
- Browser automation using Selenium WebDriver

---

## Author

João Sampaio
