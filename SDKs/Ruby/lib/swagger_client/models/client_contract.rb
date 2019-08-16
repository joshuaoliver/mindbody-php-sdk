=begin
#MINDBODY Public API

#No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

OpenAPI spec version: v6

Generated by: https://github.com/swagger-api/swagger-codegen.git
Swagger Codegen version: 2.4.6

=end

require 'date'

module SwaggerClient
  # A client contract
  class ClientContract
    # The date on which the contract was signed.
    attr_accessor :agreement_date

    # The status of the client’s autopay.
    attr_accessor :autopay_status

    # The name of the contract.
    attr_accessor :contract_name

    # The date that the contract expires.
    attr_accessor :end_date

    # The unique ID of the contract.
    attr_accessor :id

    # The ID of the location where the contract was issued.
    attr_accessor :origination_location_id

    # The date that the contract became active.
    attr_accessor :start_date

    # The ID of the site where the contract was issued.
    attr_accessor :site_id

    # Contains details of the autopay events.
    attr_accessor :upcoming_autopay_events

    class EnumAttributeValidator
      attr_reader :datatype
      attr_reader :allowable_values

      def initialize(datatype, allowable_values)
        @allowable_values = allowable_values.map do |value|
          case datatype.to_s
          when /Integer/i
            value.to_i
          when /Float/i
            value.to_f
          else
            value
          end
        end
      end

      def valid?(value)
        !value || allowable_values.include?(value)
      end
    end

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'agreement_date' => :'AgreementDate',
        :'autopay_status' => :'AutopayStatus',
        :'contract_name' => :'ContractName',
        :'end_date' => :'EndDate',
        :'id' => :'Id',
        :'origination_location_id' => :'OriginationLocationId',
        :'start_date' => :'StartDate',
        :'site_id' => :'SiteId',
        :'upcoming_autopay_events' => :'UpcomingAutopayEvents'
      }
    end

    # Attribute type mapping.
    def self.swagger_types
      {
        :'agreement_date' => :'DateTime',
        :'autopay_status' => :'String',
        :'contract_name' => :'String',
        :'end_date' => :'DateTime',
        :'id' => :'Integer',
        :'origination_location_id' => :'Integer',
        :'start_date' => :'DateTime',
        :'site_id' => :'Integer',
        :'upcoming_autopay_events' => :'Array<UpcomingAutopayEvent>'
      }
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      return unless attributes.is_a?(Hash)

      # convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h| h[k.to_sym] = v }

      if attributes.has_key?(:'AgreementDate')
        self.agreement_date = attributes[:'AgreementDate']
      end

      if attributes.has_key?(:'AutopayStatus')
        self.autopay_status = attributes[:'AutopayStatus']
      end

      if attributes.has_key?(:'ContractName')
        self.contract_name = attributes[:'ContractName']
      end

      if attributes.has_key?(:'EndDate')
        self.end_date = attributes[:'EndDate']
      end

      if attributes.has_key?(:'Id')
        self.id = attributes[:'Id']
      end

      if attributes.has_key?(:'OriginationLocationId')
        self.origination_location_id = attributes[:'OriginationLocationId']
      end

      if attributes.has_key?(:'StartDate')
        self.start_date = attributes[:'StartDate']
      end

      if attributes.has_key?(:'SiteId')
        self.site_id = attributes[:'SiteId']
      end

      if attributes.has_key?(:'UpcomingAutopayEvents')
        if (value = attributes[:'UpcomingAutopayEvents']).is_a?(Array)
          self.upcoming_autopay_events = value
        end
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      autopay_status_validator = EnumAttributeValidator.new('String', ['Active', 'Inactive', 'Suspended'])
      return false unless autopay_status_validator.valid?(@autopay_status)
      true
    end

    # Custom attribute writer method checking allowed values (enum).
    # @param [Object] autopay_status Object to be assigned
    def autopay_status=(autopay_status)
      validator = EnumAttributeValidator.new('String', ['Active', 'Inactive', 'Suspended'])
      unless validator.valid?(autopay_status)
        fail ArgumentError, 'invalid value for "autopay_status", must be one of #{validator.allowable_values}.'
      end
      @autopay_status = autopay_status
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          agreement_date == o.agreement_date &&
          autopay_status == o.autopay_status &&
          contract_name == o.contract_name &&
          end_date == o.end_date &&
          id == o.id &&
          origination_location_id == o.origination_location_id &&
          start_date == o.start_date &&
          site_id == o.site_id &&
          upcoming_autopay_events == o.upcoming_autopay_events
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Fixnum] Hash code
    def hash
      [agreement_date, autopay_status, contract_name, end_date, id, origination_location_id, start_date, site_id, upcoming_autopay_events].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.swagger_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :BOOLEAN
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        temp_model = SwaggerClient.const_get(type).new
        temp_model.build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        next if value.nil?
        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end
  end
end
