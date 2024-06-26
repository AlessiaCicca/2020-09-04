import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
       rank=self._view.txt_rank.value
       if rank=="":
           self._view.create_alert("Inserire un parametro per il rank")
           return
       grafo = self._model.creaGrafo( float(rank))
       self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
       self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                     f"{self._model.getNumNodes()} nodi."))
       self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                     f"{self._model.getNumEdges()} archi."))
       self._view.update_page()

    def handle_massimo(self, e):
       migliore=self._model.analisi()
       self._view.txt_result.controls.append(ft.Text(f"{migliore[0]} ({migliore[1]})"))
       self._view.update_page()

    def handle_cammino(self, e):
       pass
