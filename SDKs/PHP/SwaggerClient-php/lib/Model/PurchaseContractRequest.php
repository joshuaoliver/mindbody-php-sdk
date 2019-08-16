<?php
/**
 * PurchaseContractRequest
 *
 * PHP version 5
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */

/**
 * MINDBODY Public API
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: v6
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 * Swagger Codegen version: 2.4.6
 */

/**
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen
 * Do not edit the class manually.
 */

namespace Swagger\Client\Model;

use \ArrayAccess;
use \Swagger\Client\ObjectSerializer;

/**
 * PurchaseContractRequest Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class PurchaseContractRequest implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'PurchaseContractRequest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'test' => 'bool',
        'location_id' => 'int',
        'client_id' => 'string',
        'contract_id' => 'int',
        'start_date' => '\DateTime',
        'first_payment_occurs' => 'string',
        'client_signature' => 'string',
        'promotion_code' => 'string',
        'credit_card_info' => '\Swagger\Client\Model\CreditCardInfo',
        'stored_card_info' => '\Swagger\Client\Model\StoredCardInfo',
        'send_notifications' => 'bool'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'test' => null,
        'location_id' => 'int32',
        'client_id' => null,
        'contract_id' => 'int32',
        'start_date' => 'date-time',
        'first_payment_occurs' => null,
        'client_signature' => 'byte',
        'promotion_code' => null,
        'credit_card_info' => null,
        'stored_card_info' => null,
        'send_notifications' => null
    ];

    /**
     * Array of property to type mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerTypes()
    {
        return self::$swaggerTypes;
    }

    /**
     * Array of property to format mappings. Used for (de)serialization
     *
     * @return array
     */
    public static function swaggerFormats()
    {
        return self::$swaggerFormats;
    }

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @var string[]
     */
    protected static $attributeMap = [
        'test' => 'Test',
        'location_id' => 'LocationId',
        'client_id' => 'ClientId',
        'contract_id' => 'ContractId',
        'start_date' => 'StartDate',
        'first_payment_occurs' => 'FirstPaymentOccurs',
        'client_signature' => 'ClientSignature',
        'promotion_code' => 'PromotionCode',
        'credit_card_info' => 'CreditCardInfo',
        'stored_card_info' => 'StoredCardInfo',
        'send_notifications' => 'SendNotifications'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'test' => 'setTest',
        'location_id' => 'setLocationId',
        'client_id' => 'setClientId',
        'contract_id' => 'setContractId',
        'start_date' => 'setStartDate',
        'first_payment_occurs' => 'setFirstPaymentOccurs',
        'client_signature' => 'setClientSignature',
        'promotion_code' => 'setPromotionCode',
        'credit_card_info' => 'setCreditCardInfo',
        'stored_card_info' => 'setStoredCardInfo',
        'send_notifications' => 'setSendNotifications'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'test' => 'getTest',
        'location_id' => 'getLocationId',
        'client_id' => 'getClientId',
        'contract_id' => 'getContractId',
        'start_date' => 'getStartDate',
        'first_payment_occurs' => 'getFirstPaymentOccurs',
        'client_signature' => 'getClientSignature',
        'promotion_code' => 'getPromotionCode',
        'credit_card_info' => 'getCreditCardInfo',
        'stored_card_info' => 'getStoredCardInfo',
        'send_notifications' => 'getSendNotifications'
    ];

    /**
     * Array of attributes where the key is the local name,
     * and the value is the original name
     *
     * @return array
     */
    public static function attributeMap()
    {
        return self::$attributeMap;
    }

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @return array
     */
    public static function setters()
    {
        return self::$setters;
    }

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @return array
     */
    public static function getters()
    {
        return self::$getters;
    }

    /**
     * The original name of the model.
     *
     * @return string
     */
    public function getModelName()
    {
        return self::$swaggerModelName;
    }

    

    

    /**
     * Associative array for storing property values
     *
     * @var mixed[]
     */
    protected $container = [];

    /**
     * Constructor
     *
     * @param mixed[] $data Associated array of property values
     *                      initializing the model
     */
    public function __construct(array $data = null)
    {
        $this->container['test'] = isset($data['test']) ? $data['test'] : null;
        $this->container['location_id'] = isset($data['location_id']) ? $data['location_id'] : null;
        $this->container['client_id'] = isset($data['client_id']) ? $data['client_id'] : null;
        $this->container['contract_id'] = isset($data['contract_id']) ? $data['contract_id'] : null;
        $this->container['start_date'] = isset($data['start_date']) ? $data['start_date'] : null;
        $this->container['first_payment_occurs'] = isset($data['first_payment_occurs']) ? $data['first_payment_occurs'] : null;
        $this->container['client_signature'] = isset($data['client_signature']) ? $data['client_signature'] : null;
        $this->container['promotion_code'] = isset($data['promotion_code']) ? $data['promotion_code'] : null;
        $this->container['credit_card_info'] = isset($data['credit_card_info']) ? $data['credit_card_info'] : null;
        $this->container['stored_card_info'] = isset($data['stored_card_info']) ? $data['stored_card_info'] : null;
        $this->container['send_notifications'] = isset($data['send_notifications']) ? $data['send_notifications'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['client_id'] === null) {
            $invalidProperties[] = "'client_id' can't be null";
        }
        if ($this->container['contract_id'] === null) {
            $invalidProperties[] = "'contract_id' can't be null";
        }
        if (!is_null($this->container['client_signature']) && !preg_match("/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/", $this->container['client_signature'])) {
            $invalidProperties[] = "invalid value for 'client_signature', must be conform to the pattern /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/.";
        }

        return $invalidProperties;
    }

    /**
     * Validate all the properties in the model
     * return true if all passed
     *
     * @return bool True if all properties are valid
     */
    public function valid()
    {
        return count($this->listInvalidProperties()) === 0;
    }


    /**
     * Gets test
     *
     * @return bool
     */
    public function getTest()
    {
        return $this->container['test'];
    }

    /**
     * Sets test
     *
     * @param bool $test When `true`, the Public API validates input information, but does not commit it, so no client data is affected.<br />  When `false` or omitted, the transaction is committed, and client data is affected.<br />  Default: **false**
     *
     * @return $this
     */
    public function setTest($test)
    {
        $this->container['test'] = $test;

        return $this;
    }

    /**
     * Gets location_id
     *
     * @return int
     */
    public function getLocationId()
    {
        return $this->container['location_id'];
    }

    /**
     * Sets location_id
     *
     * @param int $location_id The ID of the location where the client is purchasing the contract; used for AutoPays.
     *
     * @return $this
     */
    public function setLocationId($location_id)
    {
        $this->container['location_id'] = $location_id;

        return $this;
    }

    /**
     * Gets client_id
     *
     * @return string
     */
    public function getClientId()
    {
        return $this->container['client_id'];
    }

    /**
     * Sets client_id
     *
     * @param string $client_id The ID of the client. Note that this is not the same as the client’s unique ID.
     *
     * @return $this
     */
    public function setClientId($client_id)
    {
        $this->container['client_id'] = $client_id;

        return $this;
    }

    /**
     * Gets contract_id
     *
     * @return int
     */
    public function getContractId()
    {
        return $this->container['contract_id'];
    }

    /**
     * Sets contract_id
     *
     * @param int $contract_id The ID of the contract being purchased.
     *
     * @return $this
     */
    public function setContractId($contract_id)
    {
        $this->container['contract_id'] = $contract_id;

        return $this;
    }

    /**
     * Gets start_date
     *
     * @return \DateTime
     */
    public function getStartDate()
    {
        return $this->container['start_date'];
    }

    /**
     * Sets start_date
     *
     * @param \DateTime $start_date The date that the contract starts.<br />  Default: **today’s date**
     *
     * @return $this
     */
    public function setStartDate($start_date)
    {
        $this->container['start_date'] = $start_date;

        return $this;
    }

    /**
     * Gets first_payment_occurs
     *
     * @return string
     */
    public function getFirstPaymentOccurs()
    {
        return $this->container['first_payment_occurs'];
    }

    /**
     * Sets first_payment_occurs
     *
     * @param string $first_payment_occurs The date on which the first payment is to occur. Possible values:  * Instant  * `StartDate`
     *
     * @return $this
     */
    public function setFirstPaymentOccurs($first_payment_occurs)
    {
        $this->container['first_payment_occurs'] = $first_payment_occurs;

        return $this;
    }

    /**
     * Gets client_signature
     *
     * @return string
     */
    public function getClientSignature()
    {
        return $this->container['client_signature'];
    }

    /**
     * Sets client_signature
     *
     * @param string $client_signature A representation of the client’s signature. This value can take the form of Base64-encoded byte array. The file type should be PNG. The picture of the client’s signature is uploaded and viewable from the Client Documents page in the Core Business Mode software. The title of the document is:<br />  clientContractSignature-{uniquePurchasedClientContractID}-{contractName}-{contractStartDate}.{fileType}
     *
     * @return $this
     */
    public function setClientSignature($client_signature)
    {

        if (!is_null($client_signature) && (!preg_match("/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/", $client_signature))) {
            throw new \InvalidArgumentException("invalid value for $client_signature when calling PurchaseContractRequest., must conform to the pattern /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/.");
        }

        $this->container['client_signature'] = $client_signature;

        return $this;
    }

    /**
     * Gets promotion_code
     *
     * @return string
     */
    public function getPromotionCode()
    {
        return $this->container['promotion_code'];
    }

    /**
     * Sets promotion_code
     *
     * @param string $promotion_code A promotion code, if one applies. Promotion codes are applied to items that are both marked as pay now in a contract and are discounted by the promotion code. If a pay now item is an autopay item, its autopay price is the price at the time of checkout, so, if a promotion code was applied, all autopays are scheduled using that discounted price.
     *
     * @return $this
     */
    public function setPromotionCode($promotion_code)
    {
        $this->container['promotion_code'] = $promotion_code;

        return $this;
    }

    /**
     * Gets credit_card_info
     *
     * @return \Swagger\Client\Model\CreditCardInfo
     */
    public function getCreditCardInfo()
    {
        return $this->container['credit_card_info'];
    }

    /**
     * Sets credit_card_info
     *
     * @param \Swagger\Client\Model\CreditCardInfo $credit_card_info Contains credit card payment information.<br />  Either `StoredCardInfo` or `CreditCardInfo` is required; the other becomes optional.
     *
     * @return $this
     */
    public function setCreditCardInfo($credit_card_info)
    {
        $this->container['credit_card_info'] = $credit_card_info;

        return $this;
    }

    /**
     * Gets stored_card_info
     *
     * @return \Swagger\Client\Model\StoredCardInfo
     */
    public function getStoredCardInfo()
    {
        return $this->container['stored_card_info'];
    }

    /**
     * Sets stored_card_info
     *
     * @param \Swagger\Client\Model\StoredCardInfo $stored_card_info Contains information about the stored credit card payment.<br />  Either `CreditCardInfo` or `StoredCardInfo` is required; the other becomes optional.
     *
     * @return $this
     */
    public function setStoredCardInfo($stored_card_info)
    {
        $this->container['stored_card_info'] = $stored_card_info;

        return $this;
    }

    /**
     * Gets send_notifications
     *
     * @return bool
     */
    public function getSendNotifications()
    {
        return $this->container['send_notifications'];
    }

    /**
     * Sets send_notifications
     *
     * @param bool $send_notifications When `true`, indicates that email and SMS notifications should be sent to the client after purchase.<br />  Default: **true**
     *
     * @return $this
     */
    public function setSendNotifications($send_notifications)
    {
        $this->container['send_notifications'] = $send_notifications;

        return $this;
    }
    /**
     * Returns true if offset exists. False otherwise.
     *
     * @param integer $offset Offset
     *
     * @return boolean
     */
    public function offsetExists($offset)
    {
        return isset($this->container[$offset]);
    }

    /**
     * Gets offset.
     *
     * @param integer $offset Offset
     *
     * @return mixed
     */
    public function offsetGet($offset)
    {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }

    /**
     * Sets value based on offset.
     *
     * @param integer $offset Offset
     * @param mixed   $value  Value to be set
     *
     * @return void
     */
    public function offsetSet($offset, $value)
    {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    /**
     * Unsets offset.
     *
     * @param integer $offset Offset
     *
     * @return void
     */
    public function offsetUnset($offset)
    {
        unset($this->container[$offset]);
    }

    /**
     * Gets the string presentation of the object
     *
     * @return string
     */
    public function __toString()
    {
        if (defined('JSON_PRETTY_PRINT')) { // use JSON pretty print
            return json_encode(
                ObjectSerializer::sanitizeForSerialization($this),
                JSON_PRETTY_PRINT
            );
        }

        return json_encode(ObjectSerializer::sanitizeForSerialization($this));
    }
}


