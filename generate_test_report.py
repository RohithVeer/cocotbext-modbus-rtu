import os
import xml.etree.ElementTree as ET
from datetime import datetime

# File paths
RESULTS_XML = "results.xml"
REPORT_DIR = "test_reports"
REPORT_FILE_TXT = os.path.join(REPORT_DIR, "test_report.txt")
REPORT_FILE_HTML = os.path.join(REPORT_DIR, "test_report.html")

def parse_results(xml_file):
    tests = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for testcase in root.iter("testcase"):
        name = testcase.attrib.get("name", "Unknown")
        classname = testcase.attrib.get("classname", "Unknown")
        time = testcase.attrib.get("time", "0")
        status = "PASS"
        if testcase.find("failure") is not None:
            status = "FAIL"
        elif testcase.find("skipped") is not None:
            status = "SKIP"
        tests.append((classname, name, status, time))
    return tests

def generate_txt_report(tests):
    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(REPORT_FILE_TXT, "w") as f:
        f.write("Phase 2 - MODBUS RTU VIP Test Report\n")
        f.write(f"Generated on: {datetime.now()}\n")
        f.write("=" * 70 + "\n")
        f.write("Phase Summary:\n")
        f.write("Phase 2 focuses on complete end-to-end verification:\n")
        f.write(" - Driver sends Modbus frame with address, function code, and CRC\n")
        f.write(" - Monitor captures echoed response and checks integrity\n")
        f.write(" - Scoreboard compares frames and CRC\n")
        f.write(" - Coverage and error checks ensure protocol compliance\n")
        f.write("=" * 70 + "\n\n")

        for classname, name, status, sim_time in tests:
            f.write(f"Module       : {classname}\n")
            f.write(f"Test         : {name}\n")
            f.write(f"Status       : {status}\n")
            f.write(f"Sim Time     : {sim_time} s\n")
            f.write("-" * 60 + "\n")

        passed = sum(1 for t in tests if t[2] == "PASS")
        failed = sum(1 for t in tests if t[2] == "FAIL")
        skipped = sum(1 for t in tests if t[2] == "SKIP")
        total = len(tests)
        f.write("Summary:\n")
        f.write(f"  Total   : {total}\n")
        f.write(f"  Passed  : {passed}\n")
        f.write(f"  Failed  : {failed}\n")
        f.write(f"  Skipped : {skipped}\n")

def generate_html_report(tests):
    os.makedirs(REPORT_DIR, exist_ok=True)
    with open(REPORT_FILE_HTML, "w") as f:
        f.write("<html><head><title>Phase 2 - MODBUS RTU VIP Test Report</title>\n")
        f.write("<style>")
        f.write("body { font-family: Arial; padding: 20px; }")
        f.write("table { border-collapse: collapse; width: 100%; }")
        f.write("th, td { border: 1px solid #888; padding: 8px; text-align: left; }")
        f.write("th { background-color: #f2f2f2; }")
        f.write(".PASS { color: green; font-weight: bold; }")
        f.write(".FAIL { color: red; font-weight: bold; }")
        f.write(".SKIP { color: orange; font-weight: bold; }")
        f.write("</style></head><body>\n")

        f.write("<h1>Phase 2 - MODBUS RTU VIP Test Report</h1>\n")
        f.write(f"<p><strong>Generated on:</strong> {datetime.now()}</p>\n")
        f.write("<p>This report summarizes the results of Phase 2, which verifies end-to-end MODBUS RTU communication including CRC validation, signal synchronization, and passive monitoring.</p>\n")

        f.write("<h2>Test Results</h2>\n")
        f.write("<table>\n")
        f.write("<tr><th>Test Case</th><th>Functionality</th><th>Expected Behavior</th><th>Status</th><th>Sim Time (s)</th></tr>\n")
        for classname, name, status, t in tests:
            functionality = "Full Modbus TX/RX with echo, CRC, coverage"
            expected = "Frame echoed correctly and validated"
            f.write(f"<tr><td>{name}</td><td>{functionality}</td><td>{expected}</td><td class='{status}'>{status}</td><td>{t}</td></tr>\n")
        f.write("</table>\n")

        passed = sum(1 for t in tests if t[2] == "PASS")
        failed = sum(1 for t in tests if t[2] == "FAIL")
        skipped = sum(1 for t in tests if t[2] == "SKIP")
        total = len(tests)
        f.write("<h2>Summary</h2>\n")
        f.write(f"<p>Total: {total}, Passed: <span class='PASS'>{passed}</span>, Failed: <span class='FAIL'>{failed}</span>, Skipped: <span class='SKIP'>{skipped}</span></p>\n")

        f.write("</body></html>\n")

if __name__ == "__main__":
    if not os.path.exists(RESULTS_XML):
        print(f"[ERROR] {RESULTS_XML} not found. Please run `make` first.")
    else:
        test_results = parse_results(RESULTS_XML)
        generate_txt_report(test_results)
        generate_html_report(test_results)
        print(f"[✓] Text report generated: {REPORT_FILE_TXT}")
        print(f"[✓] HTML report generated: {REPORT_FILE_HTML}")

