namespace lib {
template<typename T>
class Set {
private:
    RedBlackTree<T> tree;

public:
    void insert(const T& value) {
        tree.insert(value);
    }
    
    bool contains(const T& value) const {
        return tree.search(value);
    }
    
    void print() const {
        tree.printTree();
    }
    
    bool operator()(const T& value) const {
        return contains(value);
    }

    int size() const {
        return tree.size();
    }
};
}