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


class CrossBorderQuotesResponseQuote(object):
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
        'quote_currency': 'str',
        'quote_lines': 'list[CrossBorderQuotesResponseQuoteLines]',
        'total_price': 'float',
        'total_rates': 'CrossBorderQuotesResponseTotalRates'
    }

    attribute_map = {
        'quote_currency': 'quoteCurrency',
        'quote_lines': 'quoteLines',
        'total_price': 'totalPrice',
        'total_rates': 'totalRates'
    }

    def __init__(self, quote_currency=None, quote_lines=None, total_price=None, total_rates=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesResponseQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._quote_currency = None
        self._quote_lines = None
        self._total_price = None
        self._total_rates = None
        self.discriminator = None

        if quote_currency is not None:
            self.quote_currency = quote_currency
        if quote_lines is not None:
            self.quote_lines = quote_lines
        if total_price is not None:
            self.total_price = total_price
        if total_rates is not None:
            self.total_rates = total_rates

    @property
    def quote_currency(self):
        """Gets the quote_currency of this CrossBorderQuotesResponseQuote.  # noqa: E501


        :return: The quote_currency of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :rtype: str
        """
        return self._quote_currency

    @quote_currency.setter
    def quote_currency(self, quote_currency):
        """Sets the quote_currency of this CrossBorderQuotesResponseQuote.


        :param quote_currency: The quote_currency of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :type: str
        """

        self._quote_currency = quote_currency

    @property
    def quote_lines(self):
        """Gets the quote_lines of this CrossBorderQuotesResponseQuote.  # noqa: E501


        :return: The quote_lines of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :rtype: list[CrossBorderQuotesResponseQuoteLines]
        """
        return self._quote_lines

    @quote_lines.setter
    def quote_lines(self, quote_lines):
        """Sets the quote_lines of this CrossBorderQuotesResponseQuote.


        :param quote_lines: The quote_lines of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :type: list[CrossBorderQuotesResponseQuoteLines]
        """

        self._quote_lines = quote_lines

    @property
    def total_price(self):
        """Gets the total_price of this CrossBorderQuotesResponseQuote.  # noqa: E501


        :return: The total_price of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price):
        """Sets the total_price of this CrossBorderQuotesResponseQuote.


        :param total_price: The total_price of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :type: float
        """

        self._total_price = total_price

    @property
    def total_rates(self):
        """Gets the total_rates of this CrossBorderQuotesResponseQuote.  # noqa: E501


        :return: The total_rates of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :rtype: CrossBorderQuotesResponseTotalRates
        """
        return self._total_rates

    @total_rates.setter
    def total_rates(self, total_rates):
        """Sets the total_rates of this CrossBorderQuotesResponseQuote.


        :param total_rates: The total_rates of this CrossBorderQuotesResponseQuote.  # noqa: E501
        :type: CrossBorderQuotesResponseTotalRates
        """

        self._total_rates = total_rates

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
        if not isinstance(other, CrossBorderQuotesResponseQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesResponseQuote):
            return True

        return self.to_dict() != other.to_dict()
