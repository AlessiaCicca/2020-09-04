import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}
        self.nodirankok=[]
    def creaGrafo(self,rank):
        self.nodi = DAO.getNodi()
        for nodo in self.nodi:
            if nodo.rank>rank:
                self.nodirankok.append(nodo)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v.id] = v
        self.addEdges(rank)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self, rank):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni(rank)
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def analisi(self):
        dizio={}
        for nodo in self.grafo:
            somma=0
            for vicino in self.grafo.neighbors(nodo):
                somma+=self.grafo[nodo][vicino]["weight"]
            dizio[nodo.id]=somma
        dizioOrder=list(sorted(dizio.items(), key=lambda item:item[1], reverse=True))
        return self._idMap[dizioOrder[0][0]],dizioOrder[0][1]
