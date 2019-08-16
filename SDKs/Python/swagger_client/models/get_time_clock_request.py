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


class GetTimeClockRequest(object):
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
        'staff_id': 'int',
        'start_date_time': 'datetime',
        'end_date_time': 'datetime',
        'include_inactive_staff': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'staff_id': 'StaffId',
        'start_date_time': 'StartDateTime',
        'end_date_time': 'EndDateTime',
        'include_inactive_staff': 'IncludeInactiveStaff',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, staff_id=None, start_date_time=None, end_date_time=None, include_inactive_staff=None, limit=None, offset=None):  # noqa: E501
        """GetTimeClockRequest - a model defined in Swagger"""  # noqa: E501

        self._staff_id = None
        self._start_date_time = None
        self._end_date_time = None
        self._include_inactive_staff = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if staff_id is not None:
            self.staff_id = staff_id
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if include_inactive_staff is not None:
            self.include_inactive_staff = include_inactive_staff
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def staff_id(self):
        """Gets the staff_id of this GetTimeClockRequest.  # noqa: E501

        The staff ID for whom you want to retrieve time card information. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID.  # noqa: E501

        :return: The staff_id of this GetTimeClockRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this GetTimeClockRequest.

        The staff ID for whom you want to retrieve time card information. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID.  # noqa: E501

        :param staff_id: The staff_id of this GetTimeClockRequest.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def start_date_time(self):
        """Gets the start_date_time of this GetTimeClockRequest.  # noqa: E501

        The beginning of the date range for the time card information to be returned. If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply. The maximum allowed date range is 14 days.  # noqa: E501

        :return: The start_date_time of this GetTimeClockRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this GetTimeClockRequest.

        The beginning of the date range for the time card information to be returned. If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply. The maximum allowed date range is 14 days.  # noqa: E501

        :param start_date_time: The start_date_time of this GetTimeClockRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this GetTimeClockRequest.  # noqa: E501

        The end of the date range for the time card information to be returned. If you do not supply an `EndDateTime`, data returns for the seven days prior to today’s date. Classes that begin before the `EndDateTime` are included in the response, regardless of the time that the class ends. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**  # noqa: E501

        :return: The end_date_time of this GetTimeClockRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this GetTimeClockRequest.

        The end of the date range for the time card information to be returned. If you do not supply an `EndDateTime`, data returns for the seven days prior to today’s date. Classes that begin before the `EndDateTime` are included in the response, regardless of the time that the class ends. The maximum allowed date range is 14 days.<br />  Default: **Today’s date**  # noqa: E501

        :param end_date_time: The end_date_time of this GetTimeClockRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def include_inactive_staff(self):
        """Gets the include_inactive_staff of this GetTimeClockRequest.  # noqa: E501

        When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false**  # noqa: E501

        :return: The include_inactive_staff of this GetTimeClockRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_inactive_staff

    @include_inactive_staff.setter
    def include_inactive_staff(self, include_inactive_staff):
        """Sets the include_inactive_staff of this GetTimeClockRequest.

        When `true`, payroll information returns for both active and inactive staff members.<br />  Default: **false**  # noqa: E501

        :param include_inactive_staff: The include_inactive_staff of this GetTimeClockRequest.  # noqa: E501
        :type: bool
        """

        self._include_inactive_staff = include_inactive_staff

    @property
    def limit(self):
        """Gets the limit of this GetTimeClockRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetTimeClockRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetTimeClockRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetTimeClockRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetTimeClockRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetTimeClockRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetTimeClockRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetTimeClockRequest.  # noqa: E501
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
        if issubclass(GetTimeClockRequest, dict):
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
        if not isinstance(other, GetTimeClockRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
