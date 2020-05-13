<?php
/**
 * GetBookableItemsRequest
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
 * GetBookableItemsRequest Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class GetBookableItemsRequest implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'GetBookableItemsRequest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'session_type_ids' => 'int[]',
        'location_ids' => 'int[]',
        'staff_ids' => 'int[]',
        'start_date' => '\DateTime',
        'end_date' => '\DateTime',
        'appointment_id' => 'int',
        'ignore_default_session_length' => 'bool',
        'limit' => 'int',
        'offset' => 'int'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'session_type_ids' => 'int32',
        'location_ids' => 'int32',
        'staff_ids' => 'int64',
        'start_date' => 'date-time',
        'end_date' => 'date-time',
        'appointment_id' => 'int64',
        'ignore_default_session_length' => null,
        'limit' => 'int32',
        'offset' => 'int32'
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
        'session_type_ids' => 'SessionTypeIds',
        'location_ids' => 'LocationIds',
        'staff_ids' => 'StaffIds',
        'start_date' => 'StartDate',
        'end_date' => 'EndDate',
        'appointment_id' => 'AppointmentId',
        'ignore_default_session_length' => 'IgnoreDefaultSessionLength',
        'limit' => 'Limit',
        'offset' => 'Offset'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'session_type_ids' => 'setSessionTypeIds',
        'location_ids' => 'setLocationIds',
        'staff_ids' => 'setStaffIds',
        'start_date' => 'setStartDate',
        'end_date' => 'setEndDate',
        'appointment_id' => 'setAppointmentId',
        'ignore_default_session_length' => 'setIgnoreDefaultSessionLength',
        'limit' => 'setLimit',
        'offset' => 'setOffset'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'session_type_ids' => 'getSessionTypeIds',
        'location_ids' => 'getLocationIds',
        'staff_ids' => 'getStaffIds',
        'start_date' => 'getStartDate',
        'end_date' => 'getEndDate',
        'appointment_id' => 'getAppointmentId',
        'ignore_default_session_length' => 'getIgnoreDefaultSessionLength',
        'limit' => 'getLimit',
        'offset' => 'getOffset'
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
        $this->container['session_type_ids'] = isset($data['session_type_ids']) ? $data['session_type_ids'] : null;
        $this->container['location_ids'] = isset($data['location_ids']) ? $data['location_ids'] : null;
        $this->container['staff_ids'] = isset($data['staff_ids']) ? $data['staff_ids'] : null;
        $this->container['start_date'] = isset($data['start_date']) ? $data['start_date'] : null;
        $this->container['end_date'] = isset($data['end_date']) ? $data['end_date'] : null;
        $this->container['appointment_id'] = isset($data['appointment_id']) ? $data['appointment_id'] : null;
        $this->container['ignore_default_session_length'] = isset($data['ignore_default_session_length']) ? $data['ignore_default_session_length'] : null;
        $this->container['limit'] = isset($data['limit']) ? $data['limit'] : null;
        $this->container['offset'] = isset($data['offset']) ? $data['offset'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

        if ($this->container['session_type_ids'] === null) {
            $invalidProperties[] = "'session_type_ids' can't be null";
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
     * Gets session_type_ids
     *
     * @return int[]
     */
    public function getSessionTypeIds()
    {
        return $this->container['session_type_ids'];
    }

    /**
     * Sets session_type_ids
     *
     * @param int[] $session_type_ids A list of the requested session type IDs.
     *
     * @return $this
     */
    public function setSessionTypeIds($session_type_ids)
    {
        $this->container['session_type_ids'] = $session_type_ids;

        return $this;
    }

    /**
     * Gets location_ids
     *
     * @return int[]
     */
    public function getLocationIds()
    {
        return $this->container['location_ids'];
    }

    /**
     * Sets location_ids
     *
     * @param int[] $location_ids A list of the requested location IDs.
     *
     * @return $this
     */
    public function setLocationIds($location_ids)
    {
        $this->container['location_ids'] = $location_ids;

        return $this;
    }

    /**
     * Gets staff_ids
     *
     * @return int[]
     */
    public function getStaffIds()
    {
        return $this->container['staff_ids'];
    }

    /**
     * Sets staff_ids
     *
     * @param int[] $staff_ids A list of the requested staff IDs.
     *
     * @return $this
     */
    public function setStaffIds($staff_ids)
    {
        $this->container['staff_ids'] = $staff_ids;

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
     * @param \DateTime $start_date The start date of the requested date range.   <br />Default: **today’s date**
     *
     * @return $this
     */
    public function setStartDate($start_date)
    {
        $this->container['start_date'] = $start_date;

        return $this;
    }

    /**
     * Gets end_date
     *
     * @return \DateTime
     */
    public function getEndDate()
    {
        return $this->container['end_date'];
    }

    /**
     * Sets end_date
     *
     * @param \DateTime $end_date The end date of the requested date range.   <br />Default: **StartDate**
     *
     * @return $this
     */
    public function setEndDate($end_date)
    {
        $this->container['end_date'] = $end_date;

        return $this;
    }

    /**
     * Gets appointment_id
     *
     * @return int
     */
    public function getAppointmentId()
    {
        return $this->container['appointment_id'];
    }

    /**
     * Sets appointment_id
     *
     * @param int $appointment_id If provided, filters out the appointment with this ID.
     *
     * @return $this
     */
    public function setAppointmentId($appointment_id)
    {
        $this->container['appointment_id'] = $appointment_id;

        return $this;
    }

    /**
     * Gets ignore_default_session_length
     *
     * @return bool
     */
    public function getIgnoreDefaultSessionLength()
    {
        return $this->container['ignore_default_session_length'];
    }

    /**
     * Sets ignore_default_session_length
     *
     * @param bool $ignore_default_session_length When `true`, availabilities that are non-default return, for example, a 30-minute availability with a 60-minute default session length.<br />  When `false`, only availabilities that have the default session length return.
     *
     * @return $this
     */
    public function setIgnoreDefaultSessionLength($ignore_default_session_length)
    {
        $this->container['ignore_default_session_length'] = $ignore_default_session_length;

        return $this;
    }

    /**
     * Gets limit
     *
     * @return int
     */
    public function getLimit()
    {
        return $this->container['limit'];
    }

    /**
     * Sets limit
     *
     * @param int $limit Number of results to include, defaults to 100
     *
     * @return $this
     */
    public function setLimit($limit)
    {
        $this->container['limit'] = $limit;

        return $this;
    }

    /**
     * Gets offset
     *
     * @return int
     */
    public function getOffset()
    {
        return $this->container['offset'];
    }

    /**
     * Sets offset
     *
     * @param int $offset Page offset, defaults to 0.
     *
     * @return $this
     */
    public function setOffset($offset)
    {
        $this->container['offset'] = $offset;

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

