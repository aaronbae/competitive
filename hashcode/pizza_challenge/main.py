from Pizza import Pizza
import time

time_out = 60 * 5 # 5 minutes
file_names = ["b_small.in"]
#file_names = ["a_example.in", "b_small.in", "c_medium.in", "d_big.in"]

for file in file_names:
    zza = Pizza(file)
    start_time = time.time()
    # 1. Recognize Sparcity
    # 2. Solution  in dictionary
    #   - dict {
    #       (6, 1): [(2, 6, 1, 1)]
    #       }
    # 3. State Space Search
    zza.slice(0, 0, 0, 4)
    zza.slice(0, 5, 1, 5)
    zza.slice(0, 6, 1, 6)
    zza.slice(1, 0, 5, 0)
    zza.slice(1, 1, 5, 1)
    zza.slice(1, 2, 1, 4)
    zza.slice(2, 2, 2, 6)
    zza.slice(3, 2, 3, 6)
    zza.slice(4, 2, 4, 6)
    zza.slice(5, 2, 5, 6)
    zza.print()
    #while(time.time() - start_time <= time_out):
        # find the best solution

    zza.save_to_file("solution_to_"+file)
