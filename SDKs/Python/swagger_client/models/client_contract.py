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

from swagger_client.models.upcoming_autopay_event import UpcomingAutopayEvent  # noqa: F401,E501


class ClientContract(object):
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
        'agreement_date': 'datetime',
        'autopay_status': 'str',
        'contract_name': 'str',
        'end_date': 'datetime',
        'id': 'int',
        'origination_location_id': 'int',
        'start_date': 'datetime',
        'site_id': 'int',
        'upcoming_autopay_events': 'list[UpcomingAutopayEvent]'
    }

    attribute_map = {
        'agreement_date': 'AgreementDate',
        'autopay_status': 'AutopayStatus',
        'contract_name': 'ContractName',
        'end_date': 'EndDate',
        'id': 'Id',
        'origination_location_id': 'OriginationLocationId',
        'start_date': 'StartDate',
        'site_id': 'SiteId',
        'upcoming_autopay_events': 'UpcomingAutopayEvents'
    }

    def __init__(self, agreement_date=None, autopay_status=None, contract_name=None, end_date=None, id=None, origination_location_id=None, start_date=None, site_id=None, upcoming_autopay_events=None):  # noqa: E501
        """ClientContract - a model defined in Swagger"""  # noqa: E501

        self._agreement_date = None
        self._autopay_status = None
        self._contract_name = None
        self._end_date = None
        self._id = None
        self._origination_location_id = None
        self._start_date = None
        self._site_id = None
        self._upcoming_autopay_events = None
        self.discriminator = None

        if agreement_date is not None:
            self.agreement_date = agreement_date
        if autopay_status is not None:
            self.autopay_status = autopay_status
        if contract_name is not None:
            self.contract_name = contract_name
        if end_date is not None:
            self.end_date = end_date
        if id is not None:
            self.id = id
        if origination_location_id is not None:
            self.origination_location_id = origination_location_id
        if start_date is not None:
            self.start_date = start_date
        if site_id is not None:
            self.site_id = site_id
        if upcoming_autopay_events is not None:
            self.upcoming_autopay_events = upcoming_autopay_events

    @property
    def agreement_date(self):
        """Gets the agreement_date of this ClientContract.  # noqa: E501

        The date on which the contract was signed.  # noqa: E501

        :return: The agreement_date of this ClientContract.  # noqa: E501
        :rtype: datetime
        """
        return self._agreement_date

    @agreement_date.setter
    def agreement_date(self, agreement_date):
        """Sets the agreement_date of this ClientContract.

        The date on which the contract was signed.  # noqa: E501

        :param agreement_date: The agreement_date of this ClientContract.  # noqa: E501
        :type: datetime
        """

        self._agreement_date = agreement_date

    @property
    def autopay_status(self):
        """Gets the autopay_status of this ClientContract.  # noqa: E501

        The status of the client’s autopay.  # noqa: E501

        :return: The autopay_status of this ClientContract.  # noqa: E501
        :rtype: str
        """
        return self._autopay_status

    @autopay_status.setter
    def autopay_status(self, autopay_status):
        """Sets the autopay_status of this ClientContract.

        The status of the client’s autopay.  # noqa: E501

        :param autopay_status: The autopay_status of this ClientContract.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Inactive", "Suspended"]  # noqa: E501
        if autopay_status not in allowed_values:
            raise ValueError(
                "Invalid value for `autopay_status` ({0}), must be one of {1}"  # noqa: E501
                .format(autopay_status, allowed_values)
            )

        self._autopay_status = autopay_status

    @property
    def contract_name(self):
        """Gets the contract_name of this ClientContract.  # noqa: E501

        The name of the contract.  # noqa: E501

        :return: The contract_name of this ClientContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_name

    @contract_name.setter
    def contract_name(self, contract_name):
        """Sets the contract_name of this ClientContract.

        The name of the contract.  # noqa: E501

        :param contract_name: The contract_name of this ClientContract.  # noqa: E501
        :type: str
        """

        self._contract_name = contract_name

    @property
    def end_date(self):
        """Gets the end_date of this ClientContract.  # noqa: E501

        The date that the contract expires.  # noqa: E501

        :return: The end_date of this ClientContract.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ClientContract.

        The date that the contract expires.  # noqa: E501

        :param end_date: The end_date of this ClientContract.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def id(self):
        """Gets the id of this ClientContract.  # noqa: E501

        The unique ID of the contract.  # noqa: E501

        :return: The id of this ClientContract.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientContract.

        The unique ID of the contract.  # noqa: E501

        :param id: The id of this ClientContract.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def origination_location_id(self):
        """Gets the origination_location_id of this ClientContract.  # noqa: E501

        The ID of the location where the contract was issued.  # noqa: E501

        :return: The origination_location_id of this ClientContract.  # noqa: E501
        :rtype: int
        """
        return self._origination_location_id

    @origination_location_id.setter
    def origination_location_id(self, origination_location_id):
        """Sets the origination_location_id of this ClientContract.

        The ID of the location where the contract was issued.  # noqa: E501

        :param origination_location_id: The origination_location_id of this ClientContract.  # noqa: E501
        :type: int
        """

        self._origination_location_id = origination_location_id

    @property
    def start_date(self):
        """Gets the start_date of this ClientContract.  # noqa: E501

        The date that the contract became active.  # noqa: E501

        :return: The start_date of this ClientContract.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ClientContract.

        The date that the contract became active.  # noqa: E501

        :param start_date: The start_date of this ClientContract.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def site_id(self):
        """Gets the site_id of this ClientContract.  # noqa: E501

        The ID of the site where the contract was issued.  # noqa: E501

        :return: The site_id of this ClientContract.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ClientContract.

        The ID of the site where the contract was issued.  # noqa: E501

        :param site_id: The site_id of this ClientContract.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def upcoming_autopay_events(self):
        """Gets the upcoming_autopay_events of this ClientContract.  # noqa: E501

        Contains details of the autopay events.  # noqa: E501

        :return: The upcoming_autopay_events of this ClientContract.  # noqa: E501
        :rtype: list[UpcomingAutopayEvent]
        """
        return self._upcoming_autopay_events

    @upcoming_autopay_events.setter
    def upcoming_autopay_events(self, upcoming_autopay_events):
        """Sets the upcoming_autopay_events of this ClientContract.

        Contains details of the autopay events.  # noqa: E501

        :param upcoming_autopay_events: The upcoming_autopay_events of this ClientContract.  # noqa: E501
        :type: list[UpcomingAutopayEvent]
        """

        self._upcoming_autopay_events = upcoming_autopay_events

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
        if issubclass(ClientContract, dict):
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
        if not isinstance(other, ClientContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
