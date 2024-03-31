
"use strict";

let FileChecksum = require('./FileChecksum.js')
let ParamGet = require('./ParamGet.js')
let ParamPush = require('./ParamPush.js')
let FileOpen = require('./FileOpen.js')
let FileRename = require('./FileRename.js')
let MessageInterval = require('./MessageInterval.js')
let CommandBool = require('./CommandBool.js')
let ParamSet = require('./ParamSet.js')
let SetMode = require('./SetMode.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let FileRead = require('./FileRead.js')
let ParamPull = require('./ParamPull.js')
let MountConfigure = require('./MountConfigure.js')
let CommandHome = require('./CommandHome.js')
let CommandInt = require('./CommandInt.js')
let FileClose = require('./FileClose.js')
let FileTruncate = require('./FileTruncate.js')
let FileWrite = require('./FileWrite.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let WaypointClear = require('./WaypointClear.js')
let LogRequestData = require('./LogRequestData.js')
let LogRequestList = require('./LogRequestList.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let FileRemove = require('./FileRemove.js')
let SetMavFrame = require('./SetMavFrame.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let FileMakeDir = require('./FileMakeDir.js')
let WaypointPull = require('./WaypointPull.js')
let WaypointPush = require('./WaypointPush.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let StreamRate = require('./StreamRate.js')
let FileList = require('./FileList.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let CommandLong = require('./CommandLong.js')
let CommandTOL = require('./CommandTOL.js')
let CommandAck = require('./CommandAck.js')

module.exports = {
  FileChecksum: FileChecksum,
  ParamGet: ParamGet,
  ParamPush: ParamPush,
  FileOpen: FileOpen,
  FileRename: FileRename,
  MessageInterval: MessageInterval,
  CommandBool: CommandBool,
  ParamSet: ParamSet,
  SetMode: SetMode,
  CommandTriggerInterval: CommandTriggerInterval,
  FileRead: FileRead,
  ParamPull: ParamPull,
  MountConfigure: MountConfigure,
  CommandHome: CommandHome,
  CommandInt: CommandInt,
  FileClose: FileClose,
  FileTruncate: FileTruncate,
  FileWrite: FileWrite,
  FileRemoveDir: FileRemoveDir,
  WaypointClear: WaypointClear,
  LogRequestData: LogRequestData,
  LogRequestList: LogRequestList,
  CommandTriggerControl: CommandTriggerControl,
  FileRemove: FileRemove,
  SetMavFrame: SetMavFrame,
  WaypointSetCurrent: WaypointSetCurrent,
  LogRequestEnd: LogRequestEnd,
  FileMakeDir: FileMakeDir,
  WaypointPull: WaypointPull,
  WaypointPush: WaypointPush,
  CommandVtolTransition: CommandVtolTransition,
  StreamRate: StreamRate,
  FileList: FileList,
  VehicleInfoGet: VehicleInfoGet,
  CommandLong: CommandLong,
  CommandTOL: CommandTOL,
  CommandAck: CommandAck,
};
