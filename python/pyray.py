import ray
import time

@ray.remote
def f(x):
    time.sleep(1)
    return x + 1

if __name__ == "__main__":
    ray.init()

    init_vals = [1]*100
    print("Initial values are: ", init_vals)
    result_vals = []
    start_time = time.time()
    for x in init_vals:
        result_vals.append(f.remote(x))
    result = ray.get(result_vals)
    end_tim = time.time()
    print("Result is: ", result)
    print("Time taken: ", (end_tim - start_time))

