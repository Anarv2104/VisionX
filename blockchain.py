from web3 import Web3
from solcx import compile_source
import json

# Setup Web3 connection
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))  # Replace with your provider
private_key = "your_private_key"  # Replace with your private key

# Compile contract
def compile_contract(contract_source_code):
    compiled_sol = compile_source(contract_source_code)
    contract_id, contract_interface = compiled_sol.popitem()
    return contract_interface

# Deploy contract
def deploy_contract(contract_interface):
    bytecode = contract_interface['bin']
    abi = contract_interface['abi']
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    # Get the transaction hash from deployed contract
    tx_hash = Contract.constructor().transact({'from': w3.eth.accounts[0], 'gas': 410000})
    
    # Get tx receipt to get contract address
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt.contractAddress

# Create predefined tokens
def create_predefined_tokens(amount, user_address):
    predefined_contract_source_code = '''
    pragma solidity ^0.8.0;

    contract PredefinedToken {
        string public name = "PredefinedToken";
        string public symbol = "PTK";
        uint8 public decimals = 18;
        uint256 public totalSupply;
        mapping(address => uint256) public balanceOf;

        constructor(uint256 initialSupply) {
            totalSupply = initialSupply * 10 ** uint256(decimals);
            balanceOf[msg.sender] = totalSupply;
        }

        function transfer(address _to, uint256 _value) public returns (bool success) {
            require(balanceOf[msg.sender] >= _value);
            balanceOf[msg.sender] -= _value;
            balanceOf[_to] += _value;
            return true;
        }
    }
    '''

    compiled_contract = compile_contract(predefined_contract_source_code)
    contract_address = deploy_contract(compiled_contract)

    contract = w3.eth.contract(
        address=contract_address,
        abi=compiled_contract['abi'],
    )

    tx_hash = contract.functions.transfer(user_address, amount).transact({'from': w3.eth.accounts[0], 'gas': 410000})
    w3.eth.waitForTransactionReceipt(tx_hash)

def get_predefined_balance(user_address):
    predefined_contract_source_code = '''
    pragma solidity ^0.8.0;

    contract PredefinedToken {
        string public name = "PredefinedToken";
        string public symbol = "PTK";
        uint8 public decimals = 18;
        uint256 public totalSupply;
        mapping(address => uint256) public balanceOf;

        constructor(uint256 initialSupply) {
            totalSupply = initialSupply * 10 ** uint256(decimals);
            balanceOf[msg.sender] = totalSupply;
        }

        function transfer(address _to, uint256 _value) public returns (bool success) {
            require(balanceOf[msg.sender] >= _value);
            balanceOf[msg.sender] -= _value;
            balanceOf[_to] += _value;
            return true;
        }
    }
    '''

    compiled_contract = compile_contract(predefined_contract_source_code)
    contract_address = deploy_contract(compiled_contract)

    contract = w3.eth.contract(
        address=contract_address,
        abi=compiled_contract['abi'],
    )

    return contract.functions.balanceOf(user_address).call()

def deploy_user_created_token(name, symbol, initial_supply):
    user_created_contract_source_code = f'''
    pragma solidity ^0.8.0;

    contract {name}Token {{
        string public name = "{name}";
        string public symbol = "{symbol}";
        uint8 public decimals = 18;
        uint256 public totalSupply;
        mapping(address => uint256) public balanceOf;

        constructor(uint256 initialSupply) {{
            totalSupply = initialSupply * 10 ** uint256(decimals);
            balanceOf[msg.sender] = totalSupply;
        }}

        function transfer(address _to, uint256 _value) public returns (bool success) {{
            require(balanceOf[msg.sender] >= _value);
            balanceOf[msg.sender] -= _value;
            balanceOf[_to] += _value;
            return true;
        }}
    }}
    '''

    compiled_contract = compile_contract(user_created_contract_source_code)
    contract_address = deploy_contract(compiled_contract)
    return contract_address
