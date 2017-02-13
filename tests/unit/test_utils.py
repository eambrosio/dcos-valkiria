#!/usr/bin/env python
import json
import unittest

from dcos.errors import DCOSException
from mock import patch

from dcos_valkiria.utils import get_ips, valid_ip_format, get_pem_path, get_ips_list


class TestUtils(unittest.TestCase):
    def test_get_ips(self):
        mock_response = json.loads('''{"nodes":[
        {"host_ip":"10.200.1.221","health":1,"role":"master"},
        {"host_ip":"10.200.1.213","health":1,"role":"agent"},
        {"host_ip":"10.200.1.207","health":1,"role":"agent"},
        {"host_ip":"10.200.1.208","health":0,"role":"agent"}]}''')

        with patch('dcos_valkiria.utils.get_url') as mock:
            mock.return_value = mock_response
            self.assertEqual(list(map(lambda x: str(x), get_ips('agent'))),
                             ['10.200.1.213', '10.200.1.207', '10.200.1.208'],
                             "A list with agents' ips should be returned when agent role is applied")

        with patch('dcos_valkiria.utils.get_url') as mock:
            mock.return_value = mock_response
            self.assertEqual(list(map(lambda x: str(x), get_ips('master'))),
                             ['10.200.1.221'],
                             "A list with masters' ips should be returned when master role is applied")

        with patch('dcos_valkiria.utils.get_url') as mock:
            mock.return_value = mock_response
            self.assertEqual(list(map(lambda x: str(x), get_ips(None))),
                             ['10.200.1.221', '10.200.1.213', '10.200.1.207', '10.200.1.208'],
                             "A list with all ips should be returned when no role is applied")

        with patch('dcos_valkiria.utils.get_url') as mock:
            mock.side_effect = DCOSException
            self.assertEqual(list(map(lambda x: str(x), get_ips('agent'))),
                             [],
                             "An empty list should be returned when a DCOS exception is thrown")

    def test_valid_ip_format(self):
        self.assertTrue(valid_ip_format("0.0.0.0"))
        self.assertTrue(valid_ip_format("255.255.255.255"))
        self.assertTrue(valid_ip_format(" 0.0.0.0 "))

        self.assertFalse(valid_ip_format("255.255.255.256"))
        self.assertFalse(valid_ip_format("-255.255.255.255"))
        self.assertFalse(valid_ip_format("0.0.0.0."))
        self.assertFalse(valid_ip_format("0.0.0. 0"))

    def test_get_pem_path(self):
        self.assertEquals(get_pem_path("/path/to/pem"), "-i /path/to/pem ")

    def test_get_ips_list(self):
        self.assertEquals(get_ips_list(None), 1)
        self.assertEquals(get_ips_list('10.200.1.21'), ['10.200.1.21'])
        self.assertEquals(get_ips_list('10.200.1.21,13.12.12.123'), ['10.200.1.21', '13.12.12.123'])
        self.assertEquals(get_ips_list('123.123.123.123,123.123.123.124'), ['123.123.123.123', '123.123.123.124'])
        self.assertEquals(get_ips_list('123.123.123.123 , 123.123.123.124 , 152.245.112.152'),
                          ['123.123.123.123', '123.123.123.124', '152.245.112.152'])
        self.assertEquals(get_ips_list('333.200.1.21'), [], "[[333.200.1.21]] is a not valid ip format.")
        self.assertEquals(get_ips_list('200.1.21'), [], "[[200.1.21]] is a not valid ip format.")
        self.assertEquals(get_ips_list('1233.200.1.21'), [], "[[1233.200.1.21]] is a not valid ip format.")
        self.assertEquals(get_ips_list('1233.200.1.21, 23.23.23.23'), ['23.23.23.23'],
                          "[[1233.200.1.21]] is a not valid ip format.")

if __name__ == "__main__":
    unittest.main()
