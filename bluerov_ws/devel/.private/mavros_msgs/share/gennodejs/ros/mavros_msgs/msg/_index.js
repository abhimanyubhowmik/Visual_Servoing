
"use strict";

let HilActuatorControls = require('./HilActuatorControls.js');
let RTCM = require('./RTCM.js');
let DebugValue = require('./DebugValue.js');
let HilGPS = require('./HilGPS.js');
let RadioStatus = require('./RadioStatus.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let Param = require('./Param.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let RCOut = require('./RCOut.js');
let BatteryStatus = require('./BatteryStatus.js');
let VFR_HUD = require('./VFR_HUD.js');
let Mavlink = require('./Mavlink.js');
let Tunnel = require('./Tunnel.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let ParamValue = require('./ParamValue.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let LandingTarget = require('./LandingTarget.js');
let RTKBaseline = require('./RTKBaseline.js');
let ManualControl = require('./ManualControl.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let VehicleInfo = require('./VehicleInfo.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let HilSensor = require('./HilSensor.js');
let LogEntry = require('./LogEntry.js');
let StatusText = require('./StatusText.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let ESCInfo = require('./ESCInfo.js');
let State = require('./State.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let ExtendedState = require('./ExtendedState.js');
let ActuatorControl = require('./ActuatorControl.js');
let WaypointList = require('./WaypointList.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let HilControls = require('./HilControls.js');
let Thrust = require('./Thrust.js');
let MountControl = require('./MountControl.js');
let Altitude = require('./Altitude.js');
let RCIn = require('./RCIn.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let TerrainReport = require('./TerrainReport.js');
let GPSINPUT = require('./GPSINPUT.js');
let GPSRAW = require('./GPSRAW.js');
let FileEntry = require('./FileEntry.js');
let GPSRTK = require('./GPSRTK.js');
let ESCStatus = require('./ESCStatus.js');
let Waypoint = require('./Waypoint.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let CommandCode = require('./CommandCode.js');
let WaypointReached = require('./WaypointReached.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let Trajectory = require('./Trajectory.js');
let PositionTarget = require('./PositionTarget.js');
let Vibration = require('./Vibration.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let HomePosition = require('./HomePosition.js');
let LogData = require('./LogData.js');

module.exports = {
  HilActuatorControls: HilActuatorControls,
  RTCM: RTCM,
  DebugValue: DebugValue,
  HilGPS: HilGPS,
  RadioStatus: RadioStatus,
  MagnetometerReporter: MagnetometerReporter,
  Param: Param,
  WheelOdomStamped: WheelOdomStamped,
  ESCStatusItem: ESCStatusItem,
  RCOut: RCOut,
  BatteryStatus: BatteryStatus,
  VFR_HUD: VFR_HUD,
  Mavlink: Mavlink,
  Tunnel: Tunnel,
  ESCTelemetry: ESCTelemetry,
  ParamValue: ParamValue,
  ADSBVehicle: ADSBVehicle,
  OpticalFlowRad: OpticalFlowRad,
  HilStateQuaternion: HilStateQuaternion,
  LandingTarget: LandingTarget,
  RTKBaseline: RTKBaseline,
  ManualControl: ManualControl,
  GlobalPositionTarget: GlobalPositionTarget,
  VehicleInfo: VehicleInfo,
  ESCInfoItem: ESCInfoItem,
  HilSensor: HilSensor,
  LogEntry: LogEntry,
  StatusText: StatusText,
  AttitudeTarget: AttitudeTarget,
  CameraImageCaptured: CameraImageCaptured,
  ESCInfo: ESCInfo,
  State: State,
  CamIMUStamp: CamIMUStamp,
  ExtendedState: ExtendedState,
  ActuatorControl: ActuatorControl,
  WaypointList: WaypointList,
  NavControllerOutput: NavControllerOutput,
  PlayTuneV2: PlayTuneV2,
  HilControls: HilControls,
  Thrust: Thrust,
  MountControl: MountControl,
  Altitude: Altitude,
  RCIn: RCIn,
  CompanionProcessStatus: CompanionProcessStatus,
  TerrainReport: TerrainReport,
  GPSINPUT: GPSINPUT,
  GPSRAW: GPSRAW,
  FileEntry: FileEntry,
  GPSRTK: GPSRTK,
  ESCStatus: ESCStatus,
  Waypoint: Waypoint,
  TimesyncStatus: TimesyncStatus,
  OverrideRCIn: OverrideRCIn,
  CommandCode: CommandCode,
  WaypointReached: WaypointReached,
  ESCTelemetryItem: ESCTelemetryItem,
  Trajectory: Trajectory,
  PositionTarget: PositionTarget,
  Vibration: Vibration,
  EstimatorStatus: EstimatorStatus,
  OnboardComputerStatus: OnboardComputerStatus,
  HomePosition: HomePosition,
  LogData: LogData,
};
