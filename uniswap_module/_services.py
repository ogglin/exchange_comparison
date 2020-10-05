import json

import requests

TRUSTED = [
    {
        "id": "1",
        "token": "ETH",
        "contract": "0x0000000000000000000000000000000000000000",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "2",
        "token": "PLU",
        "contract": "0xd8912c10681d8b21fd3742244f44658dba12264e",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "80",
        "token": "CRED",
        "contract": "0x2ccbff3a042c68716ed2a2cb0c544a9f1d1935e1",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "81",
        "token": "VEE",
        "contract": "0xc27a2f05fa577a83ba0fdb4c38443c0718356501",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "83",
        "token": "SXUT",
        "contract": "0x340d2bde5eb28c1eed91b2f790723e3b160613b7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "85",
        "token": "APPC",
        "contract": "0x2c82c73d5b34aa015989462b2948cd616a37641f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "86",
        "token": "BDG",
        "contract": "0x286bda1413a2df81731d4930ce2f862a35a609fe",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "87",
        "token": "WAND",
        "contract": "0x1a7a8bd9106f2b8d977e08582dc7d24c723ab0db",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "91",
        "token": "NEU",
        "contract": "0x89303500a7abfb178b274fd89f2469c264951e1f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "93",
        "token": "KEY",
        "contract": "0xa823e6722006afe99e91c30ff5295052fe6b8e32",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "96",
        "token": "CRPT",
        "contract": "0xc5cea8292e514405967d958c2325106f2f48da77",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "241",
        "token": "VME",
        "contract": "0xca00bc15f67ebea4b20dfaaa847cace113cc5501",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "325",
        "token": "NPXS",
        "contract": "0x7c2e5b7ec572199d3841f6a38f7d4868bd0798f1",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "400",
        "token": "XNS",
        "contract": "0xa5b46ff9a887180c8fb2d97146398ddfc5fef1cd",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "406",
        "token": "CHZ",
        "contract": "0xa249de6948022783765fee4850d7b85e43118fcc",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "448",
        "token": "ANCT",
        "contract": "0xf150b9054013552a6288320dc4afe1beebb79d8e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "6",
        "token": "TRST",
        "contract": "0xe0b7927c4af23765cb51314a0e0521a9645f0e2a",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "37",
        "token": "MTH",
        "contract": "0x08f5a9235b08173b7569f83645d2c7fb55e8ccd8",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "10",
        "token": "HMQ",
        "contract": "0x667088b212ce3d06a1b553a7221e1fd19000d9af",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "31",
        "token": "MCO",
        "contract": "0x7c5a0ce9267ed19b22f8cae653f198e3e8daf098",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "11",
        "token": "ANT",
        "contract": "0xaaaf91d9b90df800df4f55c205fd6989c977e73a",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "12",
        "token": "BAT",
        "contract": "0xcbcc0f036ed4788f63fc0fee32873d6a7487b908",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "14",
        "token": "BNT",
        "contract": "0x0d8775f648430679a709e98d2b0cb6250d2887ef",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "16",
        "token": "SNM",
        "contract": "0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "18",
        "token": "PAY",
        "contract": "0x983f6d60db79ea8ca4eb9968c6aff8cfa04b3c63",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "72",
        "token": "CAJ",
        "contract": "0x8a854288a5976036a725879164ca3e91d30c6a1b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "41",
        "token": "HBT",
        "contract": "0xfec0cf7fe078a500abf15f1284958f22049c2c7e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "39",
        "token": "ART",
        "contract": "0xaf4dce16da2877f8c9e00544c93b62ac40631f16",
        "decimals": "5",
        "is_active": "t"
    },
    {
        "id": "19",
        "token": "PPT",
        "contract": "0x1776e1f26f98b1a5df9cd347953a26dd3cb46671",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "34",
        "token": "RVT",
        "contract": "0x0e0989b1f9b8a38983c2ba8053269ca62ec9b195",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "22",
        "token": "ADX",
        "contract": "0x419d0d8bdd9af5e606ae2232ed285aff190e711b",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "38",
        "token": "WTC",
        "contract": "0x0f5d2fb29fb7d3cfee444a200298f468908cc942",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "23",
        "token": "MTL",
        "contract": "0xb64ef51c888972c908cfacf59b47c1afbc0ab8ac",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "40",
        "token": "PRO2",
        "contract": "0xb7cb1c96db6b22b0d3d9536e0108d062bd488f74",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "26",
        "token": "DNT",
        "contract": "0xe3818504c1b32bf1557b16c238b2e01fd3149c17",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "30",
        "token": "ZRX",
        "contract": "0x3597bfd533a99c9aa083587b074434e61eb0a258",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "46",
        "token": "CND",
        "contract": "0x514910771af9ca656af840dff83e8264ecf986ca",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "69",
        "token": "DRGN",
        "contract": "0x80fb784b7ed66730e8b1dbd9820afd29931aab03",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "60",
        "token": "LIFE",
        "contract": "0x539efe69bcdd21a83efd9122571a64cc25e0282b",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "32",
        "token": "POE",
        "contract": "0xe41d2489571d322189246dafa5ebde1f4699f498",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "43",
        "token": "RLX",
        "contract": "0xdd6c68bb32462e01705011a4e2ad1a60740f217f",
        "decimals": "15",
        "is_active": "t"
    },
    {
        "id": "33",
        "token": "SCL",
        "contract": "0xb63b606ac810a52cca15e44bb630fd42d8d1d83d",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "47",
        "token": "BTM",
        "contract": "0xb4efd85c19999d84251304bda99e90b92300bd93",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "35",
        "token": "TNT",
        "contract": "0xd7631787b4dcc87b1254cfd1e5ce48e96823dee8",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "49",
        "token": "HVN",
        "contract": "0xcb97e65f07da24d46bcdd078ebebd7c6e6e3d750",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "50",
        "token": "EVX",
        "contract": "0x4156d3342d5c385a87d264f90653733592000581",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "54",
        "token": "ENJ",
        "contract": "0x27054b13b1b798b345b591a4d22e6562d47ea75a",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "52",
        "token": "AST",
        "contract": "0xf3db5fa2c66b7af3eb0c0b782510816cbe4813b8",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "55",
        "token": "DATA",
        "contract": "0x8f8221afbb33998d8584a2b05749ba73c37a938a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "56",
        "token": "VIB",
        "contract": "0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "57",
        "token": "RCN",
        "contract": "0x0cf0ee63788a0849fe5297f3407f701e122cc023",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "65",
        "token": "ASTRO",
        "contract": "0x12b19d3e2ccc14da04fae33e63652ce469b3f2fd",
        "decimals": "12",
        "is_active": "t"
    },
    {
        "id": "58",
        "token": "BLUE",
        "contract": "0x2c974b2d0ba1716e644c1fc59982a89ddd2ff724",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "61",
        "token": "EPY",
        "contract": "0xba5f11b16b155792cf3b2e6880e8706859a8aeb6",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "7",
        "token": "GNO",
        "contract": "0x607f4c5bb672230e8672085532f7e901544a7375",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "63",
        "token": "GRID",
        "contract": "0x50ee674689d75c0f88e8f83cfe8c4b69e8fd590d",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "68",
        "token": "ITT",
        "contract": "0x82b0e50478eeafde392d45d1259ed1071b6fda81",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "70",
        "token": "GET",
        "contract": "0x0aef06dcccc531e581f0440059e6ffcc206039ee",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "71",
        "token": "BNTY",
        "contract": "0x419c4db4b9e25d6db2ad9691ccb832c8d9fda05e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "73",
        "token": "SPANK",
        "contract": "0xd2d6158683aee4cc838067727209a0aaf4359de3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "77",
        "token": "MKR",
        "contract": "0xe469c4473af82217b30cf17b10bcdb6c8c796e75",
        "decimals": "0",
        "is_active": "t"
    },
    {
        "id": "75",
        "token": "EXRN",
        "contract": "0x42d6622dece394b54999fbd73d108123806f6a18",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "78",
        "token": "DMT",
        "contract": "0x56ba2ee7890461f463f7be02aac3099f6d5811a8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "84",
        "token": "WABI",
        "contract": "0xea097a2b1db00627b2fa17460ad260c016016977",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "8",
        "token": "WINGS",
        "contract": "0xcb94be6f13a1182e4a4b6140cb7bf2025d28e41b",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "89",
        "token": "REF",
        "contract": "0x27f610bf36eca0939093343ac28b1534a721dbb4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "9",
        "token": "TKN",
        "contract": "0x6810e776880c02933d47db1b9fc05908e5386b96",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "94",
        "token": "PRFT",
        "contract": "0x1b957dc4aefeed3b4a2351a6a6d5cbfbba0cecfa",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "95",
        "token": "STK",
        "contract": "0x4cc19356f2d37338b9802aa8e8fc58b0373296e7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "17",
        "token": "NMR",
        "contract": "0x744d70fdbe2ba4cf95131626614a1763df805b9e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "440",
        "token": "VANTA",
        "contract": "0x4db0e5c4df3562968f2d54448cd83ca65cfaa9a3",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "474",
        "token": "PRVN",
        "contract": "0x36e8ead13891de915d6a44b06d087445da1fe36c",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "20",
        "token": "FUN",
        "contract": "0xb97048628db6b661d4c2aa833e95dbe1a905b280",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "24",
        "token": "PLR",
        "contract": "0x4470bb87d77b963a013db939be332f927f2b992e",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "25",
        "token": "CVC",
        "contract": "0xf433089366899d83a9f26a773d59ec7ecf30355e",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "29",
        "token": "SAN",
        "contract": "0x5af2be193a6abca9c8817001f45744777db30756",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "15",
        "token": "SNT",
        "contract": "0xa645264c5603e96c3b0b078cdab68733794b0a71",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "42",
        "token": "KNC",
        "contract": "0x226bb599a12c826476e3a771454697ea52e9e220",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "45",
        "token": "RPL",
        "contract": "0x4a42d2c580f83dce404acad18dab26db11a1750e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "48",
        "token": "SALT",
        "contract": "0xd4c435f5b09f855c3317c8524cb1f586e42795fa",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "92",
        "token": "HQX",
        "contract": "0x5b2e4a700dfbc560061e957edec8f6eeeb74a320",
        "decimals": "10",
        "is_active": "t"
    },
    {
        "id": "171",
        "token": "LST",
        "contract": "0x737f98ac8ca59f2c68ad658e3c3d8c8963e40a4c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "174",
        "token": "BBC",
        "contract": "0x9a794dc1939f1d78fa48613b89b8f9d0a20da00e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "175",
        "token": "FSBT",
        "contract": "0xa4e8c3ec456107ea67d3075bf9e3df3a75823db0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "176",
        "token": "XBP",
        "contract": "0xe7d3e4413e29ae35b0893140f4500965c74365e5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "179",
        "token": "IPSX",
        "contract": "0xd53370acf66044910bb49cbcfe8f3cd020337f60",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "180",
        "token": "VIEW",
        "contract": "0x04f2e7221fdb1b52a68169b25793e51478ff0329",
        "decimals": "2",
        "is_active": "t"
    },
    {
        "id": "181",
        "token": "OCN",
        "contract": "0x001f0aa5da15585e5b2305dbab2bac425ea71007",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "182",
        "token": "DROP",
        "contract": "0xf03f8d65bafa598611c3495124093c56e8f638f0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "184",
        "token": "XDCE",
        "contract": "0x4672bad527107471cb5067a887f4656d585a8a31",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "151",
        "token": "EXY",
        "contract": "0x5c743a35e903f6c584514ec617acee0611cf44f3",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "185",
        "token": "BERRY",
        "contract": "0xe69a353b3152dd7b706ff7dd40fe1d18b7802d31",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "187",
        "token": "MRK",
        "contract": "0x6aeb95f06cda84ca345c2de0f3b7f96923a44f4c",
        "decimals": "14",
        "is_active": "t"
    },
    {
        "id": "188",
        "token": "GBX",
        "contract": "0x905e337c6c8645263d3521205aa37bf4d034e745",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "191",
        "token": "CMS",
        "contract": "0x9a4059c1cf329a017e0ee1337c503137fd9463b2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "194",
        "token": "MITX",
        "contract": "0xc761c8dc05ae52a8a785665e528ddbb00c098ad1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "112",
        "token": "CXO",
        "contract": "0x78b039921e84e726eb72e7b1212bb35504c645ca",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "119",
        "token": "FOTA",
        "contract": "0xfa1a856cfa3409cfa145fa4e20eb270df3eb21ab",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "115",
        "token": "TRAC",
        "contract": "0x923108a439c4e8c2315c4f6521e5ce95b44e9b4c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "117",
        "token": "IOST",
        "contract": "0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "165",
        "token": "LOC",
        "contract": "0x9a0242b7a33dacbe40edb927834f96eb39f8fbcb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "136",
        "token": "X8X",
        "contract": "0xd0352a019e9ab9d757776f532377aaebd36fd541",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "140",
        "token": "AUN",
        "contract": "0xd0929d411954c47438dc1d871dd6081f5c5e149c",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "76",
        "token": "CAT",
        "contract": "0x107c4504cd79c5d2696ea0030a8dd4e92601b82e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "167",
        "token": "NCASH",
        "contract": "0x5e3346444010135322268a4630d2ed5f8d09446c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "99",
        "token": "QSP",
        "contract": "0x75c5ee419331b6150879530d06f9ba054755f1da",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "101",
        "token": "INXT",
        "contract": "0x99ea4db9ee77acd40b119bd1dc4e33e1c070b80d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "103",
        "token": "IDXM",
        "contract": "0xa8006c4ca56f24d6836727d106349320db7fef82",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "104",
        "token": "REAL",
        "contract": "0x9041fe5b3fdea0f5e4afdc17e75180738d877a01",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "105",
        "token": "AGI",
        "contract": "0xcc13fc627effd6e35d2d2706ea3c4d7396c610ea",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "135",
        "token": "DTH",
        "contract": "0x9e6b2b11542f2bc52f3029077ace37e8fd838d7f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "106",
        "token": "JNT",
        "contract": "0x9214ec02cb71cba0ada6896b8da260736a67ab10",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "161",
        "token": "TFD",
        "contract": "0x998b3b82bc9dba173990be7afb772788b5acb8bd",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "107",
        "token": "SRN",
        "contract": "0x8eb24319393716668d768dcec29356ae9cffe285",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "109",
        "token": "ESZ",
        "contract": "0x68d57c9a1c35f63e2c83ee8e49a64e9d70528d25",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "110",
        "token": "SETH2",
        "contract": "0x5136c98a80811c3f46bdda8b5c4555cfd9f812f0",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "126",
        "token": "MWAT",
        "contract": "0x4d8fc1453a0f359e99c9675954e656d80d996fbf",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "111",
        "token": "BCDT",
        "contract": "0xe8a1df958be379045e2b46a31a98b93a2ecdfded",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "169",
        "token": "AMN",
        "contract": "0x809826cceab68c387726af962713b64cb5cb3cca",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "144",
        "token": "NGC",
        "contract": "0xc7bba5b765581efb2cdd2679db5bea9ee79b201f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "113",
        "token": "EVE",
        "contract": "0xacfa209fb73bf3dd5bbfb1101b9bc999c49062a5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "114",
        "token": "CV",
        "contract": "0xb6ee9668771a79be7967ee29a63d4184f8097143",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "118",
        "token": "CHSB",
        "contract": "0x618e75ac90b12c6049ba3b27f5d5f8651b0037f6",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "120",
        "token": "CPC",
        "contract": "0xba9d4199fab4f26efe3551d490e3821486f135ba",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "121",
        "token": "ADB",
        "contract": "0x4270bb238f6dd8b1c3ca01f96ca65b2647c06d3c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "122",
        "token": "POLY",
        "contract": "0xfae4ee59cdd86e3be9e8b90b53aa866327d7c090",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "189",
        "token": "LCD",
        "contract": "0xf453b5b9d4e0b5c62ffb256bb2378cc2bc8e8a89",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "153",
        "token": "DOCK",
        "contract": "0x5c743a35e903f6c584514ec617acee0611cf44f3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "124",
        "token": "BEE",
        "contract": "0x9992ec3cf6a55b00978cddf2b27bc6882d88d1ec",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "127",
        "token": "WPR",
        "contract": "0x5732046a883704404f284ce41ffadd5b007fd668",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "128",
        "token": "SIG",
        "contract": "0x6425c6be902d692ae2db752b3c268afadb099d3b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "133",
        "token": "HKN",
        "contract": "0x8db54ca569d3019a2ba126d03c37c44b5ef81ef6",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "137",
        "token": "ITC",
        "contract": "0x5adc961d6ac3f7062d2ea45fefb8d8167d44b190",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "138",
        "token": "RFR",
        "contract": "0x910dfc18d6ea3d6a7124a6f8b5458f281060fa4c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "142",
        "token": "GEM",
        "contract": "0x5b7093fe2491dfb058c94bcd62a1cd4d822f884c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "143",
        "token": "DRG",
        "contract": "0x69beab403438253f13b6e92db91f7fb849258263",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "156",
        "token": "ELEC",
        "contract": "0x23352036e911a22cfc692b5e2e196692658aded9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "147",
        "token": "LIF",
        "contract": "0x83cee9e086a77e492ee0bb93c2b0437ad6fdeccc",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "148",
        "token": "FKX",
        "contract": "0x2167fb82309cf76513e83b25123f8b0559d6b48f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "149",
        "token": "UTK",
        "contract": "0xeb9951021698b42e4399f9cbb6267aa35f82d59d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "150",
        "token": "SENT",
        "contract": "0x009e864923b49263c7f10d19b7f8ab7a9a5aad33",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "152",
        "token": "XNK",
        "contract": "0xa44e5137293e855b1b7bc7e2c6f8cd796ffcb037",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "157",
        "token": "NCT",
        "contract": "0xfd107b473ab90e8fbd89872144a3dc92c40fa8c9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "158",
        "token": "J8T",
        "contract": "0xd49ff13661451313ca1553fd6954bd1d9b6e02b9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "159",
        "token": "BANCA",
        "contract": "0x9e46a38f5daabe8683e10793b06749eef7d733d1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "160",
        "token": "SHIP",
        "contract": "0x0d262e5dc4a06a0f1c90ce79c7a60c09dfc884e4",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "162",
        "token": "AMB",
        "contract": "0xe25b0bba01dc5630312b6a21927e578061a13f55",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "166",
        "token": "BMH",
        "contract": "0x28b5e12cce51f15594b0b91d5b5adaa70f684a02",
        "decimals": "2",
        "is_active": "t"
    },
    {
        "id": "168",
        "token": "IGNX",
        "contract": "0xf03045a4c8077e38f3b8e2ed33b8aee69edf869f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "172",
        "token": "ABX",
        "contract": "0xd9a12cde03a86e800496469858de8581d3a5353d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "173",
        "token": "LOOM",
        "contract": "0x4de2573e27e648607b50e1cfff921a33e4a34405",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "190",
        "token": "MFG",
        "contract": "0x12fcd6463e66974cf7bbc24ffc4d40d6be458283",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "192",
        "token": "SMT3",
        "contract": "0x6710c63432a2de02954fc0f851db07146a6c0312",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "125",
        "token": "BLZ",
        "contract": "0x41dbecc1cdc5517c6f76f6a6e836adbee2754de3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "129",
        "token": "REN",
        "contract": "0x4cf488387f035ff08c371515562cba712f9015d4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "130",
        "token": "REM",
        "contract": "0x6888a16ea9792c15a4dcf2f6c623d055c8ede792",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "132",
        "token": "DAN",
        "contract": "0x83984d6142934bb535793a82adb0a46ef0f66b6d",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "134",
        "token": "FSN",
        "contract": "0x9b70740e708a083c6ff38df52297020f5dfaa5ee",
        "decimals": "10",
        "is_active": "t"
    },
    {
        "id": "141",
        "token": "NTK",
        "contract": "0x4df47b4969b2911c966506e3592c41389493953b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "164",
        "token": "NPX",
        "contract": "0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "177",
        "token": "SEN",
        "contract": "0x1ed7ae1f0e2fa4276dd7ddc786334a3df81d50c0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "282",
        "token": "GOT",
        "contract": "0x7b0c06043468469967dba22d1af33d77d44056c8",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "283",
        "token": "MFT",
        "contract": "0x509a38b7a1cc0dcd83aa9d06214663d9ec7c7f4a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "285",
        "token": "ESS",
        "contract": "0xdf2c7238198ad8b389666574f2d8bc411a4b7428",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "213",
        "token": "XTRD",
        "contract": "0x9c794f933b4dd8b49031a79b0f924d68bef43992",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "289",
        "token": "PNK",
        "contract": "0xedd7c94fd7b4971b916d15067bc454b9e1bad980",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "290",
        "token": "NCC",
        "contract": "0x63f584fa56e60e4d0fe8802b27c7e6e3b33e007f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "458",
        "token": "PXBT",
        "contract": "0x57accaad359ed96a0b4d027079b6f5351b043912",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "492",
        "token": "ANJ",
        "contract": "0x04fa0d235c4abf4bcf4787af4cf447de572ef828",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "66",
        "token": "DNA",
        "contract": "0x103c3a209da59d3e7c4a89307e66521e081cfdf0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "88",
        "token": "LEV",
        "contract": "0x1961b3331969ed52770751fc718ef530838b6dee",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "183",
        "token": "ADH",
        "contract": "0x4092678e4e78230f46a1534c0fbc8fa39780892b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "263",
        "token": "PST",
        "contract": "0x5d4abc77b8405ad177d8ac6682d584ecbfd46cec",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "199",
        "token": "PAR",
        "contract": "0xa4ea687a2a7f29cf2dc66b39c68e4411c0d00c49",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "200",
        "token": "FTX",
        "contract": "0x0e8d6b471e332f140e7d9dbb99e5e3822f728da6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "202",
        "token": "CEL",
        "contract": "0xd559f20296ff4895da39b5bd9add54b442596a61",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "204",
        "token": "SS",
        "contract": "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "209",
        "token": "GEN",
        "contract": "0x17f8afb63dfcdcc90ebe6e84f060cc306a98257d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "251",
        "token": "MVL",
        "contract": "0x08b4c866ae9d1be56a06e0c302054b4ffe067b43",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "206",
        "token": "DML",
        "contract": "0xbbff862d906e348e9946bfb2132ecb157da3d4b4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "207",
        "token": "NBAI",
        "contract": "0x6c6ee5e31d828de241282b9606c8e98ea48526e2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "208",
        "token": "XES",
        "contract": "0xbcdfe338d55c061c084d81fd793ded00a27f226d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "238",
        "token": "WEB",
        "contract": "0x436f0f3a982074c4a05084485d421466a994fe53",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "258",
        "token": "MVP",
        "contract": "0xe2ee1ac57b2e5564522b2de064a47b3f98b0e9c9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "261",
        "token": "SNX",
        "contract": "0xadc46ff5434910bd17b24ffb429e585223287d7f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "274",
        "token": "MET",
        "contract": "0x64a60493d888728cf42616e034a0dfeae38efcf0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "267",
        "token": "LIKE",
        "contract": "0x4f27053f32eda8af84956437bc00e5ffa7003287",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "275",
        "token": "QNT",
        "contract": "0x1b793e49237758dbd8b752afc9eb4b329d5da016",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "269",
        "token": "PMA",
        "contract": "0x02f61fd266da6e8b102d4121f5ce7b992640cf98",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "271",
        "token": "DAV",
        "contract": "0x846c66cf71c43f80403b51fe3906b3599d63336f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "277",
        "token": "EGT",
        "contract": "0x4a220e6096b25eadb88358cb44068a3248254675",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "210",
        "token": "KRL",
        "contract": "0xa017ac5fac5941f95010b12570b812c974469c2c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "216",
        "token": "CNN",
        "contract": "0x8400d94a5cb0fa0d041a3788e395285d61c9ee5e",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "222",
        "token": "SGN",
        "contract": "0x4a6058666cf1057eac3cd3a5a614620547559fc9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "286",
        "token": "REP",
        "contract": "0x83e2be8d114f9661221384b3a50d24b96a5653f5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "211",
        "token": "TUSD",
        "contract": "0x543ff227f64aa17ea132bf9886cab5db55dcaddf",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "287",
        "token": "ZIPT",
        "contract": "0xfc05987bd2be489accf0f509e44b0145d68240f7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "215",
        "token": "EXRT",
        "contract": "0x9c794f933b4dd8b49031a79b0f924d68bef43992",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "225",
        "token": "CEDEX",
        "contract": "0x4162178b78d6985480a308b2190ee5517460406d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "217",
        "token": "POA20",
        "contract": "0xb20043f149817bff5322f1b928e89abfc65a9925",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "218",
        "token": "SNTR",
        "contract": "0x8713d26637cf49e1b6b4a7ce57106aabc9325343",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "220",
        "token": "BBK",
        "contract": "0x2859021ee7f2cb10162e67f33af2d22764b31aff",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "223",
        "token": "CLN",
        "contract": "0xd8950fdeaa10304b7a7fd03a2fc66bc39f3c711a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "226",
        "token": "HER",
        "contract": "0xfe5f141bf94fe84bc28ded0ab966c16b17490657",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "228",
        "token": "HYDRO",
        "contract": "0x491c9a23db85623eed455a8efdd6aba9b911c5df",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "242",
        "token": "MRP",
        "contract": "0xc528c28fec0a90c083328bc45f587ee215760a0f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "230",
        "token": "FACE",
        "contract": "0xebbdf302c940c6bfd49c6b165f457fdb324649bc",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "231",
        "token": "TTV",
        "contract": "0x64cdf819d3e75ac8ec217b3496d7ce167be42e80",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "232",
        "token": "XYO",
        "contract": "0x1ccaa0f2a7210d76e1fdec740d5f323e2e1b1672",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "234",
        "token": "BBO",
        "contract": "0x55296f69f40ea6d20e478533c15a6b08b654e758",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "235",
        "token": "IOTX",
        "contract": "0xfa456cf55250a839088b27ee32a424d7dacb54ff",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "239",
        "token": "XCD",
        "contract": "0x3c4a3ffd813a107febd57b2f01bc344264d90fde",
        "decimals": "2",
        "is_active": "t"
    },
    {
        "id": "243",
        "token": "CEEK",
        "contract": "0xc343f099d3e41aa5c1b59470450e21e92e2d840b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "245",
        "token": "ZCN",
        "contract": "0xb056c38f6b7dc4064367403e26424cd2c60655e1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "246",
        "token": "BIT",
        "contract": "0xb3e2cb7cccfe139f8ff84013823bf22da6b6390a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "247",
        "token": "0XBTC",
        "contract": "0xb9ef770b6a5e12e45983c5d80545258aa38f3b78",
        "decimals": "10",
        "is_active": "t"
    },
    {
        "id": "249",
        "token": "BITCAR",
        "contract": "0xb6ed7644c69416d67b522e20bc294a9a9b405b31",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "278",
        "token": "ELY",
        "contract": "0xa253be28580ae23548a4182d95bf8201c28369a8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "250",
        "token": "LAN",
        "contract": "0xea26c4ac16d4a5a106820bc8aee85fd0b7b2b664",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "259",
        "token": "000",
        "contract": "0x97aeb5066e1a590e868b511457beb6fe99d329f5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "253",
        "token": "OMG",
        "contract": "0xa849eaae994fb86afa73382e9bd88c2b6b18dc71",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "256",
        "token": "WBT",
        "contract": "0x8d5682941ce456900b12d47ac06a88b47c764ce1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "257",
        "token": "ATMI",
        "contract": "0xd6e1401a079922469e9b965cb090ea6ff64c6839",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "262",
        "token": "DGX",
        "contract": "0xc86d054809623432210c107af2e3f619dcfbf652",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "265",
        "token": "THRT",
        "contract": "0x5d4abc77b8405ad177d8ac6682d584ecbfd46cec",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "279",
        "token": "PITCH",
        "contract": "0x8e1b448ec7adfc7fa35fc2e885678bd323176e34",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "266",
        "token": "TGAME",
        "contract": "0x622dffcc4e83c64ba959530a5a5580687a57581b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "270",
        "token": "ZINC",
        "contract": "0x82adce3b6a226f9286af99841410b04a075b54d5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "364",
        "token": "BIRD",
        "contract": "0x5c872500c00565505f3624ab435c222e558e9ff8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "227",
        "token": "SNOV",
        "contract": "0xf4065e4477e91c177ded71a7a6fb5ee07dc46bc9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "240",
        "token": "EDR",
        "contract": "0x840fe75abfadc0f2d54037829571b2782e919ce4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "248",
        "token": "QKC",
        "contract": "0x47da42696a866cdc61a4c809a515500a242909c1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "264",
        "token": "AUTO",
        "contract": "0x4f3afec4e5a3f2a6a1a411def7d7dfe50ee057bf",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "272",
        "token": "OLT",
        "contract": "0x4aac461c86abfa71e9d00d9a2cde8d74e4e1aeea",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "273",
        "token": "VITE",
        "contract": "0xd82df0abd3f51425eb15ef7580fda55727875f14",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "281",
        "token": "BST",
        "contract": "0x87f56ee356b434187105b40f96b230f5283c0ab4",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "288",
        "token": "BOX",
        "contract": "0x1985365e9f78359a9b6ad760e32412f4a445e862",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "413",
        "token": "EUULA",
        "contract": "0xff8be4b22cedc440591dcb1e641eb2a0dd9d25a5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "196",
        "token": "AUC",
        "contract": "0x4a527d8fc13c5203ab24ba0944f4cb14658d1db6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "203",
        "token": "VLD",
        "contract": "0xb98d4c97425d9908e66e53a6fdf673acca0be986",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "224",
        "token": "LBA",
        "contract": "0xb2135ab9695a7678dd590b1a996cb0f37bcb0718",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "294",
        "token": "SNR",
        "contract": "0x47d1a59cbdd19aee060c859c0009277e245328ae",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "145",
        "token": "MNTP",
        "contract": "0x814f67fa286f7572b041d041b1d99b432c9155ee",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "201",
        "token": "ABT",
        "contract": "0x1beef31946fbbb40b877a72e4ae04a8d1a5cee06",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "254",
        "token": "RMESH",
        "contract": "0xfef3884b603c33ef8ed4183346e093a173c94da6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "255",
        "token": "HOLD",
        "contract": "0xd26114cd6ee289accf82350c8d8487fedb8a0c07",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "280",
        "token": "MRPH",
        "contract": "0xa95592dcffa3c080b4b40e459c5f5692f67db7f8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "296",
        "token": "SAT",
        "contract": "0x47d1a59cbdd19aee060c859c0009277e245328ae",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "333",
        "token": "TOL",
        "contract": "0xd07d9fe2d2cc067015e2b4917d24933804f42cfa",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "297",
        "token": "T2T",
        "contract": "0xf8c595d070d104377f58715ce2e6c93e49a87f3c",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "299",
        "token": "SET",
        "contract": "0xe6824483e279d967ea6f8472ace7585862fa1185",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "343",
        "token": "AWC",
        "contract": "0xad22f63404f7305e4713ccbd4f296f34770513f4",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "301",
        "token": "ACAD",
        "contract": "0xfa75b65e52a6cbc5503f45f4abba2c5df4688875",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "305",
        "token": "ROX",
        "contract": "0xef51c9377feb29856e61625caf9390bd0b67ea18",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "306",
        "token": "DX",
        "contract": "0x05d412ce18f24040bb3fa45cf2c69e506586d8e8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "307",
        "token": "IG",
        "contract": "0x574f84108a98c575794f75483d801d1d5dc861a5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "377",
        "token": "PMNT",
        "contract": "0x81b4d08645da11374a03749ab170836e4e539767",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "309",
        "token": "SVD",
        "contract": "0x8a88f04e0c905054d2f33b26bb3a46d7091a039a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "310",
        "token": "FTT",
        "contract": "0x1d4ccc31dab6ea20f461d329a0562c1c58412515",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "358",
        "token": "BETHER",
        "contract": "0x965f109d31ccb77005858defae0ebaf7b4381652",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "313",
        "token": "CDT",
        "contract": "0xf8b358b3397a8ea5464f8cc753645d42e14b79ea",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "320",
        "token": "FTXT",
        "contract": "0x48c1b2f3efa85fbafb2ab951bf4ba860a08cdbb7",
        "decimals": "0",
        "is_active": "t"
    },
    {
        "id": "321",
        "token": "UUU",
        "contract": "0x884181554dfa9e578d36379919c05c25dc4a15bb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "322",
        "token": "ARCONA",
        "contract": "0x41875c2332b0877cdfaa699b641402b7d4642c32",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "327",
        "token": "IHF",
        "contract": "0xa15c7ebe1f07caf6bff097d8a589fb8ac49ae5b3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "332",
        "token": "USDC",
        "contract": "0x23ccc43365d9dd3882eab88f43d515208f832430",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "328",
        "token": "UBBEY",
        "contract": "0x05860d453c7974cbf46508c06cba14e211c629ce",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "330",
        "token": "MAS",
        "contract": "0x6cb1c2b61e24ad08bf5fff4d2b13ea987d211a88",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "331",
        "token": "DEC2",
        "contract": "0xb3c61539af156438951ea6cd48756d22a48fce62",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "334",
        "token": "ONE",
        "contract": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "336",
        "token": "AMO",
        "contract": "0x4d807509aece24c0fa5a102b6a3b059ec6e14392",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "337",
        "token": "TYPE",
        "contract": "0x2d184014b5658c453443aa87c8e9c4d57285620b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "338",
        "token": "FTM",
        "contract": "0x38c87aa89b2b8cd9b95b736e1fa7b612ea972169",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "381",
        "token": "CSP",
        "contract": "0x8a1e3930fde1f151471c368fdbb39f3f63a65b55",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "339",
        "token": "LQD",
        "contract": "0xeaf61fc150cd5c3bea75744e830d916e60ea5a9f",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "340",
        "token": "PSK",
        "contract": "0x4e15361fd6b4bb609fa63c81a2be19d873717870",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "341",
        "token": "COIN",
        "contract": "0xd29f0b5b3f50b07fe9a9511f7d86f4f4bac3f8c4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "344",
        "token": "FOAM",
        "contract": "0x6bd26bb09c992e09d2156b48f723e56e52eead9c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "388",
        "token": "ORBS",
        "contract": "0xe9a95d175a5f4c9369f3b74222402eb1b837693b",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "365",
        "token": "FXC",
        "contract": "0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "349",
        "token": "UTS",
        "contract": "0x1a2277c83930b7a64c3e3d5544eaa8c4f946b1b7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "350",
        "token": "ATF",
        "contract": "0xa858bc1b71a895ee83b92f149616f9b3f6afa0fb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "353",
        "token": "NKN",
        "contract": "0xa0008f510fe9ee696e7e320c9e5cbf61e27791ee",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "517",
        "token": "SWAP",
        "contract": "0x9fbfed658919a896b5dc7b00456ce22d780f9b65",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "346",
        "token": "CMCT",
        "contract": "0x4946fcea7c692606e8908002e55a582af44ac121",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "347",
        "token": "ECHT",
        "contract": "0x58b6a8a3302369daec383334672404ee733ab239",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "354",
        "token": "COVA",
        "contract": "0xb4272071ecadd69d933adcd19ca99fe80664fc08",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "348",
        "token": "KAT",
        "contract": "0x47bc01597798dcd7506dcca36ac4302fc93a8cfb",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "356",
        "token": "STASH",
        "contract": "0xb37a769b37224449d92aac57de379e1267cd3b00",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "357",
        "token": "WBTC",
        "contract": "0x3db6ba6ab6f95efed1a6e794cad492faaabf294d",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "362",
        "token": "COT",
        "contract": "0x6737fe98389ffb356f64ebb726aa1a92390d94fb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "367",
        "token": "NRP",
        "contract": "0x4a57e687b9126435a9b19e4a802113e266adebde",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "368",
        "token": "PLA",
        "contract": "0x8716fc5da009d3a208f0178b637a50f4ef42400f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "369",
        "token": "IMT",
        "contract": "0x3918c42f14f2eb1168365f911f63e540e5a306b5",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "370",
        "token": "CCN",
        "contract": "0x0198f46f520f33cd4329bd4be380a25a90536cd5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "371",
        "token": "FET",
        "contract": "0x13119e34e140097a507b07a5564bde1bc375d9e6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "372",
        "token": "PCL",
        "contract": "0x17b26400621695c2d8c2d8869f6259e82d7544c4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "373",
        "token": "HUDDL",
        "contract": "0x1d287cc25dad7ccaf76a26bc660c5f7c8e2a05bd",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "375",
        "token": "VIDT",
        "contract": "0x5137a403dd25e48de528912a4af62881e625d801",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "376",
        "token": "MESG",
        "contract": "0x8290333cef9e6d528dd5618fb97a76f268f3edd4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "378",
        "token": "CRO",
        "contract": "0x420167d87d35c3a249b32ef6225872fbd9ab85d2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "379",
        "token": "BEZ",
        "contract": "0x81b4d08645da11374a03749ab170836e4e539767",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "380",
        "token": "AERGO",
        "contract": "0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "382",
        "token": "ZAP",
        "contract": "0xae31b85bfe62747d0836b82608b4830361a3d37a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "384",
        "token": "LIT",
        "contract": "0x6781a0f84c7e9e846dcb84a9a5bd49333067b104",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "385",
        "token": "SNTVT",
        "contract": "0xb0866289e870d2efc282406cf4123df6e5bcb652",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "386",
        "token": "NOW",
        "contract": "0x763fa6806e1acf68130d2d0f0df754c93cc546b2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "387",
        "token": "CUSD",
        "contract": "0x7865af71cf0b288b4e7f654f4f7851eb46a2b7f8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "27",
        "token": "VGX",
        "contract": "0x41e5560054824ea6b0732e656e3ad64e20e94e45",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "53",
        "token": "REQ",
        "contract": "0xf0ee6b27b759c9893ce4f094b49ad28fd15a23e4",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "233",
        "token": "BTT",
        "contract": "0xa838be6e4b760e6061d4732d6b9f11bf578f9a76",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "293",
        "token": "SEAL",
        "contract": "0x6059f55751603ead7dc6d280ad83a7b33d837c90",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "298",
        "token": "NTK2",
        "contract": "0x92736b3bff1bbd72a72478d78f18a6ab9b68b791",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "300",
        "token": "PKG",
        "contract": "0x5d4d57cd06fa7fe99e26fdc481b468f77f05073c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "302",
        "token": "ONG",
        "contract": "0x02f2d4a04e6e01ace88bd2cd632875543b2ef577",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "304",
        "token": "MFTU",
        "contract": "0xd341d1680eeee3255b8c4c75bcce7eb57f144dae",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "329",
        "token": "TBE",
        "contract": "0xaf1250fa68d7decd34fd75de8742bc03b29bd58e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "352",
        "token": "XCHF",
        "contract": "0x014e42ae89b24738591e2f695e1ef6d95bd38619",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "312",
        "token": "BEAT",
        "contract": "0x2aec18c5500f21359ce1bea5dc1777344df4c0dc",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "319",
        "token": "GENE",
        "contract": "0xbb49a51ee5a66ca3a8cbe529379ba44ba67e6771",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "360",
        "token": "ZCC",
        "contract": "0x14c926f2290044b647e1bf2072e67b495eff1905",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "361",
        "token": "WMB",
        "contract": "0xfb0bdc444c8ae7e9b5beea5e4d1e8de93879e487",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "363",
        "token": "HXRO",
        "contract": "0x7a18919f0b05fa5e91f3ef43afe8a72105c9d4b8",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "456",
        "token": "PXAU",
        "contract": "0x93d3296cac208422bf587c3597d116e809870f2b",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "457",
        "token": "PKRW",
        "contract": "0x069480de51cfc3a8fdc7d2338925089a3f842740",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "459",
        "token": "PETH",
        "contract": "0x9e6fa5d7a76627cf8fc9f8640b9a0356a552f16f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "463",
        "token": "PCNY",
        "contract": "0x087cb8ca94604050abfb30d85346343368b51e36",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "464",
        "token": "PXBC",
        "contract": "0x6711a024414f68935e8320e421e59486cea4be24",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "465",
        "token": "PMXN",
        "contract": "0x76977256b9ad3cab59bf570327273c403a94dd0f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "466",
        "token": "PCHF",
        "contract": "0xb38bb9f5b9a73a3097d3a7cadd330aa6e6da8586",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "467",
        "token": "PCAD",
        "contract": "0x76ab520359a02fcd529cb889653ce27bd8ebaf57",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "471",
        "token": "PGBP",
        "contract": "0x6e95ff397ebbd73bd136b17b4166692d23d418a5",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "472",
        "token": "PJPY",
        "contract": "0xe161bd7fcaa326cd327343719b788464cbcae60f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "473",
        "token": "PINR",
        "contract": "0x8ce3686848745c8c8ceed250c1e780533f56065c",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "477",
        "token": "PBNB",
        "contract": "0xeacfd89d4299aa43ec121f1d322bc1c3b140e26c",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "478",
        "token": "PLTC",
        "contract": "0x630605234f93b4cdbe3e016f0276669cce749dc7",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "479",
        "token": "PXLM",
        "contract": "0xdc6eb54d81601f3b604388a9c3d2688beeb73955",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "480",
        "token": "PDASH",
        "contract": "0x0723da554e874e01182a567eb533a6af403896fb",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "481",
        "token": "DAI",
        "contract": "0xc93e8db665de16ad92f9a360284ac87d9b24bb87",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "482",
        "token": "TEL",
        "contract": "0x398208d9cbd270f796d753df070f73200335dd57",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "410",
        "token": "XCT",
        "contract": "0x79cdfa04e3c4eb58c4f49dae78b322e5b0d38788",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "484",
        "token": "ALG",
        "contract": "0x467bccd9d29f223bce8043b84e8c8b282827790f",
        "decimals": "2",
        "is_active": "t"
    },
    {
        "id": "485",
        "token": "FOUR",
        "contract": "0xd67b1db49801b6f4c96a01a4f7964233150dc58b",
        "decimals": "7",
        "is_active": "t"
    },
    {
        "id": "62",
        "token": "RDN",
        "contract": "0xff18dbc487b4c2e3222d115952babfda8ba52f5f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "427",
        "token": "MBN",
        "contract": "0x77c347d3ff9af04a9ed71dfad8a53e04cd2fabb6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "308",
        "token": "TALAO",
        "contract": "0x973e52691176d36453868d9d86572788d27041a9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "395",
        "token": "IDEX",
        "contract": "0xd6e49800decb64c0e195f791348c1e87a5864fd7",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "314",
        "token": "MUXE",
        "contract": "0x2fb12bccf6f5dd338b76be784a93ade072425690",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "316",
        "token": "UBEX",
        "contract": "0x515669d308f887fd83a471c7764f5d084886d34d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "397",
        "token": "RSR",
        "contract": "0xb705268213d593b8fd88d3fdeff93aff5cbdcfae",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "435",
        "token": "ESH",
        "contract": "0x12b306fa98f4cbb8d4457fdff3a0a0a56f07ccdf",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "443",
        "token": "BAND",
        "contract": "0x32b87fb81674aa79214e51ae42d571136e29d385",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "428",
        "token": "SWM",
        "contract": "0x9fadea1aff842d407893e21dbd0e2017b4c287b6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "402",
        "token": "STPT",
        "contract": "0x79c71d3436f39ce382d0f58f1b011d88100b9d91",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "404",
        "token": "JAR",
        "contract": "0xde7d85157d9714eadf595045cc12ca4a5f3e2adb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "416",
        "token": "1UP",
        "contract": "0x705ee96c1c160842c92c1aecfcffccc9c412e3d9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "444",
        "token": "TRB",
        "contract": "0xe5caef4af8780e59df925470b050fb23c43ca68c",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "446",
        "token": "ANGEL",
        "contract": "0x0ba45a8b5d5575935b8158a88c631e9f9c95a2e5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "449",
        "token": "PNG",
        "contract": "0x96b0bf939d9460095c15251f71fda11e41dcbddb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "450",
        "token": "TIOX",
        "contract": "0x5456bc77dd275c45c3c15f0cf936b763cf57c3b5",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "451",
        "token": "OXT",
        "contract": "0x9da1659a203cefe6e9c6da98c7a669a1ec3d7ede",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "415",
        "token": "LGO",
        "contract": "0x26de40bffafe73ff4e37089b2c71e35fd02eb1a7",
        "decimals": "2",
        "is_active": "t"
    },
    {
        "id": "452",
        "token": "MES",
        "contract": "0xd947b0ceab2a8885866b9a04a06ae99de852a3d4",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "345",
        "token": "LPT",
        "contract": "0xad22f63404f7305e4713ccbd4f296f34770513f4",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "355",
        "token": "LTO",
        "contract": "0x5cf04716ba20127f1e2297addcf4b5035000c9eb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "390",
        "token": "AER",
        "contract": "0xff56cc6b1e6ded347aa0b7676c85ab0b3d08b0fa",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "393",
        "token": "RC",
        "contract": "0xc96df921009b790dffca412375251ed1a2b75c60",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "394",
        "token": "ZNT",
        "contract": "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "426",
        "token": "PGF7T",
        "contract": "0xb9eefc4b0d472a44be93970254df4f4016569d27",
        "decimals": "7",
        "is_active": "t"
    },
    {
        "id": "396",
        "token": "CRE",
        "contract": "0x4fa000df40c06fc8c7d9179661535846b7cd4f87",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "398",
        "token": "SSN",
        "contract": "0x115ec79f1de567ec68b7ae7eda501b406626478e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "401",
        "token": "CHR",
        "contract": "0x1b80eeeadcc590f305945bcc258cfa770bbe1890",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "403",
        "token": "VNC",
        "contract": "0x915044526758533dfb918eceb6e44bc21632060d",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "405",
        "token": "AQU",
        "contract": "0xdf413690fb785e56895551cc21086a15b6e90386",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "411",
        "token": "URAC",
        "contract": "0xddb3422497e61e13543bea06989c0789117555c5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "412",
        "token": "ENK",
        "contract": "0xd2bb16cf38ca086cab5128d5c25de9477ebd596b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "417",
        "token": "USDQ",
        "contract": "0x0a50c93c762fdd6e56d86215c24aaad43ab629aa",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "436",
        "token": "SXP",
        "contract": "0xc12d1c73ee7dc3615ba4e37e4abfdbddfa38907e",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "418",
        "token": "KRWQ",
        "contract": "0x07597255910a51509ca469568b048f2597e72504",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "420",
        "token": "CYBR",
        "contract": "0x3c6cfbdaf0a04fc257b185bf98934a12124fe8d0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "421",
        "token": "SWACE",
        "contract": "0x3166c570935a7d8554c8f4ea792ff965d2efe1f2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "438",
        "token": "ZVC",
        "contract": "0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "423",
        "token": "MT",
        "contract": "0x03b155af3f4459193a276395dd76e357bb472da1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "424",
        "token": "XDB",
        "contract": "0x875353da48c4f9627c4d0b8b8c37b162fc43ce67",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "439",
        "token": "SLVD",
        "contract": "0x7de91b204c1c737bcee6f000aaa6569cf7061cb7",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "429",
        "token": "VID",
        "contract": "0x4eeea7b48b9c3ac8f70a9c932a8b1e8a5cb624c7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "431",
        "token": "NEXO",
        "contract": "0x2c9023bbc572ff8dc1228c7858a280046ea8c9e5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "442",
        "token": "FRM",
        "contract": "0xfdf574766ba1a96a553e175aeffa85ad78063f0b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "447",
        "token": "S",
        "contract": "0xa31b1767e09f842ecfd4bc471fe44f830e3891aa",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "454",
        "token": "PUSD",
        "contract": "0x322f4f6a48329690957a3bcbd1301516c2b83c1f",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "432",
        "token": "CHP",
        "contract": "0x12f649a9e821f90bb143089a6e56846945892ffb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "434",
        "token": "KICK",
        "contract": "0xf3db7560e820834658b590c96234c333cd3d5e5e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "455",
        "token": "PFCT",
        "contract": "0x996b396b88cc4a1d8df3dbd1c088cdfaee17e6d4",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "461",
        "token": "PEUR",
        "contract": "0x6065616a4bad5ce723a5608dcb85d3dbd20b55dd",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "469",
        "token": "PHKD",
        "contract": "0x2e7c90cb8c0e5bcce167b0eb836275a9ac703af8",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "470",
        "token": "PPHP",
        "contract": "0x110c2921d3c83111f53152fc4bbea8ce57f12959",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "408",
        "token": "TFB",
        "contract": "0x3506424f91fd33084466f402d5d97f05f8e3b4af",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "409",
        "token": "COTI",
        "contract": "0xc28e931814725bbeb9e670676fabbcb694fe7df2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "425",
        "token": "HUT",
        "contract": "0x4442556a08a841227bef04c67a7ba7acf01b6fc8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "433",
        "token": "SXDT",
        "contract": "0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "392",
        "token": "MATIC",
        "contract": "0xac4d22e40bf0b8ef4750a99ed4e935b99a42685e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "419",
        "token": "QDAO",
        "contract": "0x4954db6391f4feb5468b6b943d4935353596aec9",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "462",
        "token": "PADA",
        "contract": "0xcb2968a9bb8a1afb23c817f08c7a8c5ba591c0e2",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "522",
        "token": "AGA",
        "contract": "0x6f87d756daf0503d08eb8993686c7fc01dc44fb1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "499",
        "token": "COMP",
        "contract": "0xc00e94cb662c3520282e6f5717214004a7f26888",
        "decimals": "",
        "is_active": "t"
    },
    {
        "id": "523",
        "token": "SPRKL",
        "contract": "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "512",
        "token": "RSV",
        "contract": "0x27702a26126e0b3702af63ee09ac4d1a084ef628",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "5",
        "token": "RLC",
        "contract": "0xaf30d2a7e90d7dc361c8c4585e9bb7d2f6f15bc7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "13",
        "token": "MYST",
        "contract": "0x960b236a07cf122663c4303350609a66a7b288c0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "21",
        "token": "STORJ",
        "contract": "0xd4fa1460f537bb9085d22c7bccb5dd450ef28e3a",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "28",
        "token": "DENT",
        "contract": "0x0abdace70d3790235af448c88547603b945604ea",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "44",
        "token": "LINK",
        "contract": "0xdd974d5c2e2928dea5f71b9825b8b646686bd200",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "59",
        "token": "ARN",
        "contract": "0xf970b8e36e23f7fc3fd752eea86f8be8d83375a6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "506",
        "token": "CTSI",
        "contract": "0x24283732c3df91ee1e4354a3934c14b88b2d9a51",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "509",
        "token": "DEC",
        "contract": "0x37ee79e0b44866876de2fb7f416d0443dd5ae481",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "98",
        "token": "ELF",
        "contract": "0x80a7e048f37a50500351c204cb407766fa3bae7f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "108",
        "token": "IDH",
        "contract": "0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "292",
        "token": "AXPR",
        "contract": "0x5d48f293baed247a2d0189058ba37aa238bd4725",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "513",
        "token": "VXV",
        "contract": "0xa3bed4e1c75d00fa6f4e5e6922db7261b5e9acd2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "514",
        "token": "YFI",
        "contract": "0x196f4727526ea7fb1e17b2071b3d8eaa38486988",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "516",
        "token": "FNX",
        "contract": "0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "519",
        "token": "CRV",
        "contract": "0xcc4304a31d09258b0029ea7fe63d032f52e44efe",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "524",
        "token": "DSLA",
        "contract": "0x2d80f5f5328fdcb6eceb7cacf5dd8aedaec94e20",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "67",
        "token": "LEND",
        "contract": "0x7b22938ca841aa392c93dbb7f4c42178e3d65e88",
        "decimals": "4",
        "is_active": "t"
    },
    {
        "id": "90",
        "token": "INS",
        "contract": "0x0f4ca92660efad97a9a70cb0fe969c755439772c",
        "decimals": "9",
        "is_active": "t"
    },
    {
        "id": "97",
        "token": "SAL",
        "contract": "0xae73b38d1c9a8b274127ec30160a4927c4d71824",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "100",
        "token": "CBT",
        "contract": "0xbf2179859fc6d5bee9bf9158632dc51678a4100e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "116",
        "token": "QASH",
        "contract": "0xda6cb58a0d0c01610a29c5a65c303e13e885887c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "123",
        "token": "MTN",
        "contract": "0x2baac9330cf9ac479d819195794d79ad0c7616e3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "131",
        "token": "DXT",
        "contract": "0x408e41876cccdc0f92210600ef50372656052a38",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "139",
        "token": "FND",
        "contract": "0x5e6b6d9abad9093fdc861ea1600eba1b355cd940",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "146",
        "token": "LION",
        "contract": "0x72dd4b6bd852a3aa172be4d6c5a6dbec588cf131",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "155",
        "token": "LALA",
        "contract": "0xe5dada80aa6477e85d09747f2842f7993d0df71c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "163",
        "token": "BAX",
        "contract": "0xe5f166c0d8872b68790061317bb6cca04582c912",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "178",
        "token": "CAPP",
        "contract": "0x28dee01d53fed0edf5f6e310bf8ef9311513ae40",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "186",
        "token": "MTC",
        "contract": "0x41ab1b6fcbb2fa9dced81acbdec13ea6315f2bf2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "197",
        "token": "IVY",
        "contract": "0x0947b0e6d821378805c9598291385ce7c791a6b2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "205",
        "token": "HOT",
        "contract": "0x922ac473a3cc241fd3a0049ed14536452d58d73c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "214",
        "token": "UBT",
        "contract": "0xe1aee98495365fc179699c1bb3e761fa716bee62",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "221",
        "token": "WYS",
        "contract": "0x1829aa045e21e0d59580024a951db48096e01782",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "229",
        "token": "IPL",
        "contract": "0xbdc5bac39dbe132b1e030e898ae3830017d7d969",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "244",
        "token": "ICNQ",
        "contract": "0x21f0f0fd3141ee9e11b3d7f13a1028cd515f459c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "252",
        "token": "METM",
        "contract": "0x64ff248ddd36430e3640fbea76999941a8bccbd7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "504",
        "token": "TERN",
        "contract": "0x0ae055097c6d159879521c384f1d2123d1f195e6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "511",
        "token": "MTA",
        "contract": "0x30f271c9e86d2b7d00a6376cd96a1cfbd5f0b9b3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "515",
        "token": "PLT",
        "contract": "0x7d29a64504629172a429e64183d6673b9dacbfce",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "496",
        "token": "JRT",
        "contract": "0xd9ec3ff1f8be459bb9369b4e79e9ebcf7141c093",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "260",
        "token": "UPP",
        "contract": "0x8a77e40936bbc27e80e9a3f526368c967869c86d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "268",
        "token": "LCK",
        "contract": "0xf8e06e4e4a80287fdca5b02dccecaa9d0954840f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "276",
        "token": "DIW",
        "contract": "0xa3d58c4e56fedcae3a7c43a725aee9a71f0ece4e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "284",
        "token": "ZXC",
        "contract": "0x423b5f62b328d0d6d44870f4eee316befa0b2df5",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "295",
        "token": "DACC",
        "contract": "0xd7b3669c7d3e38ab5a441383d41f25e003e02148",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "303",
        "token": "BNC",
        "contract": "0x1efc4dfd580df95426a0f04848870bd8cb5a338e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "311",
        "token": "ABL",
        "contract": "0xbdeb4b83251fb146687fa19d1c660f99411eefe3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "326",
        "token": "EDN",
        "contract": "0x954b890704693af242613edef1b603825afcd708",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "335",
        "token": "JSE",
        "contract": "0xd07d9fe2d2cc067015e2b4917d24933804f42cfa",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "342",
        "token": "HEAL",
        "contract": "0x1c5f43710a1776b0ea7191b7ead75d4b98d69858",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "494",
        "token": "KAI",
        "contract": "0xcd62b1c403fa761baadfc74c525ce2b51780b184",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "486",
        "token": "LCX",
        "contract": "0x16b0a1a87ae8af5c792fabc429c4fe248834842b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "489",
        "token": "PYLNT",
        "contract": "0xfe2786d7d1ccab8b015f6ef7392f67d778f8d8d7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "487",
        "token": "PRQ",
        "contract": "0x4730fb1463a6f1f44aeb45f6c5c422427f37f4d0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "488",
        "token": "LEDU",
        "contract": "0x037a54aab062628c9bbae1fdb1583c195585fe41",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "490",
        "token": "UMA",
        "contract": "0xc741f06082aa47f93729070ad0dd95e223bda091",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "491",
        "token": "EDI",
        "contract": "0xd8924385cd46e6af6f377871c732bde2f8e9dd18",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "495",
        "token": "DXD",
        "contract": "0x0f7f961648ae6db43c75663ac7e5414eb79b5704",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "498",
        "token": "USDT",
        "contract": "0x8a9c67fee641579deba04928c4bc45f66e26343a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "500",
        "token": "BAL",
        "contract": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "501",
        "token": "DMG",
        "contract": "0xc00e94cb662c3520282e6f5717214004a7f26888",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "503",
        "token": "DEXT",
        "contract": "0xed91879919b71bb6905f23af0a68d231ecf87b14",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "74",
        "token": "BLT",
        "contract": "0x3c6a7ab47b5f058be0e7c7fe1a4b7925b8aca40e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "505",
        "token": "CUR",
        "contract": "0x26ce25148832c04f3d7f26f32478a9fe55197166",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "507",
        "token": "TAT",
        "contract": "0x13339fd07934cd674269726edf3b5ccee9dd93de",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "521",
        "token": "SUSHI",
        "contract": "0xd533a949740bb3306d119cc777fa900ba034cd52",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "36",
        "token": "MANA",
        "contract": "0x3d1ba9be9f66b8ee101911bc36d3fb562eac2244",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "51",
        "token": "ENG",
        "contract": "0xc0eb85285d83217cd7c891702bcbc0fc401e2d9d",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "195",
        "token": "LND",
        "contract": "0xd2fa8f92ea72abb35dbd6deca57173d22db2ba49",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "237",
        "token": "ETK",
        "contract": "0x6fb3e0a217407efff7ca062d46c26e5d60a14d69",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "291",
        "token": "HYB",
        "contract": "0x93ed3fbe21207ec2e8f2d3c3de6e058cb73bc04d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "497",
        "token": "GHOST",
        "contract": "0xa1d65e8fb6e87b60feccbc582f7f97804b725521",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "508",
        "token": "BZRX",
        "contract": "0x491604c0fdf08347dd1fa4ee062a822a5dd06b5d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "82",
        "token": "UFR",
        "contract": "0x672a1ad4f667fb18a333af13667aa0af1f5b5bdd",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "170",
        "token": "YUP",
        "contract": "0xafd8f91c4d7c2e3240f4154a1c596048035eb63c",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "4",
        "token": "DGD",
        "contract": "0xd8912c10681d8b21fd3742244f44658dba12264e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "64",
        "token": "GVT",
        "contract": "0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "79",
        "token": "TAU",
        "contract": "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "315",
        "token": "DIP",
        "contract": "0x177d39ac676ed1c67a2b268ad7f1e58826e5b0af",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "102",
        "token": "PRO",
        "contract": "0x076c97e1c869072ee22f8c91978c99b4bcb02591",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "154",
        "token": "FDZ",
        "contract": "0xbc86727e770de68b1060c91f6bb6945c73e10388",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "317",
        "token": "CST",
        "contract": "0xc719d010b63e5bbf2c0551872cd5316ed26acd83",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "318",
        "token": "HAND",
        "contract": "0x6704b673c70de9bf74c8fba4b4bd748f0e2190e1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "193",
        "token": "ORI",
        "contract": "0xf83301c5cd1ccbb86f466a6b3c53316ed2f8465a",
        "decimals": "6",
        "is_active": "t"
    },
    {
        "id": "323",
        "token": "HAVY",
        "contract": "0x3543638ed4a9006e4840b105944271bcea15605d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "324",
        "token": "CARD",
        "contract": "0x0f71b8de197a1c84d31de0f1fa7926c365f052b3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "351",
        "token": "GMB",
        "contract": "0x979ebc09e55ea0ab563cf7175e4c4b1a03afc19a",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "359",
        "token": "SPRING",
        "contract": "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "366",
        "token": "UGAS",
        "contract": "0x026e62dded1a6ad07d93d39f96b9eabd59665e0d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "374",
        "token": "ANKR",
        "contract": "0x0f02e27745e3b6e9e1310d19469e2b5d7b5ec99a",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "383",
        "token": "NFC",
        "contract": "0xa6446d655a0c34bc4f05042ee88170d056cbaf45",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "389",
        "token": "RC20",
        "contract": "0x1410d4ec3d276c0ebbf16ccbe88a4383ae734ed0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "391",
        "token": "ORME",
        "contract": "0x61b2d3ea9f1c6b387c985c73d40e8fbfb284e5c7",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "399",
        "token": "BQQQ",
        "contract": "0x8762db106b2c2a0bccb3a80d1ed41273552616e8",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "407",
        "token": "EQUAD",
        "contract": "0x7756edf05ef3c2b321a85d77b5cbf7c8a9a7c247",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "414",
        "token": "POLL",
        "contract": "0x92b914f1ddcbb1d117a718e83c9ed7eb32fc44d1",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "422",
        "token": "DPH",
        "contract": "0xaeaabb69dcb0fe926b1979f0b032fcd17fd7b2e0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "430",
        "token": "UDOO",
        "contract": "0x3505f494c3f0fed0b594e01fa41dd3967645ca39",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "437",
        "token": "XRT",
        "contract": "0xd6a55c63865affd67e2fb9f284f87b7a9e5ff3bd",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "441",
        "token": "CYFM",
        "contract": "0xdba8e8021fe321af91fc3a08e223ef15908cb2bb",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "445",
        "token": "ROOBEE",
        "contract": "0xba11d00c5f74255f56a5e366f4f77f5a186d7f55",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "453",
        "token": "PEG",
        "contract": "0x4575f41308ec1483f3d399aa9a2826d74da13deb",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "460",
        "token": "PXAG",
        "contract": "0x6a7041ff8cb4da0253a00bb1e548caf77c238bda",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "468",
        "token": "PSGD",
        "contract": "0x224d4b441cde579b5b691ee464468f90d3475bb7",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "475",
        "token": "PDCR",
        "contract": "0xb22466a9e500a609d1febf229e032f4793b339f5",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "476",
        "token": "PZEC",
        "contract": "0xb7a2e4b7a93d57133f37aa74485390053e473219",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "198",
        "token": "ABYSS",
        "contract": "0xc12d099be31567add4e4e4d0d45691c3f58f5663",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "212",
        "token": "BZNT",
        "contract": "0x464ebe77c293e473b48cfe96ddcf88fcf7bfdac0",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "219",
        "token": "FXT",
        "contract": "0x6758b7d441a9739b98552b373703d8d3d14f9e62",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "236",
        "token": "RTE",
        "contract": "0x84f7c44b6fed1080f647e354d552595be2cc602f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "483",
        "token": "KBC",
        "contract": "0x6b175474e89094c44da98b954eedeac495271d0f",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "493",
        "token": "XIO",
        "contract": "0x79c5a1ae586322a07bfb60be36e1b31ce8c84a1e",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "502",
        "token": "STAKE",
        "contract": "0xba100000625a3754423978a60c9317c58a424e3d",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "510",
        "token": "ALEPH",
        "contract": "0x56d811088235f11c8920698a204a5010a788f4b3",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "518",
        "token": "LIBERTAS",
        "contract": "0xef9cd7882c067686691b6ff49e650b43afbbcc6b",
        "decimals": "18",
        "is_active": "t"
    },
    {
        "id": "520",
        "token": "TRADE",
        "contract": "0x49184e6dae8c8ecd89d8bdc1b950c597b8167c90",
        "decimals": "2",
        "is_active": "t"
    },
    {
        "id": "525",
        "token": "FRONT",
        "contract": "0x4b7ad3a56810032782afce12d7d27122bdb96eff",
        "decimals": "8",
        "is_active": "t"
    },
    {
        "id": "3",
        "token": "1ST",
        "contract": "0x0000000000000000000000000000000000000000",
        "decimals": "18",
        "is_active": "t"
    }
]

# from exchange_pairs.models import TrustedPairs, CustomSql
# from .models import Uniswap, UniswapOne

koef = 0.99


def currencies_update_v1(direction, lowest_ask, highest_bid, tokenid):
    print(direction, lowest_ask, highest_bid, tokenid)
    # pair_id = UniswapOne.objects.filter(exch_direction=direction).values('id')
    # if len(pair_id) > 0:
    #     UniswapOne.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
    #                                                           highest_bid=highest_bid, tokenid=tokenid)
    # else:
    #     pair = UniswapOne(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
    #                       tokenid=tokenid)
    #     pair.save()


def currencies_update_v2(direction, lowest_ask, highest_bid, tokenid):
    direction, lowest_ask, highest_bid, tokenid
    # pair_id = Uniswap.objects.filter(exch_direction=direction).values('id')
    # if len(pair_id) > 0:
    #     print(pair_id[0]['id'], direction, lowest_ask, highest_bid, tokenid)
    #     Uniswap.objects.filter(id=pair_id[0]['id']).update(exch_direction=direction, lowest_ask=lowest_ask,
    #                                                        highest_bid=highest_bid, tokenid=tokenid)
    # else:
    #     pair = Uniswap(exch_direction=direction, lowest_ask=lowest_ask, highest_bid=highest_bid, is_active=True,
    #                    tokenid=tokenid)
    #     pair.save()


def set_currencies_v1(date, trusted_tokens):
    url_v1 = 'https://api.thegraph.com/subgraphs/name/graphprotocol/uniswap'
    response = requests.post(url=url_v1, data=date)
    jData = json.loads(response.content)['data']
    for data in jData['exchanges']:
        if float(data['ethLiquidity']) > 0 and float(data['ethBalance']) > 1:
            direction = data['tokenSymbol']
            lowest_ask = 1.003 / float(data['price'])
            highest_bid = lowest_ask * koef
            tokenid = data['tokenAddress']
            for row in trusted_tokens:
                if row['token'] == direction and row['contract'] == tokenid:
                    currencies_update_v1(direction, lowest_ask, highest_bid, tokenid)
                    print('--------')
                    print('equal', row['contract'], tokenid)
                    print('equal', row['token'], direction)
                elif row['token'] == direction:
                    print('--------')
                    print('equal', row['token'], direction)
                    print('not equal', row['contract'], tokenid)
                elif row['contract'] == tokenid:
                    print('--------')
                    print('equal', row['contract'], tokenid)
                    print('not equal', row['token'], direction)


def set_currencies_v2(date, trusted_tokens):
    # proxies = {
    #     'http': '46.102.73.244:53281',
    #     'https': '199.91.203.210:3128'
    # }
    url_v2 = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    # response = requests.post(url=url_v2, data=date, proxies=proxies)
    response = requests.post(url=url_v2, data=date)
    jData = json.loads(response.content)['data']
    for data in jData['tokens']:
        if data['totalLiquidity'] is not None:
            if float(data['derivedETH']) > 0 and float(data['totalLiquidity']) > 1:
                direction = data['symbol']
                highest_bid = float(data['derivedETH']) * koef
                lowest_ask = float(data['derivedETH'])
                tokenid = data['id']
                for row in trusted_tokens:
                    if row['token'] == direction and row['contract'] == tokenid:
                        currencies_update_v2(direction, lowest_ask, highest_bid, tokenid)
                        print('--------')
                        print('equal', row['contract'], tokenid)
                        print('equal', row['token'], direction)
                    elif row['token'] == direction:
                        print('--------')
                        print('equal', row['token'], direction)
                        print('not equal', row['contract'], tokenid)
                    elif row['contract'] == tokenid:
                        print('--------')
                        print('equal', row['contract'], tokenid)
                        print('not equal', row['token'], direction)
                    # else:
                    #     print('not equal all', row['token'], direction)


def set_all_currencies():
    # trusted_tokens = TrustedPairs.objects.all().values()
    trusted_tokens = TRUSTED
    pages_v1 = 4
    pages_v2 = 8
    for i in range(pages_v2):
        req_v2 = f'''
            {{"query":"{{ tokens (first: 1000, skip: {i * 1000}) {{ id derivedETH symbol name totalLiquidity tradeVolume }} }}","variables":{{}}}}
        '''
        set_currencies_v2(req_v2, trusted_tokens)

    for i in range(pages_v1):
        req_v1 = f'''
            {{"query":"{{exchanges(first: 1000, skip: {i * 1000}) {{ ethBalance ethLiquidity tokenAddress price tokenName tokenSymbol}}}}","variables":{{}}}}
        '''
        set_currencies_v1(req_v1, trusted_tokens)
    # CustomSql.objects.raw('''
    #     UPDATE exchange_pairs SET uniswap_direction_id = s.id
    #     FROM (SELECT mu.id, mu.exch_direction FROM module_uniswap mu
    #     LEFT JOIN exchange_pairs ep ON replace(ep.exch_direction, 'ETH_', '') = mu.exch_direction) s
    #     WHERE s.exch_direction = replace(exchange_pairs.exch_direction, 'ETH_', '');
    #
    #     UPDATE exchange_pairs SET uniswap_one_direction_id = s.id
    #     FROM (SELECT muo.id, muo.exch_direction FROM module_uniswap_one muo
    #     LEFT JOIN exchange_pairs ep ON replace(ep.exch_direction, 'ETH_', '') = muo.exch_direction) s
    #     WHERE s.exch_direction = replace(exchange_pairs.exch_direction, 'ETH_', '');


# ''')

set_all_currencies()
