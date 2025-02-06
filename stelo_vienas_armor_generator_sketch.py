import streamlit as st
from PIL import Image, ImageDraw

# Set Canvas Dimensions
width, height = 600, 800
canvas = Image.new("RGB", (width, height), "#F5E6C8")  # Parchment-style background
draw = ImageDraw.Draw(canvas)

# Sidebar: Armor Customization
st.sidebar.header("Customize Your Knight")

# Armor Selections
helmet = st.sidebar.selectbox("Helmet", ["None", "Great Helm", "Bascinet", "Sallet"])
chestplate = st.sidebar.selectbox("Chestplate", ["None", "Brigandine", "Steel Plate", "Scale Mail"])
pauldrons = st.sidebar.selectbox("Pauldrons", ["None", "Rounded Pauldrons", "Spiked Pauldrons"])
gauntlets = st.sidebar.selectbox("Gauntlets", ["None", "Leather Gloves", "Steel Gauntlets"])
greaves = st.sidebar.selectbox("Greaves", ["None", "Leather Boots", "Steel Greaves"])
cape = st.sidebar.selectbox("Cape", ["None", "Hooded Cloak", "Fur Mantle", "Battle Cape"])
engraving = st.sidebar.checkbox("Add Engravings")
rust_effect = st.sidebar.checkbox("Add Rust Effect")
heraldic_symbol = st.sidebar.selectbox("Heraldic Symbol", ["None", "Lion", "Cross", "Dragon", "Eagle"])

# === DRAWING FUNCTIONS === #

def draw_character():
    """Base figure of the knight."""
    draw.line([(300, 700), (300, 550)], fill="black", width=6)  # Legs
    draw.line([(270, 550), (330, 550)], fill="black", width=6)  # Torso
    draw.ellipse([280, 500, 320, 540], outline="black", width=4)  # Head

def draw_helmet():
    if helmet == "Great Helm":
        draw.rectangle([270, 480, 330, 520], outline="black", width=4)
        draw.line([(270, 500), (330, 500)], fill="black", width=2)  # Visor
    elif helmet == "Bascinet":
        draw.ellipse([270, 490, 330, 520], outline="black", width=4)

def draw_chestplate():
    if chestplate == "Brigandine":
        draw.rectangle([260, 550, 340, 620], outline="black", width=4)
        draw.line([(260, 580), (340, 580)], fill="black", width=2)
    elif chestplate == "Steel Plate":
        draw.rectangle([260, 550, 340, 620], outline="black", width=4)

def draw_pauldrons():
    if pauldrons == "Rounded Pauldrons":
        draw.ellipse([240, 540, 280, 570], outline="black", width=4)
        draw.ellipse([320, 540, 360, 570], outline="black", width=4)
    elif pauldrons == "Spiked Pauldrons":
        draw.polygon([(240, 550), (260, 570), (280, 550)], outline="black", width=4)
        draw.polygon([(320, 550), (340, 570), (360, 550)], outline="black", width=4)

def draw_gauntlets():
    if gauntlets == "Steel Gauntlets":
        draw.rectangle([250, 620, 270, 650], outline="black", width=4)
        draw.rectangle([330, 620, 350, 650], outline="black", width=4)

def draw_greaves():
    if greaves == "Steel Greaves":
        draw.rectangle([270, 700, 290, 750], outline="black", width=4)
        draw.rectangle([310, 700, 330, 750], outline="black", width=4)

def draw_cape():
    if cape != "None":
        draw.polygon([(250, 540), (300, 740), (350, 540)], outline="black", width=3)

def draw_engraving():
    if engraving:
        draw.line([(270, 570), (330, 570)], fill="black", width=1)
        draw.line([(270, 600), (330, 600)], fill="black", width=1)

def draw_rust():
    draw.ellipse([280, 570, 290, 580], fill="brown")
    draw.ellipse([320, 590, 330, 600], fill="brown")

def draw_heraldic_symbol():
    if heraldic_symbol == "Lion":
        draw.ellipse([290, 580, 310, 600], outline="black", width=2)
    elif heraldic_symbol == "Cross":
        draw.line([(290, 580), (310, 600)], fill="black", width=2)
        draw.line([(310, 580), (290, 600)], fill="black", width=2)

# === APPLY DRAWINGS BASED ON USER SELECTION === #
draw_character()
draw_helmet()
draw_chestplate()
draw_pauldrons()
draw_gauntlets()
draw_greaves()
draw_cape()
draw_engraving()
draw_heraldic_symbol()

if rust_effect:
    draw_rust()

# Display the Procedural Sketch
st.image(canvas, caption="Procedurally Generated Knight", use_column_width=True)

