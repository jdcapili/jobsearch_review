/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    if (p !== q) return false;
    if (p === null && q === null) return true;
    if ((p === null && q) || (q === null && p)) return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
};