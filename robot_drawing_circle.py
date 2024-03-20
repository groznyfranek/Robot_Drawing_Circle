from spatialmath import *
import roboticstoolbox as rtb
from roboticstoolbox.tools.trajectory import *
import matplotlib.pyplot as plt


def check_smooth_traj(sol, jump_threshold=0.15):
    dists = []
    for current_q, next_q in zip(sol.q[1:], sol.q[2:]):
        for j1, j2 in zip(current_q, next_q):
            dist = np.fabs(j1 - j2)
            dists.append(dist)
    print(max(dists))
    return max(dists) < jump_threshold


def calculate_circle_point(angle, x_0, y_0, rad, z):
    x = x_0 + rad * np.cos(angle)
    y = y_0 + rad * np.sin(angle)
    return [x, y, z]


def robot_drawing_circle(circle_center_pos_x, circle_center_pos_y, radius, points_number, eef_height):
    angles = np.linspace(0, 2 * np.pi, points_number)
    Pt_list = []
    for angle in angles:
        point = calculate_circle_point(angle, circle_center_pos_x, circle_center_pos_y, radius, eef_height)
        Pt_list.append(point)
    # print(Pt_list)
    Pt_list2 = np.asarray(Pt_list)
    x_toplot = Pt_list2[:, 0]
    y_toplot = Pt_list2[:, 1]
    plt.figure(figsize=(8, 6))
    plt.scatter(x_toplot, y_toplot, color='black', label='Points on a circle')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot of points on a circle')
    plt.grid(True)
    plt.legend()
    plt.show()

    robot = rtb.models.Panda()
    robot.q = robot.qz
    T_start = robot.fkine(robot.q)

    orientation_down = SE3.Rx(np.pi)
    T_list = [T_start]
    T_list.extend([SE3(p) * orientation_down for p in Pt_list])
    smooth_traj = False
    while not smooth_traj:
        sol = robot.ikine_LM(SE3(T_list))
        if not sol.success:
            print("IK failed!\n")
            return
        smooth_traj = check_smooth_traj(sol)

    rtb.xplot(sol.q, block=True)
    robot.plot(sol.q, backend='swift', loop=False)
    pass


if __name__ == '__main__':
    amount_of_points = 50
    height = 0.15
    r = 0.1
    x0 = 0.65
    y0 = 0.2
    robot_drawing_circle(x0, y0, r, amount_of_points, height)
