blocks = int(input("Enter number of blocks: "))

height = 0
numberOfBlocksPerLayer = 1

while height < blocks:
    height += 1
    blocks = blocks - numberOfBlocksPerLayer
    numberOfBlocksPerLayer += 1

print('height of pyramid is: {}'.format(height))
