try:
    temp = int(input("Temperature in deg C > "))
    d_open = int(input("No of times door opened > "))
    run_time = int(input("Time for which the purifier is turned on > "))
except Exception as e:
    print(f"Invalid input: {e}")

if d_open > run_time:
    raise Exception("The door can be opened once a minute."
                    + " So the number of times door opened should be"
                    + " numerically less than or equals to run time")

eff = int((temp - 25) * 2)
total = (run_time - d_open) * (40 + eff) + d_open * (30 + eff)

if total <= 0:
    raise Exception(
        "Under the given sitution the purifier will not work at all")
