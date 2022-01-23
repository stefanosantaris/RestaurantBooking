# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.actions import ActionOpenMap

import os


class OpenMap(ActionOpenMap):

    def name(self) -> Text:
        return "action_open_map"

    def run(self, dispatcher: CollectingDispatcher) :
        os.system("open https://g.page/menomale-kungsholmen?share")
        
