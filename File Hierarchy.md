## Project Structure

```
LoginAutomation/
│
├── pages/
│   └── login_page.py         # Page Object Model for the login page
│
├── tests/
│   └── test_login.py         # All test cases + pytest fixture
├── reports/
│   └── Login_Report.xlsx     # Generated automatically on first test run
│
├── utils/
│   ├── driver_factory.py     # Chrome WebDriver setup
│   └── excel_report.py       # Writes results to reports/Login_Report.xlsx
│
│
│
├── config.py                 # Base URL and test credentials
├── requirements.txt          # Project dependencies
├── .gitignore
├── README.md                 # Full project documentation

```
