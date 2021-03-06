<?php
/**
 * Staff
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
 * Staff Class Doc Comment
 *
 * @category Class
 * @package  Swagger\Client
 * @author   Swagger Codegen team
 * @link     https://github.com/swagger-api/swagger-codegen
 */
class Staff implements ModelInterface, ArrayAccess
{
    const DISCRIMINATOR = null;

    /**
      * The original name of the model.
      *
      * @var string
      */
    protected static $swaggerModelName = 'Staff';

    /**
      * Array of property to type mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerTypes = [
        'address' => 'string',
        'appointment_instructor' => 'bool',
        'always_allow_double_booking' => 'bool',
        'bio' => 'string',
        'city' => 'string',
        'country' => 'string',
        'email' => 'string',
        'first_name' => 'string',
        'home_phone' => 'string',
        'id' => 'int',
        'independent_contractor' => 'bool',
        'is_male' => 'bool',
        'last_name' => 'string',
        'mobile_phone' => 'string',
        'name' => 'string',
        'postal_code' => 'string',
        'class_teacher' => 'bool',
        'sort_order' => 'int',
        'state' => 'string',
        'work_phone' => 'string',
        'image_url' => 'string',
        'appointments' => '\Swagger\Client\Model\Appointment[]',
        'unavailabilities' => '\Swagger\Client\Model\Unavailability[]',
        'availabilities' => '\Swagger\Client\Model\Availability[]'
    ];

    /**
      * Array of property to format mappings. Used for (de)serialization
      *
      * @var string[]
      */
    protected static $swaggerFormats = [
        'address' => null,
        'appointment_instructor' => null,
        'always_allow_double_booking' => null,
        'bio' => null,
        'city' => null,
        'country' => null,
        'email' => null,
        'first_name' => null,
        'home_phone' => null,
        'id' => 'int64',
        'independent_contractor' => null,
        'is_male' => null,
        'last_name' => null,
        'mobile_phone' => null,
        'name' => null,
        'postal_code' => null,
        'class_teacher' => null,
        'sort_order' => 'int32',
        'state' => null,
        'work_phone' => null,
        'image_url' => null,
        'appointments' => null,
        'unavailabilities' => null,
        'availabilities' => null
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
        'address' => 'Address',
        'appointment_instructor' => 'AppointmentInstructor',
        'always_allow_double_booking' => 'AlwaysAllowDoubleBooking',
        'bio' => 'Bio',
        'city' => 'City',
        'country' => 'Country',
        'email' => 'Email',
        'first_name' => 'FirstName',
        'home_phone' => 'HomePhone',
        'id' => 'Id',
        'independent_contractor' => 'IndependentContractor',
        'is_male' => 'IsMale',
        'last_name' => 'LastName',
        'mobile_phone' => 'MobilePhone',
        'name' => 'Name',
        'postal_code' => 'PostalCode',
        'class_teacher' => 'ClassTeacher',
        'sort_order' => 'SortOrder',
        'state' => 'State',
        'work_phone' => 'WorkPhone',
        'image_url' => 'ImageUrl',
        'appointments' => 'Appointments',
        'unavailabilities' => 'Unavailabilities',
        'availabilities' => 'Availabilities'
    ];

    /**
     * Array of attributes to setter functions (for deserialization of responses)
     *
     * @var string[]
     */
    protected static $setters = [
        'address' => 'setAddress',
        'appointment_instructor' => 'setAppointmentInstructor',
        'always_allow_double_booking' => 'setAlwaysAllowDoubleBooking',
        'bio' => 'setBio',
        'city' => 'setCity',
        'country' => 'setCountry',
        'email' => 'setEmail',
        'first_name' => 'setFirstName',
        'home_phone' => 'setHomePhone',
        'id' => 'setId',
        'independent_contractor' => 'setIndependentContractor',
        'is_male' => 'setIsMale',
        'last_name' => 'setLastName',
        'mobile_phone' => 'setMobilePhone',
        'name' => 'setName',
        'postal_code' => 'setPostalCode',
        'class_teacher' => 'setClassTeacher',
        'sort_order' => 'setSortOrder',
        'state' => 'setState',
        'work_phone' => 'setWorkPhone',
        'image_url' => 'setImageUrl',
        'appointments' => 'setAppointments',
        'unavailabilities' => 'setUnavailabilities',
        'availabilities' => 'setAvailabilities'
    ];

    /**
     * Array of attributes to getter functions (for serialization of requests)
     *
     * @var string[]
     */
    protected static $getters = [
        'address' => 'getAddress',
        'appointment_instructor' => 'getAppointmentInstructor',
        'always_allow_double_booking' => 'getAlwaysAllowDoubleBooking',
        'bio' => 'getBio',
        'city' => 'getCity',
        'country' => 'getCountry',
        'email' => 'getEmail',
        'first_name' => 'getFirstName',
        'home_phone' => 'getHomePhone',
        'id' => 'getId',
        'independent_contractor' => 'getIndependentContractor',
        'is_male' => 'getIsMale',
        'last_name' => 'getLastName',
        'mobile_phone' => 'getMobilePhone',
        'name' => 'getName',
        'postal_code' => 'getPostalCode',
        'class_teacher' => 'getClassTeacher',
        'sort_order' => 'getSortOrder',
        'state' => 'getState',
        'work_phone' => 'getWorkPhone',
        'image_url' => 'getImageUrl',
        'appointments' => 'getAppointments',
        'unavailabilities' => 'getUnavailabilities',
        'availabilities' => 'getAvailabilities'
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
        $this->container['address'] = isset($data['address']) ? $data['address'] : null;
        $this->container['appointment_instructor'] = isset($data['appointment_instructor']) ? $data['appointment_instructor'] : null;
        $this->container['always_allow_double_booking'] = isset($data['always_allow_double_booking']) ? $data['always_allow_double_booking'] : null;
        $this->container['bio'] = isset($data['bio']) ? $data['bio'] : null;
        $this->container['city'] = isset($data['city']) ? $data['city'] : null;
        $this->container['country'] = isset($data['country']) ? $data['country'] : null;
        $this->container['email'] = isset($data['email']) ? $data['email'] : null;
        $this->container['first_name'] = isset($data['first_name']) ? $data['first_name'] : null;
        $this->container['home_phone'] = isset($data['home_phone']) ? $data['home_phone'] : null;
        $this->container['id'] = isset($data['id']) ? $data['id'] : null;
        $this->container['independent_contractor'] = isset($data['independent_contractor']) ? $data['independent_contractor'] : null;
        $this->container['is_male'] = isset($data['is_male']) ? $data['is_male'] : null;
        $this->container['last_name'] = isset($data['last_name']) ? $data['last_name'] : null;
        $this->container['mobile_phone'] = isset($data['mobile_phone']) ? $data['mobile_phone'] : null;
        $this->container['name'] = isset($data['name']) ? $data['name'] : null;
        $this->container['postal_code'] = isset($data['postal_code']) ? $data['postal_code'] : null;
        $this->container['class_teacher'] = isset($data['class_teacher']) ? $data['class_teacher'] : null;
        $this->container['sort_order'] = isset($data['sort_order']) ? $data['sort_order'] : null;
        $this->container['state'] = isset($data['state']) ? $data['state'] : null;
        $this->container['work_phone'] = isset($data['work_phone']) ? $data['work_phone'] : null;
        $this->container['image_url'] = isset($data['image_url']) ? $data['image_url'] : null;
        $this->container['appointments'] = isset($data['appointments']) ? $data['appointments'] : null;
        $this->container['unavailabilities'] = isset($data['unavailabilities']) ? $data['unavailabilities'] : null;
        $this->container['availabilities'] = isset($data['availabilities']) ? $data['availabilities'] : null;
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
     * Gets address
     *
     * @return string
     */
    public function getAddress()
    {
        return $this->container['address'];
    }

    /**
     * Sets address
     *
     * @param string $address The address of the staff member who is teaching the class.
     *
     * @return $this
     */
    public function setAddress($address)
    {
        $this->container['address'] = $address;

        return $this;
    }

    /**
     * Gets appointment_instructor
     *
     * @return bool
     */
    public function getAppointmentInstructor()
    {
        return $this->container['appointment_instructor'];
    }

    /**
     * Sets appointment_instructor
     *
     * @param bool $appointment_instructor When `true`, indicates that the staff member offers appointments.<br />  When `false`, indicates that the staff member does not offer appointments.
     *
     * @return $this
     */
    public function setAppointmentInstructor($appointment_instructor)
    {
        $this->container['appointment_instructor'] = $appointment_instructor;

        return $this;
    }

    /**
     * Gets always_allow_double_booking
     *
     * @return bool
     */
    public function getAlwaysAllowDoubleBooking()
    {
        return $this->container['always_allow_double_booking'];
    }

    /**
     * Sets always_allow_double_booking
     *
     * @param bool $always_allow_double_booking When `true`, indicates that the staff member can be scheduled for overlapping services.<br />  When `false`, indicates that the staff can only be scheduled for one service at a time in any given time-frame.
     *
     * @return $this
     */
    public function setAlwaysAllowDoubleBooking($always_allow_double_booking)
    {
        $this->container['always_allow_double_booking'] = $always_allow_double_booking;

        return $this;
    }

    /**
     * Gets bio
     *
     * @return string
     */
    public function getBio()
    {
        return $this->container['bio'];
    }

    /**
     * Sets bio
     *
     * @param string $bio The staff member’s biography. This string contains HTML.
     *
     * @return $this
     */
    public function setBio($bio)
    {
        $this->container['bio'] = $bio;

        return $this;
    }

    /**
     * Gets city
     *
     * @return string
     */
    public function getCity()
    {
        return $this->container['city'];
    }

    /**
     * Sets city
     *
     * @param string $city The staff member’s city.
     *
     * @return $this
     */
    public function setCity($city)
    {
        $this->container['city'] = $city;

        return $this;
    }

    /**
     * Gets country
     *
     * @return string
     */
    public function getCountry()
    {
        return $this->container['country'];
    }

    /**
     * Sets country
     *
     * @param string $country The staff member’s country.
     *
     * @return $this
     */
    public function setCountry($country)
    {
        $this->container['country'] = $country;

        return $this;
    }

    /**
     * Gets email
     *
     * @return string
     */
    public function getEmail()
    {
        return $this->container['email'];
    }

    /**
     * Sets email
     *
     * @param string $email The staff member’s email address.
     *
     * @return $this
     */
    public function setEmail($email)
    {
        $this->container['email'] = $email;

        return $this;
    }

    /**
     * Gets first_name
     *
     * @return string
     */
    public function getFirstName()
    {
        return $this->container['first_name'];
    }

    /**
     * Sets first_name
     *
     * @param string $first_name The staff member’s first name.
     *
     * @return $this
     */
    public function setFirstName($first_name)
    {
        $this->container['first_name'] = $first_name;

        return $this;
    }

    /**
     * Gets home_phone
     *
     * @return string
     */
    public function getHomePhone()
    {
        return $this->container['home_phone'];
    }

    /**
     * Sets home_phone
     *
     * @param string $home_phone The staff member’s home phone number.
     *
     * @return $this
     */
    public function setHomePhone($home_phone)
    {
        $this->container['home_phone'] = $home_phone;

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
     * @param int $id The ID assigned to the staff member.
     *
     * @return $this
     */
    public function setId($id)
    {
        $this->container['id'] = $id;

        return $this;
    }

    /**
     * Gets independent_contractor
     *
     * @return bool
     */
    public function getIndependentContractor()
    {
        return $this->container['independent_contractor'];
    }

    /**
     * Sets independent_contractor
     *
     * @param bool $independent_contractor When `true`, indicates that the staff member is an independent contractor.  When `false`, indicates that the staff member is not an independent contractor.
     *
     * @return $this
     */
    public function setIndependentContractor($independent_contractor)
    {
        $this->container['independent_contractor'] = $independent_contractor;

        return $this;
    }

    /**
     * Gets is_male
     *
     * @return bool
     */
    public function getIsMale()
    {
        return $this->container['is_male'];
    }

    /**
     * Sets is_male
     *
     * @param bool $is_male When `true`, indicates that the staff member is male.  When `false`, indicates that the staff member is female.
     *
     * @return $this
     */
    public function setIsMale($is_male)
    {
        $this->container['is_male'] = $is_male;

        return $this;
    }

    /**
     * Gets last_name
     *
     * @return string
     */
    public function getLastName()
    {
        return $this->container['last_name'];
    }

    /**
     * Sets last_name
     *
     * @param string $last_name The staff member’s last name.
     *
     * @return $this
     */
    public function setLastName($last_name)
    {
        $this->container['last_name'] = $last_name;

        return $this;
    }

    /**
     * Gets mobile_phone
     *
     * @return string
     */
    public function getMobilePhone()
    {
        return $this->container['mobile_phone'];
    }

    /**
     * Sets mobile_phone
     *
     * @param string $mobile_phone The staff member’s mobile phone number.
     *
     * @return $this
     */
    public function setMobilePhone($mobile_phone)
    {
        $this->container['mobile_phone'] = $mobile_phone;

        return $this;
    }

    /**
     * Gets name
     *
     * @return string
     */
    public function getName()
    {
        return $this->container['name'];
    }

    /**
     * Sets name
     *
     * @param string $name The staff member’s name.
     *
     * @return $this
     */
    public function setName($name)
    {
        $this->container['name'] = $name;

        return $this;
    }

    /**
     * Gets postal_code
     *
     * @return string
     */
    public function getPostalCode()
    {
        return $this->container['postal_code'];
    }

    /**
     * Sets postal_code
     *
     * @param string $postal_code The staff member’s postal code.
     *
     * @return $this
     */
    public function setPostalCode($postal_code)
    {
        $this->container['postal_code'] = $postal_code;

        return $this;
    }

    /**
     * Gets class_teacher
     *
     * @return bool
     */
    public function getClassTeacher()
    {
        return $this->container['class_teacher'];
    }

    /**
     * Sets class_teacher
     *
     * @param bool $class_teacher When `true`, indicates that the staff member can teach classes.  When `false`, indicates that the staff member cannot teach classes.
     *
     * @return $this
     */
    public function setClassTeacher($class_teacher)
    {
        $this->container['class_teacher'] = $class_teacher;

        return $this;
    }

    /**
     * Gets sort_order
     *
     * @return int
     */
    public function getSortOrder()
    {
        return $this->container['sort_order'];
    }

    /**
     * Sets sort_order
     *
     * @param int $sort_order If configured by the business owner, this field determines a staff member’s weight when sorting. Use this field to sort staff members on your interface.
     *
     * @return $this
     */
    public function setSortOrder($sort_order)
    {
        $this->container['sort_order'] = $sort_order;

        return $this;
    }

    /**
     * Gets state
     *
     * @return string
     */
    public function getState()
    {
        return $this->container['state'];
    }

    /**
     * Sets state
     *
     * @param string $state The staff member’s state.
     *
     * @return $this
     */
    public function setState($state)
    {
        $this->container['state'] = $state;

        return $this;
    }

    /**
     * Gets work_phone
     *
     * @return string
     */
    public function getWorkPhone()
    {
        return $this->container['work_phone'];
    }

    /**
     * Sets work_phone
     *
     * @param string $work_phone The staff member’s work phone number.
     *
     * @return $this
     */
    public function setWorkPhone($work_phone)
    {
        $this->container['work_phone'] = $work_phone;

        return $this;
    }

    /**
     * Gets image_url
     *
     * @return string
     */
    public function getImageUrl()
    {
        return $this->container['image_url'];
    }

    /**
     * Sets image_url
     *
     * @param string $image_url The URL of the staff member’s image, if one has been uploaded.
     *
     * @return $this
     */
    public function setImageUrl($image_url)
    {
        $this->container['image_url'] = $image_url;

        return $this;
    }

    /**
     * Gets appointments
     *
     * @return \Swagger\Client\Model\Appointment[]
     */
    public function getAppointments()
    {
        return $this->container['appointments'];
    }

    /**
     * Sets appointments
     *
     * @param \Swagger\Client\Model\Appointment[] $appointments A list of appointments for the staff.
     *
     * @return $this
     */
    public function setAppointments($appointments)
    {
        $this->container['appointments'] = $appointments;

        return $this;
    }

    /**
     * Gets unavailabilities
     *
     * @return \Swagger\Client\Model\Unavailability[]
     */
    public function getUnavailabilities()
    {
        return $this->container['unavailabilities'];
    }

    /**
     * Sets unavailabilities
     *
     * @param \Swagger\Client\Model\Unavailability[] $unavailabilities A list of unavailabilities for the staff.
     *
     * @return $this
     */
    public function setUnavailabilities($unavailabilities)
    {
        $this->container['unavailabilities'] = $unavailabilities;

        return $this;
    }

    /**
     * Gets availabilities
     *
     * @return \Swagger\Client\Model\Availability[]
     */
    public function getAvailabilities()
    {
        return $this->container['availabilities'];
    }

    /**
     * Sets availabilities
     *
     * @param \Swagger\Client\Model\Availability[] $availabilities A list of availabilities for the staff.
     *
     * @return $this
     */
    public function setAvailabilities($availabilities)
    {
        $this->container['availabilities'] = $availabilities;

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


