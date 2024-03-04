from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
x = 10000
for elem in ft_tqdm(range(x)):
	sleep(0.0005)
print()
for elem in tqdm(range(x)):
	sleep(0.0005)
print()