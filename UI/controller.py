import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        self._view.dd.options.append(ft.dropdown.Option("Nessun filtro"))
        self._view.dd2.options.append(ft.dropdown.Option("Nessun filtro"))

        biblioteche = self._model.get_biblioteche()
        for b in biblioteche:
            self._view.dd.options.append(ft.dropdown.Option(b.nome))

        generi = self._model.get_generi()
        for g in generi:
            self._view.dd2.options.append(ft.dropdown.Option(g))

    # CALLBACKS DROPDOWN
    # TODO
    def handler_selezione_biblioteca(self, e):
        if self._view.dd.value is not None:
            self._biblioteca_selezionata = self._view.dd.value

    def handler_selezione_genere(self, e):
        if self._view.dd2.value is not None:
            self._genere_selezionato = self._view.dd2.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handler_mostra_libri(self, e):
        risultati = self._model.get_libri_filtrati(self._biblioteca_selezionata, self._genere_selezionato)

        self._view.lista_libri_filtrati.controls.clear()
        if not risultati:
            self._view.show_alert("Nessun libro soddisfa i criteri indicati.")
        else:
            for libro in risultati:
                self._view.lista_libri_filtrati.controls.append(ft.Text(str(libro)))

        self._view.update()
