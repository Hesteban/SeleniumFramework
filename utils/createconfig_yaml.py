import yaml


def createConfigfromYaml(filepath, mode='r'):
	f = open(filepath, mode)
	config = yaml.load(f)

	return config
