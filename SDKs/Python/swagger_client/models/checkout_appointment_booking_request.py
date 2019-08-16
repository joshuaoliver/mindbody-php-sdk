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

from swagger_client.models.resource import Resource  # noqa: F401,E501


class CheckoutAppointmentBookingRequest(object):
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
        'location_id': 'int',
        'session_type_id': 'int',
        'resources': 'list[Resource]',
        'start_date_time': 'datetime',
        'end_date_time': 'datetime',
        'provider_id': 'str'
    }

    attribute_map = {
        'staff_id': 'StaffId',
        'location_id': 'LocationId',
        'session_type_id': 'SessionTypeId',
        'resources': 'Resources',
        'start_date_time': 'StartDateTime',
        'end_date_time': 'EndDateTime',
        'provider_id': 'ProviderId'
    }

    def __init__(self, staff_id=None, location_id=None, session_type_id=None, resources=None, start_date_time=None, end_date_time=None, provider_id=None):  # noqa: E501
        """CheckoutAppointmentBookingRequest - a model defined in Swagger"""  # noqa: E501

        self._staff_id = None
        self._location_id = None
        self._session_type_id = None
        self._resources = None
        self._start_date_time = None
        self._end_date_time = None
        self._provider_id = None
        self.discriminator = None

        if staff_id is not None:
            self.staff_id = staff_id
        if location_id is not None:
            self.location_id = location_id
        if session_type_id is not None:
            self.session_type_id = session_type_id
        if resources is not None:
            self.resources = resources
        if start_date_time is not None:
            self.start_date_time = start_date_time
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if provider_id is not None:
            self.provider_id = provider_id

    @property
    def staff_id(self):
        """Gets the staff_id of this CheckoutAppointmentBookingRequest.  # noqa: E501

        The ID of the staff member who is to provide the service being booked.  # noqa: E501

        :return: The staff_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this CheckoutAppointmentBookingRequest.

        The ID of the staff member who is to provide the service being booked.  # noqa: E501

        :param staff_id: The staff_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: int
        """

        self._staff_id = staff_id

    @property
    def location_id(self):
        """Gets the location_id of this CheckoutAppointmentBookingRequest.  # noqa: E501

        The ID of the location where the appointment is to take place.  # noqa: E501

        :return: The location_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this CheckoutAppointmentBookingRequest.

        The ID of the location where the appointment is to take place.  # noqa: E501

        :param location_id: The location_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def session_type_id(self):
        """Gets the session_type_id of this CheckoutAppointmentBookingRequest.  # noqa: E501

        The ID of the session type of this appointment.  # noqa: E501

        :return: The session_type_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: int
        """
        return self._session_type_id

    @session_type_id.setter
    def session_type_id(self, session_type_id):
        """Sets the session_type_id of this CheckoutAppointmentBookingRequest.

        The ID of the session type of this appointment.  # noqa: E501

        :param session_type_id: The session_type_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: int
        """

        self._session_type_id = session_type_id

    @property
    def resources(self):
        """Gets the resources of this CheckoutAppointmentBookingRequest.  # noqa: E501

        Contains information about the resources to be used for the appointment.  # noqa: E501

        :return: The resources of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: list[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this CheckoutAppointmentBookingRequest.

        Contains information about the resources to be used for the appointment.  # noqa: E501

        :param resources: The resources of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: list[Resource]
        """

        self._resources = resources

    @property
    def start_date_time(self):
        """Gets the start_date_time of this CheckoutAppointmentBookingRequest.  # noqa: E501

        The date and time that the appointment is to start in the business’ timezone. This value must be passed in the format yyyy-mm-ddThh:mm:ss.  # noqa: E501

        :return: The start_date_time of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this CheckoutAppointmentBookingRequest.

        The date and time that the appointment is to start in the business’ timezone. This value must be passed in the format yyyy-mm-ddThh:mm:ss.  # noqa: E501

        :param start_date_time: The start_date_time of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this CheckoutAppointmentBookingRequest.  # noqa: E501

        The date and time that the appointment is to end in the business’ timezone. This value must be passed in the format yyyy-mm-ddThh:mm:ss.  # noqa: E501

        :return: The end_date_time of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this CheckoutAppointmentBookingRequest.

        The date and time that the appointment is to end in the business’ timezone. This value must be passed in the format yyyy-mm-ddThh:mm:ss.  # noqa: E501

        :param end_date_time: The end_date_time of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def provider_id(self):
        """Gets the provider_id of this CheckoutAppointmentBookingRequest.  # noqa: E501

        The National Provider Identifier (NPI) of the staff member who is to provide the service. For an explanation of Provider IDs, see [Provider IDs](https://support.mindbodyonline.com/s/article/204075743-Provider-IDs?language=en_US).  # noqa: E501

        :return: The provider_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this CheckoutAppointmentBookingRequest.

        The National Provider Identifier (NPI) of the staff member who is to provide the service. For an explanation of Provider IDs, see [Provider IDs](https://support.mindbodyonline.com/s/article/204075743-Provider-IDs?language=en_US).  # noqa: E501

        :param provider_id: The provider_id of this CheckoutAppointmentBookingRequest.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

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
        if issubclass(CheckoutAppointmentBookingRequest, dict):
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
        if not isinstance(other, CheckoutAppointmentBookingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
