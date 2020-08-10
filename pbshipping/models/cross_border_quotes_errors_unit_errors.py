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


class CrossBorderQuotesErrorsUnitErrors(object):
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
        'error': 'int',
        'message': 'str'
    }

    attribute_map = {
        'error': 'error',
        'message': 'message'
    }

    def __init__(self, error=None, message=None, local_vars_configuration=None):  # noqa: E501
        """CrossBorderQuotesErrorsUnitErrors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error = None
        self._message = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if message is not None:
            self.message = message

    @property
    def error(self):
        """Gets the error of this CrossBorderQuotesErrorsUnitErrors.  # noqa: E501


        :return: The error of this CrossBorderQuotesErrorsUnitErrors.  # noqa: E501
        :rtype: int
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this CrossBorderQuotesErrorsUnitErrors.


        :param error: The error of this CrossBorderQuotesErrorsUnitErrors.  # noqa: E501
        :type: int
        """

        self._error = error

    @property
    def message(self):
        """Gets the message of this CrossBorderQuotesErrorsUnitErrors.  # noqa: E501


        :return: The message of this CrossBorderQuotesErrorsUnitErrors.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CrossBorderQuotesErrorsUnitErrors.


        :param message: The message of this CrossBorderQuotesErrorsUnitErrors.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if not isinstance(other, CrossBorderQuotesErrorsUnitErrors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CrossBorderQuotesErrorsUnitErrors):
            return True

        return self.to_dict() != other.to_dict()
