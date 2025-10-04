import streamlit as st
import matplotlib.pyplot as plt
import math
from fpdf import FPDF
import io

st.title("Body na kružnici")
st.write("Tato aplikace vykreslí body na kružnici podle zadaných údajů.")

# Vstupy
st.sidebar.header("Zadej údaje:")
x = st.sidebar.number_input("Souřadnice středu X (m)", value=0.0)
y = st.sidebar.number_input("Souřadnice středu Y (m)", value=0.0)
r = st.sidebar.number_input("Poloměr (m)", value=5.0, min_value=0.1)
n = st.sidebar.number_input("Počet bodů", min_value=1, value=8)
barva = st.sidebar.color_picker("Barva bodů", "#ff0000")

# Výpočet bodů
uhly = [2 * math.pi * i / n for i in range(n)]
body = [(x + r * math.cos(u), y + r * math.sin(u)) for u in uhly]

# Vykreslení
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlabel("X [m]")
ax.set_ylabel("Y [m]")

# Kružnice a body
kruh = plt.Circle((x, y), r, fill=False, color='blue', linestyle='--')
ax.add_artist(kruh)
x_vals, y_vals = zip(*body)
ax.scatter(x_vals, y_vals, color=barva)
for i, (bx, by) in enumerate(body):
    ax.text(bx, by, str(i+1), ha='center', va='center', fontsize=9)

ax.set_xlim(x - r - 2, x + r + 2)
ax.set_ylim(y - r - 2, y + r + 2)

st.pyplot(fig)

# Uložení do PDF
if st.button("Uložit do PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Body na kružnici", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Střed: ({x}, {y}) m", ln=True)
    pdf.cell(200, 10, txt=f"Poloměr: {r} m", ln=True)
    pdf.cell(200, 10, txt=f"Počet bodů: {n}", ln=True)
    pdf.cell(200, 10, txt=f"Barva: {barva}", ln=True)
    pdf.cell(200, 10, txt="Autor: Michaela Č.", ln=True)
    pdf.cell(200, 10, txt="Kontakt: vas_email@example.com", ln=True)

    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    st.download_button("Stáhnout PDF", data=pdf_buffer, file_name="kruznice.pdf", mime="application/pdf")

if st.sidebar.button("O aplikaci"):
    st.info("""
    **Autor:** Michaela Č.  
    **Použité technologie:** Python, Streamlit, Matplotlib, FPDF  
    """)
