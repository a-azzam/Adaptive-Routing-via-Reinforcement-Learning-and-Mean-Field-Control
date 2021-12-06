import numpy as np
from numpy.random import default_rng

rng = default_rng()
channels  = np.zeros(10,dtype=np.int64)
probability = np.ones(10,dtype=np.float32)
numOfPackets = 1000000
for x in range(numOfPackets):
    selectedChannel = rng.integers(1, high=10,endpoint=True)
    channels[selectedChannel-1] += 1 

for i in range(channels.size):
    probability[i] = channels[i]/1000000

print(channels)
print(probability)
