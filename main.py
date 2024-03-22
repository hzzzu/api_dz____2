import requests

def get_mars_rover_photos(sol, camera):
    api_key = '2pCZ4dykdHmYHURdzLlsz3SWhCcapvsTHlskfTnR'
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&camera={camera}&api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['photos']

def main():
    sol = input("Введите номер сола: ")
    camera = input("Введите название камеры (например, FHAZ, RHAZ, MAST, CHEMCAM, MAHLI): ")
    photos = get_mars_rover_photos(sol, camera)
    print(f"Найдено {len(photos)} фотографий:")
    for photo in photos:
        print(photo['img_src'])

if __name__ == "__main__":
    main()