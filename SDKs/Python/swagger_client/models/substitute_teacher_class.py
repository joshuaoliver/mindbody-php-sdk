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

from swagger_client.models.class_description import ClassDescription  # noqa: F401,E501
from swagger_client.models.location import Location  # noqa: F401,E501
from swagger_client.models.staff import Staff  # noqa: F401,E501


class SubstituteTeacherClass(object):
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
        'class_schedule_id': 'int',
        'location': 'Location',
        'max_capacity': 'int',
        'web_capacity': 'int',
        'total_booked': 'int',
        'total_booked_waitlist': 'int',
        'web_booked': 'int',
        'semester_id': 'int',
        'is_canceled': 'bool',
        'substitute': 'bool',
        'active': 'bool',
        'is_waitlist_available': 'bool',
        'hide_cancel': 'bool',
        'id': 'int',
        'is_available': 'bool',
        'start_date_time': 'datetime',
        'end_date_time': 'datetime',
        'last_modified_date_time': 'datetime',
        'class_description': 'ClassDescription',
        'staff': 'Staff'
    }

    attribute_map = {
        'class_schedule_id': 'ClassScheduleId',
        'location': 'Location',
        'max_capacity': 'MaxCapacity',
        'web_capacity': 'WebCapacity',
        'total_booked': 'TotalBooked',
        'total_booked_waitlist': 'TotalBookedWaitlist',
        'web_booked': 'WebBooked',
        'semester_id': 'SemesterId',
        'is_canceled': 'IsCanceled',
        'substitute': 'Substitute',
        'active': 'Active',
        'is_waitlist_available': 'IsWaitlistAvailable',
        'hide_cancel': 'HideCancel',
        'id': 'Id',
        'is_available': 'IsAvailable',
        'start_date_time': 'StartDateTime',
        'end_date_time': 'EndDateTime',
        'last_modified_date_time': 'LastModifiedDateTime',
        'class_description': 'ClassDescription',
        'staff': 'Staff'
    }

    def __init__(self, class_schedule_id=None, location=None, max_capacity=None, web_capacity=None, total_booked=None, total_booked_waitlist=None, web_booked=None, semester_id=None, is_canceled=None, substitute=None, active=None, is_waitlist_available=None, hide_cancel=None, id=None, is_available=None, start_date_time=None, end_date_time=None, last_modified_date_time=None, class_description=None, staff=None):  # noqa: E501
        """SubstituteTeacherClass - a model defined in Swagger"""  # noqa: E501

        self._class_schedule_id = None
        self._location = None
        self._max_capacity = None
        self._web_capacity = None
        self._total_booked = None
        self._total_booked_waitlist = None
        self._web_booked = None
        self._semester_id = None
        self._is_canceled = None
        self._substitute = None
        self._active = None
        self._is_waitlist_available = None
        self._hide_cancel = None
        self._id = None
        self._is_available = None
        self._start_date_time = None
        self._end_date_time = None
        self._last_modified_date_time = None
        self._class_description = None
        self._staff = None
        self.discriminator = None

        if class_schedule_id is not None:
            self.class_schedule_id = class_schedule_id
        if location is not None:
            self.location = location
        if max_capacity is not None:
            self.max_capacity = max_capacity
        if web_capacity is not None:
            self.web_capacity = web_capacity
        if total_booked is not None:
            self.total_booked = total_booked
        if total_booked_waitlist is not None:
            self.total_booked_waitlist = total_booked_waitlist
        if web_booked is not None:
            self.web_booked = web_booked
        if semester_id is not None:
            self.semester_id = semester_id
        if is_canceled is not None:
            self.is_canceled = is_canceled
        if substitute is not None:
            self.substitute = substitute
        if active is not None:
            self.active = active
        if is_waitlist_available is not None:
            self.is_waitlist_available = is_waitlist_available
        if hide_cancel is not None:
            self.hide_cancel = hide_cancel
        if id is not None:
            self.id = id
        if is_available is not None:
            self.is_available = is_available
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if last_modified_date_time is not None:
            self.last_modified_date_time = last_modified_date_time
        if class_description is not None:
            self.class_description = class_description
        if staff is not None:
            self.staff = staff

    @property
    def class_schedule_id(self):
        """Gets the class_schedule_id of this SubstituteTeacherClass.  # noqa: E501

        The class schedule ID of the requested class.  # noqa: E501

        :return: The class_schedule_id of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._class_schedule_id

    @class_schedule_id.setter
    def class_schedule_id(self, class_schedule_id):
        """Sets the class_schedule_id of this SubstituteTeacherClass.

        The class schedule ID of the requested class.  # noqa: E501

        :param class_schedule_id: The class_schedule_id of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._class_schedule_id = class_schedule_id

    @property
    def location(self):
        """Gets the location of this SubstituteTeacherClass.  # noqa: E501

        Contains information about the location where the class is taking place.  # noqa: E501

        :return: The location of this SubstituteTeacherClass.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SubstituteTeacherClass.

        Contains information about the location where the class is taking place.  # noqa: E501

        :param location: The location of this SubstituteTeacherClass.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def max_capacity(self):
        """Gets the max_capacity of this SubstituteTeacherClass.  # noqa: E501

        The total number of bookings allowed in the class.  # noqa: E501

        :return: The max_capacity of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """Sets the max_capacity of this SubstituteTeacherClass.

        The total number of bookings allowed in the class.  # noqa: E501

        :param max_capacity: The max_capacity of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._max_capacity = max_capacity

    @property
    def web_capacity(self):
        """Gets the web_capacity of this SubstituteTeacherClass.  # noqa: E501

        The total number of online bookings allowed in the class.  # noqa: E501

        :return: The web_capacity of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._web_capacity

    @web_capacity.setter
    def web_capacity(self, web_capacity):
        """Sets the web_capacity of this SubstituteTeacherClass.

        The total number of online bookings allowed in the class.  # noqa: E501

        :param web_capacity: The web_capacity of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._web_capacity = web_capacity

    @property
    def total_booked(self):
        """Gets the total_booked of this SubstituteTeacherClass.  # noqa: E501

        The total number of clients who are booked into the class prior to this call being made.  # noqa: E501

        :return: The total_booked of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._total_booked

    @total_booked.setter
    def total_booked(self, total_booked):
        """Sets the total_booked of this SubstituteTeacherClass.

        The total number of clients who are booked into the class prior to this call being made.  # noqa: E501

        :param total_booked: The total_booked of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._total_booked = total_booked

    @property
    def total_booked_waitlist(self):
        """Gets the total_booked_waitlist of this SubstituteTeacherClass.  # noqa: E501

        The total number of booked clients who are on the waiting list for the class prior to this call being made.  # noqa: E501

        :return: The total_booked_waitlist of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._total_booked_waitlist

    @total_booked_waitlist.setter
    def total_booked_waitlist(self, total_booked_waitlist):
        """Sets the total_booked_waitlist of this SubstituteTeacherClass.

        The total number of booked clients who are on the waiting list for the class prior to this call being made.  # noqa: E501

        :param total_booked_waitlist: The total_booked_waitlist of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._total_booked_waitlist = total_booked_waitlist

    @property
    def web_booked(self):
        """Gets the web_booked of this SubstituteTeacherClass.  # noqa: E501

        The total number of bookings in the class made by online users, prior to this call being made. This property is the current number of bookings counted toward the `WebCapacity` limit.  # noqa: E501

        :return: The web_booked of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._web_booked

    @web_booked.setter
    def web_booked(self, web_booked):
        """Sets the web_booked of this SubstituteTeacherClass.

        The total number of bookings in the class made by online users, prior to this call being made. This property is the current number of bookings counted toward the `WebCapacity` limit.  # noqa: E501

        :param web_booked: The web_booked of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._web_booked = web_booked

    @property
    def semester_id(self):
        """Gets the semester_id of this SubstituteTeacherClass.  # noqa: E501

        Identifies the semester assigned to this class.  # noqa: E501

        :return: The semester_id of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._semester_id

    @semester_id.setter
    def semester_id(self, semester_id):
        """Sets the semester_id of this SubstituteTeacherClass.

        Identifies the semester assigned to this class.  # noqa: E501

        :param semester_id: The semester_id of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._semester_id = semester_id

    @property
    def is_canceled(self):
        """Gets the is_canceled of this SubstituteTeacherClass.  # noqa: E501

        When `true`, indicates that the class has been canceled.<br />  When `false`, indicates that the class has not been canceled and may still be bookable.  # noqa: E501

        :return: The is_canceled of this SubstituteTeacherClass.  # noqa: E501
        :rtype: bool
        """
        return self._is_canceled

    @is_canceled.setter
    def is_canceled(self, is_canceled):
        """Sets the is_canceled of this SubstituteTeacherClass.

        When `true`, indicates that the class has been canceled.<br />  When `false`, indicates that the class has not been canceled and may still be bookable.  # noqa: E501

        :param is_canceled: The is_canceled of this SubstituteTeacherClass.  # noqa: E501
        :type: bool
        """

        self._is_canceled = is_canceled

    @property
    def substitute(self):
        """Gets the substitute of this SubstituteTeacherClass.  # noqa: E501

        When `true`, indicates that the class is being taught by a substitute teacher.  # noqa: E501

        :return: The substitute of this SubstituteTeacherClass.  # noqa: E501
        :rtype: bool
        """
        return self._substitute

    @substitute.setter
    def substitute(self, substitute):
        """Sets the substitute of this SubstituteTeacherClass.

        When `true`, indicates that the class is being taught by a substitute teacher.  # noqa: E501

        :param substitute: The substitute of this SubstituteTeacherClass.  # noqa: E501
        :type: bool
        """

        self._substitute = substitute

    @property
    def active(self):
        """Gets the active of this SubstituteTeacherClass.  # noqa: E501

        When `true`, indicates that the class is being shown to clients in consumer mode.  # noqa: E501

        :return: The active of this SubstituteTeacherClass.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SubstituteTeacherClass.

        When `true`, indicates that the class is being shown to clients in consumer mode.  # noqa: E501

        :param active: The active of this SubstituteTeacherClass.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def is_waitlist_available(self):
        """Gets the is_waitlist_available of this SubstituteTeacherClass.  # noqa: E501

        When `true`, indicates that the class has a waiting list and there is space available on the waiting list for another client.<br />  When `false`, indicates either that the class does not have a waiting list or there is no space available on the class waiting list.  # noqa: E501

        :return: The is_waitlist_available of this SubstituteTeacherClass.  # noqa: E501
        :rtype: bool
        """
        return self._is_waitlist_available

    @is_waitlist_available.setter
    def is_waitlist_available(self, is_waitlist_available):
        """Sets the is_waitlist_available of this SubstituteTeacherClass.

        When `true`, indicates that the class has a waiting list and there is space available on the waiting list for another client.<br />  When `false`, indicates either that the class does not have a waiting list or there is no space available on the class waiting list.  # noqa: E501

        :param is_waitlist_available: The is_waitlist_available of this SubstituteTeacherClass.  # noqa: E501
        :type: bool
        """

        self._is_waitlist_available = is_waitlist_available

    @property
    def hide_cancel(self):
        """Gets the hide_cancel of this SubstituteTeacherClass.  # noqa: E501

        When `true`, indicates that this class is should not be shown to clients when `IsCancelled` is `true`.<br />  When `false`, indicates that this class is should be shown to clients when `IsCancelled` is `true`.<br />  This property can be ignored when the `IsCancelled` property is `false`.  # noqa: E501

        :return: The hide_cancel of this SubstituteTeacherClass.  # noqa: E501
        :rtype: bool
        """
        return self._hide_cancel

    @hide_cancel.setter
    def hide_cancel(self, hide_cancel):
        """Sets the hide_cancel of this SubstituteTeacherClass.

        When `true`, indicates that this class is should not be shown to clients when `IsCancelled` is `true`.<br />  When `false`, indicates that this class is should be shown to clients when `IsCancelled` is `true`.<br />  This property can be ignored when the `IsCancelled` property is `false`.  # noqa: E501

        :param hide_cancel: The hide_cancel of this SubstituteTeacherClass.  # noqa: E501
        :type: bool
        """

        self._hide_cancel = hide_cancel

    @property
    def id(self):
        """Gets the id of this SubstituteTeacherClass.  # noqa: E501

        The unique identifier of the class.  # noqa: E501

        :return: The id of this SubstituteTeacherClass.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubstituteTeacherClass.

        The unique identifier of the class.  # noqa: E501

        :param id: The id of this SubstituteTeacherClass.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_available(self):
        """Gets the is_available of this SubstituteTeacherClass.  # noqa: E501

        When `true`, indicates that the class can be booked.<br />  When `false`, that the class cannot be booked at this time.  # noqa: E501

        :return: The is_available of this SubstituteTeacherClass.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this SubstituteTeacherClass.

        When `true`, indicates that the class can be booked.<br />  When `false`, that the class cannot be booked at this time.  # noqa: E501

        :param is_available: The is_available of this SubstituteTeacherClass.  # noqa: E501
        :type: bool
        """

        self._is_available = is_available

    @property
    def start_date_time(self):
        """Gets the start_date_time of this SubstituteTeacherClass.  # noqa: E501

        The date and time that this class is scheduled to start.  # noqa: E501

        :return: The start_date_time of this SubstituteTeacherClass.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this SubstituteTeacherClass.

        The date and time that this class is scheduled to start.  # noqa: E501

        :param start_date_time: The start_date_time of this SubstituteTeacherClass.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this SubstituteTeacherClass.  # noqa: E501

        The date and time when this class is scheduled to end.  # noqa: E501

        :return: The end_date_time of this SubstituteTeacherClass.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this SubstituteTeacherClass.

        The date and time when this class is scheduled to end.  # noqa: E501

        :param end_date_time: The end_date_time of this SubstituteTeacherClass.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this SubstituteTeacherClass.  # noqa: E501

        The last time the class was modified.  # noqa: E501

        :return: The last_modified_date_time of this SubstituteTeacherClass.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this SubstituteTeacherClass.

        The last time the class was modified.  # noqa: E501

        :param last_modified_date_time: The last_modified_date_time of this SubstituteTeacherClass.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date_time = last_modified_date_time

    @property
    def class_description(self):
        """Gets the class_description of this SubstituteTeacherClass.  # noqa: E501

        Contains information about this class.  # noqa: E501

        :return: The class_description of this SubstituteTeacherClass.  # noqa: E501
        :rtype: ClassDescription
        """
        return self._class_description

    @class_description.setter
    def class_description(self, class_description):
        """Sets the class_description of this SubstituteTeacherClass.

        Contains information about this class.  # noqa: E501

        :param class_description: The class_description of this SubstituteTeacherClass.  # noqa: E501
        :type: ClassDescription
        """

        self._class_description = class_description

    @property
    def staff(self):
        """Gets the staff of this SubstituteTeacherClass.  # noqa: E501

        Contains information about the teacher of the class.  # noqa: E501

        :return: The staff of this SubstituteTeacherClass.  # noqa: E501
        :rtype: Staff
        """
        return self._staff

    @staff.setter
    def staff(self, staff):
        """Sets the staff of this SubstituteTeacherClass.

        Contains information about the teacher of the class.  # noqa: E501

        :param staff: The staff of this SubstituteTeacherClass.  # noqa: E501
        :type: Staff
        """

        self._staff = staff

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
        if issubclass(SubstituteTeacherClass, dict):
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
        if not isinstance(other, SubstituteTeacherClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
