
uddatal = 0
jamnatal = 0

print("Beräknar differensen av jämna/udda tal ...")

for i in range(2,2001,2):
    jamnatal += i

for j in range(1,2000,2):
        uddatal += j

print(f'Differensen = {jamnatal-uddatal}')