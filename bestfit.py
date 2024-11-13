
class BestFit:
    def bestFit(self, blockSize, processSize):
        m = len(blockSize)
        n = len(processSize)
        allocation = [-1] * n

        for i in range(n):
            bestIdx = -1
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                        bestIdx = j

            if bestIdx != -1:
                allocation[i] = bestIdx
                blockSize[bestIdx] -= processSize[i]

        print("\nProcess No.\tProcess Size\tBlock no.")
        for i in range(n):
            print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")

def main():

    best = BestFit()

    while True:
        print("\nEnter the number of Blocks: ")
        m = int(input())
        print("Enter the number of Processes: ")
        n = int(input())

        blockSize = list(map(int, input("Enter the Size of all the blocks (space-separated): ").split()))
        processSize = list(map(int, input("Enter the Size of all the processes (space-separated): ").split()))


        print("Best Fit Output")
        best.bestFit(blockSize[:], processSize)

if __name__ == "__main__":
    main()