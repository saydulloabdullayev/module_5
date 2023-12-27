import os
import asyncio
import json
from httpx import AsyncClient

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

async def fetch_fruit_data(url, description_file):
    async with AsyncClient() as client:
        folder_path = r"C:\Users\AdminAppDataR\Local\Programs\Python311\Lib\bdb.py"

        file_list = os.listdir(folder_path)

        with open("descriptions.json", "r") as desc_file:
            descriptions = json.load(desc_file)

        print(descriptions)

        for filename in file_list:
            file_path = os.path.join(folder_path, filename)

            # Faylni o'qish
            with open(file_path, 'r') as file:
                data = json.load(file)

            fruit_id = data.get('id', None)
            if fruit_id in descriptions:
                description_data = descriptions[fruit_id]

                name = data.get('name', 'N/A')
                price = data.get('price', 'N/A')
                description = description_data.get('description', 'N/A')

                payload = {'name': name, 'price': price, 'description': description}

                response = await client.post(url, data=payload)

                response_text = f"Response {filename} {response.status_code} \n"
                with FileManager("Response 001.txt", "a") as response_file:
                    response_file.write(response_text)

async def main():
    url = "http://64.227.101.77"
    description_file = "descriptions.json"
    await fetch_fruit_data(url, description_file)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

