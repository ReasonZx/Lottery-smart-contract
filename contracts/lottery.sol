// SPDX-License-Identifier
pragma solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract lottery is VRFConsumerBase, Ownable{

    enum LOTTERY_STATE{
        OPEN,
        CLOSED,
        CALCULATING_WINNER
    }

    address payable[] public players;
    address payable public winner;
    uint256 public randomness;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;
    LOTTERY_STATE public LotteryState;
    uint256 public fee;
    bytes32 public keyhash;
    event RequestedRandomness(bytes32 requestId);


    constructor(address _priceFeedAdress, address _vrfCoordinator, address _link, uint256 _fee, bytes32 _keyhash) public VRFConsumerBase(_vrfCoordinator, _link) {
        usdEntryFee = 50 * (10**18);        //50$
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAdress);
        LotteryState = LOTTERY_STATE.CLOSED;
        fee = _fee;
        keyhash = _keyhash;
    }


    function enter() public payable {
        require(LotteryState == LOTTERY_STATE.OPEN, "Lottery not started yet");
        require(msg.value >= getEntraceFee(), "Not enough ETH"); 
        players.push(msg.sender);
    }

    function getEntraceFee() public view returns (uint256) { 

        (, int256 price, , , ) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10; //18 decimals
        uint256 costToEnter = (usdEntryFee * 10**18) / adjustedPrice;

        return costToEnter;
    }

    function startLottery() public onlyOwner {
        require(LotteryState == LOTTERY_STATE.CLOSED, "Can't start a lottery");
        LotteryState = LOTTERY_STATE.OPEN;
    }

    function endLottery() public{

        LotteryState = LOTTERY_STATE.CALCULATING_WINNER;
        bytes32 requestId = requestRandomness(keyhash,fee);
        emit RequestedRandomness(requestId);
        
    }

    function fulfillRandomness(bytes32 _requestId, uint256 _randomness) internal override {
        require(LotteryState == LOTTERY_STATE.CALCULATING_WINNER, "Not calculating winner yet");
        require(_randomness > 0, "random not found");
        //calculate winner
        uint256 indexOfWinner = _randomness % players.length;
        winner = players[indexOfWinner];

        //transfer all balance of smartcontract to winner
        winner.transfer(address(this).balance);

        //reset lottery
        players = new address payable[](0);
        LotteryState = LOTTERY_STATE.CLOSED;
        randomness = _randomness;
    }
}