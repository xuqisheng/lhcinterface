#/usr/loacl/bin/python3
#coding=utf-8

import requests
import unittest


class LeftTime(unittest.TestCase):
	'''剩余时间'''
	def setUp(self):
		self.url = "http://mdev.dian.so/lhc/1.0/device/leftTime"
		self.cookies = dict(cookies_are='h5uuid=afb51c40-8e1c-11e7-87ec-93bb4deb80ae; mid=NzQ2MzBBQzVEREI1QjNERDRGQTQwREU5OEQyMDJCRkIwNzg1OThDRDQwNzE2; role=merchant; lhcSid=OUQ3N0QxOTZGNEVGNjA3QzM3NkY1NUQzOUM0QzZGQUI1NkFCNzVEMjI0NjUzMjE=')
		self.params = {'data':'{}'}
	def test_leftTime_succsee(self):
		r = requests.get(self.url,cookies=self.cookies,params=self.params)
		result = r.json()
		print(result)
		self.assertEqual(result['success'],True)
		#self.assertIsNotNone(result['data']['currentTime'],msg=None)
		#self.assertIsNotNone(result['data']['orderNo'], msg=None)


if __name__ == '__main__':
	unittest.main()