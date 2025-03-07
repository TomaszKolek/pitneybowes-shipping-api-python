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


class Manifest(object):
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
        'carrier': 'str',
        'documents': 'list[Document]',
        'from_address': 'Address',
        'induction_postal_code': 'str',
        'manifest_id': 'str',
        'manifest_tracking_number': 'str',
        'parameters': 'list[Parameter]',
        'parcel_tracking_numbers': 'list[str]',
        'submission_date': 'str'
    }

    attribute_map = {
        'carrier': 'carrier',
        'documents': 'documents',
        'from_address': 'fromAddress',
        'induction_postal_code': 'inductionPostalCode',
        'manifest_id': 'manifestId',
        'manifest_tracking_number': 'manifestTrackingNumber',
        'parameters': 'parameters',
        'parcel_tracking_numbers': 'parcelTrackingNumbers',
        'submission_date': 'submissionDate'
    }

    def __init__(self, carrier=None, documents=None, from_address=None, induction_postal_code=None, manifest_id=None, manifest_tracking_number=None, parameters=None, parcel_tracking_numbers=None, submission_date=None, local_vars_configuration=None):  # noqa: E501
        """Manifest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._carrier = None
        self._documents = None
        self._from_address = None
        self._induction_postal_code = None
        self._manifest_id = None
        self._manifest_tracking_number = None
        self._parameters = None
        self._parcel_tracking_numbers = None
        self._submission_date = None
        self.discriminator = None

        self.carrier = carrier
        if documents is not None:
            self.documents = documents
        if from_address is not None:
            self.from_address = from_address
        if induction_postal_code is not None:
            self.induction_postal_code = induction_postal_code
        if manifest_id is not None:
            self.manifest_id = manifest_id
        if manifest_tracking_number is not None:
            self.manifest_tracking_number = manifest_tracking_number
        if parameters is not None:
            self.parameters = parameters
        if parcel_tracking_numbers is not None:
            self.parcel_tracking_numbers = parcel_tracking_numbers
        self.submission_date = submission_date

    @property
    def carrier(self):
        """Gets the carrier of this Manifest.  # noqa: E501


        :return: The carrier of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this Manifest.


        :param carrier: The carrier of this Manifest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and carrier is None:  # noqa: E501
            raise ValueError("Invalid value for `carrier`, must not be `None`")  # noqa: E501
        allowed_values = ["USPS", "NEWGISTICS", "PBPresort", "pbcs"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and carrier not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `carrier` ({0}), must be one of {1}"  # noqa: E501
                .format(carrier, allowed_values)
            )

        self._carrier = carrier

    @property
    def documents(self):
        """Gets the documents of this Manifest.  # noqa: E501


        :return: The documents of this Manifest.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this Manifest.


        :param documents: The documents of this Manifest.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def from_address(self):
        """Gets the from_address of this Manifest.  # noqa: E501


        :return: The from_address of this Manifest.  # noqa: E501
        :rtype: Address
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """Sets the from_address of this Manifest.


        :param from_address: The from_address of this Manifest.  # noqa: E501
        :type: Address
        """

        self._from_address = from_address

    @property
    def induction_postal_code(self):
        """Gets the induction_postal_code of this Manifest.  # noqa: E501


        :return: The induction_postal_code of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._induction_postal_code

    @induction_postal_code.setter
    def induction_postal_code(self, induction_postal_code):
        """Sets the induction_postal_code of this Manifest.


        :param induction_postal_code: The induction_postal_code of this Manifest.  # noqa: E501
        :type: str
        """

        self._induction_postal_code = induction_postal_code

    @property
    def manifest_id(self):
        """Gets the manifest_id of this Manifest.  # noqa: E501


        :return: The manifest_id of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._manifest_id

    @manifest_id.setter
    def manifest_id(self, manifest_id):
        """Sets the manifest_id of this Manifest.


        :param manifest_id: The manifest_id of this Manifest.  # noqa: E501
        :type: str
        """

        self._manifest_id = manifest_id

    @property
    def manifest_tracking_number(self):
        """Gets the manifest_tracking_number of this Manifest.  # noqa: E501


        :return: The manifest_tracking_number of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._manifest_tracking_number

    @manifest_tracking_number.setter
    def manifest_tracking_number(self, manifest_tracking_number):
        """Sets the manifest_tracking_number of this Manifest.


        :param manifest_tracking_number: The manifest_tracking_number of this Manifest.  # noqa: E501
        :type: str
        """

        self._manifest_tracking_number = manifest_tracking_number

    @property
    def parameters(self):
        """Gets the parameters of this Manifest.  # noqa: E501


        :return: The parameters of this Manifest.  # noqa: E501
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Manifest.


        :param parameters: The parameters of this Manifest.  # noqa: E501
        :type: list[Parameter]
        """

        self._parameters = parameters

    @property
    def parcel_tracking_numbers(self):
        """Gets the parcel_tracking_numbers of this Manifest.  # noqa: E501


        :return: The parcel_tracking_numbers of this Manifest.  # noqa: E501
        :rtype: list[str]
        """
        return self._parcel_tracking_numbers

    @parcel_tracking_numbers.setter
    def parcel_tracking_numbers(self, parcel_tracking_numbers):
        """Sets the parcel_tracking_numbers of this Manifest.


        :param parcel_tracking_numbers: The parcel_tracking_numbers of this Manifest.  # noqa: E501
        :type: list[str]
        """

        self._parcel_tracking_numbers = parcel_tracking_numbers

    @property
    def submission_date(self):
        """Gets the submission_date of this Manifest.  # noqa: E501


        :return: The submission_date of this Manifest.  # noqa: E501
        :rtype: str
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this Manifest.


        :param submission_date: The submission_date of this Manifest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and submission_date is None:  # noqa: E501
            raise ValueError("Invalid value for `submission_date`, must not be `None`")  # noqa: E501

        self._submission_date = submission_date

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
        if not isinstance(other, Manifest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Manifest):
            return True

        return self.to_dict() != other.to_dict()
