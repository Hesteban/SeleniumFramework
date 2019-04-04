from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

	def __init__(self,driver):
		super().__init__(driver)
		self.driver= driver


	#Locators
	_user='user'
	_password='password'
	_submit='submit'
	_errorMessage='errorMessage'
	_changepass='//a[contains(text(),"acceder")]'
	_password_recovery='password-recovery'
	_registrate='//a[contains(text(),"Regístrate")]'
	_registryForm='registerForm'
	_rememberMeCheck='//label[@for="rememberMe"]'
	_rememberMeInput='rememberMe'



	def setCredentials(self,user, password):
		self.sendKeys(user, locator=self._user, locatorType='id')
		self.sendKeys(password, locator=self._password, locatorType='id')


	def clickSubmit(self):
		self.elementClick(locator=self._submit, locatorType='id')

	def errorMessageVisible(self):
		message = self.waitForElementvisible(locator=self._errorMessage, locatorType='id')
		return message is not None

	def clickChangePass(self):
		self.elementClick(locator=self._changepass,locatorType='XPATH')

	def passwordRecoveryVisible(self):
		element = self.waitForElementvisible(locator=self._password_recovery, locatorType='id')
		return element is not None

	def clickRegistrate(self):
		self.elementClick(locator=self._registrate, locatorType='XPATH')

	def registryFormVisible(self):
		element = self.waitForElementvisible(locator=self._registryForm, locatorType='id')
		return element is not None

	def uncheckRemberme(self):

		if self.getElement(locator=self._rememberMeInput,locatorType='id').is_selected():
			self.log.debug("Remembeme check set to True")
			self.elementClick(locator=self._rememberMeCheck,locatorType='XPATH')
			self.log.debug("Remembeme check set to False")
		else:
			self.log.debug("Remembeme check set to False")

