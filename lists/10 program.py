"""Write a program that finds:

Number of passed tests
Number of failed tests
Failed test-case IDs
Slowest test case
Fastest test case
Average execution time
All tests taking more than 200 ms"""
logs = [
    ["TC001", "PASS", 120],
    ["TC002", "FAIL", 350],
    ["TC003", "PASS", 180],
    ["TC004", "FAIL", 500],
    ["TC005", "PASS", 90],
    ["TC006", "FAIL", 250]
]

passed,failed=0,0
failed_ids=[]
passed_ids=[]
slowest_tc=logs[0][len(logs[0])-1]
slowest_tc_pos=0
fastest_tc=logs[0][len(logs[0])-1]
fastest_tc_pos=0
total_execution_time=0
_200ms_execution_time=[]
for i in range(len(logs)):
    if slowest_tc>logs[i][len(logs[0])-1]:
        slowest_tc=logs[i][len(logs[0])-1]
        slowest_tc_pos=i
    if fastest_tc<logs[i][len(logs[0])-1]:
            fastest_tc=logs[i][len(logs[0])-1]
            fastest_tc_pos=i
    if logs[i][len(logs[0])-1]>=200:
         _200ms_execution_time.append(logs[i])
    total_execution_time+=logs[i][len(logs[0])-1]
    if logs[i][len(logs[0])-2].lower()=="pass":
         passed+=1
         passed_ids.append(logs[i])
    else:
         failed+=1
         failed_ids.append(logs[i])

print(f"Number of passed tests: {passed}")
print(f"Number of failed tests {failed}")
print(f"Failed test-case IDs {failed_ids}")
print(f"Slowest test case {logs[slowest_tc_pos]}")
print(f"Fastest test case {logs[fastest_tc_pos]}")
print(f"Average execution time {total_execution_time/(len(logs))}")
print(f"All tests taking more than 200 ms {_200ms_execution_time}")