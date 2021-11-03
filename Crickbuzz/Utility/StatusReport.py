from Utility import logger as cl
from prettytable import PrettyTable


class status:
    log = cl.customlogger()

    def Verify_result(self, result, msg):
        if result == True:
            assert True == True
            self.log.info("##### %s Verification passed successfully######", msg)
        else:
            self.log.error("***** %s Verification Failed ******", msg)
            assert True == False

    def verify_text(self, expected_text, actual_text, msg):
        resultTable = PrettyTable(["Expected Result", "Actual Result", "Status"])
        if expected_text == actual_text:
            assert True == True
            resultTable.add_row([expected_text, actual_text, "Pass"])
            self.log.info("\n%s", resultTable)
            self.log.info("##### %s Verification passed successfully######", msg)

        else:
            resultTable.add_row([expected_text, actual_text, "Fail"])
            self.log.error("***** %s Verification Failed ******", msg)
            self.log.info("\n %s", resultTable)
            assert True == False

    def verify_Num_Condition(self, expected_value, actual_value, condition, msg):
        resultTable = PrettyTable(["Expected Result", "Actual Result", "Status"])
        if condition == "eq":
            if actual_value == expected_value:
                assert True == True
                resultTable.add_row([condition+" "+str(expected_value), actual_value, "Pass"])
                self.log.info("\n%s", resultTable)
                self.log.info("##### %s Verification passed successfully######", msg)

            else:
                resultTable.add_row([condition+" "+str(expected_value), actual_value, "Fail"])
                self.log.error("***** %s Verification Failed ******", msg)
                self.log.info("\n %s", resultTable)
                assert True == False

        elif condition == "gt":
            if actual_value > expected_value:
                assert True == True
                resultTable.add_row([condition+" "+str(expected_value), actual_value, "Pass"])
                self.log.info("\n%s", resultTable)
                self.log.info("##### %s Verification passed successfully######", msg)

            else:
                resultTable.add_row([condition+" "+str(expected_value), actual_value, "Fail"])
                self.log.error("***** %s Verification Failed ******", msg)
                self.log.info("\n %s", resultTable)
                assert True == False

        if condition == "lt":
            if actual_value < expected_value:
                assert True == True
                resultTable.add_row([condition+" "+str(expected_value), actual_value, "Pass"])
                self.log.info("\n%s", resultTable)
                self.log.info("##### %s Verification passed successfully######", msg)

            else:
                resultTable.add_row([condition+" "+str(expected_value), actual_value, "Fail"])
                self.log.error("***** %s Verification Failed ******", msg)
                self.log.info("\n %s", resultTable)
                assert True == False
