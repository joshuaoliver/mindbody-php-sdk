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


class GetStaffPermissionsRequest(object):
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
        'staff_id': 'int'
    }

    attribute_map = {
        'staff_id': 'StaffId'
    }

    def __init__(self, staff_id=None):  # noqa: E501
        """GetStaffPermissionsRequest - a model defined in Swagger"""  # noqa: E501

        self._staff_id = None
        self.discriminator = None

        self.staff_id = staff_id

    @property
    def staff_id(self):
        """Gets the staff_id of this GetStaffPermissionsRequest.  # noqa: E501

        The ID of the staff member whose permissions you want to return.  # noqa: E501

        :return: The staff_id of this GetStaffPermissionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this GetStaffPermissionsRequest.

        The ID of the staff member whose permissions you want to return.  # noqa: E501

        :param staff_id: The staff_id of this GetStaffPermissionsRequest.  # noqa: E501
        :type: int
        """
        if staff_id is None:
            raise ValueError("Invalid value for `staff_id`, must not be `None`")  # noqa: E501

        self._staff_id = staff_id

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
        if issubclass(GetStaffPermissionsRequest, dict):
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
        if not isinstance(other, GetStaffPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
