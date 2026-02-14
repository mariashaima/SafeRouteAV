# CARLA Integration Guide

This document explains how the system interacts with the CARLA simulator.

---

# CARLA Components

## World
- Loaded via `carla.Client`
- Provides map, weather, actors

## Map
- Waypoints extracted using:
  ```python
  world.get_map().generate_waypoints(2.0)
