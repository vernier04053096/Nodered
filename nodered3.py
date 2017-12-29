[
    {
        "id": "6d126447.75027c",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "b1ae22e4.2367e",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "edbedd64.2400f",
        "type": "rpi-gpio in",
        "z": "6d126447.75027c",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 102,
        "y": 170,
        "wires": [
            [
                "4683802b.b3df4",
                "8d92f36d.ee61a"
            ]
        ]
    },
    {
        "id": "8d92f36d.ee61a",
        "type": "debug",
        "z": "6d126447.75027c",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 610,
        "y": 120,
        "wires": []
    },
    {
        "id": "397795e3.98a57a",
        "type": "rpi-gpio out",
        "z": "6d126447.75027c",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 632,
        "y": 261,
        "wires": []
    },
    {
        "id": "4683802b.b3df4",
        "type": "switch",
        "z": "6d126447.75027c",
        "name": "If input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 270,
        "y": 220,
        "wires": [
            [
                "45430f41.741d5"
            ],
            [
                "7cd9e0a6.1d472"
            ]
        ]
    },
    {
        "id": "45430f41.741d5",
        "type": "change",
        "z": "6d126447.75027c",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 200,
        "wires": [
            [
                "397795e3.98a57a"
            ]
        ]
    },
    {
        "id": "7cd9e0a6.1d472",
        "type": "change",
        "z": "6d126447.75027c",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 450,
        "y": 281,
        "wires": [
            [
                "397795e3.98a57a"
            ]
        ]
    },
    {
        "id": "638b7c28.ec5644",
        "type": "inject",
        "z": "b1ae22e4.2367e",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 192,
        "y": 139,
        "wires": [
            [
                "38a52f4c.e413d",
                "436bbf3a.8114"
            ]
        ]
    },
    {
        "id": "38a52f4c.e413d",
        "type": "function",
        "z": "b1ae22e4.2367e",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"768S0iu7dtCJDZYw\"\n};\n\nmsg.payload= \"Temperature,,30.0\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 120,
        "wires": [
            [
                "da51d924.80eeb8"
            ]
        ]
    },
    {
        "id": "da51d924.80eeb8",
        "type": "http request",
        "z": "b1ae22e4.2367e",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/Dt3t808n/datapoints.csv",
        "tls": "",
        "x": 530,
        "y": 120,
        "wires": [
            [
                "b366816b.030fe",
                "49053931.9d6728"
            ]
        ]
    },
    {
        "id": "b366816b.030fe",
        "type": "http response",
        "z": "b1ae22e4.2367e",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 770,
        "y": 120,
        "wires": []
    },
    {
        "id": "49053931.9d6728",
        "type": "debug",
        "z": "b1ae22e4.2367e",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 750,
        "y": 180,
        "wires": []
    },
    {
        "id": "436bbf3a.8114",
        "type": "function",
        "z": "b1ae22e4.2367e",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"768S0iu7dtCJDZYw\"\n};\n\nmsg.payload= \"Humidity,,50.0\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 180,
        "wires": [
            [
                "f3c07ba0.6ad208"
            ]
        ]
    },
    {
        "id": "f3c07ba0.6ad208",
        "type": "http request",
        "z": "b1ae22e4.2367e",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/Dt3t808n/datapoints.csv",
        "tls": "",
        "x": 550,
        "y": 180,
        "wires": [
            [
                "49053931.9d6728",
                "b366816b.030fe"
            ]
        ]
    }
]
