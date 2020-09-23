from TrieNode import TrieNode


class Trie(object):
    """The trie object"""

    def __init__(self, distances):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
        self.distances = distances

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix, index):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        # if node.is_end:
        #     self.output.append((prefix + [node.char], node.counter))
        node_index = index
        for child in node.children.values():
            index += 1
            try:
                self.output.append(f'{node.char}_{node_index} -> {child.char}_{index} [label={self.distances[node.char][child.char]}]')
            except KeyError:
                pass
            self.dfs(child, prefix + [node.char], index)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        # for char in x:
        #     if char in node.children:
        #         node = node.children[char]
        #     else:
        #         # cannot found the prefix, return empty list
        #         return []

        # Traverse the trie to get all candidates
        self.dfs(node, x, 0)

        # Sort the results in reverse order and return
        return self.output
