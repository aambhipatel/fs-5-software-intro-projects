# PID Controller Simulation for an Autonomous Race Car

This is a Python simulation of a PID controller that accelerates a car from 0 m/s to a set desired velocity without overshooting or maintaining just below the desired velocity.

## Requirements

- Python 3.9
- `numpy`
- `matplotlib`

```
pip install numpy matplotlib
```

## Getting Started

Run the template script that imports from `pid_template.py`:

```
python run_template.py
```

A window should pop up showing the velocity vs time and error vs time graphs.


## Functions in pid_template.py

- `make_car(desired_v, dt)`: creates the dictionary for the car's sensor values (acceleration, velocity, position, time, friction, etc). 
- `update(car, throttle_perc, mass, max_throttle_force, friction)`: updates velcoity, position, and time of the car. Also converts the throttle into force.
- `calculate_desired_acceleration(car, K_P, K_I, K_D)`: PID controller that returns the desired acceleration and the current error.
- `acceleration_to_throttle_percentage(acceleration_desired, mass, max_throttle_force)`: converts desired acceleration to a throttle percentage, clipped from -1 to 1.