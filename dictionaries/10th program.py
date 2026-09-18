test_report = {
    "TC001": {
        "result": "PASS",
        "time": 120,
        "module": "Login"
    },
    "TC002": {
        "result": "FAIL",
        "time": 350,
        "module": "Login"
    },
    "TC003": {
        "result": "PASS",
        "time": 180,
        "module": "Payment"
    },
    "TC004": {
        "result": "FAIL",
        "time": 500,
        "module": "Payment"
    },
    "TC005": {
        "result": "PASS",
        "time": 90,
        "module": "Login"
    }
}

passed,failed=0,0
failed_ids=[]
passed_ids=[]
slowest_tc={}
slowest_tc_time=0
fastest_tc={}
fastest_tc_time=0
total_execution_time=0
_200ms_execution_time={}
modules={}
for i in test_report.keys():
    if slowest_tc_time>test_report[i]["time"]:
        slowest_tc.clear()
        slowest_tc.setdefault(i,test_report[i])
        slowest_tc_time=test_report[i]["time"]
    if fastest_tc_time<test_report[i]["time"]:
            fastest_tc.clear()
            fastest_tc.setdefault(i,test_report[i])
            fastest_tc_time=test_report[i]["time"]
    if test_report[i]["time"]>=200:
         _200ms_execution_time.setdefault(i,test_report[i])
    total_execution_time+=test_report[i]["time"]
    if test_report[i]["result"].lower()=="pass":
         passed+=1
         passed_ids.append(i)
    else:
         failed+=1
         failed_ids.append(i)
    if test_report[i]["module"] in modules:
         modules[test_report[i]["module"]]=modules.get(test_report[i]["module"],0)+1
    else:
         modules[test_report[i]["module"]]=1

print(f"Number of passed tests: {passed}")
print(f"Number of failed tests {failed}")
print(f"Failed test-case IDs {failed_ids}")
print(f"Slowest test case {slowest_tc_time}")
print(f"Fastest test case {fastest_tc_time}")
print(f"Average execution time {total_execution_time/(len(test_report))}")
print(f"All tests taking more than 200 ms {_200ms_execution_time}")
print(f"modules: {modules}")