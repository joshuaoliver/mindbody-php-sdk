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

from swagger_client.models.location import Location  # noqa: F401,E501
from swagger_client.models.program import Program  # noqa: F401,E501


class ClientMembership(object):
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
        'restricted_locations': 'list[Location]',
        'icon_code': 'str',
        'active_date': 'datetime',
        'count': 'int',
        'current': 'bool',
        'expiration_date': 'datetime',
        'id': 'int',
        'name': 'str',
        'payment_date': 'datetime',
        'program': 'Program',
        'remaining': 'int',
        'site_id': 'int',
        'action': 'str'
    }

    attribute_map = {
        'restricted_locations': 'RestrictedLocations',
        'icon_code': 'IconCode',
        'active_date': 'ActiveDate',
        'count': 'Count',
        'current': 'Current',
        'expiration_date': 'ExpirationDate',
        'id': 'Id',
        'name': 'Name',
        'payment_date': 'PaymentDate',
        'program': 'Program',
        'remaining': 'Remaining',
        'site_id': 'SiteId',
        'action': 'Action'
    }

    def __init__(self, restricted_locations=None, icon_code=None, active_date=None, count=None, current=None, expiration_date=None, id=None, name=None, payment_date=None, program=None, remaining=None, site_id=None, action=None):  # noqa: E501
        """ClientMembership - a model defined in Swagger"""  # noqa: E501

        self._restricted_locations = None
        self._icon_code = None
        self._active_date = None
        self._count = None
        self._current = None
        self._expiration_date = None
        self._id = None
        self._name = None
        self._payment_date = None
        self._program = None
        self._remaining = None
        self._site_id = None
        self._action = None
        self.discriminator = None

        if restricted_locations is not None:
            self.restricted_locations = restricted_locations
        if icon_code is not None:
            self.icon_code = icon_code
        if active_date is not None:
            self.active_date = active_date
        if count is not None:
            self.count = count
        if current is not None:
            self.current = current
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if payment_date is not None:
            self.payment_date = payment_date
        if program is not None:
            self.program = program
        if remaining is not None:
            self.remaining = remaining
        if site_id is not None:
            self.site_id = site_id
        if action is not None:
            self.action = action

    @property
    def restricted_locations(self):
        """Gets the restricted_locations of this ClientMembership.  # noqa: E501

        The locations that the membership is restricted to, if any.  # noqa: E501

        :return: The restricted_locations of this ClientMembership.  # noqa: E501
        :rtype: list[Location]
        """
        return self._restricted_locations

    @restricted_locations.setter
    def restricted_locations(self, restricted_locations):
        """Sets the restricted_locations of this ClientMembership.

        The locations that the membership is restricted to, if any.  # noqa: E501

        :param restricted_locations: The restricted_locations of this ClientMembership.  # noqa: E501
        :type: list[Location]
        """

        self._restricted_locations = restricted_locations

    @property
    def icon_code(self):
        """Gets the icon_code of this ClientMembership.  # noqa: E501

        Text code that represents the `MembershipIcon`.  # noqa: E501

        :return: The icon_code of this ClientMembership.  # noqa: E501
        :rtype: str
        """
        return self._icon_code

    @icon_code.setter
    def icon_code(self, icon_code):
        """Sets the icon_code of this ClientMembership.

        Text code that represents the `MembershipIcon`.  # noqa: E501

        :param icon_code: The icon_code of this ClientMembership.  # noqa: E501
        :type: str
        """

        self._icon_code = icon_code

    @property
    def active_date(self):
        """Gets the active_date of this ClientMembership.  # noqa: E501

        The date that this pricing option became active and could be used to pay for services.  # noqa: E501

        :return: The active_date of this ClientMembership.  # noqa: E501
        :rtype: datetime
        """
        return self._active_date

    @active_date.setter
    def active_date(self, active_date):
        """Sets the active_date of this ClientMembership.

        The date that this pricing option became active and could be used to pay for services.  # noqa: E501

        :param active_date: The active_date of this ClientMembership.  # noqa: E501
        :type: datetime
        """

        self._active_date = active_date

    @property
    def count(self):
        """Gets the count of this ClientMembership.  # noqa: E501

        The number of service sessions this pricing option contained when first purchased.  # noqa: E501

        :return: The count of this ClientMembership.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ClientMembership.

        The number of service sessions this pricing option contained when first purchased.  # noqa: E501

        :param count: The count of this ClientMembership.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def current(self):
        """Gets the current of this ClientMembership.  # noqa: E501

        When `true`, there are service sessions remaining on the pricing option that can be used pay for the current session.<br />  When `false`, the client cannot use this pricing option to pay for other services.  # noqa: E501

        :return: The current of this ClientMembership.  # noqa: E501
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this ClientMembership.

        When `true`, there are service sessions remaining on the pricing option that can be used pay for the current session.<br />  When `false`, the client cannot use this pricing option to pay for other services.  # noqa: E501

        :param current: The current of this ClientMembership.  # noqa: E501
        :type: bool
        """

        self._current = current

    @property
    def expiration_date(self):
        """Gets the expiration_date of this ClientMembership.  # noqa: E501

        The date when the pricing option expires and can no longer be used to pay for services, even if unused service sessions remain on the option; expressed as UTC.  # noqa: E501

        :return: The expiration_date of this ClientMembership.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this ClientMembership.

        The date when the pricing option expires and can no longer be used to pay for services, even if unused service sessions remain on the option; expressed as UTC.  # noqa: E501

        :param expiration_date: The expiration_date of this ClientMembership.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def id(self):
        """Gets the id of this ClientMembership.  # noqa: E501

        The unique ID assigned to this pricing option.  # noqa: E501

        :return: The id of this ClientMembership.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientMembership.

        The unique ID assigned to this pricing option.  # noqa: E501

        :param id: The id of this ClientMembership.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ClientMembership.  # noqa: E501

        The name of this pricing option.  # noqa: E501

        :return: The name of this ClientMembership.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClientMembership.

        The name of this pricing option.  # noqa: E501

        :param name: The name of this ClientMembership.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def payment_date(self):
        """Gets the payment_date of this ClientMembership.  # noqa: E501

        The date on which the client paid for this pricing option.  # noqa: E501

        :return: The payment_date of this ClientMembership.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this ClientMembership.

        The date on which the client paid for this pricing option.  # noqa: E501

        :param payment_date: The payment_date of this ClientMembership.  # noqa: E501
        :type: datetime
        """

        self._payment_date = payment_date

    @property
    def program(self):
        """Gets the program of this ClientMembership.  # noqa: E501

        Contains information about the service category this service falls under.  # noqa: E501

        :return: The program of this ClientMembership.  # noqa: E501
        :rtype: Program
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this ClientMembership.

        Contains information about the service category this service falls under.  # noqa: E501

        :param program: The program of this ClientMembership.  # noqa: E501
        :type: Program
        """

        self._program = program

    @property
    def remaining(self):
        """Gets the remaining of this ClientMembership.  # noqa: E501

        The number of service sessions remaining in the pricing option that can still be used.  # noqa: E501

        :return: The remaining of this ClientMembership.  # noqa: E501
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this ClientMembership.

        The number of service sessions remaining in the pricing option that can still be used.  # noqa: E501

        :param remaining: The remaining of this ClientMembership.  # noqa: E501
        :type: int
        """

        self._remaining = remaining

    @property
    def site_id(self):
        """Gets the site_id of this ClientMembership.  # noqa: E501

        The ID of the subscriber site associated with this pricing option.  # noqa: E501

        :return: The site_id of this ClientMembership.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ClientMembership.

        The ID of the subscriber site associated with this pricing option.  # noqa: E501

        :param site_id: The site_id of this ClientMembership.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def action(self):
        """Gets the action of this ClientMembership.  # noqa: E501

        The action taken.  # noqa: E501

        :return: The action of this ClientMembership.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ClientMembership.

        The action taken.  # noqa: E501

        :param action: The action of this ClientMembership.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Added", "Updated", "Failed", "Removed"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

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
        if issubclass(ClientMembership, dict):
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
        if not isinstance(other, ClientMembership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
