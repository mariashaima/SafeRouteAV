# System Architecture

This document describes the architecture of the AV Motion Planning A* project.

## Overview

The system consists of three major subsystems:

1. **Motion Planning**
   - Graph construction from CARLA waypoints
   - A* shortest-path search
   - Safety filtering (ISO 26262, SOTIF)

2. **CARLA Integration**
   - Ego vehicle spawning
   - Sensor setup (RGB camera, LiDAR optional)
   - Route execution using a waypoint-following controller

3. **Training Framework**
   - Reinforcement learning or imitation learning agent
   - Route-following reward shaping
   - Scenario-based evaluation

---

## Architecture Diagram

