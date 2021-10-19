import sys

input_file = sys.argv[1]

with open(input_file, "rt") as f:
    lines = f.read().splitlines()
duration, num_osd = [], []
for line in lines:
    duration.append(line.split(",")[-1])
    num_osd.append(line.split(",")[1])

histogram = {}
for i in range(len(duration)):
    dur = duration[i]
    osd = num_osd[i]
    d = int(float(dur) // 300)
    key = str(d * 300) + "-" + str((d + 1) * 300)
    if key not in histogram:
        histogram [key] = 0
    histogram[key] += 1

    #histogram[key][1] += float(speech_dur)

print(histogram)
