from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoanEligibility:
    img_logo_xpath = "//a[@title='ANZ Logo']"
    text_loanelig_xpath = "//span[text()='How much could I borrow?']"
    btn_app_single_xpath = "//input[@id='application_type_single' and @class='application_type']"
    btn_app_joint_xpath = "//input[@id='application_type_joint' and @class='application_type']"
    ddn_dependent_xpath = "//select[@title='Number of dependants']"
    btn_prop_home_xpath = "//input[@id='borrow_type_home' and @class='borrow_type']"
    btn_prop_invest_xpath = "//input[@id='borrow_type_investment' and @class='borrow_type']"
    tbx_annual_inc_xpath = "//input[@aria-labelledby='q2q1']"
    tbx_other_inc_xpath = "//input[@aria-labelledby='q2q2']"
    tbx_mon_exp_xpath = "//input[@aria-labelledby='q3q1']"
    tbx_curr_hl_xpath = "//input[@aria-labelledby='q3q2']"
    tbx_other_loan_xpath = "//input[@aria-labelledby='q3q3']"
    tbx_other_moncomm_xpath = "//input[@aria-labelledby='q3q4']"
    tbx_cc_limit_xpath = "//input[@aria-labelledby='q3q5']"
    btn_borrow_id = "btnBorrowCalculater"
    webelm_hl_borrow_xpath = "//h3[@class='homeloan__borrow__text']"
    webelm_loanamt_id = "borrowResultTextAmount"
    btn_start_over_class = "start-over"
    webelm_error_xpath = "//div[@class='borrow__error__text']"

    def __init__(self, driver):
        self.driver = driver


    def verify_logo(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.img_logo_xpath)))
        logo_presence = element.is_displayed()
        return logo_presence


    def verify_loan_eligibility_page(self):
        loan_elig = self.driver.find_element(By.XPATH, self.text_loanelig_xpath)
        text_lnelig = loan_elig.text
        return text_lnelig

    def set_apptype(self,app_type):
        if app_type == "Single":
            self.driver.find_element(By.XPATH, self.btn_app_single_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.btn_app_joint_xpath).click()

    def select_dependants(self):
        ddn_dependent = self.driver.find_element(By.XPATH, self.ddn_dependent_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", ddn_dependent)
        sel = Select(ddn_dependent)
        return sel


    def click_prop_to_buy(self,prop_to_buy):
        if prop_to_buy == "Home to live in":
            self.driver.find_element(By.XPATH, self.btn_prop_home_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.btn_prop_invest_xpath).click()

    def set_annual_income(self, annual_income):
        self.driver.find_element(By.XPATH, self.tbx_annual_inc_xpath).send_keys(annual_income)

    def get_annual_income(self):
        ann_inc= self.driver.find_element(By.XPATH, self.tbx_annual_inc_xpath).get_attribute("value")
        return ann_inc

    def set_other_ann_income(self, other_income):
        self.driver.find_element(By.XPATH, self.tbx_other_inc_xpath).send_keys(other_income)


    def set_monthly_expen(self, monthly_expen):
        self.driver.find_element(By.XPATH, self.tbx_mon_exp_xpath).send_keys(monthly_expen)


    def set_current_hl(self, current_hl):
        self.driver.find_element(By.XPATH, self.tbx_curr_hl_xpath).send_keys(current_hl)


    def set_other_loan(self, other_loan):
        self.driver.find_element(By.XPATH, self.tbx_other_loan_xpath).send_keys(other_loan)


    def set_other_monthly_commitment(self, other_commitment):
        self.driver.find_element(By.XPATH, self.tbx_other_moncomm_xpath).send_keys(other_commitment)

    def set_cc_limit(self, cc_limit):
        self.driver.find_element(By.XPATH, self.tbx_cc_limit_xpath).send_keys(cc_limit)

    def click_borrow(self):
        self.driver.find_element(By.ID, self.btn_borrow_id).click()

    def verify_eligible_loan_amt(self):
        loan_amt = self.driver.find_element(By.ID, self.webelm_loanamt_id)
        if loan_amt.is_displayed() == True:
            loan_amt_text = loan_amt.text
        return loan_amt_text

    def verify_start_over(self):
        start_over = self.driver.find_element(By.CLASS_NAME, self.btn_start_over_class)
        if start_over.is_displayed() == True:
            start_over.click()

    def verify_error_message(self):
        err_msg_obj = self.driver.find_element(By.XPATH, self.webelm_error_xpath)
        err_msg_text = err_msg_obj.text
        return err_msg_text
