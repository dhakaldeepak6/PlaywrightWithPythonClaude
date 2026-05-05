class TESTCASE:
    def __init__(self, tc_id, status, priority):
        self.tc_id = tc_id
        self.status = status
        self.priority =priority
        
    def summary(self):
        return (f"Test Case ID: {self.tc_id}, Status: {self.status}, Priority: {self.priority}")
    
test1 = TESTCASE ("TC001", "Pass", "High")
test2 = TESTCASE ("TC002", "Fail", "Medium")
test3 = TESTCASE("TC003", "Pass", "Low")
print(test1.summary())
print(test2.summary())
print(test3.summary())