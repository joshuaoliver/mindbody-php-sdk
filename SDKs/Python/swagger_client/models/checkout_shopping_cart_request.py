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

from swagger_client.models.checkout_item_wrapper import CheckoutItemWrapper  # noqa: F401,E501
from swagger_client.models.checkout_payment_info import CheckoutPaymentInfo  # noqa: F401,E501


class CheckoutShoppingCartRequest(object):
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
        'cart_id': 'str',
        'client_id': 'str',
        'test': 'bool',
        'items': 'list[CheckoutItemWrapper]',
        'in_store': 'bool',
        'promotion_code': 'str',
        'payments': 'list[CheckoutPaymentInfo]',
        'send_email': 'bool',
        'location_id': 'int',
        'image': 'str',
        'image_file_name': 'str'
    }

    attribute_map = {
        'cart_id': 'CartId',
        'client_id': 'ClientId',
        'test': 'Test',
        'items': 'Items',
        'in_store': 'InStore',
        'promotion_code': 'PromotionCode',
        'payments': 'Payments',
        'send_email': 'SendEmail',
        'location_id': 'LocationId',
        'image': 'Image',
        'image_file_name': 'ImageFileName'
    }

    def __init__(self, cart_id=None, client_id=None, test=None, items=None, in_store=None, promotion_code=None, payments=None, send_email=None, location_id=None, image=None, image_file_name=None):  # noqa: E501
        """CheckoutShoppingCartRequest - a model defined in Swagger"""  # noqa: E501

        self._cart_id = None
        self._client_id = None
        self._test = None
        self._items = None
        self._in_store = None
        self._promotion_code = None
        self._payments = None
        self._send_email = None
        self._location_id = None
        self._image = None
        self._image_file_name = None
        self.discriminator = None

        if cart_id is not None:
            self.cart_id = cart_id
        self.client_id = client_id
        if test is not None:
            self.test = test
        self.items = items
        if in_store is not None:
            self.in_store = in_store
        if promotion_code is not None:
            self.promotion_code = promotion_code
        self.payments = payments
        if send_email is not None:
            self.send_email = send_email
        if location_id is not None:
            self.location_id = location_id
        if image is not None:
            self.image = image
        if image_file_name is not None:
            self.image_file_name = image_file_name

    @property
    def cart_id(self):
        """Gets the cart_id of this CheckoutShoppingCartRequest.  # noqa: E501

        The unique ID of the shopping cart to be processed. You can use this value to maintain a persistent cart. If you do not specify a cart ID, the MINDBODY software generates one.  # noqa: E501

        :return: The cart_id of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: str
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """Sets the cart_id of this CheckoutShoppingCartRequest.

        The unique ID of the shopping cart to be processed. You can use this value to maintain a persistent cart. If you do not specify a cart ID, the MINDBODY software generates one.  # noqa: E501

        :param cart_id: The cart_id of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: str
        """

        self._cart_id = cart_id

    @property
    def client_id(self):
        """Gets the client_id of this CheckoutShoppingCartRequest.  # noqa: E501

        The RSSID of the client making the purchase. A cart can be validated without a client ID, but a client ID must be specified to complete a sale.  # noqa: E501

        :return: The client_id of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this CheckoutShoppingCartRequest.

        The RSSID of the client making the purchase. A cart can be validated without a client ID, but a client ID must be specified to complete a sale.  # noqa: E501

        :param client_id: The client_id of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def test(self):
        """Gets the test of this CheckoutShoppingCartRequest.  # noqa: E501

        When `true`, indicates that the contents of the cart are validated, but the transaction does not take place. You should use this parameter during testing and when checking the calculated totals of the items in the cart.<br />  When `false`, the transaction takes place and the database is affected.<br />  Default: **false**  # noqa: E501

        :return: The test of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CheckoutShoppingCartRequest.

        When `true`, indicates that the contents of the cart are validated, but the transaction does not take place. You should use this parameter during testing and when checking the calculated totals of the items in the cart.<br />  When `false`, the transaction takes place and the database is affected.<br />  Default: **false**  # noqa: E501

        :param test: The test of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: bool
        """

        self._test = test

    @property
    def items(self):
        """Gets the items of this CheckoutShoppingCartRequest.  # noqa: E501

        A list of the items in the cart.  # noqa: E501

        :return: The items of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: list[CheckoutItemWrapper]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CheckoutShoppingCartRequest.

        A list of the items in the cart.  # noqa: E501

        :param items: The items of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: list[CheckoutItemWrapper]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def in_store(self):
        """Gets the in_store of this CheckoutShoppingCartRequest.  # noqa: E501

        When `true`, indicates that the cart is to be completed by a staff member and is to take place at one of the business’ physical locations.<br />  When `false`, indicates that the cart is to be completed by a client from the business’ online store.<br />  Default: **false**  # noqa: E501

        :return: The in_store of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: bool
        """
        return self._in_store

    @in_store.setter
    def in_store(self, in_store):
        """Sets the in_store of this CheckoutShoppingCartRequest.

        When `true`, indicates that the cart is to be completed by a staff member and is to take place at one of the business’ physical locations.<br />  When `false`, indicates that the cart is to be completed by a client from the business’ online store.<br />  Default: **false**  # noqa: E501

        :param in_store: The in_store of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: bool
        """

        self._in_store = in_store

    @property
    def promotion_code(self):
        """Gets the promotion_code of this CheckoutShoppingCartRequest.  # noqa: E501

        Promotion code to be applied to the cart.  # noqa: E501

        :return: The promotion_code of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: str
        """
        return self._promotion_code

    @promotion_code.setter
    def promotion_code(self, promotion_code):
        """Sets the promotion_code of this CheckoutShoppingCartRequest.

        Promotion code to be applied to the cart.  # noqa: E501

        :param promotion_code: The promotion_code of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: str
        """

        self._promotion_code = promotion_code

    @property
    def payments(self):
        """Gets the payments of this CheckoutShoppingCartRequest.  # noqa: E501

        A list of payment information objects to be applied to payment against the items in the cart.  # noqa: E501

        :return: The payments of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: list[CheckoutPaymentInfo]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this CheckoutShoppingCartRequest.

        A list of payment information objects to be applied to payment against the items in the cart.  # noqa: E501

        :param payments: The payments of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: list[CheckoutPaymentInfo]
        """
        if payments is None:
            raise ValueError("Invalid value for `payments`, must not be `None`")  # noqa: E501

        self._payments = payments

    @property
    def send_email(self):
        """Gets the send_email of this CheckoutShoppingCartRequest.  # noqa: E501

        When `true`, sends a purchase receipt email to the client. Note that all appropriate permissions and settings must be enabled for the client to receive an email.<br />  Default: **false**  # noqa: E501

        :return: The send_email of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_email

    @send_email.setter
    def send_email(self, send_email):
        """Sets the send_email of this CheckoutShoppingCartRequest.

        When `true`, sends a purchase receipt email to the client. Note that all appropriate permissions and settings must be enabled for the client to receive an email.<br />  Default: **false**  # noqa: E501

        :param send_email: The send_email of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: bool
        """

        self._send_email = send_email

    @property
    def location_id(self):
        """Gets the location_id of this CheckoutShoppingCartRequest.  # noqa: E501

        The location ID to be used for pulling business mode prices and taxes. If no location ID is supplied, it defaults to the online store, represented by a null value.   Default: **null** (the online store)  # noqa: E501

        :return: The location_id of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this CheckoutShoppingCartRequest.

        The location ID to be used for pulling business mode prices and taxes. If no location ID is supplied, it defaults to the online store, represented by a null value.   Default: **null** (the online store)  # noqa: E501

        :param location_id: The location_id of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def image(self):
        """Gets the image of this CheckoutShoppingCartRequest.  # noqa: E501

        The byte array data of the signature image.  # noqa: E501

        :return: The image of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this CheckoutShoppingCartRequest.

        The byte array data of the signature image.  # noqa: E501

        :param image: The image of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: str
        """
        if image is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', image):  # noqa: E501
            raise ValueError(r"Invalid value for `image`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._image = image

    @property
    def image_file_name(self):
        """Gets the image_file_name of this CheckoutShoppingCartRequest.  # noqa: E501

        The name of the signature image being uploaded.  # noqa: E501

        :return: The image_file_name of this CheckoutShoppingCartRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_file_name

    @image_file_name.setter
    def image_file_name(self, image_file_name):
        """Sets the image_file_name of this CheckoutShoppingCartRequest.

        The name of the signature image being uploaded.  # noqa: E501

        :param image_file_name: The image_file_name of this CheckoutShoppingCartRequest.  # noqa: E501
        :type: str
        """

        self._image_file_name = image_file_name

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
        if issubclass(CheckoutShoppingCartRequest, dict):
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
        if not isinstance(other, CheckoutShoppingCartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
