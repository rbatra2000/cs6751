
"use strict";

let TorqueEnable = require('./TorqueEnable.js')
let RobotInfo = require('./RobotInfo.js')
let RegisterValues = require('./RegisterValues.js')
let MotorGains = require('./MotorGains.js')
let Reboot = require('./Reboot.js')
let OperatingModes = require('./OperatingModes.js')

module.exports = {
  TorqueEnable: TorqueEnable,
  RobotInfo: RobotInfo,
  RegisterValues: RegisterValues,
  MotorGains: MotorGains,
  Reboot: Reboot,
  OperatingModes: OperatingModes,
};
