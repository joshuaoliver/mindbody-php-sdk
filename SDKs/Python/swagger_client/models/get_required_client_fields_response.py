# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetRequiredClientFieldsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'required_client_fields': 'list[str]'
    }

    attribute_map = {
        'required_client_fields': 'RequiredClientFields'
    }

    def __init__(self, required_client_fields=None):  # noqa: E501
        """GetRequiredClientFieldsResponse - a model defined in Swagger"""  # noqa: E501

        self._required_client_fields = None
        self.discriminator = None

        if required_client_fields is not None:
            self.required_client_fields = required_client_fields

    @property
    def required_client_fields(self):
        """Gets the required_client_fields of this GetRequiredClientFieldsResponse.  # noqa: E501

        A list of strings that maps to the client fields that are required by the site.  # noqa: E501

        :return: The required_client_fields of this GetRequiredClientFieldsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_client_fields

    @required_client_fields.setter
    def required_client_fields(self, required_client_fields):
        """Sets the required_client_fields of this GetRequiredClientFieldsResponse.

        A list of strings that maps to the client fields that are required by the site.  # noqa: E501

        :param required_client_fields: The required_client_fields of this GetRequiredClientFieldsResponse.  # noqa: E501
        :type: list[str]
        """

        self._required_client_fields = required_client_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GetRequiredClientFieldsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetRequiredClientFieldsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
