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


class CrossBorderQuotesResponse(object):
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
        'quote': 'list[CrossBorderQuotesResponseQuote]'
    }

    attribute_map = {
        'quote': 'quote'
    }

    def __init__(self, quote=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._quote = None
        self.discriminator = None

        if quote is not None:
            self.quote = quote

    @property
    def quote(self):
        """Gets the quote of this CrossBorderQuotesResponse.  # noqa: E501


        :return: The quote of this CrossBorderQuotesResponse.  # noqa: E501
        :rtype: list[CrossBorderQuotesResponseQuote]
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this CrossBorderQuotesResponse.


        :param quote: The quote of this CrossBorderQuotesResponse.  # noqa: E501
        :type: list[CrossBorderQuotesResponseQuote]
        """

        self._quote = quote

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
        if not isinstance(other, CrossBorderQuotesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesResponse):
            return True

        return self.to_dict() != other.to_dict()
