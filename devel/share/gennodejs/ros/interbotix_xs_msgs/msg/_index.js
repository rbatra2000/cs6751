
"use strict";

let ArmJoy = require('./ArmJoy.js');
let JointTrajectoryCommand = require('./JointTrajectoryCommand.js');
let LocobotJoy = require('./LocobotJoy.js');
let JointSingleCommand = require('./JointSingleCommand.js');
let JointTemps = require('./JointTemps.js');
let JointGroupCommand = require('./JointGroupCommand.js');
let HexJoy = require('./HexJoy.js');
let TurretJoy = require('./TurretJoy.js');

module.exports = {
  ArmJoy: ArmJoy,
  JointTrajectoryCommand: JointTrajectoryCommand,
  LocobotJoy: LocobotJoy,
  JointSingleCommand: JointSingleCommand,
  JointTemps: JointTemps,
  JointGroupCommand: JointGroupCommand,
  HexJoy: HexJoy,
  TurretJoy: TurretJoy,
};
