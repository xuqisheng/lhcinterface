#/usr/loacl/bin/python3
#coding=utf-8

import requests
import unittest

class LoginTest(unittest.TestCase):
	'''登录接口测试'''

	def setUp(self):
		self.url = "http://mdev.dian.so/lhc/1.0/login"

	def test_logintest_success(self):
		r = requests.get(self.url,params={'data':'{"wxUnionid":"oACeFweiqROLu6nf9L5dTGCeEBZQ"}'})
		result = r.json()
		#print(result)
		self.assertEqual(result["success"],True)
		self.assertEqual(result["data"]["nick"],"小宝")
		self.assertEqual(result["data"]["userId"],"2465321")


if __name__ == '__main__':
	unittest.main()