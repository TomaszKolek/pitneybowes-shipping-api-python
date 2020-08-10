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


class ContainerDetails(object):
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
        'commodity_info': 'list[CommodityInfo]',
        'container_type': 'str',
        'packaging_type': 'str'
    }

    attribute_map = {
        'commodity_info': 'commodityInfo',
        'container_type': 'containerType',
        'packaging_type': 'packagingType'
    }

    def __init__(self, commodity_info=None, container_type=None, packaging_type=None, local_vars_configuration=None):  # noqa: E501
        """ContainerDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._commodity_info = None
        self._container_type = None
        self._packaging_type = None
        self.discriminator = None

        if commodity_info is not None:
            self.commodity_info = commodity_info
        if container_type is not None:
            self.container_type = container_type
        if packaging_type is not None:
            self.packaging_type = packaging_type

    @property
    def commodity_info(self):
        """Gets the commodity_info of this ContainerDetails.  # noqa: E501


        :return: The commodity_info of this ContainerDetails.  # noqa: E501
        :rtype: list[CommodityInfo]
        """
        return self._commodity_info

    @commodity_info.setter
    def commodity_info(self, commodity_info):
        """Sets the commodity_info of this ContainerDetails.


        :param commodity_info: The commodity_info of this ContainerDetails.  # noqa: E501
        :type: list[CommodityInfo]
        """

        self._commodity_info = commodity_info

    @property
    def container_type(self):
        """Gets the container_type of this ContainerDetails.  # noqa: E501


        :return: The container_type of this ContainerDetails.  # noqa: E501
        :rtype: str
        """
        return self._container_type

    @container_type.setter
    def container_type(self, container_type):
        """Sets the container_type of this ContainerDetails.


        :param container_type: The container_type of this ContainerDetails.  # noqa: E501
        :type: str
        """

        self._container_type = container_type

    @property
    def packaging_type(self):
        """Gets the packaging_type of this ContainerDetails.  # noqa: E501


        :return: The packaging_type of this ContainerDetails.  # noqa: E501
        :rtype: str
        """
        return self._packaging_type

    @packaging_type.setter
    def packaging_type(self, packaging_type):
        """Sets the packaging_type of this ContainerDetails.


        :param packaging_type: The packaging_type of this ContainerDetails.  # noqa: E501
        :type: str
        """

        self._packaging_type = packaging_type

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
        if not isinstance(other, ContainerDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerDetails):
            return True

        return self.to_dict() != other.to_dict()
