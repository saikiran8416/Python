"""Write a program that produces:

Total Tests: 6
PASS: 3
FAIL: 2
BLOCKED: 1"""
tests = {
    "TC001": "PASS",
    "TC002": "FAIL",
    "TC003": "PASS",
    "TC004": "FAIL",
    "TC005": "PASS",
    "TC006": "BLOCKED"
}
total=len(tests)
passed,failed,blocked=0,0,0
for i in tests:
    if tests[i].lower()=="pass":
        passed+=1
    elif tests[i].lower()=="fail":
        failed+=1
    else:
        blocked+=1

print(f"Total Tests: {total}")
print(f"PASS: {passed}")
print(f"FAIL: {failed}")
print(f"BLOCKED: {blocked}")
