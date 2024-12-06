class ExcelReader:

    @staticmethod
    def readfromexcel():
        print("Read the value from excel")

class MysqlDBconnection:

    @staticmethod
    def readmysqlfile():
        print("Read the value from MySQL DB")

class TC1:

    var_Ref=10

    def testcase(self):
        ExcelReader.readfromexcel()
        MysqlDBconnection.readmysqlfile()
        print(TC1.var_Ref)  # Shared among all the instance

# TC1.testcase()

t=TC1()
t.testcase()