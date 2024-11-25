import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def lorentz_force(q, E, B, v):
    return q * (E + np.cross(v, B))

def simulate_particle_motion(q, m, r0, v0, E, B, t_max, dt):
    steps = int(t_max / dt)
    r = np.zeros((steps, 3))
    v = np.zeros((steps, 3))
    t = np.linspace(0, t_max, steps)

    r[0] = r0
    v[0] = v0

    for i in range(1, steps):
        F = lorentz_force(q, E, B, v[i - 1])
        a = F / m
        v[i] = v[i - 1] + a * dt
        r[i] = r[i - 1] + v[i] * dt

    return r, t

def plot_trajectory(r, t):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(r[:, 0], r[:, 1], r[:, 2], label='Particle Trajectory', color='blue')
    ax.set_title("Charged Particle Trajectory in Electromagnetic Fields")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")
    ax.legend()
    plt.show()

def main():
    print("Welcome to the Charged Particle Motion Simulator!")
    print("This tool simulates a charged particle in electric and magnetic fields.")

    try:
        q = float(input("Enter the charge of the particle (Coulombs): "))
        m = float(input("Enter the mass of the particle (kg): "))
        r0 = list(map(float, input("Enter the initial position (x, y, z in meters): ").split()))
        v0 = list(map(float, input("Enter the initial velocity (vx, vy, vz in m/s): ").split()))
        E = list(map(float, input("Enter the electric field (Ex, Ey, Ez in V/m): ").split()))
        B = list(map(float, input("Enter the magnetic field (Bx, By, Bz in Tesla): ").split()))
        t_max = float(input("Enter the simulation duration (seconds): "))
        dt = float(input("Enter the time step for the simulation (seconds): "))

        print("\nRunning the simulation... Please wait!")
        r, t = simulate_particle_motion(q, m, np.array(r0), np.array(v0), np.array(E), np.array(B), t_max, dt)
        plot_trajectory(r, t)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
