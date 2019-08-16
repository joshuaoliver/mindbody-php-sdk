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


class GetContractsRequest(object):
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
        'contract_ids': 'list[int]',
        'sold_online': 'bool',
        'location_id': 'int',
        'consumer_id': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'contract_ids': 'ContractIds',
        'sold_online': 'SoldOnline',
        'location_id': 'LocationId',
        'consumer_id': 'ConsumerId',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, contract_ids=None, sold_online=None, location_id=None, consumer_id=None, limit=None, offset=None):  # noqa: E501
        """GetContractsRequest - a model defined in Swagger"""  # noqa: E501

        self._contract_ids = None
        self._sold_online = None
        self._location_id = None
        self._consumer_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if contract_ids is not None:
            self.contract_ids = contract_ids
        if sold_online is not None:
            self.sold_online = sold_online
        self.location_id = location_id
        if consumer_id is not None:
            self.consumer_id = consumer_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def contract_ids(self):
        """Gets the contract_ids of this GetContractsRequest.  # noqa: E501

        When included, the response only contains details about the specified contract IDs.  # noqa: E501

        :return: The contract_ids of this GetContractsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._contract_ids

    @contract_ids.setter
    def contract_ids(self, contract_ids):
        """Sets the contract_ids of this GetContractsRequest.

        When included, the response only contains details about the specified contract IDs.  # noqa: E501

        :param contract_ids: The contract_ids of this GetContractsRequest.  # noqa: E501
        :type: list[int]
        """

        self._contract_ids = contract_ids

    @property
    def sold_online(self):
        """Gets the sold_online of this GetContractsRequest.  # noqa: E501

        When `true`, the response only contains details about contracts and AutoPay options that can be sold online.<br />  When `false`, only contracts that are not intended to be sold online are returned.<br />  Default: **all contracts**  # noqa: E501

        :return: The sold_online of this GetContractsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sold_online

    @sold_online.setter
    def sold_online(self, sold_online):
        """Sets the sold_online of this GetContractsRequest.

        When `true`, the response only contains details about contracts and AutoPay options that can be sold online.<br />  When `false`, only contracts that are not intended to be sold online are returned.<br />  Default: **all contracts**  # noqa: E501

        :param sold_online: The sold_online of this GetContractsRequest.  # noqa: E501
        :type: bool
        """

        self._sold_online = sold_online

    @property
    def location_id(self):
        """Gets the location_id of this GetContractsRequest.  # noqa: E501

        The ID of the location that has the requested contracts and AutoPay options.  # noqa: E501

        :return: The location_id of this GetContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this GetContractsRequest.

        The ID of the location that has the requested contracts and AutoPay options.  # noqa: E501

        :param location_id: The location_id of this GetContractsRequest.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def consumer_id(self):
        """Gets the consumer_id of this GetContractsRequest.  # noqa: E501

        The ID of the client.  # noqa: E501

        :return: The consumer_id of this GetContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        """Sets the consumer_id of this GetContractsRequest.

        The ID of the client.  # noqa: E501

        :param consumer_id: The consumer_id of this GetContractsRequest.  # noqa: E501
        :type: int
        """

        self._consumer_id = consumer_id

    @property
    def limit(self):
        """Gets the limit of this GetContractsRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetContractsRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetContractsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetContractsRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetContractsRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetContractsRequest.  # noqa: E501
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
        if issubclass(GetContractsRequest, dict):
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
        if not isinstance(other, GetContractsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
