# Login Automation Suite — Execution Guide

Automated test suite for the login flow on [saucedemo.com](https://www.saucedemo.com/),
built with **Selenium**, **pytest**, and the **Page Object Model**. Results are
logged automatically to an Excel report.

## Prerequisites

- Python 3.9+
- Google Chrome installed
- Internet connection (first run downloads a matching ChromeDriver automatically)

## Setup

```bash
# 1. Navigate to the project folder
cd LoginAutomation

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 4. Install dependencies
pip install -r requirements.txt
```

## Running the Suite

Run all tests, from the project root:

```bash
pytest tests/test_login.py -v
```

Run a single test case:

```bash
pytest tests/test_login.py::test_valid_login -v
```

**What happens when you run it:** a Chrome window opens automatically for
each test, performs the login steps, checks the result, then closes. This
repeats for every test case in the suite.

## Viewing Results

Two places to check after a run:

1. **Terminal output** — pytest prints PASS/FAIL per test as it runs.
2. **`reports/Login_Report.xlsx`** — a spreadsheet row is added for every
   test, with columns: Test Case, Execution Time, Status, Failure Reason, Date.
   This file is created automatically on first run.

## Test Cases in This Suite

| Test | What It Checks |
|---|---|
| Valid Login | Correct credentials reach the inventory page |
| Invalid Login | Wrong credentials trigger the mismatch error |
| Empty Username | Blank username is rejected |
| Empty Password | Blank password is rejected |
| Both Fields Empty | Blank username + password is rejected |
| Locked User | `locked_out_user` account is blocked with the correct message |

## Troubleshooting

| Issue | Likely Cause |
|---|---|
| `ModuleNotFoundError: No module named 'selenium'` | Virtual environment not activated before install/run |
| Chrome opens then closes instantly with an error | Chrome browser is out of date relative to ChromeDriver |
| `pytest` reports "no tests ran" | Command run from the wrong directory — run from the project root |
| Excel file locked / can't be written | `Login_Report.xlsx` is open in another program — close it before running tests |
