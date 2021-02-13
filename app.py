from io import BytesIO
import base64
import streamlit as st
from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw


curso = st.text_input('Seu curso:', 'medicina')
ano = st.text_input('Ano que entrou:', '2018')
turma = st.text_input('Turma, se houver. Deixe em branco se não:', '56')

str1 = 'sim por incrível que pareça eu faço'
str2 = f'{curso.upper()} na UNICAMP'
str3 = f'turma {turma}, entrei em {ano} etc' if turma else f'entrei em {ano} etc'


font = ImageFont.truetype("times-ro.ttf", 20)

img = Image.open('template.jpg')

draw = ImageDraw.Draw(img)

draw.text((155, 20), str1, (0,0,0), font=font)
draw.text((185, 45), str2, (0,0,0), font=font)
draw.text((175, 80), str3, (0,0,0), font=font)

st.write('Guarde sua capa com carinho :)')
st.image(img)

# Copy-pasta daqui https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806/19
def get_image_download_link(img):
	"""Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
	buffered = BytesIO()
	img.save(buffered, format="JPEG")
	img_str = base64.b64encode(buffered.getvalue()).decode()
	href = f'<a href="data:file/jpg;base64,{img_str}" download="capa.jpg">Clique aqui para baixar</a>'
	return href

st.markdown(get_image_download_link(img), unsafe_allow_html=True)
st.write('[Quer contriuir? Mande um pull-request!](https://github.com/tkleyton/gerador-de-capa-unicamp)')
