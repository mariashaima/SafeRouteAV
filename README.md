## 🚘 SafeRouteAV
Safety-Aware Motion Planning and Reinforcement Learning in CARLA
📌 Overview

SafeRouteAV is a modular autonomous driving framework that integrates:

## 🗺️ A* global motion planning

🛡️ Safety-aware planning aligned with ISO 26262 and SOTIF (ISO 21448)

🚗 Real-time CARLA simulator integration

🤖 Reinforcement Learning (PPO via RLlib) for route-following control

📊 Safety metric logging and evaluation

The project combines classical motion planning and learning-based control, while embedding functional safety principles into both design and runtime operation.

This repository is structured like an industry-grade AV stack and is suitable for:

Master's thesis work

Automotive R&D portfolios

ADAS / Autonomous Driving applications

Safety-critical system demonstrations

🧠 System Architecture
                +----------------------+
                |     CARLA Map        |
                +----------------------+
                           ↓
                +----------------------+
                | Waypoint Graph       |
                | Builder              |
                +----------------------+
                           ↓
                +----------------------+
                | Safety-Aware A*      |
                | Global Planner       |
                +----------------------+
                           ↓
                +----------------------+
                | Route Smoothing      |
                +----------------------+
                           ↓
                +----------------------+
                | RL Route Follower    |
                | (PPO - RLlib)        |
                +----------------------+
                           ↓
                +----------------------+
                | Safety Layer         |
                | - TTC Monitoring     |
                | - Collision Check    |
                | - Emergency Override |
                +----------------------+
                           ↓
                +----------------------+
                | CARLA Vehicle        |
                | Control              |
                +----------------------+

🚀 Features
🗺️ Motion Planning

Graph extraction from CARLA waypoints

A* shortest-path algorithm

Risk-augmented cost function:

<img width="384" height="62" alt="image" src="https://github.com/user-attachments/assets/cf587ed5-2474-466f-a63f-60fa6b5aa6c0" />


Configurable safety weighting factor (λ)

🛡️ Safety Layer (ISO 26262 & SOTIF)
Runtime Safety Monitoring

Time-To-Collision (TTC) computation

Collision detection

Emergency braking override

ISO 26262 Alignment

Hazard Analysis & Risk Assessment (HARA)

Safety goal definition

Technical safety mechanisms

Safety monitoring layer

SOTIF Considerations

Performance limitations of planner

Edge-case validation scenarios

Conservative safety margins

See:

docs/iso26262_alignment.md
docs/sotif_analysis.md

## 🤖 Reinforcement Learning Integration

PPO (Proximal Policy Optimization)

RLlib (Ray)

Continuous control (steer, throttle)

Route-following with safety constraints

Reward shaping including:

Progress reward

Collision penalty

TTC penalty

Lane deviation penalty

##
📁 Repository Structure

<img width="356" height="280" alt="image" src="https://github.com/user-attachments/assets/e706108a-8f2d-472e-b746-5f6bd6acf20a" />


<img width="600" height="224" alt="image" src="https://github.com/user-attachments/assets/ac8cd762-584e-40d7-ab9c-970483a20772" />


🧪 Installation
1️⃣ Create Environment
conda create -n saferoute python=3.10
conda activate saferoute

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install CARLA Python API

Download CARLA from:

https://carla.org/

Then add the CARLA .egg file to your PYTHONPATH.

▶️ Running the Project
🗺️ Run Planner Only (No CARLA)
python scripts/run_planner.py


This runs A* on a sample graph.

🚗 Run CARLA Integration

Start CARLA server:

./CarlaUE4.sh


Run environment:

python scripts/run_carla_route.py

🤖 Train RL Agent
python scripts/train_rl.py


Training logs will appear in:

experiments/models/

📊 Evaluate Agent
python scripts/evaluate_agent.py


Evaluation metrics include:

Collision rate

Minimum TTC

Success rate

Time to goal

Lane deviation

📈 Evaluation Metrics
Category	Metric
Safety	Collision Rate
Safety	Minimum TTC
Efficiency	Time to Goal
Comfort	Lateral Deviation
Robustness	Success Rate
🛡️ Safety Concept Summary
Hazard Example

Collision due to unsafe trajectory selection.

Safety Goal

Maintain TTC > 2 seconds at all times.

Technical Safety Mechanisms

Risk-augmented planning

Runtime TTC validation

Emergency braking override

🧪 Experimental Design

Experiments can include:

Static obstacle avoidance

Dense traffic scenarios

Narrow urban roads

Sudden braking vehicles

Cut-in scenarios

Comparative evaluation:

Variant	Description
A* only	No safety augmentation
A* + Safety	Risk-weighted planning
A* + RL	Learning-based tracking
A* + Safety + RL	Full hybrid system
🎓 Research Contribution

This project demonstrates:

Hybrid classical + learning-based AV architecture

Safety-aware motion planning

Runtime safety enforcement

CARLA-based evaluation

ISO 26262 & SOTIF alignment

Reinforcement learning in safety-critical context

🔬 Future Extensions

Multi-Agent adversarial training

RSS (Responsibility Sensitive Safety) formal model

Scenario generation framework
<img width="850" height="327" alt="image" src="https://github.com/user-attachments/assets/958b3afb-a82f-433f-9145-9fdc84c8211c" />




Monte Carlo safety validation

Formal safety verification

Docker + CI pipeline
