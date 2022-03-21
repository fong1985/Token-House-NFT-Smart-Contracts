import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# The Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/property_abi.json')) as f:
        property_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=property_abi
    )

    return contract

contract = load_contract()


################################################################################
# Register New Property
################################################################################
st.title("Register New Property")
accounts = w3.eth.accounts

address = st.selectbox("Select Property Owner", options=accounts)

# Use a Streamlit component to get the Property's URI
property_uri = st.text_input("The URI to the Property")

if st.button("Register Property"):

    # Use the contract to send a transaction to the registerProperty function
    tx_hash = contract.functions.registerProperty(
        address,
        property_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))

st.markdown("---")

################################################################################
# Display a Token
################################################################################
st.markdown("## Display a Property Token Token")

selected_address = st.selectbox("Select Account", options=accounts)

tokens = contract.functions.balanceOf(selected_address).call()

st.write(f"This address owns {tokens} tokens")

token_id = st.selectbox("Property Tokens", list(range(tokens)))

if st.button("Display"):

    # Use the contract's `ownerOf` function to get the Property token owner
    owner = contract.functions.ownerOf(token_id).call()

    st.write(f"The token is registered to {owner}")

    # Use the contract's `tokenURI` function to get the Property token's URI
    token_uri = contract.functions.tokenURI(token_id).call()

    st.write(f"The tokenURI is {token_uri}")
    st.image(token_uri)
