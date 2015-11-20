# from django.db import models

class Department():

    strategy = None
    resources = None
    structure = None
    rewards = None
    processes = None

    def __init__(self, strategy=None,structure=None, resources=None,  rewards=None, processes=None):
        
        self.strategy = strategy
        self.structure = structure
        self.resources = resources
#         self.rewards = rewards
#         self.processes = processes

    def execute(self, departments):
        
        return None

class Product(Department):

    def __init__(self):

        self.strategy = "Capture of opportunities via product development & innovation"
        self.resources = "Product development"
        self.structure = "Specialist"

    def execute(self, departments):
        
        if Marketing in departments:
            return "Product optimized for long-term market"

        if Sales in departments or BusinessDevelopment in departments:
            return "Product optimized for short-term wins"
        
class Marketing(Department):

    def __init__(self):

        self.strategy = "Discovery and creation of global optima opportunities"
        self.resources = ["Market research & sizing", "Collateral", 
                          "Lead pipeline generation"]
        self.structure = "Connector"

    def execute(self, departments=None):
        
        return "Go-to-market strategy"
    
class Sales(Department):
  
    def __init__(self):
  
        self.strategy = "Growth via direct customer engagement"
        self.resources = ["Prospecting & qualification", "Negotiation"]
        self.structure = "Specialist"

    def execute(self, departments):
        
        # return "$$$"
        return "Distribution"

class BusinessDevelopment(Department):

    def __init__(self):

        self.strategy = "Leveraged growth via strategic business partnerships"
        self.resources = ["Partner research", "Relationships", "Dealmaking"]
        self.structure = "Broker"

    def execute(self, departments):
        
        if Product in departments and Marketing in departments:
            return ["Lighthouse customer wins", "Leveraged partnership growth"]
        
        else:
            raise ValueError("\_(ツ)_/¯")

    
class PlatformRelations(BusinessDevelopment):

    def __init__(self):

        self.strategy = "Leveraged growth via technical integrations"
        self.resources = ["Ecosystem research", "Relationships", "Product integration"]
        self.structure = "Broker"

    def execute(self, departments):
        
        return ["Lighthouse customer wins", "Leveraged platform growth"]
        
