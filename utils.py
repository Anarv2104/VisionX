import re
from web3 import Web3
from solcx import compile_source

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def validate_eth_address(address):
    pattern = r'^0x[a-fA-F0-9]{40}$'
    return re.match(pattern, address)

# Blockchain interaction functions
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

def compile_contract(contract_source_code):
    compiled_sol = compile_source(contract_source_code)
    contract_id, contract_interface = compiled_sol.popitem()
    return contract_interface

def deploy_contract(contract_interface):
    bytecode = contract_interface['bin']
    abi = contract_interface['abi']
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = Contract.constructor().transact({'from': w3.eth.accounts[0], 'gas': 410000})
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt.contractAddress

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
    contract = w3.eth.contract(address=contract_address, abi=compiled_contract['abi'])
    tx_hash = contract.functions.transfer(user_address, amount).transact({'from': w3.eth.accounts[0], 'gas': 410000})
    w3.eth.waitForTransactionReceipt(tx_hash)
