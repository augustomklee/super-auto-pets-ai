"""


MIT License

Copyright (c) 2021 Ben Coveney

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


"""

Please note that these effects are from THIS VERSION XXX

In addition, there will be a new patch coming soon that will require singificant
modifications to these overall pet behaviors. 


After new patch updates:

  1. ammount -> amount
  2. Changed rabbit trigger from EatsShopFood to BuyFood
  3. Changed milk from "?" to 1-2 to multiply by cow level
  4. There isn't a cost in every food and pet item. Only for pill. 
  5. Dodo is copyattack without any indication that it should be additive and 
      is not a copy operation
  6. Bat target RandomEnergy -> NonWeakEnemy. Bat does not apply weak randomly. 
      It only applies weak to an enemy that is not already weak. 
  7. Update croc to 8,16,24
  8. Changed cat trigger from Hurt -> "PurchaseFood"
  9. Updating values to v0.16 for whale, swan, monkey, snail, and duck
  10.Delete old data that is not used

"""

data = {
    "pets": {
        "pet-otter": {
            "name": "Otter",
            "id": "pet-otter",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda6"
            },
            "tier": 1,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Buy: Give one random friend +1 health",
                "trigger": "Buy",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 1
                    },
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Buy: Give two random friends +1 health",
                "trigger": "Buy",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Buy: Give three random friends +1 health",
                "trigger": "Buy",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 3
                    },
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-blowfish": {
            "name": "Blowfish",
            "id": "pet-blowfish",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc21"
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Hurt: Deal 3 damage to a random enemy.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 3
                }
            },
            "level2Ability": {
                "description": "Hurt: Deal 6 damage to a random enemy.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 6
                }
            },
            "level3Ability": {
                "description": "Hurt: Deal 9 damage to a random enemy.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 9
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-duck": {
            "name": "Duck",
            "id": "pet-duck",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd86"
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Sell: Give shop animals +1 Health",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachShopAnimal",
                        "includingFuture": False
                    },
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Sell: Give shop animals +2 Health",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachShopAnimal",
                        "includingFuture": False
                    },
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Sell: Give shop animals +3 Health",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachShopAnimal",
                        "includingFuture": False
                    },
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-beaver": {
            "name": "Beaver",
            "id": "pet-beaver",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\uddab"
            },
            "tier": 1,
            "baseAttack": 3,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Sell: Give two random friends +1 attack",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Sell: Give two random friends +2 attack",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Sell: Give two random friends +3 attack",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-pigeon": {
            "name": "Pigeon",
            "id": "pet-pigeon",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc16"
            },
            "tier": 1,
            "baseAttack": 3,
            "baseHealth": 1,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Sell: Stock one free Bread Crumb",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "addBreadCrumb",
                    "shop": "Food",
                    "food": "food-bread-crumb"
                }
            },
            "level2Ability": {
                "description": "Sell: Stock two free Bread Crumbs",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "addBreadCrumb",
                    "shop": "Food",
                    "food": "food-bread-crumb"
                }
            },
            "level3Ability": {
                "description": "Sell: Stock three free Bread Crumbs",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "addBreadCrumb",
                    "shop": "Food",
                    "food": "food-bread-crumb"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-pig": {
            "name": "Pig",
            "id": "pet-pig",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc16"
            },
            "tier": 1,
            "baseAttack": 4,
            "baseHealth": 1,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Sell: Gain an extra 1 gold",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "GainGold",
                    "amount": 1
                }
            },
            "level2Ability": {
                "description": "Sell: Gain an extra 2 gold",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "GainGold",
                    "amount": 2
                }
            },
            "level3Ability": {
                "description": "Sell: Gain an extra 3 gold",
                "trigger": "Sell",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "GainGold",
                    "amount": 3
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-ant": {
            "name": "Ant",
            "id": "pet-ant",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc1c"
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Give a random friend +1/+1",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "target": {
                        "kind": "RandomFriend",
                        "n": 1
                    },
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Faint: Give a random friend +2/+2",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "target": {
                        "kind": "RandomFriend",
                        "n": 1
                    },
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Faint: Give a random friend +3/+3",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "target": {
                        "kind": "RandomFriend",
                        "n": 1
                    },
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-mosquito": {
            "name": "Mosquito",
            "id": "pet-mosquito",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd9f"
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Start of battle: Deal 1 damage to a random enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 1
                }
            },
            "level2Ability": {
                "description": "Start of battle: Deal 2 damage to a random enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 2
                    },
                    "amount": 1
                }
            },
            "level3Ability": {
                "description": "Start of battle: Deal 3 damage to a random enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 3
                    },
                    "amount": 1
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-fish": {
            "name": "Fish",
            "id": "pet-fish",
            "image": {
                "source": "fxemoji",
                "commit": "270af343bee346d8221f87806d2b1eee0438431a",
                "name": "fish",
                "unicodeCodePoint": "\ud83d\udc1f"
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Level-up: Give two friends +1/+1",
                "trigger": "LevelUp",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Level-up: Give two friends +2/+2",
                "trigger": "LevelUp",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-cricket": {
            "name": "Cricket",
            "id": "pet-cricket",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd97"
            },
            "tier": 1,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Summon a 1/1 Zombie Cricket",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-cricket",
                    "withAttack": 1,
                    "withHealth": 1,
                    "team": "Friendly"
                }
            },
            "level2Ability": {
                "description": "Faint: Summon a 2/2 Zombie Cricket",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-cricket",
                    "withAttack": 2,
                    "withHealth": 2,
                    "team": "Friendly"
                }
            },
            "level3Ability": {
                "description": "Faint: Summon a 3/3 Zombie Cricket",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-cricket",
                    "withAttack": 3,
                    "withHealth": 3,
                    "team": "Friendly"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793,
                        "ExpansionPack1": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-horse": {
            "name": "Horse",
            "id": "pet-horse",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc0e"
            },
            "tier": 1,
            "baseAttack": 2,
            "baseHealth": 1,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend summoned: Give it +1 Attack until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "attackAmount": 1,
                    "untilEndOfBattle": True
                }
            },
            "level2Ability": {
                "description": "Friend summoned: Give it +2 Attack until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "attackAmount": 2,
                    "untilEndOfBattle": True
                }
            },
            "level3Ability": {
                "description": "Friend summoned: Give it +3 Attack until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "attackAmount": 3,
                    "untilEndOfBattle": True
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.2976680384087793
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                }
            ]
        },
        "pet-snail": {
            "name": "Snail",
            "id": "pet-snail",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc0c"
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Buy: If you lost last battle, give all friends +1 health",
                "trigger": "BuyAfterLoss",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Buy: If you lost last battle, give all friends +2 health",
                "trigger": "BuyAfterLoss",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Buy: If you lost last battle, give all friends +3 health",
                "trigger": "BuyAfterLoss",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-crab": {
            "name": "Crab",
            "id": "pet-crab",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd80"
            },
            "tier": 2,
            "baseAttack": 4,
            "baseHealth": 1,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Start of battle: copy 50% of health from most healthy friend",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": False,
                    "copyHealth": True,
                    "from": {
                        "kind": "HighestHealthFriend"
                    },
                    "to": {
                        "kind": "Self"
                    },
                    "percentage": 50
                }
            },
            "level2Ability": {
                "description": "Start of battle: copy 100% of health from most healthy friend",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": False,
                    "copyHealth": True,
                    "from": {
                        "kind": "HighestHealthFriend"
                    },
                    "to": {
                        "kind": "Self"
                    },
                    "percentage": 100
                }
            },
            "level3Ability": {
                "description": "Start of battle: copy 150% of health from most healthy friend",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": False,
                    "copyHealth": True,
                    "from": {
                        "kind": "HighestHealthFriend"
                    },
                    "to": {
                        "kind": "Self"
                    },
                    "percentage": 150
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1
                    }
                }
            ]
        },
        "pet-swan": {
            "name": "Swan",
            "id": "pet-swan",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udda2"
            },
            "tier": 2,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Start of turn: Gain 1 gold.",
                "trigger": "StartOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "GainGold",
                    "amount": 1
                }
            },
            "level2Ability": {
                "description": "Start of turn: Gain 2 gold.",
                "trigger": "StartOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "GainGold",
                    "amount": 2
                }
            },
            "level3Ability": {
                "description": "Start of turn: Gain 3 gold.",
                "trigger": "StartOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "GainGold",
                    "amount": 3
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                }
            ]
        },
        "pet-rat": {
            "name": "Rat",
            "id": "pet-rat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc00"
            },
            "tier": 2,
            "baseAttack": 3,
            "baseHealth": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-dirty-rat",
                    "team": "Enemy"
                }
            },
            "level2Ability": {
                "description": "Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-dirty-rat",
                    "team": "Enemy"
                }
            },
            "level3Ability": {
                "description": "Faint: summon one 1/1 Dirty Rat for the opponent that betrays him.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-dirty-rat",
                    "team": "Enemy"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                }
            ]
        },
        "pet-hedgehog": {
            "name": "Hedgehog",
            "id": "pet-hedgehog",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd94"
            },
            "tier": 2,
            "baseAttack": 4,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Deal 2 damage to all.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "All"
                    },
                    "amount": 2
                }
            },
            "level2Ability": {
                "description": "Faint: Deal 4 damage to all.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "All"
                    },
                    "amount": 4
                }
            },
            "level3Ability": {
                "description": "Faint: Deal 6 damage to all.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "All"
                    },
                    "amount": 6
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                }
            ]
        },
        "pet-peacock": {
            "name": "Peacock",
            "id": "pet-peacock",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd9a"
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Hurt: Gain 4 attack.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 4,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Hurt: Gain 8 attack.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 8,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Hurt: Gain 12 attack.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 12,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                }
            ]
        },
        "pet-flamingo": {
            "name": "Flamingo",
            "id": "pet-flamingo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda9"
            },
            "tier": 2,
            "baseAttack": 3,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Give the two nearest friends behind +1/+1.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 2
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Faint: Give the two nearest friends behind +2/+2.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 2
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Faint: Give the two nearest friends behind +3/+3.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 2
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                }
            ]
        },
        "pet-worm": {
            "name": "Worm",
            "id": "pet-worm",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udeb1"
            },
            "tier": 2,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Stock one 2-gold apple",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "target": {
                        "kind": "Self"
                    },
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Stock one 2-gold better apple",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "target": {
                        "kind": "Self"
                    },
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Stock one 2-gold best apple",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "target": {
                        "kind": "Self"
                    },
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-kangaroo": {
            "name": "Kangaroo",
            "id": "pet-kangaroo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd98"
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 3,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend ahead attacks: Gain +1/+1",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Friend ahead attacks: Gain +2/+2",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Friend ahead attacks: Gain +3/+3",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-spider": {
            "name": "Spider",
            "id": "pet-spider",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udd77"
            },
            "tier": 2,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Summon a level 1 tier 3 animal as a 2/2",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 3,
                    "baseAttack": 2,
                    "baseHealth": 2,
                    "level": 1
                }
            },
            "level2Ability": {
                "description": "Faint: Summon a level 2 tier 3 animal as a 4/4",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 3,
                    "baseAttack": 4,
                    "baseHealth": 4,
                    "level": 2
                }
            },
            "level3Ability": {
                "description": "Faint: Summon a level 3 tier 3 animal as a 6/6",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonRandomPet",
                    "tier": 3,
                    "baseAttack": 6,
                    "baseHealth": 6,
                    "level": 3
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574,
                        "ExpansionPack1": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842,
                        "ExpansionPack1": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1,
                        "ExpansionPack1": 0.1
                    }
                }
            ]
        },
        "pet-dodo": {
            "name": "Dodo",
            "id": "pet-dodo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda4"
            },
            "tier": 3,
            "baseAttack": 4,
            "baseHealth": 2,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Start of battle: Give 50% attack to the nearest friend ahead.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": False,
                    "from": {
                        "kind": "Self"
                    },
                    "to": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "percentage": 50
                }
            },
            "level2Ability": {
                "description": "Start of battle: Give 100% attack to the nearest friend ahead.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": False,
                    "from": {
                        "kind": "Self"
                    },
                    "to": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "percentage": 100
                }
            },
            "level3Ability": {
                "description": "Start of battle: Give 150% attack to the nearest friend ahead.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferStats",
                    "copyAttack": True,
                    "copyHealth": False,
                    "from": {
                        "kind": "Self"
                    },
                    "to": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "percentage": 150
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1
                    }
                }
            ]
        },
        "pet-badger": {
            "name": "Badger",
            "id": "pet-badger",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda1"
            },
            "tier": 3,
            "baseAttack": 6,
            "baseHealth": 3,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Faint: Deal 50% attack damage to adjacent pets",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "AdjacentAnimals"
                    },
                    "amount": {
                        "attackDamagePercent": 50
                    }
                }
            },
            "level2Ability": {
                "description": "Faint: Deal 100% attack damage to adjacent pets",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "AdjacentAnimals"
                    },
                    "amount": {
                        "attackDamagePercent": 100
                    }
                }
            },
            "level3Ability": {
                "description": "Faint: Deal 150% attack damage to adjacent pets",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "AdjacentAnimals"
                    },
                    "amount": {
                        "attackDamagePercent": 150
                    }
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-dolphin": {
            "name": "Dolphin",
            "id": "pet-dolphin",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc2c"
            },
            "tier": 3,
            "baseAttack": 4,
            "baseHealth": 3,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Start of battle: Deal 4 damage to the lowest health enemy.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "LowestHealthEnemy"
                    },
                    "amount": 4
                }
            },
            "level2Ability": {
                "description": "Start of battle: Deal 4 damage to the lowest health enemy. Triggers 2 times.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "LowestHealthEnemy",
                        "n": 2
                    },
                    "amount": 4
                }
            },
            "level3Ability": {
                "description": "Start of battle: Deal 15 damage to the lowest health enemy. Triggers 3 times.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "LowestHealthEnemy",
                        "n": 3
                    },
                    "amount": 4
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-giraffe": {
            "name": "Giraffe",
            "id": "pet-giraffe",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd92"
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "End turn: Give the nearest friend ahead +1/+1",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "End turn: Give the nearest two friends ahead +1/+1",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendAhead",
                        "n": 2
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "End turn: Give the nearest three friends ahead +1/+1",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendAhead",
                        "n": 3
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-elephant": {
            "name": "Elephant",
            "id": "pet-elephant",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc18"
            },
            "tier": 3,
            "baseAttack": 3,
            "baseHealth": 7,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "After Attack: Deal 1 damage to nearest friend behind.",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 1
                    },
                    "amount": 1
                }
            },
            "level2Ability": {
                "description": "After Attack: Deal 1 damage to nearest friend behind. Triggers 2 times.",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 2
                    },
                    "amount": 1
                }
            },
            "level3Ability": {
                "description": "Before Attack: Deal 1 damage to nearest friends behind. Triggers 3 times.",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 3
                    },
                    "amount": 1
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.14973028138212574
                    },
                    "perSlot": {
                        "StandardPack": 0.05263157894736842
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-1",
                    "perSlot": {
                        "StandardPack": 0.1
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-2",
                    "perSlot": {
                        "StandardPack": 0.1
                    }
                }
            ]
        },
        "pet-camel": {
            "name": "Camel",
            "id": "pet-camel",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc2b"
            },
            "tier": 3,
            "baseAttack": 3,
            "baseHealth": 4,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Hurt: Give nearest friend behind +1/+2",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 1
                    },
                    "attackAmount": 1,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Hurt: Give nearest friend behind +2/+4",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 1
                    },
                    "attackAmount": 2,
                    "healthAmount": 4,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Hurt: Give nearest friend behind +3/+6",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "FriendBehind",
                        "n": 1
                    },
                    "attackAmount": 3,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-rabbit": {
            "name": "Rabbit",
            "id": "pet-rabbit",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc07"
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Friendly ate food: Give it +1 Health. Works 4 times per turn.",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                },
                "maxTriggers": 4
            },
            "level2Ability": {
                "description": "Friendly ate food: Give it +2 Health. Works 4 times per turn.",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                },
                "maxTriggers": 4
            },
            "level3Ability": {
                "description": "Friendly ate food: Give it +3 Health. Works 4 times per turn.",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                },
                "maxTriggers": 4
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-ox": {
            "name": "Ox",
            "id": "pet-ox",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc02"
            },
            "tier": 3,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend ahead faints: Gain Melon Armor and +1 attack. Works 1 time per turn.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "FriendAhead"
                },
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ApplyStatus",
                            "status": "status-melon-armor",
                            "to": {
                                "kind": "Self"
                            }
                        },
                        {
                            "kind": "ModifyStats",
                            "target": {
                                "kind": "Self"
                            },
                            "attackAmount": 1,
                            "untilEndOfBattle": False
                        }
                    ]
                },
                "maxTriggers": 1
            },
            "level2Ability": {
                "description": "Friend ahead faints: Gain Melon Armor and +2 attack. Works 2 time per turn.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "FriendAhead"
                },
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ApplyStatus",
                            "status": "status-melon-armor",
                            "to": {
                                "kind": "Self"
                            }
                        },
                        {
                            "kind": "ModifyStats",
                            "target": {
                                "kind": "Self"
                            },
                            "attackAmount": 2,
                            "untilEndOfBattle": False
                        }
                    ]
                },
                "maxTriggers": 2
            },
            "level3Ability": {
                "description": "Friend ahead faints: Gain Melon Armor and +3 attack. Works 3 time per turn.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "FriendAhead"
                },
                "effect": {
                    "kind": "AllOf",
                    "effects": [
                        {
                            "kind": "ApplyStatus",
                            "status": "status-melon-armor",
                            "to": {
                                "kind": "Self"
                            }
                        },
                        {
                            "kind": "ModifyStats",
                            "target": {
                                "kind": "Self"
                            },
                            "attackAmount": 3,
                            "untilEndOfBattle": False
                        }
                    ]
                },
                "maxTriggers": 3
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-dog": {
            "name": "Dog",
            "id": "pet-dog",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83d\udc15"
            },
            "tier": 3,
            "baseAttack": 3,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Friend summoned: Gain +2 Attack and +1 Health until end of battle.",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "OneOf",
                    "effects": [
                        {
                            "kind": "ModifyStats",
                            "untilEndOfBattle": False,
                            "target": {
                                "kind": "Self"
                            },
                            "attackAmount": 2
                        },
                        {
                            "kind": "ModifyStats",
                            "untilEndOfBattle": False,
                            "target": {
                                "kind": "Self"
                            },
                            "healthAmount": 1
                        }
                    ]
                }
            },
            "level2Ability": {
                "description": "Friend summoned: Gain +4 Attack and +2 Health until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "OneOf",
                    "effects": [
                        {
                            "kind": "ModifyStats",
                            "untilEndOfBattle": False,
                            "target": {
                                "kind": "Self"
                            },
                            "attackAmount": 4
                        },
                        {
                            "kind": "ModifyStats",
                            "untilEndOfBattle": False,
                            "target": {
                                "kind": "Self"
                            },
                            "healthAmount": 2
                        }
                    ]
                }
            },
            "level3Ability": {
                "description": "Friend summoned: Gain +6 Attack and +3 Health  until end of battle",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "OneOf",
                    "effects": [
                        {
                            "kind": "ModifyStats",
                            "untilEndOfBattle": False,
                            "target": {
                                "kind": "Self"
                            },
                            "attackAmount": 6
                        },
                        {
                            "kind": "ModifyStats",
                            "untilEndOfBattle": False,
                            "target": {
                                "kind": "Self"
                            },
                            "healthAmount": 3
                        }
                    ]
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-sheep": {
            "name": "Sheep",
            "id": "pet-sheep",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc11"
            },
            "tier": 3,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Summon two 2/2 Rams",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-ram",
                    "withAttack": 2,
                    "withHealth": 2,
                    "team": "Friendly"
                }
            },
            "level2Ability": {
                "description": "Faint: Summon two 4/4 Rams",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-ram",
                    "withAttack": 4,
                    "withHealth": 4,
                    "team": "Friendly"
                }
            },
            "level3Ability": {
                "description": "Faint: Summon two 6/6 Rams",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-ram",
                    "withAttack": 6,
                    "withHealth": 6,
                    "team": "Friendly"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-skunk": {
            "name": "Skunk",
            "id": "pet-skunk",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda8"
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Start of battle: Reduce the highest health enemy by 33%.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ReduceHealth",
                    "target": {
                        "kind": "HighestHealthEnemy"
                    },
                    "percentage": 33
                }
            },
            "level2Ability": {
                "description": "Start of battle: Reduce the highest health enemy by 66%.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ReduceHealth",
                    "target": {
                        "kind": "HighestHealthEnemy"
                    },
                    "percentage": 66
                }
            },
            "level3Ability": {
                "description": "Start of battle: Reduce the highest health enemy by 99%.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ReduceHealth",
                    "target": {
                        "kind": "HighestHealthEnemy"
                    },
                    "percentage": 99
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-hippo": {
            "name": "Hippo",
            "id": "pet-hippo",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd9b"
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 5,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Knock out: Gain +3 attack and +3 health.",
                "trigger": "KnockOut",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Knock out: Gain +6 attack and +6 health.",
                "trigger": "KnockOut",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Knock out: Gain +9 attack and +9 health.",
                "trigger": "KnockOut",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 9,
                    "healthAmount": 9,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-bison": {
            "name": "Bison",
            "id": "pet-bison",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\uddac"
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "End turn: If this has a level 3 friend, gain +1 attack and +2 health.",
                "trigger": "EndOfTurnWithLvl3Friend",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 1,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "End turn: If this has a level 3 friend, gain +2 attack and +4 health.",
                "trigger": "EndOfTurnWithLvl3Friend",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 2,
                    "healthAmount": 4,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "End turn: If this has a level 3 friend, gain +3 attack and +6 health.",
                "trigger": "EndOfTurnWithLvl3Friend",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 3,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-turtle": {
            "name": "Turtle",
            "id": "pet-turtle",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc22"
            },
            "tier": 4,
            "baseAttack": 2,
            "baseHealth": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Give Melon Perk to the nearest friend behind.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-melon-armor",
                    "to": {
                        "kind": "FriendBehind",
                        "n": 1
                    }
                }
            },
            "level2Ability": {
                "description": "Faint: Give Melon Perk to the two nearest friends behind.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-melon-armor",
                    "to": {
                        "kind": "FriendBehind",
                        "n": 2
                    }
                }
            },
            "level3Ability": {
                "description": "Faint: Give Melon Perk to the two nearest friends behind.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-melon-armor",
                    "to": {
                        "kind": "FriendBehind",
                        "n": 3
                    }
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.12681358024691358,
                        "ExpansionPack1": 0.12681358024691358
                    },
                    "perSlot": {
                        "StandardPack": 0.03333333333333333,
                        "ExpansionPack1": 0.03333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-3",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-4",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-squirrel": {
            "name": "Squirrel",
            "id": "pet-squirrel",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc3f"
            },
            "tier": 4,
            "baseAttack": 2,
            "baseHealth": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Start of turn: Discount all shop food by 1 gold",
                "trigger": "StartOfTurn",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DiscountFood",
                    "amount": 1
                }
            },
            "level2Ability": {
                "description": "Start of turn: Discount all shop food by 2 gold",
                "trigger": "StartOfTurn",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DiscountFood",
                    "amount": 2
                }
            },
            "level3Ability": {
                "description": "Start of turn: Discount all shop food by 3 gold",
                "trigger": "StartOfTurn",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DiscountFood",
                    "amount": 3
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-penguin": {
            "name": "Penguin",
            "id": "pet-penguin",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc27"
            },
            "tier": 4,
            "baseAttack": 1,
            "baseHealth": 3,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "End turn: Give two level 2 or higher friends +1 attack and +1 health.",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Level2And3Friends"
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "End turn: Give two level 2 or higher friends +2 attack and +2 health.",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Level2And3Friends"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "End turn: Give two level 2 or higher friends +3 attack and +3 health.",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Level2And3Friends"
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-deer": {
            "name": "Deer",
            "id": "pet-deer",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd8c"
            },
            "tier": 4,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Summon one 5/3 Bus with Chili.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bus",
                    "withAttack": 5,
                    "withHealth": 3,
                    "team": "Friendly"
                }
            },
            "level2Ability": {
                "description": "Faint: Summon one 10/6 Bus with Chili.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bus",
                    "withAttack": 10,
                    "withHealth": 6,
                    "team": "Friendly"
                }
            },
            "level3Ability": {
                "description": "Faint: Summon one 15/9 Bus with Chili.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bus",
                    "withAttack": 15,
                    "withHealth": 9,
                    "team": "Friendly"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-whale": {
            "name": "Whale",
            "id": "pet-whale",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc0b"
            },
            "tier": 4,
            "baseAttack": 3,
            "baseHealth": 7,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Start of battle: Swallow friend ahead and release it as a level 1 after fainting.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "Swallow",
                    "target": {
                        "kind": "FriendAhead",
                        "n": 1
                    }
                }
            },
            "level2Ability": {
                "description": "Start of battle: Swallow friend ahead and release it as a level 2 after fainting.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "Swallow",
                    "target": {
                        "kind": "FriendAhead",
                        "n": 1
                    }
                }
            },
            "level3Ability": {
                "description": "Start of battle: Swallow friend ahead and release it as a level 3 after fainting.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "Swallow",
                    "target": {
                        "kind": "FriendAhead",
                        "n": 1
                    }
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-parrot": {
            "name": "Parrot",
            "id": "pet-parrot",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd9c"
            },
            "tier": 4,
            "baseAttack": 4,
            "baseHealth": 2,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "End Turn: Copy ability from the nearest pet ahead as level 1 until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferAbility",
                    "from": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "to": {
                        "kind": "Self"
                    },
                    "level": 1
                }
            },
            "level2Ability": {
                "description": "End Turn: Copy ability from the nearest pet ahead as level 2 until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferAbility",
                    "from": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "to": {
                        "kind": "Self"
                    },
                    "level": 2
                }
            },
            "level3Ability": {
                "description": "End Turn: Copy ability from the nearest pet ahead as level 3 until end of battle.",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "TransferAbility",
                    "from": {
                        "kind": "FriendAhead",
                        "n": 1
                    },
                    "to": {
                        "kind": "Self"
                    },
                    "level": 3
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-scorpion": {
            "name": "Scorpion",
            "id": "pet-scorpion",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd82"
            },
            "tier": 5,
            "baseAttack": 1,
            "baseHealth": 1,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "status": "status-poison-attack",
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                }
            ]
        },
        "pet-crocodile": {
            "name": "Crocodile",
            "id": "pet-crocodile",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83d\udc0a"
            },
            "tier": 5,
            "baseAttack": 8,
            "baseHealth": 4,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Start of battle: Deal 8 damage to the last enemy",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "LastEnemy"
                    },
                    "amount": 8
                }
            },
            "level2Ability": {
                "description": "Start of battle: Deal 8 damage to the last enemy. Triggers 2 times.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "LastEnemy",
                        "n": 2
                    },
                    "amount": 16
                }
            },
            "level3Ability": {
                "description": "Start of battle: Deal 24 damage to the last enemy. Triggers 2 times.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "LastEnemy",
                        "n": 2
                    },
                    "amount": 8
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                }
            ]
        },
        "pet-rhino": {
            "name": "Rhino",
            "id": "pet-rhino",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd8f"
            },
            "tier": 5,
            "baseAttack": 6,
            "baseHealth": 9,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Knock out: Deal 4 damage to the first enemy.",
                "trigger": "KnockOut",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "FirstEnemy"
                    },
                    "amount": 4
                }
            },
            "level2Ability": {
                "description": "Knock out: Deal 8 damage to the first enemy.",
                "trigger": "KnockOut",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "FirstEnemy"
                    },
                    "amount": 8
                }
            },
            "level3Ability": {
                "description": "Knock out: Deal 12 damage to the first enemy.",
                "trigger": "KnockOut",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "FirstEnemy"
                    },
                    "amount": 12
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                }
            ]
        },
        "pet-monkey": {
            "name": "Monkey",
            "id": "pet-monkey",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc12"
            },
            "tier": 5,
            "baseAttack": 1,
            "baseHealth": 2,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "End turn: Give right-most friend +2/+2",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RightMostFriend"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "End turn: Give right-most friend +4/+4",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RightMostFriend"
                    },
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "End turn: Give right-most friend +6/+6",
                "trigger": "EndOfTurn",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RightMostFriend"
                    },
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                }
            ]
        },
        "pet-armadillo": {
            "name": "Armadillo",
            "id": "pet-armadillo",
            "tier": 5,
            "baseAttack": 2,
            "baseHealth": 6,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Start of battle: Give all pets +8 health",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "All"
                    },
                    "healthAmount": 8,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Start of battle: Give all pets +16 health",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "All"
                    },
                    "healthAmount": 16,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Start of battle: Give all pets +24 health",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "All"
                    },
                    "healthAmount": 24,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                }
            ]
        },
        "pet-cow": {
            "name": "Cow",
            "id": "pet-cow",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc04"
            },
            "tier": 5,
            "baseAttack": 4,
            "baseHealth": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Buy: Replace food shop with 2 free milk that gives +1/+2.",
                "trigger": "Buy",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "RefillShops",
                    "shop": "Food",
                    "food": "food-milk"
                }
            },
            "level2Ability": {
                "description": "Buy: Replace food shop with 2 free milk that gives +2/+4.",
                "trigger": "Buy",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "RefillShops",
                    "shop": "Food",
                    "food": "food-milk"
                }
            },
            "level3Ability": {
                "description": "Buy: Replace food shop with 2 free milk that gives +3/+6.",
                "trigger": "Buy",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "RefillShops",
                    "shop": "Food",
                    "food": "food-milk"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                }
            ]
        },
        "pet-seal": {
            "name": "Seal",
            "id": "pet-seal",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\uddad"
            },
            "tier": 5,
            "baseAttack": 3,
            "baseHealth": 8,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Eats shop food: Give 2 random friends +1/+1.",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Eats shop food: Give 2 random friends +2/+2.",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Eats shop food: Give 2 random friends +3/+3.",
                "trigger": "EatsShopFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125,
                        "ExpansionPack1": 0.125
                    }
                }
            ]
        },
        "pet-rooster": {
            "name": "Rooster",
            "id": "pet-rooster",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc13"
            },
            "tier": 5,
            "baseAttack": 6,
            "baseHealth": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Summon a Chick with 1 health and half the Attack of this.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-chick",
                    "team": "Friendly"
                }
            },
            "level2Ability": {
                "description": "Faint: Summon 2 Chicks with 1 health and half the Attack of this.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-chick",
                    "team": "Friendly"
                }
            },
            "level3Ability": {
                "description": "Faint: Summon 3 Chicks with 1 health and half the Attack of this.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-chick",
                    "team": "Friendly"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.09404935520024527,
                        "ExpansionPack1": 0.09404935520024527
                    },
                    "perSlot": {
                        "StandardPack": 0.024390243902439025,
                        "ExpansionPack1": 0.024390243902439025
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535,
                        "ExpansionPack1": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612,
                        "ExpansionPack1": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-5",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-6",
                    "perSlot": {
                        "StandardPack": 0.09090909090909091,
                        "ExpansionPack1": 0.09090909090909091
                    }
                }
            ]
        },
        "pet-chick": {
            "name": "Chick",
            "id": "pet-chick",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc24"
            },
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": 1
        },
        "pet-shark": {
            "name": "Shark",
            "id": "pet-shark",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd88"
            },
            "tier": 5,
            "baseAttack": 2,
            "baseHealth": 2,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend faints: Gain +2/+2.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Friend faints: Gain +4/+4.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Friend faints: Gain +6/+6.",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                }
            ]
        },
        "pet-turkey": {
            "name": "Turkey",
            "id": "pet-turkey",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd83"
            },
            "tier": 5,
            "baseAttack": 3,
            "baseHealth": 4,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend summoned: Give it +3/+3.",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Friend summoned: Give it +6/+6.",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Friend summoned: Give it +9/+9.",
                "trigger": "Summoned",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "attackAmount": 9,
                    "healthAmount": 9,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.09796001985292535
                    },
                    "perSlot": {
                        "StandardPack": 0.02040816326530612
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-7",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-8",
                    "perSlot": {
                        "StandardPack": 0.125
                    }
                }
            ]
        },
        "pet-leopard": {
            "name": "Leopard",
            "id": "pet-leopard",
            "image": {
                "source": "fxemoji",
                "commit": "270af343bee346d8221f87806d2b1eee0438431a",
                "name": "leopardside",
                "unicodeCodePoint": "\ud83d\udc06"
            },
            "tier": 6,
            "baseAttack": 10,
            "baseHealth": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Start of battle: Deal 50% Attack damage to a random enemy.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": {
                        "attackDamagePercent": 50
                    }
                }
            },
            "level2Ability": {
                "description": "Start of battle: Deal 50% Attack damage to 2 random enemies.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 2
                    },
                    "amount": {
                        "attackDamagePercent": 50
                    }
                }
            },
            "level3Ability": {
                "description": "Start of battle: Deal 50% Attack damage to 3 random enemies.",
                "trigger": "StartOfBattle",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 3
                    },
                    "amount": {
                        "attackDamagePercent": 50
                    }
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-boar": {
            "name": "Boar",
            "id": "pet-boar",
            "image": {
                "source": "noto-emoji",
                "commit": "f2a4f72bffe0212c72949a22698be235269bfab5",
                "unicodeCodePoint": "\ud83d\udc17"
            },
            "tier": 6,
            "baseAttack": 10,
            "baseHealth": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Before attack: Gain +2/+2.",
                "trigger": "BeforeAttack",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Before attack: Gain +4/+4.",
                "trigger": "BeforeAttack",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Before attack: Gain +6/+6.",
                "trigger": "BeforeAttack",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "Self"
                    },
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-tiger": {
            "name": "Tiger",
            "id": "pet-tiger",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc05"
            },
            "tier": 6,
            "baseAttack": 6,
            "baseHealth": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "The friend ahead repeats their ability in battle as if they were level 1.",
                "trigger": "CastsAbility",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "RepeatAbility",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "level": 1
                }
            },
            "level2Ability": {
                "description": "The friend ahead repeats their ability in battle as if they were level 2.",
                "trigger": "CastsAbility",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "RepeatAbility",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "level": 2
                }
            },
            "level3Ability": {
                "description": "The friend ahead repeats their ability in battle as if they were level 3.",
                "trigger": "CastsAbility",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "RepeatAbility",
                    "target": {
                        "kind": "TriggeringEntity"
                    },
                    "level": 3
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-wolverine": {
            "name": "Wolverine",
            "id": "pet-wolverine",
            "tier": 6,
            "baseAttack": 5,
            "baseHealth": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Four friends hurt: Remove 3 health from all enemies.",
                "trigger": "FourFriendsHurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachEnemy"
                    },
                    "healthAmount": -3,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Four friends hurt: Remove 6 health from all enemies.",
                "trigger": "FourFriendsHurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachEnemy"
                    },
                    "healthAmount": -6,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Four friends hurt: Remove 9 health from all enemies.",
                "trigger": "FourFriendsHurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachEnemy"
                    },
                    "healthAmount": -9,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-gorilla": {
            "name": "Gorilla",
            "id": "pet-gorilla",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd8d"
            },
            "tier": 6,
            "baseAttack": 7,
            "baseHealth": 10,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Hurt: Gain Coconut Shield. Works 1 time per turn.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-coconut-shield",
                    "to": {
                        "kind": "Self"
                    }
                },
                "maxTriggers": 1
            },
            "level2Ability": {
                "description": "Hurt: Gain Coconut Shield. Works 2 times per turn.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-coconut-shield",
                    "to": {
                        "kind": "Self"
                    }
                },
                "maxTriggers": 2
            },
            "level3Ability": {
                "description": "Hurt: Gain Coconut Shield. Works 3 times per turn.",
                "trigger": "Hurt",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ApplyStatus",
                    "status": "status-coconut-shield",
                    "to": {
                        "kind": "Self"
                    }
                },
                "maxTriggers": 3
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-dragon": {
            "name": "Dragon",
            "id": "pet-dragon",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc09"
            },
            "tier": 6,
            "baseAttack": 6,
            "baseHealth": 8,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Buy tier 1 animal: Give all friends +1/+1.",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Buy tier 1 animal: Give all friends +2/+2.",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Buy tier 1 animal: Give all friends +3/+3.",
                "trigger": "BuyTier1Animal",
                "triggeredBy": {
                    "kind": "Player"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachFriend"
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-mammoth": {
            "name": "Mammoth",
            "id": "pet-mammoth",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda3"
            },
            "tier": 6,
            "baseAttack": 4,
            "baseHealth": 12,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "level1Ability": {
                "description": "Faint: Give all friends +2/+2",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "target": {
                        "kind": "EachFriend"
                    },
                    "untilEndOfBattle": False
                }
            },
            "level2Ability": {
                "description": "Faint: Give all friends +4/+4",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 4,
                    "healthAmount": 4,
                    "target": {
                        "kind": "EachFriend"
                    },
                    "untilEndOfBattle": False
                }
            },
            "level3Ability": {
                "description": "Faint: Give all friends +6/+6",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 6,
                    "healthAmount": 6,
                    "target": {
                        "kind": "EachFriend"
                    },
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906,
                        "ExpansionPack1": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827,
                        "ExpansionPack1": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-cat": {
            "name": "Cat",
            "id": "pet-cat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc08\u200d\u2b1b"
            },
            "tier": 6,
            "baseAttack": 4,
            "baseHealth": 5,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Food with Health and Attack effects are doubled. Works 2 times per turn.",
                "trigger": "PurchaseFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "FoodMultiplier",
                    "amount": 2
                },
                "maxTriggers": 2
            },
            "level2Ability": {
                "description": "Food with Health and Attack effects are tripled. Works 2 times per turn.",
                "trigger": "PurchaseFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "FoodMultiplier",
                    "amount": 3
                },
                "maxTriggers": 2
            },
            "level3Ability": {
                "description": "Food with Health and Attack effects are quadrupled. Works 2 times per turn.",
                "trigger": "PurchaseFood",
                "triggeredBy": {
                    "kind": "Self"
                },
                "effect": {
                    "kind": "FoodMultiplier",
                    "amount": 4
                },
                "maxTriggers": 3
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-snake": {
            "name": "Snake",
            "id": "pet-snake",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc0d"
            },
            "tier": 6,
            "baseAttack": 6,
            "baseHealth": 6,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend ahead attacks: Deal 5 damage to a random enemy.",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 5
                }
            },
            "level2Ability": {
                "description": "Friend ahead attacks: Deal 10 damage to a random enemy.",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 10
                }
            },
            "level3Ability": {
                "description": "Friend ahead attacks: Deal 15 damage to a random enemy.",
                "trigger": "AfterAttack",
                "triggeredBy": {
                    "kind": "FriendAhead",
                    "n": 1
                },
                "effect": {
                    "kind": "DealDamage",
                    "target": {
                        "kind": "RandomEnemy",
                        "n": 1
                    },
                    "amount": 15
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-fly": {
            "name": "Fly",
            "id": "pet-fly",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udeb0"
            },
            "tier": 6,
            "baseAttack": 5,
            "baseHealth": 5,
            "packs": [
                "StandardPack"
            ],
            "level1Ability": {
                "description": "Friend faints: Summon a 5/5 fly in its place (Max 3 times)",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-fly",
                    "withAttack": 5,
                    "withHealth": 5,
                    "team": "Friendly"
                },
                "maxTriggers": 3
            },
            "level2Ability": {
                "description": "Friend faints: Summon a 10/10 fly in its place (Max 3 times)",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-fly",
                    "withAttack": 10,
                    "withHealth": 10,
                    "team": "Friendly"
                },
                "maxTriggers": 3
            },
            "level3Ability": {
                "description": "Friend faints: Summon a 15/15 fly in its place (Max 3 times)",
                "trigger": "Faint",
                "triggeredBy": {
                    "kind": "EachFriend"
                },
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-zombie-fly",
                    "withAttack": 15,
                    "withHealth": 15,
                    "team": "Friendly"
                },
                "maxTriggers": 3
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.08328505725105906
                    },
                    "perSlot": {
                        "StandardPack": 0.017241379310344827
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-9",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-10",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                },
                {
                    "kind": "levelup",
                    "turn": "turn-11",
                    "perSlot": {
                        "StandardPack": 0.1111111111111111
                    }
                }
            ]
        },
        "pet-zombie-cricket": {
            "name": "Zombie Cricket",
            "id": "pet-zombie-cricket",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udd97"
            },
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?"
        },
        "pet-bus": {
            "name": "Bus",
            "id": "pet-bus",
            "image": {
                "source": "noto-emoji",
                "commit": "f2a4f72bffe0212c72949a22698be235269bfab5",
                "unicodeCodePoint": "\ud83d\ude8c"
            },
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?",
            "status": "status-splash-attack"
        },
        "pet-dirty-rat": {
            "name": "Dirty Rat",
            "id": "pet-dirty-rat",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc00"
            },
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "tier": "Summoned",
            "baseAttack": 1,
            "baseHealth": 1
        },
        "pet-bee": {
            "name": "Bee",
            "id": "pet-bee",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc1d"
            },
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "tier": "Summoned",
            "baseAttack": 1,
            "baseHealth": 1
        },
        "pet-ram": {
            "name": "Ram",
            "id": "pet-ram",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83d\udc0f"
            },
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?"
        },
        "pet-zombie-fly": {
            "name": "Zombie Fly",
            "id": "pet-zombie-fly",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udeb0"
            },
            "packs": [
                "StandardPack"
            ],
            "tier": "Summoned",
            "baseAttack": "?",
            "baseHealth": "?"
        }
    },
    "foods": {
        "food-bread-crumb": {
            "name": "Bread Crumb",
            "id": "food-bread-crumb",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83c\udf5e"
            },
            "tier": 1,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "cost": 0,
            "ability": {
                "description": "Give one animal +1/+1",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "target": {
                        "kind": "DifferentPosition",
                        "n": 1
                    },
                    "expectedPets": 1
                }
            }
        },
        "food-apple": {
            "name": "Apple",
            "id": "food-apple",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf4e"
            },
            "tier": 1,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal +1/+1.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "PurchaseTarget"
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    },
                    "perSlot": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    },
                    "perSlot": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-honey": {
            "name": "Honey",
            "id": "food-honey",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf6f"
            },
            "tier": 1,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Honey Bee.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-honey-bee"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-1",
                    "perShop": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    },
                    "perSlot": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-2",
                    "perShop": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    },
                    "perSlot": {
                        "StandardPack": 0.5,
                        "ExpansionPack1": 0.5
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-cupcake": {
            "name": "Cupcake",
            "id": "food-cupcake",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\uddc1"
            },
            "tier": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal +3/+3 until end of battle.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "PurchaseTarget"
                    },
                    "attackAmount": 3,
                    "healthAmount": 3,
                    "untilEndOfBattle": True
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-meat-bone": {
            "name": "Meat Bone",
            "id": "food-meat-bone",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf56"
            },
            "tier": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Bone Attack.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-bone-attack"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-sleeping-pill": {
            "name": "Sleeping Pill",
            "id": "food-sleeping-pill",
            "image": {
                "source": "fxemoji",
                "commit": "270af343bee346d8221f87806d2b1eee0438431a",
                "unicodeCodePoint": "\ud83d\udc8a",
                "name": "pill"
            },
            "notes": "This costs 1 gold.",
            "tier": 2,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "cost": 1,
            "ability": {
                "description": "Make a friendly animal faint.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "Faint",
                    "target": {
                        "kind": "PurchaseTarget"
                    }
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-3",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-4",
                    "perShop": {
                        "StandardPack": 0.3599999999999999,
                        "ExpansionPack1": 0.3599999999999999
                    },
                    "perSlot": {
                        "StandardPack": 0.2,
                        "ExpansionPack1": 0.2
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-garlic": {
            "name": "Garlic",
            "id": "food-garlic",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\uddc4"
            },
            "tier": 3,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Garlic Armor.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-garlic-armor"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-salad-bowl": {
            "name": "Salad Bowl",
            "id": "food-salad-bowl",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd57"
            },
            "tier": 3,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give 2 random animals +1/+1.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-5",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-6",
                    "perShop": {
                        "StandardPack": 0.26530612244897966,
                        "ExpansionPack1": 0.26530612244897966
                    },
                    "perSlot": {
                        "StandardPack": 0.14285714285714285,
                        "ExpansionPack1": 0.14285714285714285
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-canned-food": {
            "name": "Canned Food",
            "id": "food-canned-food",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd6b"
            },
            "tier": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give all current and future shop animals +2/+1.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "EachShopAnimal",
                        "includingFuture": True
                    },
                    "attackAmount": 2,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-pear": {
            "name": "Pear",
            "id": "food-pear",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf50"
            },
            "tier": 4,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal +2/+2.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "PurchaseTarget"
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-7",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-8",
                    "perShop": {
                        "StandardPack": 0.2098765432098766,
                        "ExpansionPack1": 0.2098765432098766
                    },
                    "perSlot": {
                        "StandardPack": 0.1111111111111111,
                        "ExpansionPack1": 0.1111111111111111
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-chili": {
            "name": "Chili",
            "id": "food-chili",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf36"
            },
            "tier": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Splash Attack.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-splash-attack"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-chocolate": {
            "name": "Chocolate",
            "id": "food-chocolate",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf6b"
            },
            "tier": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal +1 Experience.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "GainExperience",
                    "target": {
                        "kind": "PurchaseTarget"
                    },
                    "amount": 1
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-sushi": {
            "name": "Sushi",
            "id": "food-sushi",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf63"
            },
            "tier": 5,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give 3 random animals +1/+1.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 3
                    },
                    "attackAmount": 1,
                    "healthAmount": 1,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-9",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-10",
                    "perShop": {
                        "StandardPack": 0.15972222222222232,
                        "ExpansionPack1": 0.15972222222222232
                    },
                    "perSlot": {
                        "StandardPack": 0.08333333333333333,
                        "ExpansionPack1": 0.08333333333333333
                    }
                },
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-melon": {
            "name": "Melon",
            "id": "food-melon",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf48"
            },
            "tier": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Melon Armor.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-melon-armor"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-mushroom": {
            "name": "Mushroom",
            "id": "food-mushroom",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf44"
            },
            "tier": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Extra Life.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-extra-life"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-pizza": {
            "name": "Pizza",
            "id": "food-pizza",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf55"
            },
            "tier": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give 2 random animals +2/+2.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "RandomFriend",
                        "n": 2
                    },
                    "attackAmount": 2,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-steak": {
            "name": "Steak",
            "id": "food-steak",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd69"
            },
            "tier": 6,
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "ability": {
                "description": "Give an animal Steak Attack.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ApplyStatus",
                    "to": {
                        "kind": "PurchaseTarget"
                    },
                    "status": "status-steak-attack"
                }
            },
            "probabilities": [
                {
                    "kind": "shop",
                    "turn": "turn-11",
                    "perShop": {
                        "StandardPack": 0.12109375,
                        "ExpansionPack1": 0.12109375
                    },
                    "perSlot": {
                        "StandardPack": 0.0625,
                        "ExpansionPack1": 0.0625
                    }
                }
            ]
        },
        "food-milk": {
            "name": "Milk",
            "id": "food-milk",
            "notes": "This is free!",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd5b"
            },
            "tier": "Summoned",
            "packs": [
                "StandardPack",
                "ExpansionPack1"
            ],
            "cost": 0,
            "ability": {
                "description": "Give an animal +1/2/3 attack and +2/4/6 health (depending on level of Cow).",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Buy",
                "effect": {
                    "kind": "ModifyStats",
                    "target": {
                        "kind": "PurchaseTarget"
                    },
                    "attackAmount": 1,
                    "healthAmount": 2,
                    "untilEndOfBattle": False
                }
            }
        }
    },
    "statuses": {
        "status-weak": {
            "name": "Weak",
            "id": "status-weak",
            "image": {
                "source": "noto-emoji",
                "commit": "e022fd6573782431ac9a65b520376b57511c31cd",
                "unicodeCodePoint": "\ud83e\udda0"
            },
            "ability": {
                "description": "Take 3 extra damage.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": 3,
                    "appliesOnce": False
                }
            }
        },
        "status-coconut-shield": {
            "name": "Coconut Shield",
            "id": "status-coconut-shield",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd65"
            },
            "ability": {
                "description": "Ignore damage once.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": None,
                    "appliesOnce": True
                }
            }
        },
        "status-honey-bee": {
            "name": "Honey Bee",
            "id": "status-honey-bee",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf6f"
            },
            "ability": {
                "description": "Summon a 1/1 Bee after fainting.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Faint",
                "effect": {
                    "kind": "SummonPet",
                    "pet": "pet-bee",
                    "team": "Friendly"
                }
            }
        },
        "status-bone-attack": {
            "name": "Bone Attack",
            "id": "status-bone-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf56"
            },
            "ability": {
                "description": "Attack for 5 more damage.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": 5,
                    "appliesOnce": False
                }
            }
        },
        "status-garlic-armor": {
            "name": "Garlic Armor",
            "id": "status-garlic-armor",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\uddc4"
            },
            "ability": {
                "description": "Take 2 less damage.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": -2,
                    "appliesOnce": False
                }
            }
        },
        "status-splash-attack": {
            "name": "Splash Attack",
            "id": "status-splash-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf36"
            },
            "ability": {
                "description": "Attack second enemy for 5 damage.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "SplashDamage",
                    "amount": 5
                }
            }
        },
        "status-melon-armor": {
            "name": "Melon Armor",
            "id": "status-melon-armor",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf48"
            },
            "ability": {
                "description": "Take 20 damage less, once.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenDamaged",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": -20,
                    "appliesOnce": True
                }
            }
        },
        "status-extra-life": {
            "name": "Extra Life",
            "id": "status-extra-life",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83c\udf44"
            },
            "ability": {
                "description": "Come back as a 1/1 after fainting",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "Faint",
                "effect": {
                    "kind": "RespawnPet",
                    "baseAttack": 1,
                    "baseHealth": 1
                }
            }
        },
        "status-steak-attack": {
            "name": "Steak Attack",
            "id": "status-steak-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd69"
            },
            "ability": {
                "description": "Attack for 20 more damage, once.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": 20,
                    "appliesOnce": True
                }
            }
        },
        "status-poison-attack": {
            "name": "Poison Attack",
            "id": "status-poison-attack",
            "image": {
                "source": "twemoji",
                "commit": "793a6a93f303c08877dd6eb589b2fabb3d1c45ee",
                "unicodeCodePoint": "\ud83e\udd5c"
            },
            "ability": {
                "description": "Knock out any animal hit by this.",
                "triggeredBy": {
                    "kind": "Self"
                },
                "trigger": "WhenAttacking",
                "effect": {
                    "kind": "ModifyDamage",
                    "damageModifier": None,
                    "appliesOnce": False
                }
            }
        }
    },
    "turns": {
        "turn-1": {
            "name": "Turn 1",
            "id": "turn-1",
            "index": 1,
            "foodShopSlots": 1,
            "animalShopSlots": 3,
            "livesLost": 1,
            "tiersAvailable": 1,
            "levelUpTier": 2
        },
        "turn-2": {
            "name": "Turn 2",
            "id": "turn-2",
            "index": 2,
            "foodShopSlots": 1,
            "animalShopSlots": 3,
            "livesLost": 1,
            "tiersAvailable": 1,
            "levelUpTier": 2
        },
        "turn-3": {
            "name": "Turn 3",
            "id": "turn-3",
            "index": 3,
            "foodShopSlots": 2,
            "animalShopSlots": 3,
            "livesLost": 2,
            "tiersAvailable": 2,
            "levelUpTier": 3
        },
        "turn-4": {
            "name": "Turn 4",
            "id": "turn-4",
            "index": 4,
            "foodShopSlots": 2,
            "animalShopSlots": 3,
            "livesLost": 2,
            "tiersAvailable": 2,
            "levelUpTier": 3
        },
        "turn-5": {
            "name": "Turn 5",
            "id": "turn-5",
            "index": 5,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 3,
            "levelUpTier": 4
        },
        "turn-6": {
            "name": "Turn 6",
            "id": "turn-6",
            "index": 6,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 3,
            "levelUpTier": 4
        },
        "turn-7": {
            "name": "Turn 7",
            "id": "turn-7",
            "index": 7,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 4,
            "levelUpTier": 5
        },
        "turn-8": {
            "name": "Turn 8",
            "id": "turn-8",
            "index": 8,
            "foodShopSlots": 2,
            "animalShopSlots": 4,
            "livesLost": 3,
            "tiersAvailable": 4,
            "levelUpTier": 5
        },
        "turn-9": {
            "name": "Turn 9",
            "id": "turn-9",
            "index": 9,
            "foodShopSlots": 2,
            "animalShopSlots": 5,
            "livesLost": 4,
            "tiersAvailable": 5,
            "levelUpTier": 6
        },
        "turn-10": {
            "name": "Turn 10",
            "id": "turn-10",
            "index": 10,
            "foodShopSlots": 2,
            "animalShopSlots": 5,
            "livesLost": 4,
            "tiersAvailable": 5,
            "levelUpTier": 6
        },
        "turn-11": {
            "name": "Turn 11+",
            "id": "turn-11",
            "index": 11,
            "foodShopSlots": 2,
            "animalShopSlots": 5,
            "livesLost": 5,
            "tiersAvailable": 6,
            "levelUpTier": 6
        }
    }
}


################################################################################
#### Creating empty fields for pets and foods
################################################################################


def get_fields(d):
    """
    Recursive function to get all possible fields for the input dict

    """
    key_list = []
    for key, value in d.items():
        temp_key_list = [key]

        if type(value) == dict:
            temp_key_list.append(get_fields(value))

        key_list.append(temp_key_list)

    return key_list


def add_dummy_fields(fields, d):
    if d == "none":
        ### Sometimes there are dict or int datatype collisions in the give
        ### json information. This should probably be corrected.
        return

    if type(fields[0]) == str:
        if len(fields) == 1:
            ### Break recursion condition
            d[fields[0]] = "none"
            return
        if type(fields[1]) == list:
            if fields[0] not in d:
                d[fields[0]] = {}

            for temp_fields in fields[1:]:
                add_dummy_fields(temp_fields, d[fields[0]])
    else:
        for temp_list in fields:
            add_dummy_fields(temp_list, d)


dummy_pet = {}
for temp_pet, value in data["pets"].items():
    temp_all_fields = get_fields(value)
    add_dummy_fields(temp_all_fields, dummy_pet)
data["pets"]["pet-none"] = dummy_pet

dummy_foods = {}
for temp_pet, value in data["foods"].items():
    temp_all_fields = get_fields(value)
    add_dummy_fields(temp_all_fields, dummy_foods)
data["foods"]["food-none"] = dummy_foods