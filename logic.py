import aiohttp  # A library for asynchronous HTTP requests
import random
import asyncio
from datetime import timedelta,datetime

class Pokemon:
    pokemons = {}

    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer,):
        self.pokemon_trainer = pokemon_trainer
        self.hp = random.randint(10, 50)
        self.power = random.randint(1, 15)
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.last_feed_time = datetime.now()
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]
    
    async def feed(self, feed_interval = 0, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(minutes=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = delta_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {self.last_feed_time+delta_time}"
    
    async def attack(self, enemy):
        if isinstance(enemy, Wizard):  # Periksa apakah musuh adalah tipe data Penyihir (instance dari kelas Penyihir)
            kesempatan = random.randint(1,5)
            if kesempatan == 1:
                return "Pokemon penyihir menggunakan perisai dalam pertarungan"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pertarungan @{self.pokemon_trainer} dengan @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"@{self.pokemon_trainer} menang melawan @{enemy.pokemon_trainer}!"

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['forms'][0]['name']  # Returning a Pokémon's name
                else:
                    return "Pikachu" 

    async def info(self):
        # A method that returns information about the pokémon
        if not self.name:
            self.name = await self.get_name()  # Retrieving a name if it has not yet been uploaded
        return f"The name of your Pokémon: {self.name} The HP your pokemon get :{self.hp} The Power your pokemon get :{self.power}"  # Returning the string with the Pokémon's name

    async def show_img(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['sprites']['front_default']  # Returning a Pokémon's name
                else:
                    return "Image Not Found."  # Return the default name if the request fails
                
    
    async def show_skill(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['abilities'][0]['ability']['name']  # Returning a Pokémon's name
                else:
                    return "Skill Not Found."  # Return the default name if the request fails
                
    async def show_moves(self):
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['moves'][0]['move']['name']  # Returning a Pokémon's name
                else:
                    return "Moves Not Found."  # Return the default name if the request fails

class Wizard(Pokemon):

    async def feed(self, feed_interval = 0, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(minutes=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = delta_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {self.last_feed_time+delta_time}"
        
    async def attack(self, enemy):
        return await super().attack(enemy)

class Fighter(Pokemon):
    async def feed(self, feed_interval = 0, hp_increase = 15 ):
        current_time = datetime.now()  
        delta_time = timedelta(minutes=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = delta_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {self.last_feed_time+delta_time}"
        
    async def attack(self, enemy):
        kekuatan_super = random.randint(5,15)
        self.power += kekuatan_super
        hasil = await super().attack(enemy)
        self.power-= kekuatan_super
        return hasil + f"\nPetarung menggunakan serangan super dengan kekuatan:{kekuatan_super} "


async def main():
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(await wizard.info())
    print()
    print(await fighter.info())
    print()
    print(await fighter.attack(wizard))   

if __name__ == '__main__':
    asyncio.run(main())





