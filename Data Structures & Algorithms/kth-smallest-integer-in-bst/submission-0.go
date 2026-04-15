/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func kthSmallest(root *TreeNode, k int) int {
    res := []int{}
	traverse(root, &res)
	return res[k-1]
}

func traverse(node *TreeNode, elements *[]int){
	if node == nil{
		return
	}
	traverse(node.Left, elements)
	*elements = append(*elements, node.Val)
	traverse(node.Right, elements)
}