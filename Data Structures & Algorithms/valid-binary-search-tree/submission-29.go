/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    return check(root, -1001, 1001)
}

func check(node *TreeNode, min, max int) bool {
    if node == nil {
        return true 
    }
    if node.Val <= min || node.Val >= max {
        return false
    }
    return check(node.Left, min, node.Val) && check(node.Right, node.Val, max)
}