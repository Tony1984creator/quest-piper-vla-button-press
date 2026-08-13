# Data contract and evaluation split

## Recorded schema

| Field | Shape / modality | Contract |
| --- | --- | --- |
| `observation.images.up` | RGB video, 640x480 | External/top-facing view recorded at the episode frame rate. |
| `observation.images.wrist` | RGB video, 640x480 | Wrist view used by visual pre-annotation. |
| `observation.state` | 7D | Six arm joints plus gripper, stored in degrees. |
| `action` | 7D | Demonstrator command aligned to the state convention, stored in degrees. |
| metadata | episode/frame index and capture details | Must remain linkable at episode granularity. |

The public evidence snapshot contains 40 episodes and 14,653 frames at 30 FPS. Raw videos, labels, and metadata records are not committed here.

## Unit boundary

The project uses a strict unit convention:

```text
LeRobot storage / training loader: degrees
kinematic/model computation boundary: degrees -> radians (once)
IK, FK, Jacobian, dynamics, loss geometry: radians
```

Avoid chained loaders that convert the same signal twice. Each experiment should record the conversion owner and assert expected numerical ranges immediately after conversion.

## Split policy

Do not randomly split individual frames. Nearby frames in one trajectory are strongly correlated and would leak motion context across splits. The planned split is by complete episode:

1. freeze a seeded episode-level train/validation/test assignment;
2. publish only split IDs or a salted manifest where data disclosure is restricted;
3. select models by validation results;
4. use the held-out episodes once for the final open-loop/closed-loop report.

## Stage and outcome labels

Visual pre-annotation records a candidate `press_confirmed_visual` stage. It does not establish that the requested floor was selected, that the robot performed the contact, or that the task succeeded.

The closed-loop protocol requires human-reviewed labels:

| Label | Meaning |
| --- | --- |
| `success` | Requested button was pressed under the defined task criterion. |
| `failure_reason` | Controlled taxonomy, e.g. perception, approach, contact, retraction, safety stop, or operator abort. |
| `task_stage` | At minimum: approach, contact, visual confirmation, retraction. |

This distinction prevents a convenient visual signal from being promoted into an unsupported success metric.
