#!/usr/bin/env python

"""Add Docstring"""

import requests
from models import Info

API = "https://api.ssllabs.com/api/v2/"

def request(path, payload={}):

	"""This is a helper method that takes the path to the relevant
		API call and the user-defined payload and requests the 
		data/server test from Qualys SSL Labs.  

		Returns a Python Object"""

	url = "%s%s" %(API, path)
	response = requests.get(url, params=payload)
	data = response.json()

	return data

def info():
	
	"""Add Docstring"""

	path = "info"
	data = request(path)

	info = Info.Info(data['engineVersion'], data['criteriaVersion'], data['clientMaxAssessments'], data['maxAssessments'], data['currentAssessments'], data['messages'] )
	return info

def analyze(host, publish="off", all="done"):
	
	"""Add Docstring"""

	path = "analyze"
	payload = {'host': host, 'publish': publish}
	data = request(path, payload)
	return data

def getEndpointData(host, s):
	
	"""Add Docstring"""

	path = "getEndpointData"
	payload = {'host': host, 's': s}
	data = request(path, payload)
	return data

def checkMyServers():
	"""This method takes a CSV file of an agency's servers
		and performs a Qualys Server Test on each one.  
		Returns a CSV file with the results."""


def test():
	info()

if __name__ == "__main__":
	test()

