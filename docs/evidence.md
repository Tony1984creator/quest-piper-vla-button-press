# Portfolio evidence index

This portfolio is organized for a research reviewer who needs to distinguish practical ownership from an overstated robotics claim.

| Capability | What was solved | Evidence level | Concise interview framing |
| --- | --- | --- | --- |
| Robot systems | Isolated a private command owner and a reject-first safety boundary across VR, ROS 2, IK, and robot transport. | Systems integration | I treated teleoperation as a time-sensitive systems problem, not just a pose-mapping demo. |
| Quest VR data | Made units, complete-episode splitting, stream alignment, and frame indexing explicit for a 40-episode LeRobot asset. | Offline probe | I made the collected VR data auditable before comparing policies. |
| Elevator VLA data | Kept the 952-episode VLA experiment asset separate from Quest VR data and used it for model/vision aggregates. | Offline probe | I prevent dataset identity from becoming an untracked experimental variable. |
| VLA / JEPA | Converted a teacher upgrade into strict loading, tensor, gradient, and pilot-loss checks. | Offline probe | I separated compatibility evidence from a model-performance claim. |
| Deployment reasoning | Audited action dimensions/chunks and isolated fixed-protocol loss from endpoint timing. | Offline probe | I state what a metric measures before using it to make a systems decision. |
| Computer vision | Built a conservative video-review cue and discarded a brittle identity shortcut. | Offline probe | I used vision to triage labels, while retaining human outcome verification. |
| Transformer engineering | Implemented and profiled a 3.37M Transformer at operator/shape level before applying the same discipline to VLA interfaces. | Offline probe | I can explain tensor flow and runtime trade-offs beyond model API use. |

The result is an evidence chain: **collect safely → validate data → compare models fairly → constrain output → verify outcomes separately**. Current acceptance gates are in the [roadmap](roadmap/README.md).

