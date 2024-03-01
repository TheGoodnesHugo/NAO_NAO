import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "oe": "Una llamado hacia una persona de manera poco bonita",
            "Bocon": "Alguien que habla de mas",
            "Camaron": "Alguien que es malo para una cosa":
            }

palabra = input("Que palabra no entiendes?")

if palabra in meme_dict:
    print(palabra+ ":", meme_dict[palabra] )
else:
    print("Nope , nada brother")
    clave = random.choice( meme_dict.keys() )
