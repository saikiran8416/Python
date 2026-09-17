# write a program to check the pass and failed cases in the nested list an print the total test cases and numbe rof passed test and failed tests.
test_results = [
    ["TC001", "PASS"],
    ["TC002", "FAIL"],
    ["TC003", "PASS"],
    ["TC004", "FAIL"],
    ["TC005", "PASS"]
]
total_tests=len(test_results)
passed,failed=0,0
for i in range(len(test_results)):
    if test_results[i][1].lower()=="pass":
        passed+=1
    else:
        failed+=1
print(f"total tests:{total_tests}")
print(f"passed: {passed}")
print(f"faield: {failed}")

"""output:
Total Tests: 5
Passed: 3
Failed: 2"""