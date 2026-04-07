/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil{
		return false
	}
	if isSameTree(root, subRoot){
		return true
	}
	if isSubtree(root.Left, subRoot){
		return true
	}
	if isSubtree(root.Right, subRoot){
		return true
	}
	return false
}


func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil{
		return true
	}
	if p == nil && q != nil || p != nil && q == nil{
		return false
	}
	if p.Val != q.Val{
		return false 
	}
	if !isSameTree(p.Left, q.Left){
		return false
	}
	if !isSameTree(p.Right, q.Right){
		return false
	}
	return true
}