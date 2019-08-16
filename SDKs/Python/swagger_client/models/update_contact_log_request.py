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

from swagger_client.models.update_contact_log_comment import UpdateContactLogComment  # noqa: F401,E501
from swagger_client.models.update_contact_log_type import UpdateContactLogType  # noqa: F401,E501


class UpdateContactLogRequest(object):
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
        'test': 'bool',
        'assigned_to_staff_id': 'int',
        'text': 'str',
        'contact_name': 'str',
        'followup_by_date': 'datetime',
        'contact_method': 'str',
        'comments': 'list[UpdateContactLogComment]',
        'types': 'list[UpdateContactLogType]'
    }

    attribute_map = {
        'id': 'Id',
        'test': 'Test',
        'assigned_to_staff_id': 'AssignedToStaffId',
        'text': 'Text',
        'contact_name': 'ContactName',
        'followup_by_date': 'FollowupByDate',
        'contact_method': 'ContactMethod',
        'comments': 'Comments',
        'types': 'Types'
    }

    def __init__(self, id=None, test=None, assigned_to_staff_id=None, text=None, contact_name=None, followup_by_date=None, contact_method=None, comments=None, types=None):  # noqa: E501
        """UpdateContactLogRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._test = None
        self._assigned_to_staff_id = None
        self._text = None
        self._contact_name = None
        self._followup_by_date = None
        self._contact_method = None
        self._comments = None
        self._types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if test is not None:
            self.test = test
        if assigned_to_staff_id is not None:
            self.assigned_to_staff_id = assigned_to_staff_id
        if text is not None:
            self.text = text
        if contact_name is not None:
            self.contact_name = contact_name
        if followup_by_date is not None:
            self.followup_by_date = followup_by_date
        if contact_method is not None:
            self.contact_method = contact_method
        if comments is not None:
            self.comments = comments
        if types is not None:
            self.types = types

    @property
    def id(self):
        """Gets the id of this UpdateContactLogRequest.  # noqa: E501

        The ID of the contact log being updated.  # noqa: E501

        :return: The id of this UpdateContactLogRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateContactLogRequest.

        The ID of the contact log being updated.  # noqa: E501

        :param id: The id of this UpdateContactLogRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def test(self):
        """Gets the test of this UpdateContactLogRequest.  # noqa: E501

        When `true`, indicates that this is a test request and no data is inserted into the subscriber’s database.<br />  When `false`, the database is updated.  # noqa: E501

        :return: The test of this UpdateContactLogRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this UpdateContactLogRequest.

        When `true`, indicates that this is a test request and no data is inserted into the subscriber’s database.<br />  When `false`, the database is updated.  # noqa: E501

        :param test: The test of this UpdateContactLogRequest.  # noqa: E501
        :type: bool
        """

        self._test = test

    @property
    def assigned_to_staff_id(self):
        """Gets the assigned_to_staff_id of this UpdateContactLogRequest.  # noqa: E501

        The ID of the staff member to whom the contact log is now being assigned.  # noqa: E501

        :return: The assigned_to_staff_id of this UpdateContactLogRequest.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_staff_id

    @assigned_to_staff_id.setter
    def assigned_to_staff_id(self, assigned_to_staff_id):
        """Sets the assigned_to_staff_id of this UpdateContactLogRequest.

        The ID of the staff member to whom the contact log is now being assigned.  # noqa: E501

        :param assigned_to_staff_id: The assigned_to_staff_id of this UpdateContactLogRequest.  # noqa: E501
        :type: int
        """

        self._assigned_to_staff_id = assigned_to_staff_id

    @property
    def text(self):
        """Gets the text of this UpdateContactLogRequest.  # noqa: E501

        The contact log’s new text.  # noqa: E501

        :return: The text of this UpdateContactLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this UpdateContactLogRequest.

        The contact log’s new text.  # noqa: E501

        :param text: The text of this UpdateContactLogRequest.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def contact_name(self):
        """Gets the contact_name of this UpdateContactLogRequest.  # noqa: E501

        The name of the new person to be contacted by the assigned staff member.  # noqa: E501

        :return: The contact_name of this UpdateContactLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this UpdateContactLogRequest.

        The name of the new person to be contacted by the assigned staff member.  # noqa: E501

        :param contact_name: The contact_name of this UpdateContactLogRequest.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def followup_by_date(self):
        """Gets the followup_by_date of this UpdateContactLogRequest.  # noqa: E501

        The new date by which the assigned staff member should complete this contact log.  # noqa: E501

        :return: The followup_by_date of this UpdateContactLogRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._followup_by_date

    @followup_by_date.setter
    def followup_by_date(self, followup_by_date):
        """Sets the followup_by_date of this UpdateContactLogRequest.

        The new date by which the assigned staff member should complete this contact log.  # noqa: E501

        :param followup_by_date: The followup_by_date of this UpdateContactLogRequest.  # noqa: E501
        :type: datetime
        """

        self._followup_by_date = followup_by_date

    @property
    def contact_method(self):
        """Gets the contact_method of this UpdateContactLogRequest.  # noqa: E501

        The new method by which the client wants to be contacted.  # noqa: E501

        :return: The contact_method of this UpdateContactLogRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_method

    @contact_method.setter
    def contact_method(self, contact_method):
        """Sets the contact_method of this UpdateContactLogRequest.

        The new method by which the client wants to be contacted.  # noqa: E501

        :param contact_method: The contact_method of this UpdateContactLogRequest.  # noqa: E501
        :type: str
        """

        self._contact_method = contact_method

    @property
    def comments(self):
        """Gets the comments of this UpdateContactLogRequest.  # noqa: E501

        Contains information about the comments being updated or added to the contact log. Comments that have an ID of `0` are added to the contact log.  # noqa: E501

        :return: The comments of this UpdateContactLogRequest.  # noqa: E501
        :rtype: list[UpdateContactLogComment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this UpdateContactLogRequest.

        Contains information about the comments being updated or added to the contact log. Comments that have an ID of `0` are added to the contact log.  # noqa: E501

        :param comments: The comments of this UpdateContactLogRequest.  # noqa: E501
        :type: list[UpdateContactLogComment]
        """

        self._comments = comments

    @property
    def types(self):
        """Gets the types of this UpdateContactLogRequest.  # noqa: E501

        Contains information about the contact logs types being assigned to the contact log, in addition to the contact log types that are already assigned.  # noqa: E501

        :return: The types of this UpdateContactLogRequest.  # noqa: E501
        :rtype: list[UpdateContactLogType]
        """
        return self._types

    @types.setter
    def types(self, types):
        """Sets the types of this UpdateContactLogRequest.

        Contains information about the contact logs types being assigned to the contact log, in addition to the contact log types that are already assigned.  # noqa: E501

        :param types: The types of this UpdateContactLogRequest.  # noqa: E501
        :type: list[UpdateContactLogType]
        """

        self._types = types

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
        if issubclass(UpdateContactLogRequest, dict):
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
        if not isinstance(other, UpdateContactLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
