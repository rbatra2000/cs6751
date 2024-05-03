// Auto-generated. Do not edit!

// (in-package interbotix_xs_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ArmJoy {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ee_x_cmd = null;
      this.ee_y_cmd = null;
      this.ee_z_cmd = null;
      this.ee_roll_cmd = null;
      this.ee_pitch_cmd = null;
      this.waist_cmd = null;
      this.gripper_cmd = null;
      this.pose_cmd = null;
      this.speed_cmd = null;
      this.speed_toggle_cmd = null;
      this.gripper_pwm_cmd = null;
      this.torque_cmd = null;
    }
    else {
      if (initObj.hasOwnProperty('ee_x_cmd')) {
        this.ee_x_cmd = initObj.ee_x_cmd
      }
      else {
        this.ee_x_cmd = 0;
      }
      if (initObj.hasOwnProperty('ee_y_cmd')) {
        this.ee_y_cmd = initObj.ee_y_cmd
      }
      else {
        this.ee_y_cmd = 0;
      }
      if (initObj.hasOwnProperty('ee_z_cmd')) {
        this.ee_z_cmd = initObj.ee_z_cmd
      }
      else {
        this.ee_z_cmd = 0;
      }
      if (initObj.hasOwnProperty('ee_roll_cmd')) {
        this.ee_roll_cmd = initObj.ee_roll_cmd
      }
      else {
        this.ee_roll_cmd = 0;
      }
      if (initObj.hasOwnProperty('ee_pitch_cmd')) {
        this.ee_pitch_cmd = initObj.ee_pitch_cmd
      }
      else {
        this.ee_pitch_cmd = 0;
      }
      if (initObj.hasOwnProperty('waist_cmd')) {
        this.waist_cmd = initObj.waist_cmd
      }
      else {
        this.waist_cmd = 0;
      }
      if (initObj.hasOwnProperty('gripper_cmd')) {
        this.gripper_cmd = initObj.gripper_cmd
      }
      else {
        this.gripper_cmd = 0;
      }
      if (initObj.hasOwnProperty('pose_cmd')) {
        this.pose_cmd = initObj.pose_cmd
      }
      else {
        this.pose_cmd = 0;
      }
      if (initObj.hasOwnProperty('speed_cmd')) {
        this.speed_cmd = initObj.speed_cmd
      }
      else {
        this.speed_cmd = 0;
      }
      if (initObj.hasOwnProperty('speed_toggle_cmd')) {
        this.speed_toggle_cmd = initObj.speed_toggle_cmd
      }
      else {
        this.speed_toggle_cmd = 0;
      }
      if (initObj.hasOwnProperty('gripper_pwm_cmd')) {
        this.gripper_pwm_cmd = initObj.gripper_pwm_cmd
      }
      else {
        this.gripper_pwm_cmd = 0;
      }
      if (initObj.hasOwnProperty('torque_cmd')) {
        this.torque_cmd = initObj.torque_cmd
      }
      else {
        this.torque_cmd = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ArmJoy
    // Serialize message field [ee_x_cmd]
    bufferOffset = _serializer.int8(obj.ee_x_cmd, buffer, bufferOffset);
    // Serialize message field [ee_y_cmd]
    bufferOffset = _serializer.int8(obj.ee_y_cmd, buffer, bufferOffset);
    // Serialize message field [ee_z_cmd]
    bufferOffset = _serializer.int8(obj.ee_z_cmd, buffer, bufferOffset);
    // Serialize message field [ee_roll_cmd]
    bufferOffset = _serializer.int8(obj.ee_roll_cmd, buffer, bufferOffset);
    // Serialize message field [ee_pitch_cmd]
    bufferOffset = _serializer.int8(obj.ee_pitch_cmd, buffer, bufferOffset);
    // Serialize message field [waist_cmd]
    bufferOffset = _serializer.int8(obj.waist_cmd, buffer, bufferOffset);
    // Serialize message field [gripper_cmd]
    bufferOffset = _serializer.int8(obj.gripper_cmd, buffer, bufferOffset);
    // Serialize message field [pose_cmd]
    bufferOffset = _serializer.int8(obj.pose_cmd, buffer, bufferOffset);
    // Serialize message field [speed_cmd]
    bufferOffset = _serializer.int8(obj.speed_cmd, buffer, bufferOffset);
    // Serialize message field [speed_toggle_cmd]
    bufferOffset = _serializer.int8(obj.speed_toggle_cmd, buffer, bufferOffset);
    // Serialize message field [gripper_pwm_cmd]
    bufferOffset = _serializer.int8(obj.gripper_pwm_cmd, buffer, bufferOffset);
    // Serialize message field [torque_cmd]
    bufferOffset = _serializer.int8(obj.torque_cmd, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ArmJoy
    let len;
    let data = new ArmJoy(null);
    // Deserialize message field [ee_x_cmd]
    data.ee_x_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [ee_y_cmd]
    data.ee_y_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [ee_z_cmd]
    data.ee_z_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [ee_roll_cmd]
    data.ee_roll_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [ee_pitch_cmd]
    data.ee_pitch_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [waist_cmd]
    data.waist_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [gripper_cmd]
    data.gripper_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [pose_cmd]
    data.pose_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [speed_cmd]
    data.speed_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [speed_toggle_cmd]
    data.speed_toggle_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [gripper_pwm_cmd]
    data.gripper_pwm_cmd = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [torque_cmd]
    data.torque_cmd = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'interbotix_xs_msgs/ArmJoy';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '09eb0cc37cce12e41a0f984f2c2f53cd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # This message is used specifically in the interbotix_xsarm_joy package
    #
    # Maps raw 'joy' commands to more specific ones to control an Interbotix manipulator
    
    # enum values that define the joystick controls for the robot
    
    #########################################################################################################
    
    # Control the motion of the virtual 'ee_gripper_link' or end effector using the modern_robotics_ik engine
    # Position Control
    int8 EE_X_INC = 1
    int8 EE_X_DEC = 2
    int8 EE_Y_INC = 3
    int8 EE_Y_DEC = 4
    int8 EE_Z_INC = 5
    int8 EE_Z_DEC = 6
    
    # Orientation Control
    int8 EE_ROLL_CCW = 7
    int8 EE_ROLL_CW = 8
    int8 EE_PITCH_UP = 9
    int8 EE_PITCH_DOWN = 10
    
    #########################################################################################################
    
    # Control the motion of independent joints on the Arm or send predefined robot poses
    # Waist Joint Control
    int8 WAIST_CCW = 11
    int8 WAIST_CW = 12
    
    # Gripper Control
    int8 GRIPPER_OPEN = 13
    int8 GRIPPER_CLOSE = 14
    
    # Pose Control
    int8 HOME_POSE = 15
    int8 SLEEP_POSE = 16
    
    #########################################################################################################
    
    # Customize configurations for the Interbotix Arm
    # Inc/Dec Joint speed
    int8 SPEED_INC = 17
    int8 SPEED_DEC = 18
    
    # Quickly toggle between a fast and slow speed setting
    int8 SPEED_COURSE = 19
    int8 SPEED_FINE = 20
    
    # Inc/Dec Gripper pressure
    int8 GRIPPER_PWM_INC = 21
    int8 GRIPPER_PWM_DEC = 22
    
    # Torque On/Off all servos
    int8 TORQUE_ON = 23
    int8 TORQUE_OFF = 24
    
    #########################################################################################################
    
    # Control the motion of the Interbotix Arm
    int8 ee_x_cmd
    int8 ee_y_cmd
    int8 ee_z_cmd
    int8 ee_roll_cmd
    int8 ee_pitch_cmd
    
    # Independent Joint/Pose Control
    int8 waist_cmd
    int8 gripper_cmd
    int8 pose_cmd
    
    # Misc. Configs
    int8 speed_cmd
    int8 speed_toggle_cmd
    int8 gripper_pwm_cmd
    int8 torque_cmd
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ArmJoy(null);
    if (msg.ee_x_cmd !== undefined) {
      resolved.ee_x_cmd = msg.ee_x_cmd;
    }
    else {
      resolved.ee_x_cmd = 0
    }

    if (msg.ee_y_cmd !== undefined) {
      resolved.ee_y_cmd = msg.ee_y_cmd;
    }
    else {
      resolved.ee_y_cmd = 0
    }

    if (msg.ee_z_cmd !== undefined) {
      resolved.ee_z_cmd = msg.ee_z_cmd;
    }
    else {
      resolved.ee_z_cmd = 0
    }

    if (msg.ee_roll_cmd !== undefined) {
      resolved.ee_roll_cmd = msg.ee_roll_cmd;
    }
    else {
      resolved.ee_roll_cmd = 0
    }

    if (msg.ee_pitch_cmd !== undefined) {
      resolved.ee_pitch_cmd = msg.ee_pitch_cmd;
    }
    else {
      resolved.ee_pitch_cmd = 0
    }

    if (msg.waist_cmd !== undefined) {
      resolved.waist_cmd = msg.waist_cmd;
    }
    else {
      resolved.waist_cmd = 0
    }

    if (msg.gripper_cmd !== undefined) {
      resolved.gripper_cmd = msg.gripper_cmd;
    }
    else {
      resolved.gripper_cmd = 0
    }

    if (msg.pose_cmd !== undefined) {
      resolved.pose_cmd = msg.pose_cmd;
    }
    else {
      resolved.pose_cmd = 0
    }

    if (msg.speed_cmd !== undefined) {
      resolved.speed_cmd = msg.speed_cmd;
    }
    else {
      resolved.speed_cmd = 0
    }

    if (msg.speed_toggle_cmd !== undefined) {
      resolved.speed_toggle_cmd = msg.speed_toggle_cmd;
    }
    else {
      resolved.speed_toggle_cmd = 0
    }

    if (msg.gripper_pwm_cmd !== undefined) {
      resolved.gripper_pwm_cmd = msg.gripper_pwm_cmd;
    }
    else {
      resolved.gripper_pwm_cmd = 0
    }

    if (msg.torque_cmd !== undefined) {
      resolved.torque_cmd = msg.torque_cmd;
    }
    else {
      resolved.torque_cmd = 0
    }

    return resolved;
    }
};

// Constants for message
ArmJoy.Constants = {
  EE_X_INC: 1,
  EE_X_DEC: 2,
  EE_Y_INC: 3,
  EE_Y_DEC: 4,
  EE_Z_INC: 5,
  EE_Z_DEC: 6,
  EE_ROLL_CCW: 7,
  EE_ROLL_CW: 8,
  EE_PITCH_UP: 9,
  EE_PITCH_DOWN: 10,
  WAIST_CCW: 11,
  WAIST_CW: 12,
  GRIPPER_OPEN: 13,
  GRIPPER_CLOSE: 14,
  HOME_POSE: 15,
  SLEEP_POSE: 16,
  SPEED_INC: 17,
  SPEED_DEC: 18,
  SPEED_COURSE: 19,
  SPEED_FINE: 20,
  GRIPPER_PWM_INC: 21,
  GRIPPER_PWM_DEC: 22,
  TORQUE_ON: 23,
  TORQUE_OFF: 24,
}

module.exports = ArmJoy;
