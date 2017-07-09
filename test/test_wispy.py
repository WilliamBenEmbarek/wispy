import sys
from os.path import abspath
sys.path.append(abspath('..'))
import unittest
from manuf import manuf
import wispy

class WispyTests(unittest.TestCase):

	pkt1 = b'\x00\x00\x1a\x00/H\x00\x00\xc4\x86\x0f\rY\x05\x00\x00\x10\x02\x8f\t\xa0\x00\xc3\x01\x00\x00@\x00\x00\x00\xff\xff\xff\xff\xff\xff\x00\x124\x00\r\xef\xff\xff\xff\xff\xff\xffp\xa2\x00\x08JaffaNet\x01\x04\x02\x04\x0b\x162\x08\x0c\x12\x18$0H`l-\x1a\x0c\x10\x19\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\x06\xdd\t\x00\x10\x18\x02\x00\x00\x00\x00\x00\xdd\x1e\x00\x90L3\x0c\x10\x19\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcfy\x16*'
	#{'timestamp': '2017-07-09 10:12:04:231981', 'mac': '00:12:34:00:0d:ef', 'channel': 2447, 'rssi': -61, 'ssid': 'JaffaNet', 'vendor': 'Camille Bauer'} 

	pk2 = b'\x00\x00\x1a\x00/H\x00\x00[\xbdM\x11Y\x05\x00\x00\x10\x02\x9e\t\xa0\x00\xbf\x01\x00\x00@\x00\x00\x00\xff\xff\xff\xff\xff\xffT`\t\\\rD\xff\xff\xff\xff\xff\xffp.\x00\x0bSHAW-BED319\x01\x08\x02\x04\x0b\x0c\x12\x16\x18$\x03\x01\x0b-\x1ab\x00\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xe0\xe1\t\x002\x040H`l\x7f\x08\x00\x00\x00\x00 \x00\x00@\xbf\x0c0p\xc03\xfc\xff$\x01\xfc\xff$\x010\xa8\x14\xba'
	#{'timestamp': '2017-07-09 10:13:15:418697', 'mac': '54:60:09:5c:0d:44', 'channel': 2462, 'rssi': -65, 'ssid': 'SHAW-BED319', 'vendor': 'Google, Inc.'}

	pk3 = b'\x00\x00\x1a\x00/H\x00\x00\xae\xf7\xe1\x12Y\x05\x00\x00\x10\x02\x80\t\xa0\x00\xc1\x01\x00\x00@\x00\x00\x00\xff\xff\xff\xff\xff\xffLfA\xa5\x9cx\xff\xff\xff\xff\xff\xff\xe0H\x00\x00\x01\x04\x02\x04\x0b\x162\x08\x0c\x12\x18$0H`l\x03\x01\x05-\x1a-\x00\x17\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x08\x00\x00\x08\x80\x01@\x00@k\x01\x0f\xdd\x05Po\x9a\x10\x10\xdd\x13\x00\x90L\x04\x08\xbf\x0c2X\x81\x0f\xfa\xff\x00\x00\xfa\xff\x00\x00\xdd\x07\x00P\xf2\x08\x00\x11\x00\xdd\t\x00\x10\x18\x02\x00\x00\x10\x00\x00S\xb1\x8d\xc2'
	#{'timestamp': '2017-07-09 10:13:41:910725', 'mac': '4c:66:41:a5:9c:78', 'channel': 2432, 'rssi': -63, 'ssid': 'None', 'vendor': 'SAMSUNG ELECTRO-MECHANICS(THAILAND)'}
	
	def setUp(self):
		parsed_packet = wispy.parse_packet()

	def test_packet_parser_timestamp(self):
		self.assertEqual(len(self.parsed_packet['timestamp']), 10, 'Unix epoch should be a length of 10.')

if __name__ == '__main__':
	unittest.main()
