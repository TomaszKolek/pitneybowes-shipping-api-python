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
from pbshipping.models.parcel_protection_policy_response_content import ParcelProtectionPolicyResponseContent  # noqa: E501
from pbshipping.rest import ApiException

class TestParcelProtectionPolicyResponseContent(unittest.TestCase):
    """ParcelProtectionPolicyResponseContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ParcelProtectionPolicyResponseContent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.parcel_protection_policy_response_content.ParcelProtectionPolicyResponseContent()  # noqa: E501
        if include_optional :
            return ParcelProtectionPolicyResponseContent(
                transaction_id = '0', 
                developer_id = '0', 
                subscription_acc_no = '0', 
                client_transaction_id = '0', 
                policy_details = pbshipping.models.parcel_protection_policy_response_policy_details.ParcelProtectionPolicyResponse_policyDetails(
                    policy_id = '0', 
                    policy_date = '0', 
                    policy_status = '0', 
                    claim_status = '0', 
                    claim_status_update_date = '0', 
                    value_of_goods = 1.337, 
                    insurance_value = 1.337, 
                    premium_value = 1.337, 
                    base_premium = 1.337, 
                    technology_fee = 1.337, 
                    currency_code = '0', 
                    mail_class = '0', 
                    mail_class_option = '0', ), 
                shipment_details = pbshipping.models.parcel_protection_policy_response_shipment_details.ParcelProtectionPolicyResponse_shipmentDetails(
                    shipment_date = '0', 
                    shipment_transaction_id = '0', 
                    shipment_id = '0', 
                    parcel_tracking_number = '0', 
                    carrier = '0', 
                    amount = '0', 
                    package_length = '0', 
                    package_width = '0', 
                    package_height = '0', 
                    weight = '0', 
                    zone = '0', ), 
                shipper_info = pbshipping.models.parcel_protection_policy_response_shipper_info.ParcelProtectionPolicyResponse_shipperInfo(
                    shipper_id = '0', 
                    first_name = '0', 
                    middle_name = '0', 
                    last_name = '0', 
                    company = '0', 
                    email = '0', 
                    phone_number1 = '0', 
                    phone_number2 = '0', 
                    fax_number = '0', 
                    address = pbshipping.models.parcel_protection_policy_response_shipper_info_address.ParcelProtectionPolicyResponse_shipperInfo_address(
                        street1 = '0', 
                        street2 = '0', 
                        street3 = '0', 
                        city = '0', 
                        region = '0', 
                        country = '0', 
                        postal_code = '0', ), ), 
                consignee_info = pbshipping.models.parcel_protection_policy_response_shipper_info.ParcelProtectionPolicyResponse_shipperInfo(
                    shipper_id = '0', 
                    first_name = '0', 
                    middle_name = '0', 
                    last_name = '0', 
                    company = '0', 
                    email = '0', 
                    phone_number1 = '0', 
                    phone_number2 = '0', 
                    fax_number = '0', 
                    address = pbshipping.models.parcel_protection_policy_response_shipper_info_address.ParcelProtectionPolicyResponse_shipperInfo_address(
                        street1 = '0', 
                        street2 = '0', 
                        street3 = '0', 
                        city = '0', 
                        region = '0', 
                        country = '0', 
                        postal_code = '0', ), ), 
                created_at = '0', 
                updated_at = '0'
            )
        else :
            return ParcelProtectionPolicyResponseContent(
        )

    def testParcelProtectionPolicyResponseContent(self):
        """Test ParcelProtectionPolicyResponseContent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
