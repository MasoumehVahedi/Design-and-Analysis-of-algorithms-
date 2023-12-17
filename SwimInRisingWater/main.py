from solution import Solution

def main():
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    # Solution for Swimming In Rising Water
    solution = Solution()
    minTime = solution.move(grid)
    print(f"Minimum time to reach the destination: {minTime}")


if __name__ == "__main__":
    main()