
class NextFit:
    def nextFit(self, blockSize, processSize):
        m = len(blockSize)
        n = len(processSize)
        allocation = [-1] * n
        j = 0

        for i in range(n):
            count = 0
            while count < m:
                if blockSize[j] >= processSize[i]:
                    allocation[i] = j
                    blockSize[j] -= processSize[i]
                    break
                j = (j + 1) % m
                count += 1

        print("\nProcess No.\tProcess Size\tBlock no.")
        for i in range(n):
            print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")

def main():

    next_fit = NextFit()


    while True:
        print("\nEnter the number of Blocks: ")
        m = int(input())
        print("Enter the number of Processes: ")
        n = int(input())

        blockSize = list(map(int, input("Enter the Size of all the blocks (space-separated): ").split()))
        processSize = list(map(int, input("Enter the Size of all the processes (space-separated): ").split()))


        print("Next Fit Output")
        next_fit.nextFit(blockSize[:], processSize)


if __name__ == "__main__":
    main()