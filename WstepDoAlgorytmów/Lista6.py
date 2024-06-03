import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq

# ---------------------------------------------------------------------------
# Zadanie 1 

np.random.seed(35)
random.seed(35)

def generuj_graf(n, p):
    lista = []
    for i in range(n + 1):
        sub = []
        for j in range(i+1):
            sub.append(random.randint(0, 100) / 100.0 < p)
        lista.append(sub)
    n = len(lista)

    macierz = np.zeros((n, n), dtype=int)
    wagi = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(len(lista[i])):
            if lista[i][j]:
                weight = random.randint(1, 10)
                macierz[i][j] = 1
                macierz[j][i] = 1
                wagi[i][j] = weight
                wagi[j][i] = weight

    return macierz, wagi

def dfs(graf, start, odwiedzony, czesci):
    stos = [start]
    while stos:
        wierzcholek = stos.pop()
        if not odwiedzony[wierzcholek]:
            odwiedzony[wierzcholek] = True
            czesci.append(wierzcholek)
            sasiad = np.where(graf[wierzcholek] == 1)[0]
            stos.extend(sasiad)
    return czesci

def polaczone(graf):
    n = graf.shape[0]
    odwiedzony = [False] * n
    czesci = []
    
    for wierzcholek in range(n):
        if not odwiedzony[wierzcholek]:
            czesc = dfs(graf, wierzcholek, odwiedzony, [])
            czesci.append(czesc)
    
    return czesci

def wizualizuj(graf, wagi, czesci):
    G = nx.from_numpy_array(graf)
    pos = nx.spring_layout(G, k=0.18, iterations=10)
    plt.figure(figsize=(12, 9))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(czesci)))
    for czesc, color in zip(czesci, colors):
        nx.draw_networkx_nodes(G, pos, nodelist=czesc, node_color=[color], node_size=300, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=1)
    labels = { (i, j): f"{wagi[i][j]}" for i in range(len(graf)) for j in range(len(graf)) if graf[i][j] }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_labels(G, pos, font_size=12)
    plt.title("Grafy z wagami")
    plt.show()

# liczba wierzchołków
n = 20  
# prawdopodobieństwo połączenia
p = 0.1 

graf, wagi = generuj_graf(n, p)

polaczone_grafy = polaczone(graf)

for id, czesc in enumerate(polaczone_grafy):
    print(f"Graf {id + 1}: {czesc}")

wizualizuj(graf, wagi, polaczone_grafy)

# ---------------------------------------------------------------------------
# Zadanie 2 
def dijkstra(graf, wagi, start, end):
    n = graf.shape[0]
    distances = {node: float('inf') for node in range(n)}
    previous_nodes = {node: None for node in range(n)}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor in np.where(graf[current_node] == 1)[0]:
            distance = current_distance + wagi[current_node][neighbor]
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    path, total_distance = [], distances[end]
    if total_distance < float('inf'):
        while end is not None:
            path.insert(0, end)
            end = previous_nodes[end]
    
    return path, total_distance

def wizualizuj_sciezka(graf, wagi, czesci, path=None):
    G = nx.from_numpy_array(graf)
    for i in range(len(graf)):
        for j in range(i):
            if graf[i][j]:
                G[i][j]['weight'] = wagi[i][j]
    
    pos = nx.spring_layout(G, k=0.3, iterations=10, weight='weight')
    
    plt.figure(figsize=(12, 9))
    colors = plt.cm.rainbow(np.linspace(0, 1, len(czesci)))
    for czesc, color in zip(czesci, colors):
        nx.draw_networkx_nodes(G, pos, nodelist=czesc, node_color=[color], node_size=300, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    labels = { (i, j): f"{wagi[i][j]:.2f}" for i in range(len(graf)) for j in range(len(graf)) if graf[i][j] }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_labels(G, pos, font_size=12)
    
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=2.0, alpha=0.8, edge_color='r')
    
    plt.title("Grafy z wagami i najkrótszą ścieżką")
    plt.show()

# tutaj wybieram losowo ale skoro seet jest ustawiony to wybiore "lepsze"
start_node = random.randint(0, n-1)
end_node = random.randint(0, n-1)
while start_node == end_node:
    end_node = random.randint(0, n-1)
start_node = 18
end_node = 16

print(f"Start: {start_node}, Koniec: {end_node}")

path, total_distance = dijkstra(graf, wagi, start_node, end_node)

if path:
    print(f"Najkrótsza ścieżka: {path}")
    print(f"Całkowita odległość: {total_distance}")
else:
    print("Nie istnieje ścieżka między wybranymi wierzchołkami.")

wizualizuj_sciezka(graf, wagi, polaczone_grafy, path if path else None)


# ---------------------------------------------------------------------------
# Zadanie 3

# Algorytm Kruskala
def kruskal(graf, wagi):
    krawedzie = []
    n = graf.shape[0]
    
    for i in range(n):
        for j in range(i + 1, n):
            if graf[i][j] == 1:
                krawedzie.append((wagi[i][j], i, j))
    
    krawedzie.sort()
    
    rodzic = list(range(n))
    ranga = [0] * n
    
    def znajdz(wezly):
        if rodzic[wezly] != wezly:
            rodzic[wezly] = znajdz(rodzic[wezly])
        return rodzic[wezly]
    
    def polacz(wezly1, wezly2):
        korzen1 = znajdz(wezly1)
        korzen2 = znajdz(wezly2)
        
        if korzen1 != korzen2:
            if ranga[korzen1] > ranga[korzen2]:
                rodzic[korzen2] = korzen1
            elif ranga[korzen1] < ranga[korzen2]:
                rodzic[korzen1] = korzen2
            else:
                rodzic[korzen2] = korzen1
                ranga[korzen1] += 1
    
    mst = []
    calkowita_waga = 0
    for waga, u, v in krawedzie:
        if znajdz(u) != znajdz(v):
            polacz(u, v)
            mst.append((u, v, waga))
            calkowita_waga += waga
    
    return mst, calkowita_waga

# Algorytm Prima
def prim(graf, wagi):
    n = graf.shape[0]
    wybrane = [False] * n
    # (waga, start, koniec)
    pq = [(0, 0, 0)]  
    mst = []
    calkowita_waga = 0

    while pq:
        waga, u, v = heapq.heappop(pq)
        if not wybrane[v]:
            wybrane[v] = True
            if u != v:
                mst.append((u, v, waga))
                calkowita_waga += waga
            
            for sasiad in np.where(graf[v] == 1)[0]:
                if not wybrane[sasiad]:
                    heapq.heappush(pq, (wagi[v][sasiad], v, sasiad))
    
    return mst, calkowita_waga

def wizualizuj_kruskal(graf, wagi, mst_kruskal):
    G = nx.from_numpy_array(graf)
    
    for i in range(len(graf)):
        for j in range(i):
            if graf[i][j]:
                G[i][j]['weight'] = wagi[i][j]
    
    pos = nx.spring_layout(G, weight='weight')
    
    plt.figure(figsize=(12, 9))
    
    nx.draw_networkx_nodes(G, pos, node_size=300, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    etykiety = {(i, j): f"{wagi[i][j]:.2f}" for i in range(len(graf)) for j in range(len(graf)) if graf[i][j]}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etykiety)
    nx.draw_networkx_labels(G, pos, font_size=12)
    
    kruskal_krawedzie = [(u, v) for u, v, waga in mst_kruskal]
    
    nx.draw_networkx_edges(G, pos, edgelist=kruskal_krawedzie, width=2.0, alpha=0.8, edge_color='r')
    plt.title("Graf z MST Kruskal")
    plt.show()

def wizualizuj_prim(graf, wagi, mst_prim):
    G = nx.from_numpy_array(graf)
    
    # Dodaj wagi do krawędzi
    for i in range(len(graf)):
        for j in range(i):
            if graf[i][j]:
                G[i][j]['weight'] = wagi[i][j]
    
    pos = nx.spring_layout(G, weight='weight')
    
    plt.figure(figsize=(12, 9))
    
    nx.draw_networkx_nodes(G, pos, node_size=300, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    etykiety = {(i, j): f"{wagi[i][j]:.2f}" for i in range(len(graf)) for j in range(len(graf)) if graf[i][j]}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etykiety)
    nx.draw_networkx_labels(G, pos, font_size=12)
    
    prim_krawedzie = [(u, v) for u, v, waga in mst_prim]
    
    nx.draw_networkx_edges(G, pos, edgelist=prim_krawedzie, width=2.0, alpha=0.8, edge_color='g', style='dashed')
    
    plt.title("Graf z MST Prim")
    plt.show()


# MST algorytm Kruskala
mst_kruskal, calkowita_waga_kruskal = kruskal(graf, wagi)
print("MST algorytmu Kruskala:")
for u, v, waga in mst_kruskal:
    print(f"{u} - {v}: {waga:.2f}")
print(f"Całkowita waga: {calkowita_waga_kruskal:.2f}\n")

# MST algorytm Prima
mst_prim, calkowita_waga_prim = prim(graf, wagi)
print("MST algorytmu Prima:")
for u, v, waga in mst_prim:
    print(f"{u} - {v}: {waga:.2f}")
print(f"Całkowita waga: {calkowita_waga_prim:.2f}\n")

# Wizualizacje grafu z MST
wizualizuj_kruskal(graf, wagi, mst_kruskal)
wizualizuj_prim(graf, wagi, mst_prim)