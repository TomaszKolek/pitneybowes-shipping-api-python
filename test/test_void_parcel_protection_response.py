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
from pbshipping.models.void_parcel_protection_response import VoidParcelProtectionResponse  # noqa: E501
from pbshipping.rest import ApiException

class TestVoidParcelProtectionResponse(unittest.TestCase):
    """VoidParcelProtectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VoidParcelProtectionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.void_parcel_protection_response.VoidParcelProtectionResponse()  # noqa: E501
        if include_optional :
            return VoidParcelProtectionResponse(
                status = '0'
            )
        else :
            return VoidParcelProtectionResponse(
        )

    def testVoidParcelProtectionResponse(self):
        """Test VoidParcelProtectionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
