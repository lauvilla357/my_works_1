######     NODES IN PYTHON
##  Nodes are information sets of two kinds of data: the data in case and the link with another node.

class node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node
    def set_next_node(self,next_node):
        self.next_node=next_node
    def get_next_node(self):
        return self.next_node
    def get_value(self):
        return self.value

# Ejemplo de ejecución:

node1=node(20)
print(node1.value,node1.next_node)

node1.set_next_node(1)
next_node=node1.get_next_node()
value=node1.get_value()
print(value,next_node)



