from web3 import Web3
from eth_account import Account

wallet = '0x54643E14E6C30b5FBBC6d90eF1b42d7ad45b52bD'
private_key = 'e44a63ff02e33a7f30230bdf0a4185418c1c2bc96fdc585dd82e778c12cf1440'

abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "target",
                "type": "address"
            }
        ],
        "name": "AddressEmptyCode",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "ERC1967InvalidImplementation",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967NonPayable",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FailedInnerCall",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidInitialization",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NotInitializing",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "OwnableInvalidOwner",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "OwnableUnauthorizedAccount",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ReentrancyGuardReentrantCall",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UUPSUnauthorizedCallContext",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "slot",
                "type": "bytes32"
            }
        ],
        "name": "UUPSUnsupportedProxiableUUID",
        "type": "error"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "payouts",
                "type": "uint256[]"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "proposer",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "answerCid",
                "type": "string"
            }
        ],
        "name": "AnswerProposed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "wallet",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "fpmmAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "investmentAmount",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "feeAmount",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "outcomeTokensBought",
                "type": "uint256"
            }
        ],
        "name": "BuyPosition",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amountRecovered",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            }
        ],
        "name": "FundingRecovered",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "uint64",
                "name": "version",
                "type": "uint64"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "initializerAddress",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "allowed",
                "type": "bool"
            }
        ],
        "name": "InitializerUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "payouts",
                "type": "uint256[]"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "resolver",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "answerCid",
                "type": "string"
            }
        ],
        "name": "MarketResolved",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "proposerAddress",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "allowed",
                "type": "bool"
            }
        ],
        "name": "ProposerUpdated",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "wallet",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "fpmmAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256[]",
                "name": "indexSets",
                "type": "uint256[]"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "totalPayout",
                "type": "uint256"
            }
        ],
        "name": "RedeemPosition",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "wallet",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "fpmmAddress",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "returnAmount",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "outcomeTokensSold",
                "type": "uint256"
            }
        ],
        "name": "SellPosition",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "FPMMFactory",
        "outputs": [
            {
                "internalType": "contract IFactory",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "UPGRADE_INTERFACE_VERSION",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "name": "answers",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "answerTimestamp",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "answerCid",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minOutcomeTokensToBuy",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "conditionTokensReceiver",
                "type": "address"
            }
        ],
        "name": "buyPosition",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minOutcomeTokensToBuy",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "buyPositionWithLocked",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minOutcomeTokensToBuy",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "buyPositionWithLockedOnBehalf",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minOutcomeTokensToBuy",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "deadline",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "nonce",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amount",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct OnchainPoints.Request",
                "name": "request",
                "type": "tuple"
            },
            {
                "internalType": "bytes",
                "name": "signature",
                "type": "bytes"
            }
        ],
        "name": "buyPositionWithSignature",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "minOutcomeTokensToBuy",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "deadline",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "nonce",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "amount",
                        "type": "uint256"
                    },
                    {
                        "internalType": "address",
                        "name": "owner",
                        "type": "address"
                    }
                ],
                "internalType": "struct OnchainPoints.DelegatedRequest",
                "name": "request",
                "type": "tuple"
            },
            {
                "internalType": "bytes",
                "name": "signature",
                "type": "bytes"
            }
        ],
        "name": "buyPositionWithSignatureOnBehalf",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "buyWithUnlockedEnabled",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "collateralToken",
        "outputs": [
            {
                "internalType": "contract WPOP",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "conditionalTokens",
        "outputs": [
            {
                "internalType": "contract ConditionalTokens",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "endTimestamp",
                "type": "uint256"
            },
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "outcomeSlots",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256"
            },
            {
                "internalType": "uint256[]",
                "name": "distributionHints",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256",
                "name": "initialFunding",
                "type": "uint256"
            }
        ],
        "name": "createMarket",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "emergencyWithdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getInitializers",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            }
        ],
        "name": "getMarketData",
        "outputs": [
            {
                "components": [
                    {
                        "components": [
                            {
                                "internalType": "uint256",
                                "name": "beginTimestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "endTimestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "uint256",
                                "name": "outcomeSlots",
                                "type": "uint256"
                            },
                            {
                                "internalType": "address",
                                "name": "fpmm",
                                "type": "address"
                            },
                            {
                                "internalType": "bytes32",
                                "name": "conditionId",
                                "type": "bytes32"
                            }
                        ],
                        "internalType": "struct PredictionsOracle.QuestionData",
                        "name": "questionData",
                        "type": "tuple"
                    },
                    {
                        "components": [
                            {
                                "internalType": "uint256[]",
                                "name": "payouts",
                                "type": "uint256[]"
                            },
                            {
                                "internalType": "uint256",
                                "name": "answerTimestamp",
                                "type": "uint256"
                            },
                            {
                                "internalType": "string",
                                "name": "answerCid",
                                "type": "string"
                            }
                        ],
                        "internalType": "struct PredictionsOracle.AnswerData",
                        "name": "answerData",
                        "type": "tuple"
                    },
                    {
                        "internalType": "uint256",
                        "name": "uniqueBuys",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "probabilities",
                        "type": "uint256[]"
                    },
                    {
                        "internalType": "uint256[]",
                        "name": "buyAmounts",
                        "type": "uint256[]"
                    }
                ],
                "internalType": "struct PredictionsOracle.MarketData",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256[]",
                "name": "indexSets",
                "type": "uint256[]"
            },
            {
                "internalType": "address",
                "name": "holder",
                "type": "address"
            }
        ],
        "name": "getPositionBalances",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "balances",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getProposers",
        "outputs": [
            {
                "internalType": "address[]",
                "name": "",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
        ],
        "name": "getRemainingBuyAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            }
        ],
        "name": "getUniqueBuys",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getUserOpenPositions",
        "outputs": [
            {
                "internalType": "bytes32[]",
                "name": "",
                "type": "bytes32[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "initialOwner",
                "type": "address"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "maxBuyAmountPerQuestion",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "minBuyAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "",
                "type": "uint256[]"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "onERC1155BatchReceived",
        "outputs": [
            {
                "internalType": "bytes4",
                "name": "",
                "type": "bytes4"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "name": "onERC1155Received",
        "outputs": [
            {
                "internalType": "bytes4",
                "name": "",
                "type": "bytes4"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256[]",
                "name": "payouts",
                "type": "uint256[]"
            },
            {
                "internalType": "string",
                "name": "answerCid",
                "type": "string"
            }
        ],
        "name": "proposeAndResolve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256[]",
                "name": "payouts",
                "type": "uint256[]"
            },
            {
                "internalType": "string",
                "name": "answerCid",
                "type": "string"
            }
        ],
        "name": "proposeAnswer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "name": "questions",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "beginTimestamp",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "endTimestamp",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "outcomeSlots",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "fpmm",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "conditionId",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256[]",
                "name": "indexSets",
                "type": "uint256[]"
            }
        ],
        "name": "recoverFundingToken",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256[]",
                "name": "indexSets",
                "type": "uint256[]"
            }
        ],
        "name": "redeemPosition",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "num",
                "type": "uint256"
            }
        ],
        "name": "redeemPositions",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            }
        ],
        "name": "resolveMarket",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "sellEnabled",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "questionId",
                "type": "bytes32"
            },
            {
                "internalType": "uint256",
                "name": "returnAmount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "outcomeIndex",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxOutcomeTokensToSell",
                "type": "uint256"
            }
        ],
        "name": "sellPosition",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "stopTradingBeforeMarketEnd",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "_buyWithUnlockedEnabled",
                "type": "bool"
            }
        ],
        "name": "updateBuyWithUnlockedEnabled",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "conditionalTokensAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "FPMMFactoryAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "collateralTokenAddress",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_onchainPointsAddress",
                "type": "address"
            }
        ],
        "name": "updateContracts",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "_initializers",
                "type": "address[]"
            },
            {
                "internalType": "bool[]",
                "name": "_status",
                "type": "bool[]"
            }
        ],
        "name": "updateInitializers",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_maxBuyAmountPerQuestion",
                "type": "uint256"
            }
        ],
        "name": "updateMaxBuyAmountPerQuestion",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_minBuyAmount",
                "type": "uint256"
            }
        ],
        "name": "updateMinBuyAmount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "_proposers",
                "type": "address[]"
            },
            {
                "internalType": "bool[]",
                "name": "_status",
                "type": "bool[]"
            }
        ],
        "name": "updateProposers",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "_sellEnabled",
                "type": "bool"
            }
        ],
        "name": "updateSellEnabled",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_stopTradingBeforeMarketEnd",
                "type": "uint256"
            }
        ],
        "name": "updateStopTradingBeforeMarketEnd",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "userBuyAmounts",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "userRedeemed",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "userSpendings",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]


rpc = 'https://rpc.onchainpoints.xyz'


w3 = Web3(Web3.HTTPProvider(rpc))

address = '0x83d68F41Ac028148FDA9Bf2eA16f9f0359A509F0'
kontrak = w3.eth.contract(address=address, abi=abi)

def get_balance():
    web3 = Web3(Web3.HTTPProvider(rpc))
    balance = web3.eth.get_balance(wallet)
    return round(web3.from_wei(balance, 'ether'))

def yes_unlocked(question_id, output_min, amount):
    tx = kontrak.functions.buyPosition(question_id, 0, output_min, wallet).build_transaction({
        'from': wallet,
        'value': amount,
        'gas': 600000,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(wallet)
    })
    try:
        gas_estimate = w3.eth.estimate_gas(tx)
        
        signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return True
    except Exception as e:
        print(e)
        return False

def no_unlocked(question_id, output_min, amount):
    tx = kontrak.functions.buyPosition(question_id, 1, output_min, wallet).build_transaction({
        'from': wallet,
        'gas': 600000,
        'value': amount,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(wallet)
    })
    try:
        gas_estimate = w3.eth.estimate_gas(tx)
        
        signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return True
    except Exception as e:
        print(e)
        return False


def yes_locked(question_id, output_min, amount):
    tx = kontrak.functions.buyPositionWithLocked(question_id, 0, output_min, amount).build_transaction({
        'from': wallet,
        'gas': 600000,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(wallet)
    })
    try:
        gas_estimate = w3.eth.estimate_gas(tx)
        
        signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return True
    except Exception as e:
        print(e)
        return False

def no_locked(question_id, output_min, amount):
    tx = kontrak.functions.buyPositionWithLocked(question_id, 1, output_min, amount).build_transaction({
        'from': wallet,
        'gas': 600000,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(wallet)
    })
    try:
        gas_estimate = w3.eth.estimate_gas(tx)
        
        signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return True
    except Exception as e:
        print(e)
        return False
        
def redeem(question_id):
    tx = kontrak.functions.redeemPosition(question_id, [1, 2]).build_transaction({
        'from': wallet,
        'gas': 500000,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(wallet)
    })
    try:
        gas_estimate = w3.eth.estimate_gas(tx)
        
        signed_txn = w3.eth.account.sign_transaction(tx, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        return True
    except Exception as e:
        print(e)
        return False

def is_answered(question_id):
    a = kontrak.functions.getMarketData(question_id).call()
    element = a[1]
    # print(element[-1])
    if element[-1] != "":
        return True
    else:
        return False
