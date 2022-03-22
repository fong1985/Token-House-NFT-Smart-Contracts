# Token House

## Your solution to Tokenizing Property

### Project Overview
Our objective was to create a decentralized Real Estate platform where users can create property transactions without passing through agents and third party consultants. 

Users could upload their property to the DApp, have it appraised, convert it to an NFT and then proceed to sell their property via an auction. 


### Tokenization of the NFT
The first step of the platform is to tokenize properties that vendors want to sell into tokens.

The tokenization follows the standard ERC-721 template for NFTs.

Next, we created a Python streamlit application (app.py) to create a friendly userface so that vendors enter the details of the property (Name of the property if necessary, estimated price, pictures, address etc.)

The NFT needs to be deployed prior to the auction contract.



### Auction Contract

The 'Auction Contract' follows the layout of an English Auction.

A starting price is set by the seller and a time limit given for the auction.

Bidders are able to bid for the NFT once the auction has started and can withdraw their funds after the auction if they are not successful. 

The 'Sale Contract' must be deployed prior to commencing the Token House Auction. 

[Token House Auction operation](https://youtu.be/8mTFvZqeJyc)

## Summary

The Team was able to successfully register a property and convert it into an NFT. 

That NFT was then sold to the highest bidder via an English Auction. 


## Analysis 

Further developments:

. UX for the Auction Contract to allow for a more client friendly interface. 

. Linking RP data via an API to allow sellers access to real time market information. This would give them an indication of what their property is worth in the current market. 

. The streamlit app seem to have some technical errors when trying to deploy a token. A stable version is necessary in order to ensure reliability of the program. 

. Crowfunding would be an evolved phase of this project. Instead of only creating a single NFT representing a specific property, allowing to break it down to multiple tokens would allow multiple ownership of a property, which could be beneficial for investors looking for property to hold reliable passive income.


# Project Resources

* [Remix - Solidity IDE](https://remix.ethereum.org/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Truffle Framework](https://truffleframework.com/)
* [Ganache - One Click Blockchain](https://truffleframework.com/ganache)
* [Open Zeppelin ](https://openzeppelin.org/)



