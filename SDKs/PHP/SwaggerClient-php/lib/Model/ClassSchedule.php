<?php
/**
 * ClassSchedule
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
 * ClassSchedule Class Doc Comment
 *
 * @category Class
 * @description Represents a single class instance. The class meets at the start time, goes until the end time.
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class ClassSchedule implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'ClassSchedule';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'classes' => '\Swagger\Client\Model\ModelClass[]',
        'clients' => '\Swagger\Client\Model\Client[]',
        'course' => '\Swagger\Client\Model\Course',
        'semester_id' => 'int',
        'is_available' => 'bool',
        'id' => 'int',
        'class_description' => '\Swagger\Client\Model\ClassDescription',
        'day_sunday' => 'bool',
        'day_monday' => 'bool',
        'day_tuesday' => 'bool',
        'day_wednesday' => 'bool',
        'day_thursday' => 'bool',
        'day_friday' => 'bool',
        'day_saturday' => 'bool',
        'allow_open_enrollment' => 'bool',
        'allow_date_forward_enrollment' => 'bool',
        'start_time' => '\DateTime',
        'end_time' => '\DateTime',
        'start_date' => '\DateTime',
        'end_date' => '\DateTime',
        'staff' => '\Swagger\Client\Model\Staff',
        'location' => '\Swagger\Client\Model\Location'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'classes' => null,
        'clients' => null,
        'course' => null,
        'semester_id' => 'int32',
        'is_available' => null,
        'id' => 'int32',
        'class_description' => null,
        'day_sunday' => null,
        'day_monday' => null,
        'day_tuesday' => null,
        'day_wednesday' => null,
        'day_thursday' => null,
        'day_friday' => null,
        'day_saturday' => null,
        'allow_open_enrollment' => null,
        'allow_date_forward_enrollment' => null,
        'start_time' => 'date-time',
        'end_time' => 'date-time',
        'start_date' => 'date-time',
        'end_date' => 'date-time',
        'staff' => null,
        'location' => null
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
        'classes' => 'Classes',
        'clients' => 'Clients',
        'course' => 'Course',
        'semester_id' => 'SemesterId',
        'is_available' => 'IsAvailable',
        'id' => 'Id',
        'class_description' => 'ClassDescription',
        'day_sunday' => 'DaySunday',
        'day_monday' => 'DayMonday',
        'day_tuesday' => 'DayTuesday',
        'day_wednesday' => 'DayWednesday',
        'day_thursday' => 'DayThursday',
        'day_friday' => 'DayFriday',
        'day_saturday' => 'DaySaturday',
        'allow_open_enrollment' => 'AllowOpenEnrollment',
        'allow_date_forward_enrollment' => 'AllowDateForwardEnrollment',
        'start_time' => 'StartTime',
        'end_time' => 'EndTime',
        'start_date' => 'StartDate',
        'end_date' => 'EndDate',
        'staff' => 'Staff',
        'location' => 'Location'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'classes' => 'setClasses',
        'clients' => 'setClients',
        'course' => 'setCourse',
        'semester_id' => 'setSemesterId',
        'is_available' => 'setIsAvailable',
        'id' => 'setId',
        'class_description' => 'setClassDescription',
        'day_sunday' => 'setDaySunday',
        'day_monday' => 'setDayMonday',
        'day_tuesday' => 'setDayTuesday',
        'day_wednesday' => 'setDayWednesday',
        'day_thursday' => 'setDayThursday',
        'day_friday' => 'setDayFriday',
        'day_saturday' => 'setDaySaturday',
        'allow_open_enrollment' => 'setAllowOpenEnrollment',
        'allow_date_forward_enrollment' => 'setAllowDateForwardEnrollment',
        'start_time' => 'setStartTime',
        'end_time' => 'setEndTime',
        'start_date' => 'setStartDate',
        'end_date' => 'setEndDate',
        'staff' => 'setStaff',
        'location' => 'setLocation'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'classes' => 'getClasses',
        'clients' => 'getClients',
        'course' => 'getCourse',
        'semester_id' => 'getSemesterId',
        'is_available' => 'getIsAvailable',
        'id' => 'getId',
        'class_description' => 'getClassDescription',
        'day_sunday' => 'getDaySunday',
        'day_monday' => 'getDayMonday',
        'day_tuesday' => 'getDayTuesday',
        'day_wednesday' => 'getDayWednesday',
        'day_thursday' => 'getDayThursday',
        'day_friday' => 'getDayFriday',
        'day_saturday' => 'getDaySaturday',
        'allow_open_enrollment' => 'getAllowOpenEnrollment',
        'allow_date_forward_enrollment' => 'getAllowDateForwardEnrollment',
        'start_time' => 'getStartTime',
        'end_time' => 'getEndTime',
        'start_date' => 'getStartDate',
        'end_date' => 'getEndDate',
        'staff' => 'getStaff',
        'location' => 'getLocation'
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
        $this->container['classes'] = isset($data['classes']) ? $data['classes'] : null;
        $this->container['clients'] = isset($data['clients']) ? $data['clients'] : null;
        $this->container['course'] = isset($data['course']) ? $data['course'] : null;
        $this->container['semester_id'] = isset($data['semester_id']) ? $data['semester_id'] : null;
        $this->container['is_available'] = isset($data['is_available']) ? $data['is_available'] : null;
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['class_description'] = isset($data['class_description']) ? $data['class_description'] : null;
        $this->container['day_sunday'] = isset($data['day_sunday']) ? $data['day_sunday'] : null;
        $this->container['day_monday'] = isset($data['day_monday']) ? $data['day_monday'] : null;
        $this->container['day_tuesday'] = isset($data['day_tuesday']) ? $data['day_tuesday'] : null;
        $this->container['day_wednesday'] = isset($data['day_wednesday']) ? $data['day_wednesday'] : null;
        $this->container['day_thursday'] = isset($data['day_thursday']) ? $data['day_thursday'] : null;
        $this->container['day_friday'] = isset($data['day_friday']) ? $data['day_friday'] : null;
        $this->container['day_saturday'] = isset($data['day_saturday']) ? $data['day_saturday'] : null;
        $this->container['allow_open_enrollment'] = isset($data['allow_open_enrollment']) ? $data['allow_open_enrollment'] : null;
        $this->container['allow_date_forward_enrollment'] = isset($data['allow_date_forward_enrollment']) ? $data['allow_date_forward_enrollment'] : null;
        $this->container['start_time'] = isset($data['start_time']) ? $data['start_time'] : null;
        $this->container['end_time'] = isset($data['end_time']) ? $data['end_time'] : null;
        $this->container['start_date'] = isset($data['start_date']) ? $data['start_date'] : null;
        $this->container['end_date'] = isset($data['end_date']) ? $data['end_date'] : null;
        $this->container['staff'] = isset($data['staff']) ? $data['staff'] : null;
        $this->container['location'] = isset($data['location']) ? $data['location'] : null;
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
     * Gets classes
     *
     * @return \Swagger\Client\Model\ModelClass[]
     */
    public function getClasses()
    {
        return $this->container['classes'];
    }

    /**
     * Sets classes
     *
     * @param \Swagger\Client\Model\ModelClass[] $classes Contains information about classes.
     *
     * @return $this
     */
    public function setClasses($classes)
    {
        $this->container['classes'] = $classes;

        return $this;
    }

    /**
     * Gets clients
     *
     * @return \Swagger\Client\Model\Client[]
     */
    public function getClients()
    {
        return $this->container['clients'];
    }

    /**
     * Sets clients
     *
     * @param \Swagger\Client\Model\Client[] $clients Contains information about clients.
     *
     * @return $this
     */
    public function setClients($clients)
    {
        $this->container['clients'] = $clients;

        return $this;
    }

    /**
     * Gets course
     *
     * @return \Swagger\Client\Model\Course
     */
    public function getCourse()
    {
        return $this->container['course'];
    }

    /**
     * Sets course
     *
     * @param \Swagger\Client\Model\Course $course Contains information about the course that the enrollment is a part of.
     *
     * @return $this
     */
    public function setCourse($course)
    {
        $this->container['course'] = $course;

        return $this;
    }

    /**
     * Gets semester_id
     *
     * @return int
     */
    public function getSemesterId()
    {
        return $this->container['semester_id'];
    }

    /**
     * Sets semester_id
     *
     * @param int $semester_id The semester ID for the enrollment (if any).
     *
     * @return $this
     */
    public function setSemesterId($semester_id)
    {
        $this->container['semester_id'] = $semester_id;

        return $this;
    }

    /**
     * Gets is_available
     *
     * @return bool
     */
    public function getIsAvailable()
    {
        return $this->container['is_available'];
    }

    /**
     * Sets is_available
     *
     * @param bool $is_available When `true`, indicates that the enrollment shows in consumer mode, has not started yet, and there is room in each class of the enrollment.<br />  When `false`, indicates that either the enrollment does not show in consumer mode, has already started, or there is no room in some classes of the enrollment.
     *
     * @return $this
     */
    public function setIsAvailable($is_available)
    {
        $this->container['is_available'] = $is_available;

        return $this;
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
     * @param int $id The unique ID of the class schedule.
     *
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

        return $this;
    }

    /**
     * Gets class_description
     *
     * @return \Swagger\Client\Model\ClassDescription
     */
    public function getClassDescription()
    {
        return $this->container['class_description'];
    }

    /**
     * Sets class_description
     *
     * @param \Swagger\Client\Model\ClassDescription $class_description Contains information about the class.
     *
     * @return $this
     */
    public function setClassDescription($class_description)
    {
        $this->container['class_description'] = $class_description;

        return $this;
    }

    /**
     * Gets day_sunday
     *
     * @return bool
     */
    public function getDaySunday()
    {
        return $this->container['day_sunday'];
    }

    /**
     * Sets day_sunday
     *
     * @param bool $day_sunday When `true`, indicates that this schedule occurs on Sundays.
     *
     * @return $this
     */
    public function setDaySunday($day_sunday)
    {
        $this->container['day_sunday'] = $day_sunday;

        return $this;
    }

    /**
     * Gets day_monday
     *
     * @return bool
     */
    public function getDayMonday()
    {
        return $this->container['day_monday'];
    }

    /**
     * Sets day_monday
     *
     * @param bool $day_monday When `true`, indicates that this schedule occurs on Mondays.
     *
     * @return $this
     */
    public function setDayMonday($day_monday)
    {
        $this->container['day_monday'] = $day_monday;

        return $this;
    }

    /**
     * Gets day_tuesday
     *
     * @return bool
     */
    public function getDayTuesday()
    {
        return $this->container['day_tuesday'];
    }

    /**
     * Sets day_tuesday
     *
     * @param bool $day_tuesday When `true`, indicates that this schedule occurs on Tuesdays.
     *
     * @return $this
     */
    public function setDayTuesday($day_tuesday)
    {
        $this->container['day_tuesday'] = $day_tuesday;

        return $this;
    }

    /**
     * Gets day_wednesday
     *
     * @return bool
     */
    public function getDayWednesday()
    {
        return $this->container['day_wednesday'];
    }

    /**
     * Sets day_wednesday
     *
     * @param bool $day_wednesday When `true`, indicates that this schedule occurs on Wednesdays.
     *
     * @return $this
     */
    public function setDayWednesday($day_wednesday)
    {
        $this->container['day_wednesday'] = $day_wednesday;

        return $this;
    }

    /**
     * Gets day_thursday
     *
     * @return bool
     */
    public function getDayThursday()
    {
        return $this->container['day_thursday'];
    }

    /**
     * Sets day_thursday
     *
     * @param bool $day_thursday When `true`, indicates that this schedule occurs on Thursdays.
     *
     * @return $this
     */
    public function setDayThursday($day_thursday)
    {
        $this->container['day_thursday'] = $day_thursday;

        return $this;
    }

    /**
     * Gets day_friday
     *
     * @return bool
     */
    public function getDayFriday()
    {
        return $this->container['day_friday'];
    }

    /**
     * Sets day_friday
     *
     * @param bool $day_friday When `true`, indicates that this schedule occurs on Fridays.
     *
     * @return $this
     */
    public function setDayFriday($day_friday)
    {
        $this->container['day_friday'] = $day_friday;

        return $this;
    }

    /**
     * Gets day_saturday
     *
     * @return bool
     */
    public function getDaySaturday()
    {
        return $this->container['day_saturday'];
    }

    /**
     * Sets day_saturday
     *
     * @param bool $day_saturday When `true`, indicates that this schedule occurs on Saturdays.
     *
     * @return $this
     */
    public function setDaySaturday($day_saturday)
    {
        $this->container['day_saturday'] = $day_saturday;

        return $this;
    }

    /**
     * Gets allow_open_enrollment
     *
     * @return bool
     */
    public function getAllowOpenEnrollment()
    {
        return $this->container['allow_open_enrollment'];
    }

    /**
     * Sets allow_open_enrollment
     *
     * @param bool $allow_open_enrollment When `true`, indicates that the enrollment allows booking after the enrollment has started.
     *
     * @return $this
     */
    public function setAllowOpenEnrollment($allow_open_enrollment)
    {
        $this->container['allow_open_enrollment'] = $allow_open_enrollment;

        return $this;
    }

    /**
     * Gets allow_date_forward_enrollment
     *
     * @return bool
     */
    public function getAllowDateForwardEnrollment()
    {
        return $this->container['allow_date_forward_enrollment'];
    }

    /**
     * Sets allow_date_forward_enrollment
     *
     * @param bool $allow_date_forward_enrollment When `true`, indicates that this the enrollment shows in consumer mode, the enrollment has not started yet, and there is room in each class of the enrollment.
     *
     * @return $this
     */
    public function setAllowDateForwardEnrollment($allow_date_forward_enrollment)
    {
        $this->container['allow_date_forward_enrollment'] = $allow_date_forward_enrollment;

        return $this;
    }

    /**
     * Gets start_time
     *
     * @return \DateTime
     */
    public function getStartTime()
    {
        return $this->container['start_time'];
    }

    /**
     * Sets start_time
     *
     * @param \DateTime $start_time The time this class schedule starts.
     *
     * @return $this
     */
    public function setStartTime($start_time)
    {
        $this->container['start_time'] = $start_time;

        return $this;
    }

    /**
     * Gets end_time
     *
     * @return \DateTime
     */
    public function getEndTime()
    {
        return $this->container['end_time'];
    }

    /**
     * Sets end_time
     *
     * @param \DateTime $end_time The time this class schedule ends.
     *
     * @return $this
     */
    public function setEndTime($end_time)
    {
        $this->container['end_time'] = $end_time;

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
     * @param \DateTime $start_date The date this class schedule starts.
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
     * @param \DateTime $end_date The date this class schedule ends.
     *
     * @return $this
     */
    public function setEndDate($end_date)
    {
        $this->container['end_date'] = $end_date;

        return $this;
    }

    /**
     * Gets staff
     *
     * @return \Swagger\Client\Model\Staff
     */
    public function getStaff()
    {
        return $this->container['staff'];
    }

    /**
     * Sets staff
     *
     * @param \Swagger\Client\Model\Staff $staff Contains information about the staff member who is regularly scheduled to teach the class.
     *
     * @return $this
     */
    public function setStaff($staff)
    {
        $this->container['staff'] = $staff;

        return $this;
    }

    /**
     * Gets location
     *
     * @return \Swagger\Client\Model\Location
     */
    public function getLocation()
    {
        return $this->container['location'];
    }

    /**
     * Sets location
     *
     * @param \Swagger\Client\Model\Location $location Contains information about the regularly scheduled location of this class.
     *
     * @return $this
     */
    public function setLocation($location)
    {
        $this->container['location'] = $location;

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


