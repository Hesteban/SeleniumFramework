import unittest
import utils.custom_logger as cl
import logging
import utils.createconfig_yaml as cc
import os



root_path = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))
print(root_path)
config_path = os.path.join(root_path, 'conf')
config_file = os.path.join(config_path, 'config_tuenti.yml')

class testunittest(unittest.TestCase):

	log = cl.customLogger(logging.DEBUG)

	@classmethod
	def setUpClass(cls):

		cls.config = cc.createConfigfromYaml(config_file)
		cls.log.info("Executing Setup Class")

		driverKeys = cls.config['driver'].keys()
		if 'chrome' in driverKeys:
			cls.driverLocation = cls.config['driver']['chrome']

		else:
			raise (
				"Invalid driver error"
			)



	# @classmethod
	# def tearDownClass(cls):
	# 	cls.log.info("Executing Teardown Class")
	# 	cls.log.info("Closing webdriver")
	# 	cls.driver.quit()
