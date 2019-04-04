from base.selenium_driver import SeleniumDriver
from pages.navbar.navbar import NavBar

class LandingPage(NavBar):

	def __init__(self,driver):
		super().__init__(driver)
		self.driver= driver


	#Locators
