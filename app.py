import streamlit as st
import qrcode
from PIL import Image
import io

# 1. Page Layout Configuration
st.set_page_config(page_title="Codédex QR Generator", layout="centered")
st.title("🔗 Instant Air QR Code Generator")
st.write("Convert any URL, text message, or social media link into a scannable QR Code instantly!")

# 2. Input Box for User Data
user_input = st.text_input("👇 Enter your link or text here:", placeholder="https://github.com/amna01ejaz")

st.write("---")

if user_input:
    with st.spinner("Generating your QR Code..."):
        # 3. Configure QR code sizing and design properties
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)

        # 4. Compile the QR matrix into an image map
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert PIL Image object to bytes so Streamlit can handle downloads
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # 5. Display Layout columns
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(byte_im, caption="Scan Me!", width=200)
            
        with col2:
            st.success("✨ QR Code generated successfully!")
            st.write("Test it by pointing your mobile phone camera at the screen right now.")
            
            # 6. Streamlit Download Asset Wire-up
            st.download_button(
                label="💾 Download QR Code (PNG)",
                data=byte_im,
                file_name="my_codedex_qrcode.png",
                mime="image/png"
            )
else:
    st.info("💡 Type a link into the input box above to generate your dynamic QR image overlay!")