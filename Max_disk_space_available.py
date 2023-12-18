def max_disk_space(freeSpaces, blockSize):
    start = 0
    end = blockSize
    mds = 0

    while end <= len(freeSpaces):
        mds = max(mds, min(freeSpaces[start:end]))
        start += 1
        end += 1
    return mds

print(max_disk_space([8,2,4,5], 2))

# Time complexity: O(n), as we have to irerate the array freeSpaces once and the solution time is dependant on the size of that array.
# Space complexity: O(1) if we use a variable to update the max value instead of an array
