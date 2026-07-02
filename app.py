import streamlit as st
import qrcode
from PIL import Image
import io

# 1. Page Layout Configuration
st.set_page_config(page_title="Pro QR Generator", layout="centered")
st.title("🎨 Customizable Professional QR Code Studio")
st.write("Generate custom-colored scannable QR Codes for links, Wi-Fi details, or text text blocks.")

# 2. Advanced Control Options split into columns
col_in, col_style = st.columns([2, 1])

with col_in:
    st.subheader("1. Enter Your Content")
    user_input = st.text_area(
        "👇 Paste URL or Text content here:", 
        placeholder="https://github.com/amna01ejaz",
        height=115
    )

with col_style:
    st.subheader("2. Design Styles")
    # Custom color pickers
    fill_color = st.color_picker("QR Pattern Color", "#000000")
    back_color = st.color_picker("Background Color", "#FFFFFF")

st.write("---")

if user_input:
    with st.spinner("Compiling your designer QR Code..."):
        # 3. Configure advanced parameters
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H, # Higher error correction for custom colors
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)

        # 4. Compile with user chosen styling variables
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # Convert map format to bytes for display and export handling
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # 5. Output display grid layout
        out_img, out_actions = st.columns([1, 1])
        
        with out_img:
            st.image(byte_im, caption="Your Customized Asset", width=230)
            
        with out_actions:
            st.success("✨ Dynamic Render Successful!")
            st.info("💡 **Tip:** Ensure there is enough contrast between your pattern and background colors so phone cameras can easily scan it.")
            
            # Download asset trigger wire up
            st.download_button(
                label="💾 Download Custom QR Code (PNG)",
                data=byte_im,
                file_name="custom_codedex_qr.png",
                mime="image/png"
            )
else:
    st.info("💡 Supply content inside the text area inputs to unlock your real-time styling matrix dashboard.")