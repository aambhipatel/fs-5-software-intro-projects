import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 2.0
K_I = 0.5
K_D = 0.0
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

car_velocity = []
car_errors = []
car_times = []

for i in range(STEPS):
    desired_a, car_error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle = acceleration_to_throttle_percentage(desired_a)
    update(car, throttle)

    car_velocity.append(car["v"])
    car_errors.append(car_error)
    car_times.append(car["t"])


plt.subplot(211)
plt.plot(car_times, car_velocity)
plt.title("Velocity over Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)


plt.subplot(212)
plt.plot(car_times, car_errors)
plt.title("Error over Time")
plt.xlabel("Time (s)")
plt.ylabel("Error (m/s)")
plt.grid(True)


plt.show()
