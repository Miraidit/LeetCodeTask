func strStr(haystack string, needle string) int {
    if strings.Contains(haystack, needle) {
		for i := 0; i < len(haystack)-len(needle)+1; i++ {
			if haystack[i:i+len(needle)] == needle {
				return i
			}
		}
	}
	return -1
}