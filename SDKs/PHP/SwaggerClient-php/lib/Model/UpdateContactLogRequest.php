<?php
/**
 * UpdateContactLogRequest
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
 * UpdateContactLogRequest Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class UpdateContactLogRequest implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'UpdateContactLogRequest';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'id' => 'int',
        'test' => 'bool',
        'assigned_to_staff_id' => 'int',
        'text' => 'string',
        'contact_name' => 'string',
        'followup_by_date' => '\DateTime',
        'contact_method' => 'string',
        'comments' => '\Swagger\Client\Model\UpdateContactLogComment[]',
        'types' => '\Swagger\Client\Model\UpdateContactLogType[]'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'id' => 'int32',
        'test' => null,
        'assigned_to_staff_id' => 'int64',
        'text' => null,
        'contact_name' => null,
        'followup_by_date' => 'date-time',
        'contact_method' => null,
        'comments' => null,
        'types' => null
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
        'id' => 'Id',
        'test' => 'Test',
        'assigned_to_staff_id' => 'AssignedToStaffId',
        'text' => 'Text',
        'contact_name' => 'ContactName',
        'followup_by_date' => 'FollowupByDate',
        'contact_method' => 'ContactMethod',
        'comments' => 'Comments',
        'types' => 'Types'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'id' => 'setId',
        'test' => 'setTest',
        'assigned_to_staff_id' => 'setAssignedToStaffId',
        'text' => 'setText',
        'contact_name' => 'setContactName',
        'followup_by_date' => 'setFollowupByDate',
        'contact_method' => 'setContactMethod',
        'comments' => 'setComments',
        'types' => 'setTypes'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'id' => 'getId',
        'test' => 'getTest',
        'assigned_to_staff_id' => 'getAssignedToStaffId',
        'text' => 'getText',
        'contact_name' => 'getContactName',
        'followup_by_date' => 'getFollowupByDate',
        'contact_method' => 'getContactMethod',
        'comments' => 'getComments',
        'types' => 'getTypes'
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
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['test'] = isset($data['test']) ? $data['test'] : null;
        $this->container['assigned_to_staff_id'] = isset($data['assigned_to_staff_id']) ? $data['assigned_to_staff_id'] : null;
        $this->container['text'] = isset($data['text']) ? $data['text'] : null;
        $this->container['contact_name'] = isset($data['contact_name']) ? $data['contact_name'] : null;
        $this->container['followup_by_date'] = isset($data['followup_by_date']) ? $data['followup_by_date'] : null;
        $this->container['contact_method'] = isset($data['contact_method']) ? $data['contact_method'] : null;
        $this->container['comments'] = isset($data['comments']) ? $data['comments'] : null;
        $this->container['types'] = isset($data['types']) ? $data['types'] : null;
    }

    /**
     * Show all the invalid properties with reasons.
     *
     * @return array invalid properties with reasons
     */
    public function listInvalidProperties()
    {
        $invalidProperties = [];

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
     * Gets id
     *
     * @return int
     */
    public function getId()
    {
        return $this->container['id'];
    }

    /**
     * Sets id
     *
     * @param int $id The ID of the contact log being updated.
     *
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

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
     * @param bool $test When `true`, indicates that this is a test request and no data is inserted into the subscriber’s database.<br />  When `false`, the database is updated.
     *
     * @return $this
     */
    public function setTest($test)
    {
        $this->container['test'] = $test;

        return $this;
    }

    /**
     * Gets assigned_to_staff_id
     *
     * @return int
     */
    public function getAssignedToStaffId()
    {
        return $this->container['assigned_to_staff_id'];
    }

    /**
     * Sets assigned_to_staff_id
     *
     * @param int $assigned_to_staff_id The ID of the staff member to whom the contact log is now being assigned.
     *
     * @return $this
     */
    public function setAssignedToStaffId($assigned_to_staff_id)
    {
        $this->container['assigned_to_staff_id'] = $assigned_to_staff_id;

        return $this;
    }

    /**
     * Gets text
     *
     * @return string
     */
    public function getText()
    {
        return $this->container['text'];
    }

    /**
     * Sets text
     *
     * @param string $text The contact log’s new text.
     *
     * @return $this
     */
    public function setText($text)
    {
        $this->container['text'] = $text;

        return $this;
    }

    /**
     * Gets contact_name
     *
     * @return string
     */
    public function getContactName()
    {
        return $this->container['contact_name'];
    }

    /**
     * Sets contact_name
     *
     * @param string $contact_name The name of the new person to be contacted by the assigned staff member.
     *
     * @return $this
     */
    public function setContactName($contact_name)
    {
        $this->container['contact_name'] = $contact_name;

        return $this;
    }

    /**
     * Gets followup_by_date
     *
     * @return \DateTime
     */
    public function getFollowupByDate()
    {
        return $this->container['followup_by_date'];
    }

    /**
     * Sets followup_by_date
     *
     * @param \DateTime $followup_by_date The new date by which the assigned staff member should complete this contact log.
     *
     * @return $this
     */
    public function setFollowupByDate($followup_by_date)
    {
        $this->container['followup_by_date'] = $followup_by_date;

        return $this;
    }

    /**
     * Gets contact_method
     *
     * @return string
     */
    public function getContactMethod()
    {
        return $this->container['contact_method'];
    }

    /**
     * Sets contact_method
     *
     * @param string $contact_method The new method by which the client wants to be contacted.
     *
     * @return $this
     */
    public function setContactMethod($contact_method)
    {
        $this->container['contact_method'] = $contact_method;

        return $this;
    }

    /**
     * Gets comments
     *
     * @return \Swagger\Client\Model\UpdateContactLogComment[]
     */
    public function getComments()
    {
        return $this->container['comments'];
    }

    /**
     * Sets comments
     *
     * @param \Swagger\Client\Model\UpdateContactLogComment[] $comments Contains information about the comments being updated or added to the contact log. Comments that have an ID of `0` are added to the contact log.
     *
     * @return $this
     */
    public function setComments($comments)
    {
        $this->container['comments'] = $comments;

        return $this;
    }

    /**
     * Gets types
     *
     * @return \Swagger\Client\Model\UpdateContactLogType[]
     */
    public function getTypes()
    {
        return $this->container['types'];
    }

    /**
     * Sets types
     *
     * @param \Swagger\Client\Model\UpdateContactLogType[] $types Contains information about the contact logs types being assigned to the contact log, in addition to the contact log types that are already assigned.
     *
     * @return $this
     */
    public function setTypes($types)
    {
        $this->container['types'] = $types;

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


