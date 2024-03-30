# Creating Trajectory for Panda Robot

## Description

This program creates a trajectory for a Panda robot with 7 degrees of freedom. The trajectory starts from the zero configuration `qz`, and then the robot "draws" a circle in the XY plane. Additionally, the program generates a plot showing the points of the circle on the XY plane and the values of the angles of the robot's axes during the movement. Moreover, it creates an animation showing the execution of the entire trajectory by the Panda robot.

## Trajectory Data

- End-effector height (during drawing the circle): 0.15
- Circle center position: x = 0.65, y = 0.2
- Circle radius: 0.1

## Requirements

- Python 3.x
- NumPy library
- Matplotlib library
- Roboticstoolbox library
- Spatialmath

## Results

After running the program, two plots and an animation will be generated:

1. **Circle Points Plot**: Shows the points of the circle on the XY plane.
2. **Robot Axis Angle Values Plot**: Illustrates the changes in the values of the angles of the robot's axes during movement.
3. **Panda Robot Trajectory Animation**: Displays an animation of the entire trajectory execution by the Panda robot in the Swift enviroment.
