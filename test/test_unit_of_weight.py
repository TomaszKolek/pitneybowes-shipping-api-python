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
import datetime

import pbshipping
from pbshipping.models.unit_of_weight import UnitOfWeight  # noqa: E501
from pbshipping.rest import ApiException

class TestUnitOfWeight(unittest.TestCase):
    """UnitOfWeight unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UnitOfWeight
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.unit_of_weight.UnitOfWeight()  # noqa: E501
        if include_optional :
            return UnitOfWeight(
            )
        else :
            return UnitOfWeight(
        )

    def testUnitOfWeight(self):
        """Test UnitOfWeight"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
