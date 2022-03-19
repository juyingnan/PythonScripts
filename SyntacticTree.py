import pickle


class syntactic_node:
    def __init__(self, id, syntactic, parent, lexical=''):
        self.id = id
        self.syntactic = syntactic
        self.parent = parent
        self.lexical = lexical
        self.children = []

    def __str__(self):
        if (self.parent == None):
            parent = "NULL"
        else:
            parent = self.parent.syntactic
        child_id = ''
        for child in self.children:
            child_id += str(child.id) + " "
        child_id.strip()
        result = "SYN: " + self.syntactic + " | PARENT: " + parent + " | LEX: " + self.lexical + " | ID: " + str(
            self.id) + " | CHILD: " + child_id
        return result


def generate_tree(elements):
    result = []

    # initial
    elements.reverse()
    upper_level = None
    id = 0

    # generate the tree
    while (len(elements) > 0):
        top = elements.pop()
        if top != '(' and top != ')':
            node = syntactic_node(id, top, upper_level)
            result.append(node)
            id += 1
            upper_level = node
            if elements[-1] != '(' and elements[-1] != ')':
                node.lexical = elements.pop()
        elif top == ')':
            if upper_level != None:
                upper_level = upper_level.parent

    # get children
    refresh_children(result)
    return result


def refresh_children(tree):
    for node in tree:
        node.children = []
        for n in tree:
            if n.parent == node:
                node.children.append(n)
        node.children.sort(key=lambda child:child.id)

def passive_2_active(tree):
    for node in tree:

        # 5 Conditions
        is_PP = False
        has_VP_upper_parent = False
        VP_upper_parent = None
        has_IN_by_child = False
        has_NP_child = False
        NP_child = None
        has_NP_parent_sibling = False
        NP_parent_sibling = None

        # condition 1: node is PP
        if node.syntactic == 'PP':
            is_PP = True

        # condition 2: find the top VP
        temp_node = node
        while temp_node.parent != None:
            if temp_node.parent.syntactic == 'VP':
                has_VP_upper_parent = True
                VP_upper_parent = temp_node.parent
            temp_node = temp_node.parent

        # condition 3: child is IN-by
        for child in node.children:
            if child.syntactic == 'IN' and child.lexical == 'by':
                has_IN_by_child = True

        # condition 4: has a NP child
        for child in node.children:
            if child.syntactic == 'NP':
                has_NP_child = True
                NP_child = child

        # find top VP's NP sibling
        if VP_upper_parent != None:
            if VP_upper_parent.parent != None:
                for sibling in VP_upper_parent.parent.children:
                    if sibling.syntactic == 'NP':
                        has_NP_parent_sibling = True
                        NP_parent_sibling = sibling

        if is_PP and has_VP_upper_parent and has_IN_by_child and has_NP_child and has_NP_parent_sibling:
            # change id: NP_child & NP_top
            temp = NP_child.id
            NP_child.id = NP_parent_sibling.id
            NP_parent_sibling.id = temp

            # change parent
            temp = NP_child.parent
            NP_child.parent = NP_parent_sibling.parent
            NP_parent_sibling.parent = temp

            # refresh children
            refresh_children(tree)

def print_tree(tree):
    root = None
    for node in tree:
        if node.id == 0:
            root = node
            break
    result = []
    read(root, result)
    print result

def read(node, result):
    if node == None:
        return None
    elif len(node.children)>0:
        if len(node.lexical)>0:
            result.append(node.lexical)
        for child in node.children:
            read(child, result)
    else:
        if len(node.lexical)>0:
            result.append(node.lexical)
            # print result+" ",

filename = "passives_curated.parsed"
tree_original_file = open(filename, "r")
tree_list = []

for eachline in tree_original_file:
    line_with_space = eachline.replace('(', ' ( ').replace(')', ' ) ')
    elements = line_with_space.split()
    tree_list.append(generate_tree(elements))

for tree in tree_list:
    passive_2_active(tree)

# print test
for node in tree_list[-1]:
    print node

print_tree(tree_list[-1])

    # pickle save
    # pickle.dump(tree_list, open("syntactic_tree_pickle.txt", "w"))
    # pickle read
    # another_list = pickle.load(open("syntactic_tree_pickle.txt", "r"))
