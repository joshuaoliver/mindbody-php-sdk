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


class GetClassDescriptionsRequest(object):
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
        'class_description_id': 'int',
        'program_ids': 'list[int]',
        'start_class_date_time': 'datetime',
        'end_class_date_time': 'datetime',
        'staff_id': 'int',
        'location_id': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'class_description_id': 'ClassDescriptionId',
        'program_ids': 'ProgramIds',
        'start_class_date_time': 'StartClassDateTime',
        'end_class_date_time': 'EndClassDateTime',
        'staff_id': 'StaffId',
        'location_id': 'LocationId',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, class_description_id=None, program_ids=None, start_class_date_time=None, end_class_date_time=None, staff_id=None, location_id=None, limit=None, offset=None):  # noqa: E501
        """GetClassDescriptionsRequest - a model defined in Swagger"""  # noqa: E501

        self._class_description_id = None
        self._program_ids = None
        self._start_class_date_time = None
        self._end_class_date_time = None
        self._staff_id = None
        self._location_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if class_description_id is not None:
            self.class_description_id = class_description_id
        if program_ids is not None:
            self.program_ids = program_ids
        if start_class_date_time is not None:
            self.start_class_date_time = start_class_date_time
        if end_class_date_time is not None:
            self.end_class_date_time = end_class_date_time
        if staff_id is not None:
            self.staff_id = staff_id
        if location_id is not None:
            self.location_id = location_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def class_description_id(self):
        """Gets the class_description_id of this GetClassDescriptionsRequest.  # noqa: E501

        Filters to the single result with the given ID.  # noqa: E501

        :return: The class_description_id of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._class_description_id

    @class_description_id.setter
    def class_description_id(self, class_description_id):
        """Sets the class_description_id of this GetClassDescriptionsRequest.

        Filters to the single result with the given ID.  # noqa: E501

        :param class_description_id: The class_description_id of this GetClassDescriptionsRequest.  # noqa: E501
        :type: int
        """

        self._class_description_id = class_description_id

    @property
    def program_ids(self):
        """Gets the program_ids of this GetClassDescriptionsRequest.  # noqa: E501

        Filters results to class descriptions belonging to the given programs.  # noqa: E501

        :return: The program_ids of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._program_ids

    @program_ids.setter
    def program_ids(self, program_ids):
        """Sets the program_ids of this GetClassDescriptionsRequest.

        Filters results to class descriptions belonging to the given programs.  # noqa: E501

        :param program_ids: The program_ids of this GetClassDescriptionsRequest.  # noqa: E501
        :type: list[int]
        """

        self._program_ids = program_ids

    @property
    def start_class_date_time(self):
        """Gets the start_class_date_time of this GetClassDescriptionsRequest.  # noqa: E501

        Filters the results to class descriptions for scheduled classes that happen on or after the given date and time.  # noqa: E501

        :return: The start_class_date_time of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_class_date_time

    @start_class_date_time.setter
    def start_class_date_time(self, start_class_date_time):
        """Sets the start_class_date_time of this GetClassDescriptionsRequest.

        Filters the results to class descriptions for scheduled classes that happen on or after the given date and time.  # noqa: E501

        :param start_class_date_time: The start_class_date_time of this GetClassDescriptionsRequest.  # noqa: E501
        :type: datetime
        """

        self._start_class_date_time = start_class_date_time

    @property
    def end_class_date_time(self):
        """Gets the end_class_date_time of this GetClassDescriptionsRequest.  # noqa: E501

        Filters the results to class descriptions for scheduled classes that happen before the given date and time.  # noqa: E501

        :return: The end_class_date_time of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_class_date_time

    @end_class_date_time.setter
    def end_class_date_time(self, end_class_date_time):
        """Sets the end_class_date_time of this GetClassDescriptionsRequest.

        Filters the results to class descriptions for scheduled classes that happen before the given date and time.  # noqa: E501

        :param end_class_date_time: The end_class_date_time of this GetClassDescriptionsRequest.  # noqa: E501
        :type: datetime
        """

        self._end_class_date_time = end_class_date_time

    @property
    def staff_id(self):
        """Gets the staff_id of this GetClassDescriptionsRequest.  # noqa: E501

        Filters results to class descriptions for scheduled classes taught by the given staff member.  # noqa: E501

        :return: The staff_id of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this GetClassDescriptionsRequest.

        Filters results to class descriptions for scheduled classes taught by the given staff member.  # noqa: E501

        :param staff_id: The staff_id of this GetClassDescriptionsRequest.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def location_id(self):
        """Gets the location_id of this GetClassDescriptionsRequest.  # noqa: E501

        Filters results to classes descriptions for schedule classes as the given location.  # noqa: E501

        :return: The location_id of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetClassDescriptionsRequest.

        Filters results to classes descriptions for schedule classes as the given location.  # noqa: E501

        :param location_id: The location_id of this GetClassDescriptionsRequest.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def limit(self):
        """Gets the limit of this GetClassDescriptionsRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetClassDescriptionsRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetClassDescriptionsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetClassDescriptionsRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetClassDescriptionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetClassDescriptionsRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetClassDescriptionsRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

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
        if issubclass(GetClassDescriptionsRequest, dict):
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
        if not isinstance(other, GetClassDescriptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
