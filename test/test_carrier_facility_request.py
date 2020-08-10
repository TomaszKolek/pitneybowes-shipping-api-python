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
from pbshipping.models.carrier_facility_request import CarrierFacilityRequest  # noqa: E501
from pbshipping.rest import ApiException

class TestCarrierFacilityRequest(unittest.TestCase):
    """CarrierFacilityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CarrierFacilityRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.carrier_facility_request.CarrierFacilityRequest()  # noqa: E501
        if include_optional :
            return CarrierFacilityRequest(
                address = pbshipping.models.carrier_facility_request_address.CarrierFacilityRequest_address(
                    address_lines = [
                        '0'
                        ], 
                    city_town = '0', 
                    state_province = '0', 
                    country_code = '0', ), 
                carrier = '0', 
                carrier_facility_options = [
                    pbshipping.models.carrier_facility_response_carrier_facility_options.CarrierFacilityResponse_carrierFacilityOptions(
                        name = '0', 
                        value = '0', )
                    ]
            )
        else :
            return CarrierFacilityRequest(
        )

    def testCarrierFacilityRequest(self):
        """Test CarrierFacilityRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
