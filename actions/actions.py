# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

import pandas as pd


class DataExcel:
    def get_data_from_excel():
        concepts = pd.read_excel("data.xlsx", usecols=[2])
        return concepts
    
    def get_img_from_excel():
        images = pd.read_excel("data.xlsx", sheet_name="Images", usecols=[0])
        return images

class ActionDfsConcept(Action):
    def name(self) -> Text:
        return "dfs_concept"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        concepts_df = DataExcel.get_data_from_excel()
        dfs_concept = concepts_df.iloc[0, 0]
        dispatcher.utter_message(text=dfs_concept)
        return []

class ActionBfsConcept(Action):
    def name(self) -> Text:
        return "bfs_concept"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        concepts_df = DataExcel.get_data_from_excel()
        bfs_concept = concepts_df.iloc[1, 0]
        dispatcher.utter_message(text=bfs_concept)
        return []

class ActionHConcept(Action):
    def name(self) -> Text:
        return "h_concept"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        concepts_df = DataExcel.get_data_from_excel()
        h_concept = concepts_df.iloc[2, 0]
        dispatcher.utter_message("Primeiramente precisamos saber que:")
        dispatcher.utter_message("Uma busca heurística, também conhecida como busca informada, faz uso de informações adicionais sobre o problema, o que ajuda no processo de busca de soluções")
        dispatcher.utter_message(text=h_concept)
        return []

class ActionGreedyConcept(Action):
    def name(self) -> Text:
        return "greedy_concept"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        concepts_df = DataExcel.get_data_from_excel()
        greedy_concept = concepts_df.iloc[3, 0]
        dispatcher.utter_message("Como exemplo de busca heurística, usaremos a Busca gananciosa:")
        dispatcher.utter_message(text=greedy_concept)
        return []
        
        
class ActionDfsImg(Action):
    def name(self) -> Text:
        return "img_dfsExample"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        images_df = DataExcel.get_img_from_excel()
        dfsimage = images_df.iloc[0,0]
        dispatcher.utter_message("Para exemplificar vamos pensar no seguinte caso da imagem a seguir, qual seria a solução a partir do nó raiz S, chegar a G, utilizando a busca em profundidade?")
        dispatcher.utter_message(image=dfsimage)
        return[]

class ActionBfsImg(Action):
    def name(self) -> Text:
        return "img_bfsExample"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        images_df = DataExcel.get_img_from_excel()
        bfsimage = images_df.iloc[2,0]
        dispatcher.utter_message("Como exemplo para esse conceito, temos o seguinte exercicio:")
        dispatcher.utter_message(image=bfsimage)
        dispatcher.utter_message("Através da busca em largura, a partir do nó raiz S, qual seria o caminho para encontrar G?")
        return[]

class ActionHImg(Action):
    def name(self) -> Text:
        return "img_HExample"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        images_df = DataExcel.get_img_from_excel()
        himage = images_df.iloc[4,0]
        dispatcher.utter_message("Ache o caminho de S para G utilizando a busca gananciosa:")
        dispatcher.utter_message(image=himage)
        return []
    


class ValidateDfsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_dfs_form"
    
    @staticmethod
    def dfs_db() -> List[Text]:
        return ["s->a->b->c->g", "s-a-b-c-g", "s a b c g"]
    
    def validate_dfs(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value in self.dfs_db():
            dispatcher.utter_message(text="Acertou!")
            return {"dfs": slot_value}
        else:
            dispatcher.utter_message(text="Resposta incorreta, tente novamente")
            return {"dfs": None}

class ValidateBfsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bfs_form"
    
    @staticmethod
    def bfs_db() -> List[Text]:
        return ["s->d->g", "s-d-g", "s d g"]
    
    def validate_bfs(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value in self.dfs_db():
            dispatcher.utter_message(text="Parabéns, você acertou!")
            return {"bfs": slot_value}
        else:
            dispatcher.utter_message(text="Resposta incorreta, tente novamente")
            return {"bfs": None}
        
class ValidateHForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_h_form"
    
    @staticmethod
    def h_db() -> List[Text]:
        return ["s->d->e->g", "s-d-e-g", "s d e g"]
    
    def validate_h(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Dict[Text, Any]:
        if slot_value in self.h_db():
            dispatcher.utter_message(text="Dale, acertou!")
            return {"h": slot_value}
        else:
            dispatcher.utter_message("Errou, pense mais um pouco")
            return {"h": None}
    
"""
class dataExcel:
    def getDataFromExcel():
        global concepts
        concepts = pd.read_excel("data.xlsx", usecols=[2])
        return concepts

content = dataExcel.getDataFromExcel()

concepts = content[0]

        #dfsConcept = df.iloc[0,0]
        #bfsConcept = df.iloc[0,1]

class ActionDfsConcept(Action):
    def name(self) -> Text:
        return "dfs_concepts"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global concepts
        dispatcher.utter_message(text=concepts[0])
        return[]

class ActionBfsConcept(Action):
    def name(self) -> Text:
        return "bfs_concepts"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global concepts
        dispatcher.utter_message(text=concepts[1])
        return[]
"""
"""
class ActionGetContentFromExcel(Action):
    def name(self) -> Text:
        return "get_concepts"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_excel('data.xlsx', usecols=[2])
        
        if not df.empty:
            concept = df.iloc[0,0]
            dispatcher.utter_message(text=concept)
        else:
            dispatcher.utter_message(text="Não achei a definição")

        return[]
"""




#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
