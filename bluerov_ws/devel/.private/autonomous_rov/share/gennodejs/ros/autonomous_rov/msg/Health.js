// Auto-generated. Do not edit!

// (in-package autonomous_rov.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Health {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.cpu_used = null;
      this.mem_used = null;
      this.v_batt = null;
      this.i_batt = null;
      this.t_internal = null;
      this.p_internal = null;
      this.sw_1 = null;
      this.sw_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('cpu_used')) {
        this.cpu_used = initObj.cpu_used
      }
      else {
        this.cpu_used = 0.0;
      }
      if (initObj.hasOwnProperty('mem_used')) {
        this.mem_used = initObj.mem_used
      }
      else {
        this.mem_used = 0.0;
      }
      if (initObj.hasOwnProperty('v_batt')) {
        this.v_batt = initObj.v_batt
      }
      else {
        this.v_batt = 0.0;
      }
      if (initObj.hasOwnProperty('i_batt')) {
        this.i_batt = initObj.i_batt
      }
      else {
        this.i_batt = 0.0;
      }
      if (initObj.hasOwnProperty('t_internal')) {
        this.t_internal = initObj.t_internal
      }
      else {
        this.t_internal = 0.0;
      }
      if (initObj.hasOwnProperty('p_internal')) {
        this.p_internal = initObj.p_internal
      }
      else {
        this.p_internal = 0.0;
      }
      if (initObj.hasOwnProperty('sw_1')) {
        this.sw_1 = initObj.sw_1
      }
      else {
        this.sw_1 = false;
      }
      if (initObj.hasOwnProperty('sw_2')) {
        this.sw_2 = initObj.sw_2
      }
      else {
        this.sw_2 = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Health
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [cpu_used]
    bufferOffset = _serializer.float32(obj.cpu_used, buffer, bufferOffset);
    // Serialize message field [mem_used]
    bufferOffset = _serializer.float32(obj.mem_used, buffer, bufferOffset);
    // Serialize message field [v_batt]
    bufferOffset = _serializer.float32(obj.v_batt, buffer, bufferOffset);
    // Serialize message field [i_batt]
    bufferOffset = _serializer.float32(obj.i_batt, buffer, bufferOffset);
    // Serialize message field [t_internal]
    bufferOffset = _serializer.float32(obj.t_internal, buffer, bufferOffset);
    // Serialize message field [p_internal]
    bufferOffset = _serializer.float32(obj.p_internal, buffer, bufferOffset);
    // Serialize message field [sw_1]
    bufferOffset = _serializer.bool(obj.sw_1, buffer, bufferOffset);
    // Serialize message field [sw_2]
    bufferOffset = _serializer.bool(obj.sw_2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Health
    let len;
    let data = new Health(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [cpu_used]
    data.cpu_used = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [mem_used]
    data.mem_used = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [v_batt]
    data.v_batt = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [i_batt]
    data.i_batt = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [t_internal]
    data.t_internal = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [p_internal]
    data.p_internal = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [sw_1]
    data.sw_1 = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [sw_2]
    data.sw_2 = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 26;
  }

  static datatype() {
    // Returns string type for a message object
    return 'autonomous_rov/Health';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3759c570a6250d1aa85350125e6ecdda';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header    header
    float32   cpu_used    # percent cpu utilization
    float32   mem_used    # percent memory used
    float32   v_batt      # volts
    float32   i_batt      # amps
    float32   t_internal  # degrees C
    float32   p_internal  # Pa
    bool      sw_1        # on/off
    bool      sw_2        # on/off
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Health(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.cpu_used !== undefined) {
      resolved.cpu_used = msg.cpu_used;
    }
    else {
      resolved.cpu_used = 0.0
    }

    if (msg.mem_used !== undefined) {
      resolved.mem_used = msg.mem_used;
    }
    else {
      resolved.mem_used = 0.0
    }

    if (msg.v_batt !== undefined) {
      resolved.v_batt = msg.v_batt;
    }
    else {
      resolved.v_batt = 0.0
    }

    if (msg.i_batt !== undefined) {
      resolved.i_batt = msg.i_batt;
    }
    else {
      resolved.i_batt = 0.0
    }

    if (msg.t_internal !== undefined) {
      resolved.t_internal = msg.t_internal;
    }
    else {
      resolved.t_internal = 0.0
    }

    if (msg.p_internal !== undefined) {
      resolved.p_internal = msg.p_internal;
    }
    else {
      resolved.p_internal = 0.0
    }

    if (msg.sw_1 !== undefined) {
      resolved.sw_1 = msg.sw_1;
    }
    else {
      resolved.sw_1 = false
    }

    if (msg.sw_2 !== undefined) {
      resolved.sw_2 = msg.sw_2;
    }
    else {
      resolved.sw_2 = false
    }

    return resolved;
    }
};

module.exports = Health;
