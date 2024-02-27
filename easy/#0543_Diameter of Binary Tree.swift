/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        var tmp = 0

        func height(_ node: TreeNode?) -> Int {
            if(node == nil){ return 0 }
            let leftH = height(node?.left)
            let rightH = height(node?.right)

            tmp = max(tmp, leftH + rightH)
            return max(leftH, rightH) + 1
        }

        height(root)
        return tmp
    }
}
