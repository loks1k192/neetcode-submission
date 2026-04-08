/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func levelOrder(root *TreeNode) [][]int {
    var res [][]int
    if root == nil{
        return nil
    }
    queue := []*TreeNode{root}
    for len(queue) > 0{
        currentSize := len(queue)
        current := make([]int, 0, currentSize)
        for i := 0; i < currentSize; i++{
            current = append(current, queue[i].Val)

            if queue[i].Left != nil{
                queue = append(queue, queue[i].Left)
            }
            if queue[i].Right != nil{
                queue = append(queue, queue[i].Right)
            }
        }
        queue = queue[currentSize:]
        res = append(res, current)
    }
    return res

}