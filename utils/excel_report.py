import os
from datetime import datetime
import openpyxl
from openpyxl import Workbook

REPORT_PATH = os.path.join("reports", "Login_Report.xlsx")


def init_report():
    """
    Creates the reports/ folder and the Excel file with headers,
    but only if it doesn't already exist. Safe to call before every test.
    """
    os.makedirs("reports", exist_ok=True)
    if not os.path.exists(REPORT_PATH):
        wb = Workbook()
        ws = wb.active
        ws.title = "Login Report"
        ws.append(["Test Case", "Execution Time", "Status", "Failure Reason", "Date"])
        wb.save(REPORT_PATH)


def log_result(test_case, status, failure_reason=""):
    """
    Appends one row to the Excel report.
    Called from inside each test's try/except block so every test —
    pass or fail — leaves a record.
    """
    init_report()
    wb = openpyxl.load_workbook(REPORT_PATH)
    ws = wb["Login Report"]
    now = datetime.now()
    ws.append([
        test_case,
        now.strftime("%H:%M:%S"),
        status,
        failure_reason,
        now.strftime("%Y-%m-%d"),
    ])
    wb.save(REPORT_PATH)
