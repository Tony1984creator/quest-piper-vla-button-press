# Quest control principles

## One actuator owner

The component that interfaces with the physical arm is a single guarded
actuation process. VR input, ROS 2 transport, recording, model inference, and
evaluation code must not open a competing control channel.

## Separate candidate generation from actuation

Teleoperation and learned policies generate candidate commands. A supervisor
checks freshness, measured state, authorization, limits, and abort conditions
before the actuator may use them. This makes offline inference and dry-path
tests non-actuating by default.

## Treat tracking and time as safety signals

A command is invalid when its source has stopped updating, tracking is lost, or
its timestamp falls outside the allowed freshness window. The correct response
is to stop generating new targets and keep a safe state, not to extrapolate
from the last pose.

## Make data ownership explicit

The VR recording adapter observes named seven-dimensional command and
measured-state streams. It validates ordering and type, writes the dataset at a
fixed rate, and does not execute IK or control the robot. Image provenance is
tracked separately from joint-stream recording.

## Keep unit boundaries singular and testable

For the Quest/LeRobot corpus, state and action are stored in degrees.
Kinematic or model computation converts degrees to radians once at its declared
boundary. The physical Piper client has a separate interface convention for its
active joint and gripper dimensions; that convention must be validated
explicitly rather than assumed to match a model tensor.

## Evidence ladder before closed loop

Import checks, shape checks, unit tests, smoke steps, pilot training, and
offline replay each establish limited claims. A real-robot success claim
requires a guarded trial protocol, reviewed video, and explicit
success/failure/stage labels.
