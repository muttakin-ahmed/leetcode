def max_disk_space(freeSpaces, blockSize):
    start = 0
    end = blockSize
    disk_sizes = []

    while end <= len(freeSpaces):
        disk_sizes.append(min(freeSpaces[start:end]))
        start += 1
        end += 1
    return max(disk_sizes)

print(max_disk_space([8,2,4,5], 2))

# Time complexity: O(n), as we have to irerate the array freeSpaces once and the solution time is dependant on the size of that array.
# Space complexity: O(n), as we have used an array to store all the possible disk sizes.