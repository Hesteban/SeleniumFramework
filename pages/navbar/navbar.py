from base.selenium_driver import SeleniumDriver
import time

class NavBar(SeleniumDriver):

	# Locators
	_navbar = 'topnavbar'
	_other= 'account-page-content'
	_navbarNavigation = 'topnavbar-main-navigation'

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver


	def waitForNavBarvisible(self,timeout=20):

		element= self.waitForElementvisible(locator=self._navbar, locatorType='id', timeout=timeout)
		return element is not None


	def getNavElements(self):
		_locator="//ul[@id='{}']/li/a".format(self._navbarNavigation)
		print(_locator)
		elemList = self.getElementList(_locator, locatorType='XPATH')
		print(elemList)
		elemTextList=  [elem.text for elem in elemList]
		return elemTextList