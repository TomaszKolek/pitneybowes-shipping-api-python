# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pbshipping
from pbshipping.api.pickup_api import PickupApi  # noqa: E501
from pbshipping.rest import ApiException


class TestPickupApi(unittest.TestCase):
    """PickupApi unit test stubs"""

    def setUp(self):
        self.api = pbshipping.api.pickup_api.PickupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_pickup(self):
        """Test case for cancel_pickup

        Cancel Pickup  # noqa: E501
        """
        pass

    def test_get_pickupschedule(self):
        """Test case for get_pickupschedule

        Address validation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
