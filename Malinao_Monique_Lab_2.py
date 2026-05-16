class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


def insertNodeAtTheBeginning(data):
    global head

    newNode = Node(data)

    if head is None:
        head = newNode
    else:
        newNode.next = head
        head = newNode


def traverseLinkedList():
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


def insertNodeAtTheEnd(data):
    global head

    newNode = Node(data)

    if head is None:
        head = newNode
    else:
        current = head

        while current.next is not None:
            current = current.next

        current.next = newNode


def insertNodeAfterGivenNode(data, node):
    global head

    current = head

    while current is not None:
        if current.data == node:
            newNode = Node(data)

            newNode.next = current.next
            current.next = newNode
            return

        current = current.next

    print("The node does not exist")


# Initial node
node1 = Node('Buksan mo by Willie Revillame')
head = node1


# Insert at beginning
insertNodeAtTheBeginning('Ale by The Bloomfields')
insertNodeAtTheBeginning('Narda by Kamikazee')
insertNodeAtTheBeginning('Elesi by Rivermaya')

traverseLinkedList()


# Insert at end
insertNodeAtTheEnd('Ang Huling El Bimbo by Eraserheads')
insertNodeAtTheEnd('Kisapmata by Rivermaya')

traverseLinkedList()


# Insert after given node
insertNodeAfterGivenNode(
    'Line to Heaven by Introvoys',
    'Ale by The Bloomfields'
)

insertNodeAfterGivenNode(
    'Kanlungan by Noel Cabangon',
    'Narda by Kamikazee'
)

traverseLinkedList()