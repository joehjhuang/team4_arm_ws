// Auto-generated. Do not edit!

// (in-package a_b_action_server.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class a_bFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.moved_distance = null;
    }
    else {
      if (initObj.hasOwnProperty('moved_distance')) {
        this.moved_distance = initObj.moved_distance
      }
      else {
        this.moved_distance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type a_bFeedback
    // Serialize message field [moved_distance]
    bufferOffset = _serializer.float32(obj.moved_distance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type a_bFeedback
    let len;
    let data = new a_bFeedback(null);
    // Deserialize message field [moved_distance]
    data.moved_distance = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'a_b_action_server/a_bFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7b76df385ed63be519f1a18aa757604d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    float32 moved_distance
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new a_bFeedback(null);
    if (msg.moved_distance !== undefined) {
      resolved.moved_distance = msg.moved_distance;
    }
    else {
      resolved.moved_distance = 0.0
    }

    return resolved;
    }
};

module.exports = a_bFeedback;
