/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    unordered_map<Node*, Node*> m;


    Node* dfs (Node* node){
        if (node == nullptr) return nullptr;

        //store visited inside hashmap
        if (m.count(node)){
            return m[node];
        }

        Node* clone = new Node(node->val);
        m[node] = clone;
        //marked visited

        
        for (auto adj : node->neighbors){
            clone->neighbors.push_back(dfs(adj));
            //dfs returns a cloned node, and goes deep into graph
        }
        return clone;

    }
    Node* cloneGraph(Node* node) {
        return dfs(node);
    }
};
