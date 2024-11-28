import json
import random
import os


class AnalyticsData:
    """
    An in memory persistence object.
    Declare more variables to hold analytics tables.
    """
    # statistics table 1
    # fact_clicks is a dictionary with the click counters: key = doc id | value = click counter
    fact_clicks = dict([])

    # statistics table 2 --> id 
    fact_two = dict([])

    # statistics table 3 --> agent
    fact_three = dict([])

    fact_query_terms = dict([])

    def open_data(self):
        if os.path.exists('data_collection.json'):
            print("OPEN")
            with open('data_collection.json', 'r') as f:
                data = json.load(f)
                self.fact_clicks = data.get('fact_clicks', {})
                self.fact_two = data.get('fact_two', {})
                self.fact_three = data.get('fact_three', {})
                self.fact_query_terms = data.get('fact_query_terms', {})

        else:
            with open('data_collection.json', 'w') as f:
                json.dump({'fact_clicks': self.fact_clicks, 'fact_two': self.fact_two, 'fact_three': self.fact_three, 'fact_query_terms': self.fact_query_terms}, f)
    
    def save_data(self):
        """Save the current data to the JSON file."""
        with open('data_collection.json', 'w') as f:
            json.dump({
                'fact_clicks': self.fact_clicks,
                'fact_two': self.fact_two,
                'fact_three': self.fact_three,
                'fact_query_terms': self.fact_query_terms
            }, f)
            print("SAVE IT")
        

    def save_query_terms(self, terms: str) -> int:
        if terms in self.fact_query_terms:
            self.fact_query_terms[terms] = self.fact_query_terms[terms] + 1
        else:
            self.fact_query_terms[terms] = 1
        return 0
    
    def save_clicks(self):
        self.save_data()
        return 0
    
    def save_session_terms(self,ip,agent) -> int:
        #self.open_data()
        if ip in self.fact_two:
            self.fact_two[ip] = self.fact_two[ip] + 1
        else:
            self.fact_two[ip] = 1

        agent_= str(agent)
        if agent_ in self.fact_three:
            self.fact_three[agent_] = [1+ self.fact_three[agent_][0],agent["platform"]["name"], agent["bot"], agent["browser"]["name"], agent["browser"]["version"]]
        else:
            self.fact_three[agent_] = [1,agent["platform"]["name"], agent["bot"], agent["browser"]["name"], agent["browser"]["version"]]
        
        self.save_data()
        return 0
            



class ClickedDoc:
    def __init__(self, doc_id, description, counter):
        self.doc_id = doc_id
        self.description = description
        self.counter = counter

    def to_json(self):
        return self.__dict__

    def __str__(self):
        """
        Print the object content as a JSON string
        """
        return json.dumps(self)
