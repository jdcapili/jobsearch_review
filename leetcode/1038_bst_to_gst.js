/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var bstToGst = function (root) {
    summation = 0
    function traverse(node) {
        if (node === null) return 0;
        traverse(node.right);
        node.val += summation;
        summation = node.val;
        traverse(node.left)
    }
    traverse(root)
    return root
};