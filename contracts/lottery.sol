// SPDX-License-Identifier
pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";


contract lottery {

    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor(address _priceFeedAdress) public {
        usdEntryFee = 50 * (10**18);        //50$
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAdress);
    }


    function enter() public payable {
        //50$
        players.push(msg.sender);
    }

    function getEntraceFee() public view returns (uint256) { 

        (, int256 price, , , ) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10; //18 decimals
        uint256 costToEnter = (usdEntryFee * 10**18) / adjustedPrice;

        return costToEnter;
    }

    function startLottery() public{}

    function endLottery() public{}


}