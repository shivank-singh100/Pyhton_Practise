# Program to add two time values in hh:mm:ss format
# Takes two time inputs from the user, adds them, and prints the result

try:
    # Read and split the first and second time values into hours, minutes, and seconds
    t1 = list(map(int, input("Enter first time (hh:mm:ss): ").split(':')))
    t2 = list(map(int, input("Enter second time (hh:mm:ss): ").split(':')))
    
    # Add seconds, then minutes (including overflow from seconds), then hours (including overflow from minutes)
    s = t1[2] + t2[2]
    m = t1[1] + t2[1] + s // 60
    h = t1[0] + t2[0] + m // 60
    
    # Format the result to hh:mm:ss, ensuring minutes and seconds are within 0-59
    print(f"Sum of times: {h:02d}:{m%60:02d}:{s%60:02d}")
except:
    # Handle invalid input (e.g., wrong format or non-integer values)
    print("Invalid input. Please enter time in hh:mm:ss format.")