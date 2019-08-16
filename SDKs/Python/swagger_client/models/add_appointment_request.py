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


class AddAppointmentRequest(object):
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
        'apply_payment': 'bool',
        'client_id': 'str',
        'duration': 'int',
        'execute': 'str',
        'end_date_time': 'datetime',
        'gender_preference': 'str',
        'location_id': 'int',
        'notes': 'str',
        'provider_id': 'str',
        'resource_ids': 'list[int]',
        'send_email': 'bool',
        'session_type_id': 'int',
        'staff_id': 'int',
        'staff_requested': 'bool',
        'start_date_time': 'datetime',
        'test': 'bool'
    }

    attribute_map = {
        'apply_payment': 'ApplyPayment',
        'client_id': 'ClientId',
        'duration': 'Duration',
        'execute': 'Execute',
        'end_date_time': 'EndDateTime',
        'gender_preference': 'GenderPreference',
        'location_id': 'LocationId',
        'notes': 'Notes',
        'provider_id': 'ProviderId',
        'resource_ids': 'ResourceIds',
        'send_email': 'SendEmail',
        'session_type_id': 'SessionTypeId',
        'staff_id': 'StaffId',
        'staff_requested': 'StaffRequested',
        'start_date_time': 'StartDateTime',
        'test': 'Test'
    }

    def __init__(self, apply_payment=None, client_id=None, duration=None, execute=None, end_date_time=None, gender_preference=None, location_id=None, notes=None, provider_id=None, resource_ids=None, send_email=None, session_type_id=None, staff_id=None, staff_requested=None, start_date_time=None, test=None):  # noqa: E501
        """AddAppointmentRequest - a model defined in Swagger"""  # noqa: E501

        self._apply_payment = None
        self._client_id = None
        self._duration = None
        self._execute = None
        self._end_date_time = None
        self._gender_preference = None
        self._location_id = None
        self._notes = None
        self._provider_id = None
        self._resource_ids = None
        self._send_email = None
        self._session_type_id = None
        self._staff_id = None
        self._staff_requested = None
        self._start_date_time = None
        self._test = None
        self.discriminator = None

        if apply_payment is not None:
            self.apply_payment = apply_payment
        self.client_id = client_id
        if duration is not None:
            self.duration = duration
        if execute is not None:
            self.execute = execute
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if gender_preference is not None:
            self.gender_preference = gender_preference
        self.location_id = location_id
        if notes is not None:
            self.notes = notes
        if provider_id is not None:
            self.provider_id = provider_id
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if send_email is not None:
            self.send_email = send_email
        self.session_type_id = session_type_id
        self.staff_id = staff_id
        if staff_requested is not None:
            self.staff_requested = staff_requested
        self.start_date_time = start_date_time
        if test is not None:
            self.test = test

    @property
    def apply_payment(self):
        """Gets the apply_payment of this AddAppointmentRequest.  # noqa: E501

        When `true`, indicates that a payment should be applied to the appointment.   <br />Default: **true**  # noqa: E501

        :return: The apply_payment of this AddAppointmentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._apply_payment

    @apply_payment.setter
    def apply_payment(self, apply_payment):
        """Sets the apply_payment of this AddAppointmentRequest.

        When `true`, indicates that a payment should be applied to the appointment.   <br />Default: **true**  # noqa: E501

        :param apply_payment: The apply_payment of this AddAppointmentRequest.  # noqa: E501
        :type: bool
        """

        self._apply_payment = apply_payment

    @property
    def client_id(self):
        """Gets the client_id of this AddAppointmentRequest.  # noqa: E501

        The RRSID of the client for whom the new appointment is being made.  # noqa: E501

        :return: The client_id of this AddAppointmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AddAppointmentRequest.

        The RRSID of the client for whom the new appointment is being made.  # noqa: E501

        :param client_id: The client_id of this AddAppointmentRequest.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def duration(self):
        """Gets the duration of this AddAppointmentRequest.  # noqa: E501

        The duration of the appointment. This parameter is used to change the default duration of an appointment.  # noqa: E501

        :return: The duration of this AddAppointmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AddAppointmentRequest.

        The duration of the appointment. This parameter is used to change the default duration of an appointment.  # noqa: E501

        :param duration: The duration of this AddAppointmentRequest.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def execute(self):
        """Gets the execute of this AddAppointmentRequest.  # noqa: E501

        The action taken to add this appointment.  # noqa: E501

        :return: The execute of this AddAppointmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._execute

    @execute.setter
    def execute(self, execute):
        """Sets the execute of this AddAppointmentRequest.

        The action taken to add this appointment.  # noqa: E501

        :param execute: The execute of this AddAppointmentRequest.  # noqa: E501
        :type: str
        """

        self._execute = execute

    @property
    def end_date_time(self):
        """Gets the end_date_time of this AddAppointmentRequest.  # noqa: E501

        The end date and time of the new appointment. <br />  Default: **StartDateTime**, offset by the staff member’s default appointment duration.  # noqa: E501

        :return: The end_date_time of this AddAppointmentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this AddAppointmentRequest.

        The end date and time of the new appointment. <br />  Default: **StartDateTime**, offset by the staff member’s default appointment duration.  # noqa: E501

        :param end_date_time: The end_date_time of this AddAppointmentRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def gender_preference(self):
        """Gets the gender_preference of this AddAppointmentRequest.  # noqa: E501

        The client’s service provider gender preference.  # noqa: E501

        :return: The gender_preference of this AddAppointmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._gender_preference

    @gender_preference.setter
    def gender_preference(self, gender_preference):
        """Sets the gender_preference of this AddAppointmentRequest.

        The client’s service provider gender preference.  # noqa: E501

        :param gender_preference: The gender_preference of this AddAppointmentRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Female", "Male"]  # noqa: E501
        if gender_preference not in allowed_values:
            raise ValueError(
                "Invalid value for `gender_preference` ({0}), must be one of {1}"  # noqa: E501
                .format(gender_preference, allowed_values)
            )

        self._gender_preference = gender_preference

    @property
    def location_id(self):
        """Gets the location_id of this AddAppointmentRequest.  # noqa: E501

        The ID of the location where the new appointment is to take place.  # noqa: E501

        :return: The location_id of this AddAppointmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this AddAppointmentRequest.

        The ID of the location where the new appointment is to take place.  # noqa: E501

        :param location_id: The location_id of this AddAppointmentRequest.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def notes(self):
        """Gets the notes of this AddAppointmentRequest.  # noqa: E501

        Any general notes about this appointment.  # noqa: E501

        :return: The notes of this AddAppointmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AddAppointmentRequest.

        Any general notes about this appointment.  # noqa: E501

        :param notes: The notes of this AddAppointmentRequest.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def provider_id(self):
        """Gets the provider_id of this AddAppointmentRequest.  # noqa: E501

        If a user has Complementary and Alternative Medicine features enabled, this parameter assigns a provider ID to the appointment.  # noqa: E501

        :return: The provider_id of this AddAppointmentRequest.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this AddAppointmentRequest.

        If a user has Complementary and Alternative Medicine features enabled, this parameter assigns a provider ID to the appointment.  # noqa: E501

        :param provider_id: The provider_id of this AddAppointmentRequest.  # noqa: E501
        :type: str
        """

        self._provider_id = provider_id

    @property
    def resource_ids(self):
        """Gets the resource_ids of this AddAppointmentRequest.  # noqa: E501

        A list of resource IDs to associate with the new appointment.  # noqa: E501

        :return: The resource_ids of this AddAppointmentRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this AddAppointmentRequest.

        A list of resource IDs to associate with the new appointment.  # noqa: E501

        :param resource_ids: The resource_ids of this AddAppointmentRequest.  # noqa: E501
        :type: list[int]
        """

        self._resource_ids = resource_ids

    @property
    def send_email(self):
        """Gets the send_email of this AddAppointmentRequest.  # noqa: E501

         Whether to send client an email for cancellations. An email is sent only if the client has an email address and automatic emails have been set up.   <br />Default: **false**  # noqa: E501

        :return: The send_email of this AddAppointmentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        """Sets the send_email of this AddAppointmentRequest.

         Whether to send client an email for cancellations. An email is sent only if the client has an email address and automatic emails have been set up.   <br />Default: **false**  # noqa: E501

        :param send_email: The send_email of this AddAppointmentRequest.  # noqa: E501
        :type: bool
        """

        self._send_email = send_email

    @property
    def session_type_id(self):
        """Gets the session_type_id of this AddAppointmentRequest.  # noqa: E501

        The session type associated with the new appointment.  # noqa: E501

        :return: The session_type_id of this AddAppointmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._session_type_id

    @session_type_id.setter
    def session_type_id(self, session_type_id):
        """Sets the session_type_id of this AddAppointmentRequest.

        The session type associated with the new appointment.  # noqa: E501

        :param session_type_id: The session_type_id of this AddAppointmentRequest.  # noqa: E501
        :type: int
        """
        if session_type_id is None:
            raise ValueError("Invalid value for `session_type_id`, must not be `None`")  # noqa: E501

        self._session_type_id = session_type_id

    @property
    def staff_id(self):
        """Gets the staff_id of this AddAppointmentRequest.  # noqa: E501

        The ID of the staff member who is adding the new appointment.  # noqa: E501

        :return: The staff_id of this AddAppointmentRequest.  # noqa: E501
        :rtype: int
        """
        return self._staff_id

    @staff_id.setter
    def staff_id(self, staff_id):
        """Sets the staff_id of this AddAppointmentRequest.

        The ID of the staff member who is adding the new appointment.  # noqa: E501

        :param staff_id: The staff_id of this AddAppointmentRequest.  # noqa: E501
        :type: int
        """
        if staff_id is None:
            raise ValueError("Invalid value for `staff_id`, must not be `None`")  # noqa: E501

        self._staff_id = staff_id

    @property
    def staff_requested(self):
        """Gets the staff_requested of this AddAppointmentRequest.  # noqa: E501

        When `true`, indicates that the staff member was requested specifically by the client.  # noqa: E501

        :return: The staff_requested of this AddAppointmentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._staff_requested

    @staff_requested.setter
    def staff_requested(self, staff_requested):
        """Sets the staff_requested of this AddAppointmentRequest.

        When `true`, indicates that the staff member was requested specifically by the client.  # noqa: E501

        :param staff_requested: The staff_requested of this AddAppointmentRequest.  # noqa: E501
        :type: bool
        """

        self._staff_requested = staff_requested

    @property
    def start_date_time(self):
        """Gets the start_date_time of this AddAppointmentRequest.  # noqa: E501

        The start date and time of the new appointment.  # noqa: E501

        :return: The start_date_time of this AddAppointmentRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this AddAppointmentRequest.

        The start date and time of the new appointment.  # noqa: E501

        :param start_date_time: The start_date_time of this AddAppointmentRequest.  # noqa: E501
        :type: datetime
        """
        if start_date_time is None:
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")  # noqa: E501

        self._start_date_time = start_date_time

    @property
    def test(self):
        """Gets the test of this AddAppointmentRequest.  # noqa: E501

         When true, indicates that the method is to be validated, but no new appointment data is added.   <br />Default: **false**  # noqa: E501

        :return: The test of this AddAppointmentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this AddAppointmentRequest.

         When true, indicates that the method is to be validated, but no new appointment data is added.   <br />Default: **false**  # noqa: E501

        :param test: The test of this AddAppointmentRequest.  # noqa: E501
        :type: bool
        """

        self._test = test

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
        if issubclass(AddAppointmentRequest, dict):
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
        if not isinstance(other, AddAppointmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
