
# Monkey Patching

class Test:
    def __init__(self, a):
        self.a=a
    def get_data(self):
        print("fetch data from database")
    def f1(self):
        self.get_data()
obj=Test(5)
obj.f1()
print("\n")
def new_get_data(self):
    print("fetch data from Test")
Test.get_data=new_get_data
print("after monkey patching")
obj.f1()
