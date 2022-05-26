import time

import pytest
from Pageobjects.checkLoanEligibility import LoanEligibility
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGenerator
from Utilities.readDataSheet import ReadDataSheet


class TestCheckLoanEligibility:
    print("inside Test_Check_Loan_Eligibility")
    baseurl = ReadConfig.get_app_url()
    logger = LogGenerator.log_gen()
    xlpath = "..\\TestData\\Loan_Eligibility_Calc.xlsx"
    sheetname = "Loan_amt_calc"

    #@pytest.mark.skip
    def test_01_check_loan_amount(self, set_up):
        self.driver = set_up
        self.driver.get(self.baseurl)
        self.cle = LoanEligibility(self.driver)
        self.logger.info("***start of test 01 ***")

        if self.cle.verify_logo()== True:
            self.logger.info("Logo is present")
        else:
            self.logger.info("Logo is not present")

        self.rows = ReadDataSheet.get_max_rcount(self.xlpath, self.sheetname)
        print(self.rows)

        try:
            for r in range(2, self.rows+1):
                self.app_type = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 1)
                self.dependant_val = ReadDataSheet.read_data(self.xlpath, self.sheetname,r, 2)
                self.prop_to_buy = ReadDataSheet.read_data(self.xlpath, self.sheetname,r, 3)
                self.annual_income = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 4)
                self.other_ann_income = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 5)
                self.monthly_expense = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 6)
                self.current_hl = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 7)
                self.other_loan = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 8)
                self.other_commitment = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 9)
                self.cc_limit = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 10)
                self.loan_eligibility = ReadDataSheet.read_data(self.xlpath, self.sheetname, r, 11)
                print("dependant_val is: ", self.dependant_val)
                time.sleep(2)
                self.cle.set_apptype(self.app_type)
                obj_dependant = self.cle.select_dependants()
                obj_dependant.select_by_visible_text(str(self.dependant_val))
                self.logger.info("Dependant selected")
                self.cle.click_prop_to_buy(self.prop_to_buy)
                self.cle.set_annual_income(self.annual_income)
                self.cle.set_other_ann_income(self.other_ann_income)
                self.cle.set_monthly_expen(self.monthly_expense)
                self.cle.set_current_hl(self.current_hl)
                self.cle.set_other_loan(self.other_loan)
                self.cle.set_other_monthly_commitment(self.other_commitment)
                self.cle.set_cc_limit(self.cc_limit)
                self.logger.info("*** Form filled completely***")
                self.cle.click_borrow()
                loan_amt = self.cle.verify_eligible_loan_amt()
                assert loan_amt != self.loan_eligibility
                self.logger.info("Test case passed")
        except Exception as err:
            self.driver.save_screenshot("..\\Screenshots\\" + "test.png")
            print("Exception occurred is :", err)
            self.logger.info("Inside Except block: ")
        finally:
            self.logger.info("Test_01_Execution completed")
            self.driver.close()

    #@pytest.mark.skip
    def test_02_start_over(self,set_up):
        self.driver = set_up
        self.driver.get(self.baseurl)
        self.cle = LoanEligibility(self.driver)
        self.logger.info("***start of test_02_start_over ***")

        if self.cle.verify_logo()== True:
            self.logger.info("Logo is present")
        else:
            self.logger.info("Logo is not present")

        try:
            obj_dependant = self.cle.select_dependants()
            self.logger.info("selecting the dependants")
            obj_dependant.select_by_visible_text(str(ReadDataSheet.read_data(self.xlpath, self.sheetname, 2, 2)))
            self.cle.set_annual_income(ReadDataSheet.read_data(self.xlpath, self.sheetname, 2, 4))
            self.logger.info("Dependant selected and annual income set")
            self.cle.verify_start_over()
            time.sleep(2)
            if obj_dependant.first_selected_option.text == "0" and self.cle.get_annual_income() == "0":
                self.logger.info("All values reset.Please do it again")
            else:
                self.logger.info("Reset not working")

        except Exception as err:
            self.driver.save_screenshot("..\\Screenshots\\" + "test.png")
            self.logger.info("Inside Except block: ")

        finally:
            self.logger.info("Test case no 02 Execution completed")
            self.driver.close()

    #@pytest.mark.skip
    def test_03_low_monthly_expense(self, set_up):
        self.driver = set_up
        self.driver.get(self.baseurl)
        self.cle = LoanEligibility(self.driver)
        self.logger.info("***start of test_03_low_monthly_expense ***")

        if self.cle.verify_logo()== True:
            self.logger.info("Logo is present")
        else:
            self.logger.info("Logo is not present")

        try:
            self.cle.set_monthly_expen("1")
            self.cle.click_borrow()
            time.sleep(2)
            self.logger.info("Borrow button clicked")
            err_txt = self.cle.verify_error_message()
            err_msg = "Based on the details you've entered, we're unable to give you an estimate" \
                      " of your borrowing power with this calculator. For questions, " \
                      "call us on 1800 035 500."
            if err_txt == err_msg:
                self.logger.info("Error message matched")

        except Exception as err:
            self.driver.save_screenshot("..\\Screenshots\\"+"test.png")
            self.logger.info("Inside Except block: ")

        finally:
            self.logger.info("Test case no 03 Execution completed")
            self.driver.close()

