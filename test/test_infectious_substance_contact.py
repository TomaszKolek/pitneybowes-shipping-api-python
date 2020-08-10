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
from pbshipping.models.infectious_substance_contact import InfectiousSubstanceContact  # noqa: E501
from pbshipping.rest import ApiException

class TestInfectiousSubstanceContact(unittest.TestCase):
    """InfectiousSubstanceContact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InfectiousSubstanceContact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pbshipping.models.infectious_substance_contact.InfectiousSubstanceContact()  # noqa: E501
        if include_optional :
            return InfectiousSubstanceContact(
                company_name = '0', 
                contact_id = '0', 
                email_address = '0', 
                person_name = '0', 
                phone_number = '0'
            )
        else :
            return InfectiousSubstanceContact(
        )

    def testInfectiousSubstanceContact(self):
        """Test InfectiousSubstanceContact"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
