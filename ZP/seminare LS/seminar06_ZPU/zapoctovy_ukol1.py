LABEL = 0
EDGES = 1



def add_edge(graph, f, to, value):
        for node in graph:
            if node[LABEL] == f:
                v = node
            elif node[LABEL] == to:
                w = node
            
        v[EDGES].append((w,value))
        w[EDGES].append((v,value))

"""def prvni_struktura(pocet_radku, pocet_sloupcu):
    radky = druha_struktura_radku(0, pocet_radku)
    sloupce = druha_struktura_sloupce(0, pocet_sloupcu)
    root = []
    if pocet_radku > 0:
        add_node(root, radky)
    if pocet_sloupcu > 0:
        add_node(root, sloupce)
    return root"""

############################################################¨
def add_node(graph, label):
    graph.append([label, []])

def vytvor_matici(pocet_radku, pocet_sloupcu):
    radky = druha_struktura_radku(0, pocet_radku)
    sloupce = druha_struktura_sloupce(0, pocet_sloupcu)
    root = [[],pocet_radku, pocet_sloupcu]
    if pocet_radku > 0:
        add_node(root, radky)
    if pocet_sloupcu > 0:
        add_node(root, sloupce)
    return root

def druha_struktura_radku(index, pocet_radku):
    radky = [index]
    if index+1 < pocet_radku:
        add_node(radky, druha_struktura_radku(index + 1, pocet_radku))
    return radky

def druha_struktura_sloupce(index, pocet_sloupcu):
    sloupce = [index]
    if index+1 < pocet_sloupcu:
        add_node(sloupce, druha_struktura_sloupce(index + 1, pocet_sloupcu))
    return sloupce


def add_edge(node, edge):
    node[1].append(edge)

def vloz_prvek(matice, prvek, radek, sloupec):
    pass
                

# Testování
matice = vytvor_matici(3, 3)
print(matice)
vloz_prvek(matice, 1, 1, 1)



