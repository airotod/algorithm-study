class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        node = self.head
        for c in string:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.data = string

    def search(self, string):
        node = self.head
        for c in string:
            if c in node.children:
                node = node.children[c]
            else:
                return False

        if node.data != None:
            return True

    def starts_with(self, string):
        node = self.head
        result = []
        subtrie = None

        for c in string:
            if c in node.children:
                node = node.children[c]
                subtrie = node
            else:
                return None

        queue = list(subtrie.children.values())
        while queue:
            node = queue.pop()
            if node.data != None:
                result.append(node.data)
            queue.extend(node.children.values())

        return result

if __name__ == '__main__':
    insert_arr1 = ['bee', 'can', 'cat', 'cd']
    search_arr1 = ['caw', 'be', 'can']
    tree = Trie()

    for word in insert_arr1:
        print(f'insert {word}')
        tree.insert(word)

    for word in search_arr1:
        if tree.search(word):
            print(f'{word} is in tree')
        else:
            print(f'{word} is not in tree')