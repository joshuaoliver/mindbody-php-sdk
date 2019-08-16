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


class AddContactLogType(object):
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
        'id': 'int',
        'sub_types': 'list[int]'
    }

    attribute_map = {
        'id': 'Id',
        'sub_types': 'SubTypes'
    }

    def __init__(self, id=None, sub_types=None):  # noqa: E501
        """AddContactLogType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._sub_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sub_types is not None:
            self.sub_types = sub_types

    @property
    def id(self):
        """Gets the id of this AddContactLogType.  # noqa: E501

        The contact log type’s ID.  # noqa: E501

        :return: The id of this AddContactLogType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddContactLogType.

        The contact log type’s ID.  # noqa: E501

        :param id: The id of this AddContactLogType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def sub_types(self):
        """Gets the sub_types of this AddContactLogType.  # noqa: E501

        A list of the subtype IDs used to tag this contact log type.  # noqa: E501

        :return: The sub_types of this AddContactLogType.  # noqa: E501
        :rtype: list[int]
        """
        return self._sub_types

    @sub_types.setter
    def sub_types(self, sub_types):
        """Sets the sub_types of this AddContactLogType.

        A list of the subtype IDs used to tag this contact log type.  # noqa: E501

        :param sub_types: The sub_types of this AddContactLogType.  # noqa: E501
        :type: list[int]
        """

        self._sub_types = sub_types

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
        if issubclass(AddContactLogType, dict):
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
        if not isinstance(other, AddContactLogType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
