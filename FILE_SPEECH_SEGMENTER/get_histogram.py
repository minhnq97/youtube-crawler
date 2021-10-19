import sys

input_file = sys.argv[1]

with open(input_file, "rt") as f:
    lines = f.read().splitlines()
duration, speech_duration = [], []
for line in lines:
    duration.append(line.split(",")[-1])
    speech_duration.append(line.split(",")[2])

histogram = {}
for i in range(len(duration)):
    dur = duration[i]
    speech_dur = speech_duration[i]
    d = int(float(dur) // 10)
    key = str(d * 10) + "-" + str((d + 1) * 10)
    if key not in histogram:
        histogram [key] = [0, 0]
    histogram[key][0] += float(dur)
    histogram[key][1] += float(speech_dur)

print(histogram)



