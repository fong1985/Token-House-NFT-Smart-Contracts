pragma solidity ^0.5.5;
# import smart contract template
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract PropertyRegistry is ERC721Full {
    constructor() public ERC721Full("PropertyRegistryToken", "PROPERTY") {}

    struct Property {
        string name;
        string developer;
        uint256 appraisalValue;
    }

    mapping(uint256 => Property) public propertyCollection;

    event Appraisal(uint256 tokenId, uint256 appraisalValue, string reportURI);

# Details of the property 
    function registerProperty(
        address owner,
        string memory name,
        string memory developer,
        uint256 initialAppraisalValue,
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = totalSupply();

        _mint(owner, tokenId);
        _setTokenURI(tokenId, tokenURI);

        propertyCollection[tokenId] = Property(name, developer, initialAppraisalValue);

        return tokenId;
    }

    function newAppraisal(
        uint256 tokenId,
        uint256 newAppraisalValue,
        string memory reportURI
    ) public returns (uint256) {
        propertyCollection[tokenId].appraisalValue = newAppraisalValue;

        emit Appraisal(tokenId, newAppraisalValue, reportURI);

        return propertyCollection[tokenId].appraisalValue;
    }
}
