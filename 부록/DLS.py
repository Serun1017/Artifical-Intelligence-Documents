'''
    Depth-Limited Search 파이썬 코드 구현
    2023-2학기 인공지능(김용국 교수) 과제 2.
    세종대학교 소프트웨어학과 19011625 허진수
'''

class NODE :
    def __init__(self, data, parentNode=None) :
        # Initialize Parent Node
        self.paretNode = parentNode

        # Child Node List
        self.childNode = []

        # Node Data
        self.data = data

    def IsLeafNode(self) :
        # When there are no child nodes, it is considered as a Leaf Node.
        if not self.childNode :
            return True
        return False
    
    # Iterates through child nodes, starting from the current node.
    def TreeTraversal(self, depth) :
        if depth <= 0 :
            return
        if self.IsLeafNode() :
            return
        for currNode in self.childNode :
            # Print Current Node Data
            print(f"currNode Data: {currNode.data}")
            # Travel Child Node
            currNode.TreeTraversal(depth - 1)

    # DFS algorithm for finding a node with specific data.
    # Return None if a node with the specified data is not found.
    def FindNode(self, data) :
        if self.data == data :
            return self
        elif self.IsLeafNode() :
            return None
        for currNode in self.childNode :
            # Travel Child Node
            node = currNode.FindNode(data)
            if node != None :
                return node
        return None

# Initialize the root node.
RootNode = None

while True :
    command = input("Command: ")
    # Input Node
    if command == "input" :
        if RootNode == None :
            input_Data = input("Input Data: ")
            RootNode = NODE(input_Data)

            print("INFO: RootNode Created.")
        else :
            parentData = input("Parent Data: ")
            parentNode = RootNode.FindNode(parentData)
            
            # If the parentNode does not exist, the input will not proceed.
            if parentNode == None :
                print("WORNING: There is no parentNode")
                continue
            # Input Node
            input_Data = input("Input Data: ")
            # Excludes duplicate node data.
            if RootNode.FindNode(input_Data):
                print("WORNING: Node duplication!")
            else :
                parentNode.childNode.append(NODE(input_Data))
                print(f"INFO: Node saved below {parentNode.data}")
    # Travel Node
    elif command == "Travel Node" :
        if RootNode == None :
            print("WORNING: There is No node")
        else :
            depth = input("Depth: ")
            depth = int(depth)

            if depth >= 0 :
                print(f"RootNode: {RootNode.data}")
                RootNode.TreeTraversal(depth)
            else :
                print("WORNING: Wrong Depth!")
    # Exit Program
    elif command == "Exit" :
        print("Exit Program")
        break
    # Input an invalid command
    else :
        print("Wrong Command")