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


class CrossBorderQuotesResponseLineRates(object):
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
        'line_price': 'float',
        'total_tax_amount': 'float',
        'total_duty_amount': 'int',
        'service_id': 'str',
        'base_charge': 'float',
        'delivery_commitment': 'CrossBorderQuotesResponseUnitRatesDeliveryCommitment',
        'total_carrier_charge': 'float'
    }

    attribute_map = {
        'line_price': 'linePrice',
        'total_tax_amount': 'totalTaxAmount',
        'total_duty_amount': 'totalDutyAmount',
        'service_id': 'serviceId',
        'base_charge': 'baseCharge',
        'delivery_commitment': 'deliveryCommitment',
        'total_carrier_charge': 'totalCarrierCharge'
    }

    def __init__(self, line_price=None, total_tax_amount=None, total_duty_amount=None, service_id=None, base_charge=None, delivery_commitment=None, total_carrier_charge=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesResponseLineRates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._line_price = None
        self._total_tax_amount = None
        self._total_duty_amount = None
        self._service_id = None
        self._base_charge = None
        self._delivery_commitment = None
        self._total_carrier_charge = None
        self.discriminator = None

        if line_price is not None:
            self.line_price = line_price
        if total_tax_amount is not None:
            self.total_tax_amount = total_tax_amount
        if total_duty_amount is not None:
            self.total_duty_amount = total_duty_amount
        if service_id is not None:
            self.service_id = service_id
        if base_charge is not None:
            self.base_charge = base_charge
        if delivery_commitment is not None:
            self.delivery_commitment = delivery_commitment
        if total_carrier_charge is not None:
            self.total_carrier_charge = total_carrier_charge

    @property
    def line_price(self):
        """Gets the line_price of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The line_price of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: float
        """
        return self._line_price

    @line_price.setter
    def line_price(self, line_price):
        """Sets the line_price of this CrossBorderQuotesResponseLineRates.


        :param line_price: The line_price of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: float
        """

        self._line_price = line_price

    @property
    def total_tax_amount(self):
        """Gets the total_tax_amount of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The total_tax_amount of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: float
        """
        return self._total_tax_amount

    @total_tax_amount.setter
    def total_tax_amount(self, total_tax_amount):
        """Sets the total_tax_amount of this CrossBorderQuotesResponseLineRates.


        :param total_tax_amount: The total_tax_amount of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: float
        """

        self._total_tax_amount = total_tax_amount

    @property
    def total_duty_amount(self):
        """Gets the total_duty_amount of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The total_duty_amount of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: int
        """
        return self._total_duty_amount

    @total_duty_amount.setter
    def total_duty_amount(self, total_duty_amount):
        """Sets the total_duty_amount of this CrossBorderQuotesResponseLineRates.


        :param total_duty_amount: The total_duty_amount of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: int
        """

        self._total_duty_amount = total_duty_amount

    @property
    def service_id(self):
        """Gets the service_id of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The service_id of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this CrossBorderQuotesResponseLineRates.


        :param service_id: The service_id of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def base_charge(self):
        """Gets the base_charge of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The base_charge of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: float
        """
        return self._base_charge

    @base_charge.setter
    def base_charge(self, base_charge):
        """Sets the base_charge of this CrossBorderQuotesResponseLineRates.


        :param base_charge: The base_charge of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: float
        """

        self._base_charge = base_charge

    @property
    def delivery_commitment(self):
        """Gets the delivery_commitment of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The delivery_commitment of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: CrossBorderQuotesResponseUnitRatesDeliveryCommitment
        """
        return self._delivery_commitment

    @delivery_commitment.setter
    def delivery_commitment(self, delivery_commitment):
        """Sets the delivery_commitment of this CrossBorderQuotesResponseLineRates.


        :param delivery_commitment: The delivery_commitment of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: CrossBorderQuotesResponseUnitRatesDeliveryCommitment
        """

        self._delivery_commitment = delivery_commitment

    @property
    def total_carrier_charge(self):
        """Gets the total_carrier_charge of this CrossBorderQuotesResponseLineRates.  # noqa: E501


        :return: The total_carrier_charge of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :rtype: float
        """
        return self._total_carrier_charge

    @total_carrier_charge.setter
    def total_carrier_charge(self, total_carrier_charge):
        """Sets the total_carrier_charge of this CrossBorderQuotesResponseLineRates.


        :param total_carrier_charge: The total_carrier_charge of this CrossBorderQuotesResponseLineRates.  # noqa: E501
        :type: float
        """

        self._total_carrier_charge = total_carrier_charge

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
        if not isinstance(other, CrossBorderQuotesResponseLineRates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesResponseLineRates):
            return True

        return self.to_dict() != other.to_dict()
