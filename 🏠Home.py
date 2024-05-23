import streamlit as st
import streamlit.components.v1 as components
header = st.header("Meat Burgers")
imageCarouselComponent = components.declare_component("image-carousel-component", path="public")
imageUrls = ['https://i.ibb.co/4tWTbXM/1.png', 'https://i.ibb.co/BzTnz5P/2.png', 'https://i.ibb.co/6DyRD42/3.png', 'https://i.ibb.co/98Vkpz0/4.png', 'https://i.ibb.co/LYnmCv3/5.png', 'https://i.ibb.co/yY0zY1J/6.png', 'https://i.ibb.co/L6BrLty/7.png', 'https://i.ibb.co/85R0Lz1/9.png', 'https://i.ibb.co/mh5wcNM/10.png', 'https://i.ibb.co/LJMqCNd/11.png', 'https://i.ibb.co/YQprmpc/12.png', 'https://i.ibb.co/Y2J3tth/8.png', 'https://i.ibb.co/c27rbsT/8.png']
imageUrls_chicken = ['https://i.ibb.co/5Gt1yWw/1.png', 'https://i.ibb.co/N7cTyNP/2.png', 'https://i.ibb.co/XSs93jh/3.png', 'https://i.ibb.co/vmm0C1M/4.png', 'https://i.ibb.co/3rGCrSJ/5.png', 'https://i.ibb.co/wYdxLSr/6.png', 'https://i.ibb.co/syF05XM/7.png', 'https://i.ibb.co/c27rbsT/8.png']
selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)
