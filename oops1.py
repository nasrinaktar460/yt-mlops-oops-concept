
class employee:
 
    def __init__(self):
        self.id = 123
        self.salary = 9000
        self.designation = "SDE"
        
        
    def travel (self, destination):
            print(f"employee is now Travel to {destination}")


sam = employee()
print(sam.salary)
sam.travel("kerala")

