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
from pbshipping.api.container_api import ContainerApi  # noqa: E501
from pbshipping.rest import ApiException


class TestContainerApi(unittest.TestCase):
    """ContainerApi unit test stubs"""

    def setUp(self):
        self.api = pbshipping.api.container_api.ContainerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_containerized_parcels_labels(self):
        """Test case for get_containerized_parcels_labels

        Create Container Manifest Label  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
