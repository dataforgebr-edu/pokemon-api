import random

import requests

# rand = random.randint(1, 10)

i = 1
while i <= 10:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{random.randint(1, 100)}"
    )

    data = response.json()

    tp = ", ".join([t["type"]["name"] for t in data["types"]])

    print(f"Pokemon={data['name']} - types={tp}")

    i += 1
