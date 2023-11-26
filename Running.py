####### UNFINISHED PROJECT #########


motor = False
normal = False
running = False

print("Enter meter:")
meter = int(input())
print("Enter a speed[walking, running, motor]?")
is_run = input()

def error():
    line = "__________________________________"
    print(line + "\nERROR\nCheck if there a misspelled\nletter from your input\n" + line)

if is_run.lower() == 'walking':
    print(",,,,,,,,,,,,,,,,")
elif is_run.lower() == 'running':
    print("running....")
elif is_run.lower() == 'motor':
    print("motoring...")
else:
    error()