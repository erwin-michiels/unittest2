import unittest
import IPv4_subnets as t

class TestIPv4_subnets(unittest.TestCase):

    def test_get_net_prefix(self):
        self.assertEqual(t.get_net_prefix('255.255.255.252'), '/30')
        #self.assertTrue()
        #self.assertFalse()
        #

    def test_get_number_ip_addresses(self):
        self.assertEqual(t.get_number_ip_addresses('/30'), 4)

    def test_get_number_ip_hosts(self):
        self.assertEqual(t.get_number_ip_hosts('/30'), 2)

    def test_get_netmask(self):
        self.assertEqual(t.get_netmask('/30'), '255.255.255.252')

    def test_get_network_bits(self):
        self.assertEqual(t.get_network_bits('255.255.255.252'), '1111 1111 1111 1111 1111 1111 1111 1100')

if __name__ == "__main__":
    unittest.main()