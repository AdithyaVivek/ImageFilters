
import streamlit as st
from PIL import Image, ImageFilter

# uploaded_image = st.file_uploader("Upload File")


def download_file(image):
    with open("altered_img.png", "rb") as file:
        btn = st.download_button(
            label="Download",
            data=file,
            file_name=image,
            mime="image/png")


with st.expander("Open Camera"):
    camera_image = st.camera_input("Camera")


if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert("L")
    blur_image = img.filter(ImageFilter.BLUR)
    contour = img.filter(ImageFilter.CONTOUR)
    detail = img.filter(ImageFilter.DETAIL)
    edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE)
    more_edge_enhance = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    emboss = img.filter(ImageFilter.EMBOSS)
    outline = img.filter(ImageFilter.FIND_EDGES)
    sharpen = img.filter(ImageFilter.SHARPEN)
    smooth = img.filter(ImageFilter.SMOOTH)
    more_smooth = img.filter(ImageFilter.SMOOTH_MORE)

    option = st.selectbox("Select Option: ", ["Original", "Gray Scale", "Blur",
                                              "Contour", "Detail", "Edge Enhance",
                                              "More Edge Enhance", "Emboss", "Outline",
                                              "Sharpen", "Smooth","More Smooth"], key="Option")
    match option:
        case "Original":
            st.image(img)
            img.save("original_img.png")
            download_file("original_img.png")
        case "Gray Scale":
            st.image(gray_image)
            gray_image.save("gray_img.png")
            download_file("gray_img.png")
            # st.download_button("Download", data=gray_image, file_name="altered_img.png", mime="image/png")

        case ("Blur"):
            st.image(blur_image)
            blur_image.save("blur_img.png")
            download_file("blur_img.png")
        case "Contour":
            st.image(contour)
            contour.save("contour_img.png")
            download_file("contour_img.png")
        case "Detail":
            st.image(detail)
            detail.save("detail_img.png")
            download_file("detail_img.png")
        case "Edge Enhance":
            st.image(edge_enhance)
            edge_enhance.save("edge_enhanced.png")
            download_file("edge_enhanced.png")
        case "More Edge Enhance":
            st.image(more_edge_enhance)
            more_edge_enhance.save("more_edge_enhanced.png")
            download_file("more_edge_enhanced.png")
        case "Emboss":
            st.image(emboss)
            emboss.save("emboss.png")
            download_file("emboss.png")
        case "Outline":
            st.image(outline)
            outline.save("outline.png")
            download_file("outline.png")
        case "Sharpen":
            st.image(sharpen)
            sharpen.save("sharpen.png")
            download_file("sharpen.png")
        case "Smooth":
            st.image(smooth)
            smooth.save("smooth.png")
            download_file("smooth.png")
        case "More Smooth":
            st.image(more_smooth)
            more_smooth.save("more_smooth.png")
            download_file("more_smooth.png")



# st.session_state