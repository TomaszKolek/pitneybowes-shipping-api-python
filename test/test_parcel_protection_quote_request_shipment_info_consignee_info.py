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
from pbshipping.models.parcel_protection_quote_request_shipment_info_consignee_info import ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo  # noqa: E501
from pbshipping.rest import ApiException

class TestParcelProtectionQuoteRequestShipmentInfoConsigneeInfo(unittest.TestCase):
    """ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.parcel_protection_quote_request_shipment_info_consignee_info.ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo()  # noqa: E501
        if include_optional :
            return ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo(
                address = pbshipping.models.parcel_protection_quote_request_shipment_info_shipper_info_address.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo_address(
                    address_lines = [
                        '0'
                        ], 
                    city_town = '0', 
                    state_province = '0', 
                    postal_code = '0', 
                    country_code = '0', )
            )
        else :
            return ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo(
                address = pbshipping.models.parcel_protection_quote_request_shipment_info_shipper_info_address.ParcelProtectionQuoteRequest_shipmentInfo_shipperInfo_address(
                    address_lines = [
                        '0'
                        ], 
                    city_town = '0', 
                    state_province = '0', 
                    postal_code = '0', 
                    country_code = '0', ),
        )

    def testParcelProtectionQuoteRequestShipmentInfoConsigneeInfo(self):
        """Test ParcelProtectionQuoteRequestShipmentInfoConsigneeInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
