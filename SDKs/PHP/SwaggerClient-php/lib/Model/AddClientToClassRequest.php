<?php
/**
 * AddClientToClassRequest
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
 * AddClientToClassRequest Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class AddClientToClassRequest implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'AddClientToClassRequest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'client_id' => 'string',
        'class_id' => 'int',
        'test' => 'bool',
        'require_payment' => 'bool',
        'waitlist' => 'bool',
        'send_email' => 'bool',
        'waitlist_entry_id' => 'int',
        'client_service_id' => 'int',
        'cross_regional_booking' => 'bool',
        'cross_regional_booking_client_service_site_id' => 'int'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'client_id' => null,
        'class_id' => 'int32',
        'test' => null,
        'require_payment' => null,
        'waitlist' => null,
        'send_email' => null,
        'waitlist_entry_id' => 'int32',
        'client_service_id' => 'int32',
        'cross_regional_booking' => null,
        'cross_regional_booking_client_service_site_id' => 'int32'
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
        'client_id' => 'ClientId',
        'class_id' => 'ClassId',
        'test' => 'Test',
        'require_payment' => 'RequirePayment',
        'waitlist' => 'Waitlist',
        'send_email' => 'SendEmail',
        'waitlist_entry_id' => 'WaitlistEntryId',
        'client_service_id' => 'ClientServiceId',
        'cross_regional_booking' => 'CrossRegionalBooking',
        'cross_regional_booking_client_service_site_id' => 'CrossRegionalBookingClientServiceSiteId'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'client_id' => 'setClientId',
        'class_id' => 'setClassId',
        'test' => 'setTest',
        'require_payment' => 'setRequirePayment',
        'waitlist' => 'setWaitlist',
        'send_email' => 'setSendEmail',
        'waitlist_entry_id' => 'setWaitlistEntryId',
        'client_service_id' => 'setClientServiceId',
        'cross_regional_booking' => 'setCrossRegionalBooking',
        'cross_regional_booking_client_service_site_id' => 'setCrossRegionalBookingClientServiceSiteId'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'client_id' => 'getClientId',
        'class_id' => 'getClassId',
        'test' => 'getTest',
        'require_payment' => 'getRequirePayment',
        'waitlist' => 'getWaitlist',
        'send_email' => 'getSendEmail',
        'waitlist_entry_id' => 'getWaitlistEntryId',
        'client_service_id' => 'getClientServiceId',
        'cross_regional_booking' => 'getCrossRegionalBooking',
        'cross_regional_booking_client_service_site_id' => 'getCrossRegionalBookingClientServiceSiteId'
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
        $this->container['client_id'] = isset($data['client_id']) ? $data['client_id'] : null;
        $this->container['class_id'] = isset($data['class_id']) ? $data['class_id'] : null;
        $this->container['test'] = isset($data['test']) ? $data['test'] : null;
        $this->container['require_payment'] = isset($data['require_payment']) ? $data['require_payment'] : null;
        $this->container['waitlist'] = isset($data['waitlist']) ? $data['waitlist'] : null;
        $this->container['send_email'] = isset($data['send_email']) ? $data['send_email'] : null;
        $this->container['waitlist_entry_id'] = isset($data['waitlist_entry_id']) ? $data['waitlist_entry_id'] : null;
        $this->container['client_service_id'] = isset($data['client_service_id']) ? $data['client_service_id'] : null;
        $this->container['cross_regional_booking'] = isset($data['cross_regional_booking']) ? $data['cross_regional_booking'] : null;
        $this->container['cross_regional_booking_client_service_site_id'] = isset($data['cross_regional_booking_client_service_site_id']) ? $data['cross_regional_booking_client_service_site_id'] : null;
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
        if ($this->container['class_id'] === null) {
            $invalidProperties[] = "'class_id' can't be null";
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
     * @param string $client_id The ID of the client who is being booked into the class
     *
     * @return $this
     */
    public function setClientId($client_id)
    {
        $this->container['client_id'] = $client_id;

        return $this;
    }

    /**
     * Gets class_id
     *
     * @return int
     */
    public function getClassId()
    {
        return $this->container['class_id'];
    }

    /**
     * Sets class_id
     *
     * @param int $class_id The ID of the class into which the client is being booked
     *
     * @return $this
     */
    public function setClassId($class_id)
    {
        $this->container['class_id'] = $class_id;

        return $this;
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
     * @param bool $test When `true`, indicates that input information is validated, but not committed.<br />  When `false`, the information is committed and the database is affected.<br />  Default: **false**
     *
     * @return $this
     */
    public function setTest($test)
    {
        $this->container['test'] = $test;

        return $this;
    }

    /**
     * Gets require_payment
     *
     * @return bool
     */
    public function getRequirePayment()
    {
        return $this->container['require_payment'];
    }

    /**
     * Sets require_payment
     *
     * @param bool $require_payment When `true`, the client must have an active, usable pricing option on their account.<br />  When `false` or omitted, an active pricing option is not required to complete the client’s booking.
     *
     * @return $this
     */
    public function setRequirePayment($require_payment)
    {
        $this->container['require_payment'] = $require_payment;

        return $this;
    }

    /**
     * Gets waitlist
     *
     * @return bool
     */
    public function getWaitlist()
    {
        return $this->container['waitlist'];
    }

    /**
     * Sets waitlist
     *
     * @param bool $waitlist When `true`, indicates that the client should be added to a specific class waiting list.<br />  When `false`, the client should not be added to the waiting list.
     *
     * @return $this
     */
    public function setWaitlist($waitlist)
    {
        $this->container['waitlist'] = $waitlist;

        return $this;
    }

    /**
     * Gets send_email
     *
     * @return bool
     */
    public function getSendEmail()
    {
        return $this->container['send_email'];
    }

    /**
     * Sets send_email
     *
     * @param bool $send_email When `true`, the subscriber’s configured Booking Confirmation automatic email is sent to the client. Note that an email is sent only if the client has an email address and automatic emails have been set up.<br />  When `false`, indicates that the client does not receive emails.<br />  Default: **false**
     *
     * @return $this
     */
    public function setSendEmail($send_email)
    {
        $this->container['send_email'] = $send_email;

        return $this;
    }

    /**
     * Gets waitlist_entry_id
     *
     * @return int
     */
    public function getWaitlistEntryId()
    {
        return $this->container['waitlist_entry_id'];
    }

    /**
     * Sets waitlist_entry_id
     *
     * @param int $waitlist_entry_id The ID of the waiting list entry from which you are moving a client into a class.
     *
     * @return $this
     */
    public function setWaitlistEntryId($waitlist_entry_id)
    {
        $this->container['waitlist_entry_id'] = $waitlist_entry_id;

        return $this;
    }

    /**
     * Gets client_service_id
     *
     * @return int
     */
    public function getClientServiceId()
    {
        return $this->container['client_service_id'];
    }

    /**
     * Sets client_service_id
     *
     * @param int $client_service_id The ID of the pricing option on the client’s account that you want to use to pay for this booking, if payment is required at the time of the update.
     *
     * @return $this
     */
    public function setClientServiceId($client_service_id)
    {
        $this->container['client_service_id'] = $client_service_id;

        return $this;
    }

    /**
     * Gets cross_regional_booking
     *
     * @return bool
     */
    public function getCrossRegionalBooking()
    {
        return $this->container['cross_regional_booking'];
    }

    /**
     * Sets cross_regional_booking
     *
     * @param bool $cross_regional_booking When `true`, cross regional series are checked and used if applicable.
     *
     * @return $this
     */
    public function setCrossRegionalBooking($cross_regional_booking)
    {
        $this->container['cross_regional_booking'] = $cross_regional_booking;

        return $this;
    }

    /**
     * Gets cross_regional_booking_client_service_site_id
     *
     * @return int
     */
    public function getCrossRegionalBookingClientServiceSiteId()
    {
        return $this->container['cross_regional_booking_client_service_site_id'];
    }

    /**
     * Sets cross_regional_booking_client_service_site_id
     *
     * @param int $cross_regional_booking_client_service_site_id If the request is cross regional, use a purchased pricing option from this specified site. If omitted, an attempt is made to use an applicable pricing option from the local site.
     *
     * @return $this
     */
    public function setCrossRegionalBookingClientServiceSiteId($cross_regional_booking_client_service_site_id)
    {
        $this->container['cross_regional_booking_client_service_site_id'] = $cross_regional_booking_client_service_site_id;

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


