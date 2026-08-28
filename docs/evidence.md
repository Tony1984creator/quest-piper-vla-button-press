# Portfolio evidence index

This portfolio is organized for a research reviewer who needs to distinguish practical ownership from an overstated robotics claim.

| Capability | What was solved | Evidence level | Concise interview framing |
| --- | --- | --- | --- |
| Robot systems | Isolated a private command owner and a reject-first safety boundary across VR, ROS 2, IK, and robot transport. | Systems integration | I treated teleoperation as a time-sensitive systems problem, not just a pose-mapping demo. |
| Robot data | Made units, complete-episode splitting, stream alignment, and frame indexing explicit. | Offline probe | I made the collected data auditable before comparing policies. |
| VLA / JEPA | Converted a teacher upgrade into strict loading, tensor, gradient, and pilot-loss checks. | Offline probe | I separated compatibility evidence from a model-performance claim. |
| Deployment reasoning | Audited action dimensions/chunks and isolated fixed-protocol loss from endpoint timing. | Offline probe | I state what a metric measures before using it to make a systems decision. |
| Computer vision | Built a conservative video-review cue and discarded a brittle identity shortcut. | Offline probe | I used vision to triage labels, while retaining human outcome verification. |

The result is an evidence chain: **collect safely → validate data → compare models fairly → constrain output → verify outcomes separately**. Current acceptance gates are in the [roadmap](roadmap/README.md).

