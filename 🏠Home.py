import json
import streamlit as st
import streamlit.components.v1 as components

def load_database(path:str)-> dict:
    with open(path, 'r') as file:
        data: dict = json.load(file)
    return data



     

database:dict = load_database("menu\meat_burger.json")

header = st.header("Meat Burgers")

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
imageUrls = []
imageUrls_chicken = []
for q in database["items"]:
    imageUrls.append(q["img"])
selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

database:dict = load_database("menu\chicken_burger.json")
header = st.header("Chicken Burgers")
imageCarouselComponent_chiken = components.declare_component("image-carousel-component", path="frontend/public")
for q in database["items"]:
    imageUrls_chicken.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="chiken",imageUrls=imageUrls_chicken, height=200)



imageUrls_fries = []
header = st.header("Chili Fries")
database_chili:dict = load_database("menu\chili_fries.json")
imageCarouselComponent_fries = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_chili["items"]:
    imageUrls_fries.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="fries",imageUrls=imageUrls_fries, height=200)


imageUrls_fries = []
header = st.header("Salads")
database_chili:dict = load_database("menu\salads.json")
imageCarouselComponent_fries = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_chili["items"]:
    imageUrls_fries.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="salads",imageUrls=imageUrls_fries, height=200)


imageUrls_health = []
header = st.header("Healthy")
database_healthy:dict = load_database("menu\healthy.json")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_healthy["items"]:
    imageUrls_health.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="healthy",imageUrls=imageUrls_health, height=200)


imageUrls_health = []
header = st.header("Apptigers")
database_healthy:dict = load_database("menu\apigers.json")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_healthy["items"]:
    imageUrls_health.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="appigers",imageUrls=imageUrls_health, height=200)


imageUrls_health = []
header = st.header("Adds")
database_healthy:dict = load_database("menu\adds.json")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_healthy["items"]:
    imageUrls_health.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="adds",imageUrls=imageUrls_health, height=200)


imageUrls_health = []
header = st.header("Drinks")
database_healthy:dict = load_database("menu\drinks.json")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_healthy["items"]:
    imageUrls_health.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="drinks",imageUrls=imageUrls_health, height=200)



imageUrls_health = []
header = st.header("Sauces")
database_healthy:dict = load_database("menu\sauces.json")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="frontend/public")
for q in database_healthy["items"]:
    imageUrls_health.append(q["img"])
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="sauces",imageUrls=imageUrls_health, height=200)
