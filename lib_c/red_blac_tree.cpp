#include <iostream>
#include <memory>
#include <string>

enum class Color { RED, BLACK };

template<typename TKey>
class Node {
public:
    TKey key;
    Color color;
    std::shared_ptr<Node<TKey>> parent;
    std::shared_ptr<Node<TKey>> left;
    std::shared_ptr<Node<TKey>> right;
    int size; // Количество узлов в поддереве с этим корнем

    Node(TKey k, Color c, 
         std::shared_ptr<Node<TKey>> p = nullptr,
         std::shared_ptr<Node<TKey>> l = nullptr,
         std::shared_ptr<Node<TKey>> r = nullptr)
        : key(k), color(c), parent(p), left(l), right(r), size(1) {}
};

namespace lib {
template<typename TKey>
class RedBlackTree {
private:
    std::shared_ptr<Node<TKey>> nil;
    std::shared_ptr<Node<TKey>> root;

public:
    RedBlackTree() {
        nil = std::make_shared<Node<TKey>>(TKey(), Color::BLACK);
        nil->size = 0;
        root = nil;
    }

    void insert(const TKey& key) {
        auto node = std::make_shared<Node<TKey>>(key, Color::RED, nil, nil, nil);
        
        auto parent = nil;
        auto current = root;
        
        while (current != nil) {
            parent = current;
            if (node->key < current->key) {
                current = current->left;
            } else if (node->key > current->key) {
                current = current->right;
            } else {
                return; 
            }
        }
        
        node->parent = parent;
        
        if (parent == nil) {
            root = node;
        } else if (node->key < parent->key) {
            parent->left = node;
        } else {
            parent->right = node;
        }
        
        update_size_upwards(node);
        
        fix_insert(node);
    }

    bool search(const TKey& key) const {
        return search(root, key);
    }

    int size() const {
        return root->size;
    }

    bool empty() const {
        return root == nil;
    }

    void print_tree() const {
        std::cout << "Tree (size: " << size() << "):" << std::endl;
        print_tree(root, 0, "Root:");
    }

private:
    bool search(std::shared_ptr<Node<TKey>> node, const TKey& key) const {
        while (node != nil) {
            if (key == node->key) {
                return true;
            } else if (key < node->key) {
                node = node->left;
            } else {
                node = node->right;
            }
        }
        return false;
    }

    void update_size(std::shared_ptr<Node<TKey>> node) {
        if (node != nil) {
            node->size = 1 + node->left->size + node->right->size;
        }
    }

    void update_size_upwards(std::shared_ptr<Node<TKey>> node) {
        while (node != nil) {
            update_size(node);
            node = node->parent;
        }
    }

    void fix_insert(std::shared_ptr<Node<TKey>> node) {
        while (node->parent->color == Color::RED) {
            if (node->parent == node->parent->parent->left) {
                auto uncle = node->parent->parent->right;
                if (uncle->color == Color::RED) {
                    node->parent->color = Color::BLACK;
                    uncle->color = Color::BLACK;
                    node->parent->parent->color = Color::RED;
                    node = node->parent->parent;
                } else {
                    if (node == node->parent->right) {
                        node = node->parent;
                        left_rotate(node);
                    }
                    node->parent->color = Color::BLACK;
                    node->parent->parent->color = Color::RED;
                    right_rotate(node->parent->parent);
                }
            } else {
                auto uncle = node->parent->parent->left;
                if (uncle->color == Color::RED) {
                    node->parent->color = Color::BLACK;
                    uncle->color = Color::BLACK;
                    node->parent->parent->color = Color::RED;
                    node = node->parent->parent;
                } else {
                    if (node == node->parent->left) {
                        node = node->parent;
                        right_rotate(node);
                    }
                    node->parent->color = Color::BLACK;
                    node->parent->parent->color = Color::RED;
                    left_rotate(node->parent->parent);
                }
            }
            
            if (node == root) {
                break;
            }
        }
        
        root->color = Color::BLACK;
    }

    void left_rotate(std::shared_ptr<Node<TKey>> x) {
        auto y = x->right;
        x->right = y->left;
        
        if (y->left != nil) {
            y->left->parent = x;
        }
        
        y->parent = x->parent;
        
        if (x->parent == nil) {
            root = y;
        } else if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }
        
        y->left = x;
        x->parent = y;
        
        update_size(x);
        update_size(y);
    }

    void right_rotate(std::shared_ptr<Node<TKey>> y) {
        auto x = y->left;
        y->left = x->right;
        
        if (x->right != nil) {
            x->right->parent = y;
        }
        
        x->parent = y->parent;
        
        if (y->parent == nil) {
            root = x;
        } else if (y == y->parent->right) {
            y->parent->right = x;
        } else {
            y->parent->left = x;
        }
        
        x->right = y;
        y->parent = x;
        
        update_size(y);
        update_size(x);
    }

    void print_tree(std::shared_ptr<Node<TKey>> node, int level, const std::string& prefix) const {
        if (node != nil) {
            std::string indent(level * 4, ' ');
            std::string colorStr = (node->color == Color::RED) ? "RED" : "BLACK";
            std::cout << indent << prefix << " " << node->key << "(" << colorStr << ", size:" << node->size << ")" << std::endl;
            
            if (node->left != nil) {
                print_tree(node->left, level + 1, "L---");
            }
            if (node->right != nil) {
                print_tree(node->right, level + 1, "R---");
            }
        }
    }
};
}