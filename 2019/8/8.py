width, height = 25, 6
data = open('input').read().strip()
layers = []
while data:
    layer, data = data[:width * height], data[width * height:]
    layers.append(layer)

print('A:', min((l.count('0'), l.count('1') * l.count('2')) for l in layers)[1])

image = list(layers[0])
for layer in layers[1:]:
    for i in range(len(image)):
        if image[i] == '2':
            image[i] = layer[i]

print('B:')
while image:
    print(''.join(image[:width]).replace('0', ' '))
    image = image[width:]
