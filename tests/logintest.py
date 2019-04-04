import unittest
from selenium import webdriver
from tests.basetest import testunittest
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from pages.landing.landing_page import LandingPage
import time


class LoginTests(testunittest):

    def setUp(self):

       self.log.info("Executing test setup")
       self.driver = webdriver.Chrome(self.driverLocation)
       self.driver.maximize_window()
       self.driver.implicitly_wait(3)
       baseUrl = self.config['credentials']['url']
       self.log.info("url: {}".format(baseUrl))
       self.driver.get(baseUrl)

       homepage = HomePage(self.driver)
       homepage.clickonEntrar()

    def tearDown(self):
        self.log.info("Executing test tearDown")
        self.driver.quit()



    def test_10_Login_using_phonenumber(self):
        self.log.info("Executing test: {}".format(self.id().split('.')[-1]))

        username = self.config['credentials']['phone_number']
        password= self.config['credentials']['password']

        loginpage= LoginPage(self.driver)
        loginpage.uncheckRemberme()
        loginpage.setCredentials(username, password)
        loginpage.clickSubmit()

        landingpage= LandingPage(self.driver)

        self.assertTrue(landingpage.waitForNavBarvisible())

    def test_20_Login_using_email(self):
        self.log.info("Executing test: {}".format(self.id().split('.')[-1]))

        username = self.config['credentials']['email']
        password = self.config['credentials']['password']

        loginpage = LoginPage(self.driver)
        loginpage.uncheckRemberme()
        loginpage.setCredentials(username, password)
        loginpage.clickSubmit()

        landingpage = LandingPage(self.driver)
        self.assertTrue(landingpage.waitForNavBarvisible())

    def test_30_Login_using_wrong_credentials(self):
        self.log.info("Executing test: {}".format(self.id().split('.')[-1]))

        username = '2342342'
        password= self.config['credentials']['password']

        loginpage= LoginPage(self.driver)
        loginpage.setCredentials(username, password)
        loginpage.clickSubmit()

        self.assertTrue(loginpage.errorMessageVisible())

    def test_40_ChangePassword_is_shown(self):
        self.log.info("Executing test: {}".format(self.id().split('.')[-1]))

        loginpage= LoginPage(self.driver)
        loginpage.clickChangePass()

        self.assertTrue(loginpage.passwordRecoveryVisible())

    def test_50_RegisterForm_is_shown(self):
        self.log.info("Executing test: {}".format(self.id().split('.')[-1]))

        loginpage = LoginPage(self.driver)
        loginpage.clickRegistrate()

        self.assertTrue(loginpage.registryFormVisible())

    def test_60_NavBar_elements_are_correct(self):
        self.log.info("Executing test: {}".format(self.id().split('.')[-1]))

        expectedElements=["Tarifas","Comunidad","Blog","Ayuda", "Cuenta", "Mi Tuenti"]

        username = self.config['credentials']['email']
        password = self.config['credentials']['password']

        loginpage = LoginPage(self.driver)
        loginpage.setCredentials(username, password)
        loginpage.clickSubmit()

        landingpage = LandingPage(self.driver)
        landingpage.waitForNavBarvisible(timeout=20)

        currentElements = landingpage.getNavElements()
        self.assertListEqual(expectedElements, currentElements )

if __name__ == '__main__':
    unittest.main(verbosity=2)



