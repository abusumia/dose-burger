import streamlit as st
import streamlit.components.v1 as components


     



header = st.header("Meat Burgers")

imageCarouselComponent = components.declare_component("image-carousel-component", path="public")
imageUrls = ['https://i.ibb.co/4tWTbXM/1.png', 'https://i.ibb.co/BzTnz5P/2.png', 'https://i.ibb.co/6DyRD42/3.png', 'https://i.ibb.co/98Vkpz0/4.png', 'https://i.ibb.co/LYnmCv3/5.png', 'https://i.ibb.co/yY0zY1J/6.png', 'https://i.ibb.co/L6BrLty/7.png', 'https://i.ibb.co/85R0Lz1/9.png', 'https://i.ibb.co/mh5wcNM/10.png', 'https://i.ibb.co/LJMqCNd/11.png', 'https://i.ibb.co/YQprmpc/12.png', 'https://i.ibb.co/Y2J3tth/8.png', 'https://i.ibb.co/c27rbsT/8.png']
imageUrls_chicken = ['https://i.ibb.co/5Gt1yWw/1.png', 'https://i.ibb.co/N7cTyNP/2.png', 'https://i.ibb.co/XSs93jh/3.png', 'https://i.ibb.co/vmm0C1M/4.png', 'https://i.ibb.co/3rGCrSJ/5.png', 'https://i.ibb.co/wYdxLSr/6.png', 'https://i.ibb.co/syF05XM/7.png', 'https://i.ibb.co/c27rbsT/8.png']

selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

header = st.header("Chicken Burgers")
imageCarouselComponent_chiken = components.declare_component("image-carousel-component", path="public")
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="chiken",imageUrls=imageUrls_chicken, height=200)



imageUrls_fries = ['https://i.ibb.co/3kfM7j7/1.png', 'https://i.ibb.co/0FCdywW/2.png', 'https://i.ibb.co/DgJ4CQ3/3.png']
header = st.header("Chili Fries")
imageCarouselComponent_fries = components.declare_component("image-carousel-component", path="public")
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="fries",imageUrls=imageUrls_fries, height=200)


imageUrls_salads = ['https://i.ibb.co/cLjVL0P/1.png', 'https://i.ibb.co/qkknBkT/2.png']
header = st.header("Salads")
imageCarouselComponent_fries = components.declare_component("image-carousel-component", path="public")

selectedImageUrl_chicken = imageCarouselComponent_chiken(key="salads",imageUrls=imageUrls_salads, height=200)


imageUrls_health = ['https://i.ibb.co/CbK2Wgh/1.png', 'https://i.ibb.co/vmszS6g/2.png']
header = st.header("Healthy")

imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="public")
selectedImageUrl_chicken = imageCarouselComponent_chiken(key="healthy",imageUrls=imageUrls_health, height=200)


imageUrls_apigers = ['https://i.ibb.co/HXXxCZ0/1.png', 'https://i.ibb.co/5nPBfG4/2.png', 'https://i.ibb.co/k0RT3SV/3.png', 'https://i.ibb.co/6s791Df/4.png', 'https://i.ibb.co/kDTd81d/5.png', 'https://i.ibb.co/DfhWMjp/6.png', 'https://i.ibb.co/C77P5Zr/7.png', 'https://i.ibb.co/tQrDSWy/8.png', 'https://i.ibb.co/rskrxt8/9.png']
header = st.header("Apptigers")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="public")

selectedImageUrl_chicken = imageCarouselComponent_chiken(key="appigers",imageUrls=imageUrls_apigers, height=200)


imageUrls_adds = ['https://i.ibb.co/XsMGkTj/1.png', 'https://i.ibb.co/XCLLwCD/2.png', 'https://i.ibb.co/QmnRv6b/3.png', 'https://i.ibb.co/dkJZbJv/4.png']
header = st.header("Adds")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="public")

selectedImageUrl_chicken = imageCarouselComponent_chiken(key="adds",imageUrls=imageUrls_adds, height=200)


imageUrls_drinks = ['https://i.ibb.co/QcXBb84/1.png', 'https://i.ibb.co/x2jxqfW/2.png', 'https://i.ibb.co/5rQ0Yh9/3.png', 'https://i.ibb.co/RQ2WjJP/4.png']
header = st.header("Drinks")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="public")

selectedImageUrl_chicken = imageCarouselComponent_chiken(key="drinks",imageUrls=imageUrls_drinks, height=200)



imageUrls_sauces = ['https://i.ibb.co/PGMZrdM/1.png', 'https://i.ibb.co/YWFC7TX/2.png', 'https://i.ibb.co/rF6cH27/3.png', 'https://i.ibb.co/S694Rpj/4.png', 'https://i.ibb.co/h1frsKG/5.png', 'https://i.ibb.co/zSsZSmV/6.png', 'https://i.ibb.co/mvDR1KH/7.png', 'https://i.ibb.co/HHGmpwK/8.png', 'https://i.ibb.co/2W5fnRT/9.png']
header = st.header("Sauces")
imageCarouselComponent_healthy = components.declare_component("image-carousel-component", path="public")

selectedImageUrl_chicken = imageCarouselComponent_chiken(key="sauces",imageUrls=imageUrls_sauces, height=200)
