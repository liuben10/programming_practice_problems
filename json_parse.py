class JsonTreeNode:
    def __init__(self):
        self.children = None
        self.value = None

    def withValue(self, value):
        self.value = value
        return self

    def setChildren(self, children):
        self.children = children
        return self

    def getChildren(self):
        return self.children

    def isLeaf(self):
        return self.value is not None

    def dfsPretty(self):
        return self.dfsPrettyHelp(1)
        
    def dfsPrettyHelp(self, pad):
        padding = "".join([" " for i in range(pad)])
        rest_string = ""
        if (self.isLeaf()):
            return padding + self.value + "\n"
        if (type(self.children) is list):
            for c in self.children:
                rest_string += c.dfsPrettyHelp(pad + 1)
        elif (type(self.children) is dict):
            rest_string = "{\n"
            for k in self.children:
                rest_string += padding + " " + k + ": " + self.children[k].dfsPrettyHelp(pad + 1)
            rest_string += padding + "},"
        return padding + rest_string + "\n"
            
                


def parse_json(json_string):
    if not len(json_string):
        return ""
    if len(json_string) == 1:
        if (json_string[0] == "{"):
            raise Exception("Invalid Json")
        else:
            leaf = JsonTreeNode()
            return leaf.withValue(json_string[0])

    if json_string[len(json_string) - 1] == ",":
        json_string = json_string[1: len(json_string) - 2]
    else:
        json_string = json_string[1: len(json_string) - 1]
    
    toks = json_string.split()
    print("Toks=%s" % (toks))

    idx = 0
    parent = JsonTreeNode().setChildren({})
    
    while idx < len(toks):
        key, kidx = ingest_key(toks, idx)
        print("Key=%s and kidx=%s" % (key, kidx))
        if (kidx < len(toks)):
            value, vidx = ingest_value(toks, kidx)
            parent.getChildren()[key] = value
            idx = vidx
        else:
            raise Exception("Not a valid json. Key=%s should be followed by value" % key)
    return parent


def ingest_key(toks, idx):
    print("String  starting at idx+1=%s" % toks[idx+1])
    if (idx + 1 < len(toks)):
        if (toks[idx + 1] == ":"):
            return (toks[idx], idx+2)
    raise Exception("Not a valid Json. Key=%s should be followed by colon" % (toks[idx]))

def ingest_value(toks, idx):
    if (toks[idx] == "["):
        return handle_list(toks, idx)
    elif toks[idx] == "{":
        return handle_json(toks, idx)
    else:
        res = JsonTreeNode()
        res.withValue(toks[idx])
        return res, idx+1

def handle_list(toks, idx):
    parent = JsonTreeNode().setChildren([])
    
    if (toks[idx] == "["):
        idx += 1
    else:
        raise Exception("Invalid list passed into handle_list. Lists must start with open [")
    while idx < len(toks):
        cur = toks[idx]
        if (cur == "["):
            listNode, endIdx = handle_list(toks, idx)
            parent.getChildren().append(listNode)
            idx = endIdx + 1
        elif cur == "]":
            return parent, idx
        else:
            if (cur[len(cur) - 1] == ","):
                cur = cur[0:len(cur)-1]
            child = JsonTreeNode().withValue(cur)
            parent.getChildren().append(child)
            idx += 1
    raise Exception("Invalid list passed into handle_list. Lists must end with ]")


def handle_json(toks, idx):
    parent = JsonTreeNode().setChildren({})

    if (toks[idx] == "{"):
        braces_count = 1
        idx += 1
        json_string = "{"
    else:
        raise Exception("Error invalid Json child passed into handle_json")

    while idx < len(toks) and braces_count > 0:
        cur = toks[idx]
        if (cur == "{"):
            braces_count += 1            
        elif (cur[0] == "}"):
            braces_count -= 1
            
        json_string += " " + cur
        idx += 1

    if (idx >= len(toks) and braces_count > 0):
        raise Exception("Error invalid Json format passed in. Curly braces are not balanced")
    return parse_json(json_string), idx




res, idx = handle_list(["[", "[", "foo,", "bar,", "]", "baz,", "]"], 0)
print("res[0]=%s, and idx=%s" % (res.getChildren()[0].children, idx))


print(handle_json(["{", "foo", ":", "bar,", "abc", ":", "def", "}"], 0)[0])
print(handle_json(["{", "foo", ":", "{", "a", ":", "b,", "},", "bad", ":", "bogus", "}"], 0)[0].dfsPretty())
