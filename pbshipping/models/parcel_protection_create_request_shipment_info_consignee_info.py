# coding: utf-8

"""
    Shipping API

    Shipping API Sample.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@pb.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pbshipping.configuration import Configuration


class ParcelProtectionCreateRequestShipmentInfoConsigneeInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address': 'Address',
        'company_name': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'middle_name': 'str',
        'email': 'str',
        'phone_numbers': 'list[object]'
    }

    attribute_map = {
        'address': 'address',
        'company_name': 'companyName',
        'family_name': 'familyName',
        'given_name': 'givenName',
        'middle_name': 'middleName',
        'email': 'email',
        'phone_numbers': 'phoneNumbers'
    }

    def __init__(self, address=None, company_name=None, family_name=None, given_name=None, middle_name=None, email=None, phone_numbers=None, local_vars_configuration=None):  # noqa: E501
        """ParcelProtectionCreateRequestShipmentInfoConsigneeInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._company_name = None
        self._family_name = None
        self._given_name = None
        self._middle_name = None
        self._email = None
        self._phone_numbers = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if company_name is not None:
            self.company_name = company_name
        if family_name is not None:
            self.family_name = family_name
        if given_name is not None:
            self.given_name = given_name
        if middle_name is not None:
            self.middle_name = middle_name
        if email is not None:
            self.email = email
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers

    @property
    def address(self):
        """Gets the address of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The address of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param address: The address of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: Address
        """

        self._address = address

    @property
    def company_name(self):
        """Gets the company_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The company_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param company_name: The company_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def family_name(self):
        """Gets the family_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The family_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param family_name: The family_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: str
        """

        self._family_name = family_name

    @property
    def given_name(self):
        """Gets the given_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The given_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param given_name: The given_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def middle_name(self):
        """Gets the middle_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The middle_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param middle_name: The middle_name of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def email(self):
        """Gets the email of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The email of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param email: The email of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501


        :return: The phone_numbers of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :rtype: list[object]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.


        :param phone_numbers: The phone_numbers of this ParcelProtectionCreateRequestShipmentInfoConsigneeInfo.  # noqa: E501
        :type: list[object]
        """

        self._phone_numbers = phone_numbers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParcelProtectionCreateRequestShipmentInfoConsigneeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParcelProtectionCreateRequestShipmentInfoConsigneeInfo):
            return True

        return self.to_dict() != other.to_dict()
