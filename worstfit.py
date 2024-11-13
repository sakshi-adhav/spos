
class WorstFit:
    def worstFit(self, blockSize, processSize):
        m = len(blockSize)
        n = len(processSize)
        allocation = [-1] * n

        for i in range(n):
            wstIdx = -1
            for j in range(m):
                if blockSize[j] >= processSize[i]:
                    if wstIdx == -1 or blockSize[wstIdx] < blockSize[j]:
                        wstIdx = j

            if wstIdx != -1:
                allocation[i] = wstIdx
                blockSize[wstIdx] -= processSize[i]

        print("\nProcess No.\tProcess Size\tBlock no.")
        for i in range(n):
            print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
            if allocation[i] != -1:
                print(allocation[i] + 1)
            else:
                print("Not Allocated")


def main():

    worst = WorstFit()


    while True:
        print("\nEnter the number of Blocks: ")
        m = int(input())
        print("Enter the number of Processes: ")
        n = int(input())

        blockSize = list(map(int, input("Enter the Size of all the blocks (space-separated): ").split()))
        processSize = list(map(int, input("Enter the Size of all the processes (space-separated): ").split()))


        print("Worst Fit Output")
        worst.worstFit(blockSize[:], processSize)


if __name__ == "__main__":
    main()