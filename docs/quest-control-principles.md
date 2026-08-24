# Quest control principles

## Scope

These principles summarize the verified Quest–Piper engineering contract without
publishing launch commands, device identifiers, controller gains, network
details, or robot configuration. They are not a substitute for a site-specific
safety review or an operating procedure.

## One actuator owner

Only one guarded actuation process may own a physical-arm channel. Quest input,
ROS 2 transport, recording, model inference, and evaluation generate or observe
candidate data; none may open a competing SDK/CAN channel.

This rule applies independently to each arm in a future dual-arm system. It is
not safe to copy a single-arm Piper process or CAN configuration directly into
a NERO setup.

## Deliberate modes

| Mode | Permitted behavior | Prohibited behavior |
| --- | --- | --- |
| Dry path | Read Quest input, map pose, run IK, publish candidate commands | Enabling an arm or owning a hardware channel |
| Guarded evaluation | A separately authorized actuator consumes fresh, valid candidates | Bypassing limits, freshness checks, or an operator abort |
| Recording | Observe named command and measured-state streams at a declared rate | Running IK twice, writing hardware, or assuming image provenance |
| Offline policy probe | Produce and inspect candidate actions | Treating tensor output as permission to actuate |

## Hold-to-enable and re-anchoring

Teleoperation uses an explicit hold-to-enable gate. A new target is generated
only while the gate is deliberately held and tracking is current. Releasing the
gate holds the last safe target; it does not extrapolate from a stale pose.
After a tracking interruption, re-establish a stable controller reference before
generating another target.

A separate deliberate combination is required for a home/reset request. Home
motion and task motion are never inferred from ordinary tracking input.

## Tracking, time, and faults

Tracking freshness, command freshness, measured state, limits, and actuator
health are first-class safety signals. Loss of tracking, a stale command,
invalid state, a transport fault, or an operator abort stops **new** candidate
generation. The event and its timestamps belong in the private trial record.

The response is not to enlarge discontinuity thresholds or continue from an
old pose. Diagnose the failure at the input, ROS 2, IK, supervisor, and
actuator boundary before a repeat.

## Data ownership and units

The recorder observes explicitly named command and measured-state streams,
checks type/order, and writes at a declared fixed rate. Image-source provenance
is a separate contract. For Quest/LeRobot data, state/action unit conversion has
one declared owner; model, kinematics, and physical-client conventions must not
silently duplicate conversion.

## Evidence ladder

Import checks, unit tests, dry-path mapping, training smoke, offline replay,
and visual pre-annotation make bounded claims. A physical task-success claim
requires a guarded trial protocol, reviewed evidence, explicit
success/failure/stage labels, and an operator-authorized record.
