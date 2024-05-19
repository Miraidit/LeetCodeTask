// my code
func minimumTotal(triangle [][]int) int {
	b := 0
	for _, row := range triangle {
		min := row[0]
		for _, num := range row {
			if num < min {
				min = num
			}
		}
		b = b + min
	}
	return b
}

//code work
func minimumTotal(triangle [][]int) int {
	n := len(triangle)

	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, len(triangle[i]))
	}

	copy(dp[n-1], triangle[n-1])

	for i := n - 2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
		}
	}

	return dp[0][0]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}