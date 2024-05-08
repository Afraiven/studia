import copy


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.temp = None

    def insert_left(self, key):
        t = BinaryTree(key)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def insert_right(self, key):
        t = BinaryTree(key)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t
    
    def find_path_to(self, desired_key):
        if self.key == desired_key:
            return [self] 

        if self.left:
            path = self.left.find_path_to(desired_key)
            if path is not None:  
                return [self] + path

        if self.right:
            path = self.right.find_path_to(desired_key)
            if path is not None:
                return [self] + path

        return None
    
    def print_tree(self, indent="", last="root"):
        if self.right:
            self.right.print_tree(indent + ("│   " if last == "left" else "    "), "right")

        print(indent + ("└──" if last == "left" else "┌──" if last == "right" else ""), self.key)

        if self.left:
            self.left.print_tree(indent + ("│   " if last == "right" else "    "), "left")

    def __str__(self):
        return f"[{self.key}; {self.left}; {self.right}]"
    
class Queue:
    def __init__(self):
        self.queue = []

    def head(self):
        return self.queue[0]
    
    def tail(self):
        return self.queue[-1]
    
    def add_to_queue(self, item):
        self.queue.append(item)

    def remove_from_queue(self):
        self.queue.pop(0)

    def get_list(self):
        return self.queue

class Stack:
    def __init__(self):
        self.stack = []

    def get_stack_top(self):
        return self.stack[-1]
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def get_list_of_keys(self):
        return [k.key for k in self.stack]
    
# inicjalizowanie drzewa o zadanej strukturze
#         a
#        / \
#       b   c
#      /|   |\
#     d e   f g
#    /  |\    |\
#   h   i j   k l

a = BinaryTree('A')
a.insert_left('B')
b = a.left
a.insert_right('C')
c = a.right

b.insert_left('D')
d = b.left
b.insert_right('E')
e = b.right

d.insert_left("H")
e.insert_left("I")
e.insert_right("J")

c.insert_left("F")
c.insert_right("G")
g = c.right
g.insert_left("K")
g.insert_right("L")

# ---------------------------------------------------------------------------
# Zadanie 1 
# breadth first search

# Stwórz pustą kolejkę  q
# Oznacz  t0 jako odkryty i umieść go na końcu  q
# Dopóki  q jest niepusta:
# 3a. Weź wierzchołek  t z początku kolejki.
# 3b. Oznacz nieodwiedzone, nieodkryte sąsiady  t jako odkryte i umieść je na końcu  q
# 3c. Oznacz  t jako odwiedzony.

def BFS(korzen):
    # lista na wynik
    result = []
    # pusta kolejka
    kolejka = Queue()
    kolejka.add_to_queue(korzen)
    while len(kolejka.get_list()) > 0:
        lewy = kolejka.head().left
        prawy = kolejka.head().right
        if lewy is not None:
            kolejka.add_to_queue(lewy)
        if prawy is not None:
            kolejka.add_to_queue(prawy)
        result.append(kolejka.head())
        kolejka.remove_from_queue()
    return result

# algorytm bfs dla drzewa [a]
bfs = BFS(a)
print("Klucze z drzewa, metoda: bfs")
print([x.key for x in bfs])

# ---------------------------------------------------------------------------
# Zadanie 1
# depth first search

def DFS(korzen):
    # lista na wynik
    result = []
    # pusty stos
    stos = Stack()
    stos.push(korzen)
    while len(stos.get_list_of_keys()) > 0:
        lewy = stos.get_stack_top().left
        prawy = stos.get_stack_top().right
        
        result.append(stos.get_stack_top())
        stos.pop()

        if lewy is not None:
            stos.push(lewy)
        if prawy is not None:
            stos.push(prawy)
    return result
        
# algorytm dfs dla drzewa [a]
dfs = DFS(a)
print("Klucze z drzewa, metoda: dfs")
print([x.key for x in dfs])

# ---------------------------------------------------------------------------
# Zadanie 2
# new root
#         a                     d
#        / \                   / \
#       b   c       <d>       h   b
#      /|   |\      --->         / \
#     d e   f g                 e   a
#    /  |\    |\               /|    \
#   h   i j   k l             i j     c
#                                    / \
#                                   f   g
#                                      / \
#                                     k   l
#
# Aby utworzyc nowy <korzeń> musi on mieć maksymalnie jedno dziecko (związek z pełnością)


# funkcja przyjmuje obiekt old_root oraz obiekt nowego korzenia
def newRoot(old_root, new_root):
    if new_root.left is not None and new_root.right is not None:
        print("Nowy korzeń nie spełnia zasady: korzeń ma 3 krawędzie (2 dzieci)")
        return 0
    
    # OPTYMALIZACJA
    # ||| algorytm działa tylko na lini stary-nowy korzeń |||
    # nie trzeaba zmieniać tej częsci drzewa, która jest w innym poddrzewie względem nowego korzenia
    # ALGORYTM
    # 1. wyznaczam scieżkę w dół od starego do nowego korzenia
    # 2. ide od góry ścieżką (od starego korzenia) aż dojde do nowego korzenia
    #    - ustawiam obecny wierzchołek jako self.temp swojego dziecka ze scieżki ( tymczasowe dziecko )
    #    - wydziedziczam kolejny element z dzieci obecnego wierzchołka
    #    - sprawdzam obecny wierzchołek ma self.temp
    #       - jeśli ma: sprawdzam które z dzieci obecnego wierzchołka jest None
    #         i zamieniam self.temp z nim              
    #    - przechodze dalej
    
    sciezka = old_root.find_path_to(new_root.key)
    for i in range(len(sciezka)):
        # dla wszystkich oprócz nowego korzenia
        if i < len(sciezka) - 1:
            # wydziedzicz i ustaw temp child
            sciezka[i+1].temp = sciezka[i]
            if sciezka[i].left == sciezka[i+1]:
                sciezka[i].left = None
            elif sciezka[i].right == sciezka[i+1]:
                sciezka[i].right = None
        if i != 0:
            # wstaw w odpowiednie miejsce temp dzieci
            if sciezka[i].temp:
                if sciezka[i].left is None:
                    sciezka[i].left = sciezka[i].temp
                if sciezka[i].right is None:
                    sciezka[i].right = sciezka[i].temp
                sciezka[i].temp = None
        
# narysuj drzewo
print("-"*40)
print("Drzewo")
a.print_tree()
drzewo_cztery_poziomy = copy.deepcopy(a)
print("-"*40)
newRoot(a, a.left.left)
# narysuj drzewo
print("Drzewo po wybraniu nowego korzenia")
d.print_tree()

# ---------------------------------------------------------------------------
# Zadanie 3
print("-"*40)
print("Zadanie 3")
drzewo_cztery_poziomy.print_tree()

def modifiedDFS(korzen):
    # lista na wynik
    result = []
    # pusty stos
    stos = Stack()
    levels = Stack()
    level = 1
    stos.push(korzen)
    levels.push(level)
    while len(stos.get_list_of_keys()) > 0:
        wiercholek = stos.get_stack_top()
        level = levels.get_stack_top()

        stos.pop()
        levels.pop()

        result.append([wiercholek, level])

        if wiercholek.right is not None:
            stos.push(wiercholek.right)
            levels.push(level + 1)

        if wiercholek.left is not None:
            stos.push(wiercholek.left)
            levels.push(level + 1)
    return result

def DFS_liscie(korzen):
    # lista na wynik
    result = []
    # pusty stos
    stos = Stack()
    stos.push(korzen)
    while len(stos.get_list_of_keys()) > 0:
        lewy = stos.get_stack_top().left
        prawy = stos.get_stack_top().right
        obecny = stos.get_stack_top()
        stos.pop()

        if lewy is not None:
            stos.push(lewy)
        if prawy is not None:
            stos.push(prawy)
        if prawy is None and lewy is None:
            result.append(obecny)
    return result


dfs_drzewa = modifiedDFS(drzewo_cztery_poziomy)
analiza_glebokosci = [[x[0].key, x[1]] for x in dfs_drzewa]
max_depth = max([x[1] for x in dfs_drzewa])
liscie = DFS_liscie(drzewo_cztery_poziomy)
liscie = [x.key for x in liscie]
level_count = {}
for _, level in analiza_glebokosci:
    if level in level_count:
        level_count[level] += 1
    else:
        level_count[level] = 1
for key, value in level_count.items():
    print(f"Na głębokości {key} jest {value} wierzchołków")
print(f"Liście to {liscie}, jest ich {len(liscie)}")

najkrotsza_sciezka = max_depth
sciezki = []
for lisc in liscie:
    sciezka = [x.key for x in drzewo_cztery_poziomy.find_path_to(lisc)]
    if len(sciezka) == najkrotsza_sciezka:
        sciezki.append(lisc)
    elif len(sciezka) < najkrotsza_sciezka:
        najkrotsza_sciezka = len(sciezka)
        sciezki = [lisc]
print(analiza_glebokosci)
print(f"Najkrótsza ścieżka do liścia to {najkrotsza_sciezka}, i są to scieżki do {sciezki}")
na_wysokosci_liscia = []
for wierzchlek, level in analiza_glebokosci:
    if level == najkrotsza_sciezka:
        na_wysokosci_liscia.append(wierzchlek)

print(f"Na tej głębokości znajdują się nastepujace liscie: {na_wysokosci_liscia}")