# Safety Concepts (ISO 26262 & SOTIF)

This document outlines how safety concepts are integrated into the motion planning system.

---

# ISO 26262 (Functional Safety)

## Hazard Analysis and Risk Assessment (HARA)

Identified hazards:
- Collision due to incorrect route
- Unsafe curvature leading to loss of control
- Entering forbidden or dangerous zones
- Driving too close to obstacles

## Safety Goals

1. **SG1:** The planner must avoid unsafe areas.
2. **SG2:** The planner must ensure curvature limits are respected.
3. **SG3:** The vehicle must maintain safe clearance.
4. **SG4:** The system must provide fallback behavior if planning fails.

## Functional Safety Mechanisms

- Safety Layer filters unsafe edges.
- Emergency stop if no safe path exists.
- Logging of safety violations.
- Configurable safety parameters.

---

# SOTIF (ISO/PAS 21448)

## Known Performance Limitations

- Map uncertainty
- Sensor occlusion
- Dynamic obstacles not included in static A* graph

## SOTIF Measures

- Scenario-based testing in CARLA
- Randomized weather and lighting
- Edge-case route validation
- Monitoring deviation from planned path

---

# Safety Parameterization

Defined in `config/safety_params.yaml`:
- `min_clearance`
- `max_curvature`
- `forbidden_areas`
- `speed_limits`

---

# Summary

The system integrates:
- ISO 26262 functional safety mechanisms
- SOTIF performance limitation handling
- Configurable safety parameters
- Scenario-based validation in CARLA
