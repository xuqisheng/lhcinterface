#/usr/loacl/bin/python3
#coding=utf-8

import requests
import unittest


class UserTest(unittest.TestCase):
	'''用户信息'''
	def setUp(self):
		self.url = "http://mdev.dian.so/lhc/1.0/user/getInfo"
		self.cookies = dict(cookies_are='h5uuid=afb51c40-8e1c-11e7-87ec-93bb4deb80ae; mid=NzQ2MzBBQzVEREI1QjNERDRGQTQwREU5OEQyMDJCRkIwNzg1OThDRDQwNzE2; role=merchant; lhcSid=OUQ3N0QxOTZGNEVGNjA3QzM3NkY1NUQzOUM0QzZGQUI1NkFCNzVEMjI0NjUzMjE=')

	def test_usertest_succsee(self):
		r = requests.get(self.url,cookies=self.cookies)
		result = r.json()
		#print(result)
		self.assertEqual(result['success'],True)
		self.assertEqual(result['data']['nick'],'小宝')
		self.assertEqual(result['data']['userId'],2465321)

if __name__ == '__main__':
	unittest.main()