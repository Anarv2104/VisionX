class User:
    def __init__(self, id, username, email, password_hash, eth_address, collaborations=0, special_tag=False):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.eth_address = eth_address
        self.collaborations = collaborations
        self.special_tag = special_tag

    def get_id(self):
        return self.id

class Token:
    def __init__(self, id, name, symbol, initial_supply, contract_address):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.initial_supply = initial_supply
        self.contract_address = contract_address

class Event:
    def __init__(self, id, name, description, date, participants):
        self.id = id
        self.name = name
        self.description = description
        self.date = date
        self.participants = participants
