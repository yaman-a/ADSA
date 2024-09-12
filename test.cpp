#include <iostream>
#include <queue>

// Im writing code mainly in python, but ill write c++ code as well for testing mainly

struct Node {
    int val;
    Node *left;
    Node *right;
    int height;

    Node(int k) {
        val = k;
        left = nullptr;
        right = nullptr;
        height = 1;
    }
};

int height(Node* n) {
    if (!n) {
        return 0;
    }
    return n->height;
}

// Level order traversal, mainly for testing purposes
void levelOrder(Node* root) {
    if (!root) {
        return;
    }
    
    std::queue<Node*> q;
    Node* curr;
    q.push(root);
    q.push(NULL);

    while (q.size() > 1) {
        curr = q.front();
        q.pop();

        if (!curr) {
            q.push(NULL);
            std::cout << std::endl;
        } else {
            if (curr->left) {
                q.push(curr->left);
            }
            if (curr->right) {
                q.push(curr->right);
            }

            std::cout << curr->val << " ";

        }
    }
}

int main() {
    Node* root = new Node(5);

    root->left = new Node(6);
    root->right = new Node(4);

    levelOrder(root);

    return 0;
}

