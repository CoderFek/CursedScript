from tokens import Integer, Float

class Interpreter:
    def __init__(self, tree, base):
        self.tree = tree
        self.base = base

    def read_INT(self, value):
        return int(value)
    
    def read_FLT(self, value):
        return float(value)
    
    def read_VAR(self, id):
        variable = self.base.read(id)
        variable_type = variable.type

        return getattr(self, f"read_{variable_type}")(variable.value)

    def compute_bin(self, left, op, right):

        left_type = "VAR" if str(left.type).startswith("VAR") else str(left.type)        #storing the type of data as left_type else VAR
        right_type = "VAR" if str(right.type).startswith("VAR") else str(right.type)       #storing the type of data as right_type else VAR

        if op.value == "=":
            left.type = f"VAR({right_type})"
            self.base.write(left, right)
            return self.base.read_all()


        #pass the parameter left.value(INT/FLT) to the read_(INT/FLT) method
        left = getattr(self, f"read_{left_type}")(left.value)         # store the converted data in left_node as left

        #pass the parameter right.value(INT/FLT) to the read_(INT/FLT) method
        right = getattr(self, f"read_{right_type}")(right.value)      # store the converted data in right_node as right
        
        if op.value == "+":
            output = left + right
        elif op.value == "-":
            output = left - right
        elif op.value == "/":
            output = left / right
        elif op.value == "*":
            output = left * right

        return Integer(output) if (left_type == "INT" and right_type == "INT") else Float(output)


    def interpret(self, tree = None):
        if tree is None:
            tree = self.tree

        # Evaluating the left subtree
        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)         #recurssively interpreting the left subtree
        
        # Evaluating the right subtree
        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)       #recurssively interpreting the right subtree

        operator = tree[1]      #root_node

        return self.compute_bin(left_node, operator, right_node)