from base.selenium_driver import SeleniumDriver

class HomePage(SeleniumDriver):

	def __init__(self,driver):
		super().__init__(driver)
		self.driver= driver


	#Locators
	_entrar ='//a[contains(text(),"Entrar")]'

	def clickonEntrar(self):
		entrarButton = self.waitForElementvisible(locator=self._entrar, locatorType='XPATH')
		self.elementClick(element=entrarButton)


