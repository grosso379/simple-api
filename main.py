from fastapi import FastAPI
import json

app = FastAPI()

# Opening JSON file
with open('pokemonTypes.json') as json_file:
    pokemon_types = json.load(json_file)

@app.get("/")
def home():
    return "API running"


@app.get("/pokemon/{pokemon_name}")
def get_pokemon_types(pokemon_name: str):
    if pokemon_name in pokemon_types:
        return pokemon_types[pokemon_name]
    else:
        return {"error": "Pokémon not found"}
