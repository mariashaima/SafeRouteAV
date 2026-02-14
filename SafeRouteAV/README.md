# AV Motion Planning with A* and CARLA

## Description

This project provides an industrial-style motion planning stack for
autonomous vehicles using A* on map graphs, with safety-aware filtering
inspired by ISO 26262 and SOTIF, and integration with the CARLA simulator
for training and evaluation.

## Features

- A* shortest-path planning on CARLA or Lanelet2 maps
- Safety layer for route validation (no-go zones, curvature limits, etc.)
- CARLA integration for route execution
- Training interface for route-following agents (RL or imitation)

## Safety (ISO 26262 & SOTIF)

- Hazard-oriented route constraints (forbidden areas, speed limits)
- Scenario-based validation (cut-in, intersections, occlusions)
- Separation of safety-related configuration in `config/safety_params.yaml`
- Clear assumptions and limitations documented in `docs/safety_concepts_iso26262_sotif.md`

## Getting Started

```bash
conda create -n avs_planner python=3.10
conda activate avs_planner
pip install -r requirements.txt
