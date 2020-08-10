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
from pbshipping.models.radio_activity_detail import RadioActivityDetail  # noqa: E501
from pbshipping.rest import ApiException

class TestRadioActivityDetail(unittest.TestCase):
    """RadioActivityDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RadioActivityDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.radio_activity_detail.RadioActivityDetail()  # noqa: E501
        if include_optional :
            return RadioActivityDetail(
                criticality_safety_index = 1.337, 
                radio_active_parcel_dimension = pbshipping.models.radio_active_parcel_dimension.RadioActiveParcelDimension(
                    uom = 'CM', 
                    height = 1.337, 
                    length = 1.337, 
                    width = 1.337, ), 
                surface_reading = 1.337, 
                transport_index = 1.337
            )
        else :
            return RadioActivityDetail(
        )

    def testRadioActivityDetail(self):
        """Test RadioActivityDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
