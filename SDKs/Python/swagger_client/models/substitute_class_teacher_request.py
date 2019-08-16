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


class SubstituteClassTeacherRequest(object):
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
        'class_id': 'int',
        'staff_id': 'int',
        'override_conflicts': 'bool',
        'send_client_email': 'bool',
        'send_original_teacher_email': 'bool',
        'send_substitute_teacher_email': 'bool'
    }

    attribute_map = {
        'class_id': 'ClassId',
        'staff_id': 'StaffId',
        'override_conflicts': 'OverrideConflicts',
        'send_client_email': 'SendClientEmail',
        'send_original_teacher_email': 'SendOriginalTeacherEmail',
        'send_substitute_teacher_email': 'SendSubstituteTeacherEmail'
    }

    def __init__(self, class_id=None, staff_id=None, override_conflicts=None, send_client_email=None, send_original_teacher_email=None, send_substitute_teacher_email=None):  # noqa: E501
        """SubstituteClassTeacherRequest - a model defined in Swagger"""  # noqa: E501

        self._class_id = None
        self._staff_id = None
        self._override_conflicts = None
        self._send_client_email = None
        self._send_original_teacher_email = None
        self._send_substitute_teacher_email = None
        self.discriminator = None

        self.class_id = class_id
        self.staff_id = staff_id
        if override_conflicts is not None:
            self.override_conflicts = override_conflicts
        if send_client_email is not None:
            self.send_client_email = send_client_email
        if send_original_teacher_email is not None:
            self.send_original_teacher_email = send_original_teacher_email
        if send_substitute_teacher_email is not None:
            self.send_substitute_teacher_email = send_substitute_teacher_email

    @property
    def class_id(self):
        """Gets the class_id of this SubstituteClassTeacherRequest.  # noqa: E501

        The ID of the class to which a substitute teacher needs to be assigned.  # noqa: E501

        :return: The class_id of this SubstituteClassTeacherRequest.  # noqa: E501
        :rtype: int
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """Sets the class_id of this SubstituteClassTeacherRequest.

        The ID of the class to which a substitute teacher needs to be assigned.  # noqa: E501

        :param class_id: The class_id of this SubstituteClassTeacherRequest.  # noqa: E501
        :type: int
        """
        if class_id is None:
            raise ValueError("Invalid value for `class_id`, must not be `None`")  # noqa: E501

        self._class_id = class_id

    @property
    def staff_id(self):
        """Gets the staff_id of this SubstituteClassTeacherRequest.  # noqa: E501

        The staff ID of the teacher to substitute.  # noqa: E501

        :return: The staff_id of this SubstituteClassTeacherRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this SubstituteClassTeacherRequest.

        The staff ID of the teacher to substitute.  # noqa: E501

        :param staff_id: The staff_id of this SubstituteClassTeacherRequest.  # noqa: E501
        :type: int
        """
        if staff_id is None:
            raise ValueError("Invalid value for `staff_id`, must not be `None`")  # noqa: E501

        self._staff_id = staff_id

    @property
    def override_conflicts(self):
        """Gets the override_conflicts of this SubstituteClassTeacherRequest.  # noqa: E501

        When `true`, overrides any conflicts in the schedule.  # noqa: E501

        :return: The override_conflicts of this SubstituteClassTeacherRequest.  # noqa: E501
        :rtype: bool
        """
        return self._override_conflicts

    @override_conflicts.setter
    def override_conflicts(self, override_conflicts):
        """Sets the override_conflicts of this SubstituteClassTeacherRequest.

        When `true`, overrides any conflicts in the schedule.  # noqa: E501

        :param override_conflicts: The override_conflicts of this SubstituteClassTeacherRequest.  # noqa: E501
        :type: bool
        """

        self._override_conflicts = override_conflicts

    @property
    def send_client_email(self):
        """Gets the send_client_email of this SubstituteClassTeacherRequest.  # noqa: E501

        When `true`, sends the client an automatic email about the substitution, if the client has opted to receive email.  # noqa: E501

        :return: The send_client_email of this SubstituteClassTeacherRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_client_email

    @send_client_email.setter
    def send_client_email(self, send_client_email):
        """Sets the send_client_email of this SubstituteClassTeacherRequest.

        When `true`, sends the client an automatic email about the substitution, if the client has opted to receive email.  # noqa: E501

        :param send_client_email: The send_client_email of this SubstituteClassTeacherRequest.  # noqa: E501
        :type: bool
        """

        self._send_client_email = send_client_email

    @property
    def send_original_teacher_email(self):
        """Gets the send_original_teacher_email of this SubstituteClassTeacherRequest.  # noqa: E501

        When `true`, sends the originally scheduled teacher an automatic email about the substitution.  # noqa: E501

        :return: The send_original_teacher_email of this SubstituteClassTeacherRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_original_teacher_email

    @send_original_teacher_email.setter
    def send_original_teacher_email(self, send_original_teacher_email):
        """Sets the send_original_teacher_email of this SubstituteClassTeacherRequest.

        When `true`, sends the originally scheduled teacher an automatic email about the substitution.  # noqa: E501

        :param send_original_teacher_email: The send_original_teacher_email of this SubstituteClassTeacherRequest.  # noqa: E501
        :type: bool
        """

        self._send_original_teacher_email = send_original_teacher_email

    @property
    def send_substitute_teacher_email(self):
        """Gets the send_substitute_teacher_email of this SubstituteClassTeacherRequest.  # noqa: E501

        When `true`, sends the substituted teacher an automatic email about the substitution.  # noqa: E501

        :return: The send_substitute_teacher_email of this SubstituteClassTeacherRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_substitute_teacher_email

    @send_substitute_teacher_email.setter
    def send_substitute_teacher_email(self, send_substitute_teacher_email):
        """Sets the send_substitute_teacher_email of this SubstituteClassTeacherRequest.

        When `true`, sends the substituted teacher an automatic email about the substitution.  # noqa: E501

        :param send_substitute_teacher_email: The send_substitute_teacher_email of this SubstituteClassTeacherRequest.  # noqa: E501
        :type: bool
        """

        self._send_substitute_teacher_email = send_substitute_teacher_email

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
        if issubclass(SubstituteClassTeacherRequest, dict):
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
        if not isinstance(other, SubstituteClassTeacherRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
