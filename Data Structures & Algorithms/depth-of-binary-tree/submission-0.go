/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxDepth(root *TreeNode) int {
    count := 0
	if root == nil{
		return 0
	} 
	count += max(maxDepth(root.Left), maxDepth(root.Right)) + 1
	return count
}
