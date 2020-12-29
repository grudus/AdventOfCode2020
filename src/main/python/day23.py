class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self): return str(self.data)

class LinkedCircularList:
    def __init__(self, nodes):
        self.dataMap = {}
        self.maxValue = max(nodes)
        self.minValue = min(nodes)
        
        node = Node(data=nodes.pop(0))
        self.head = node
        self.dataMap[node.data] = node

        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
            self.dataMap[elem] = node

        node.next = self.head # circular loop

    def __repr__(self):
        node = self.head
        first_value = node.data
        nodes = [str(first_value)]
        node = node.next
        while node.data != first_value: # prevent infinite loop
            nodes.append(str(node.data))
            node = node.next

        return "".join(nodes)

    def find_smaller_value(self, node: Node, values_to_ignore) -> Node:
        decrease_in_range = lambda value: value - 1 if value > self.minValue else self.maxValue
    
        searched = decrease_in_range(node.data)
        while searched in values_to_ignore: searched = decrease_in_range(searched)
        return self.dataMap[searched]



def first_star(cups):
    linked_cups = play_a_game(cups, 100)
    linked_cups.head = linked_cups.dataMap[1]
    return str(linked_cups)[1:]

def second_star(cups):
    cups = cups + list(range(max(cups) + 1, 1000000 + 1))
    linked_cups = play_a_game(cups, 10000000)
    node_1 = linked_cups.dataMap[1]
    return node_1.next.data * node_1.next.next.data

def play_a_game(cups, number_of_plays) -> LinkedCircularList:
    linked_cups = LinkedCircularList(cups)
    current_cup = linked_cups.head
    for _ in range(number_of_plays): current_cup = move_cups(linked_cups, current_cup)
    return linked_cups


def move_cups(cups: LinkedCircularList, current_cup: Node):
    picked = [current_cup.next, current_cup.next.next, current_cup.next.next.next]
    current_cup.next = picked[-1].next

    destination = cups.find_smaller_value(current_cup, values_to_ignore=[cup.data for cup in picked])
    picked[-1].next = destination.next
    destination.next = picked[0]
    
    return current_cup.next


if __name__ == "__main__":
    cups = list(open('src/main/resources/day23/input.txt', 'r').read())
    cups = [int(cup) for cup in cups]
    print(first_star(cups[:]))
    print(second_star(cups[:]))