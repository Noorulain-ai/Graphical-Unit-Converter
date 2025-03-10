
import streamlit as st
import matplotlib.pyplot as plt

# --- Streamlit Page Configuration ---
st.set_page_config(page_title="Graphical Unit Converter", page_icon="📏", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
        /* Background Color */
        body {
            background-color: #121212;
        }

        /* Title Styling */
        .title {
            color: #ffffff;
            text-align: center;
            font-size: 60px;
            font-weight: bold;
        }

        /* Sidebar Styling */
        .sidebar .sidebar-content {
            background-color: #1E1E1E !important;
            color: white;
        }

        /* Labels */
        label {
            font-weight: bold;
            font-size: 16px;
            color: ##EFC4C4 !important;
        }

        /* Result Box */
        .result-box {
            background-color: #1E88E5;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 20px;
            color: #ffffff;
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 20px;
            color: #D49DA4C;
        }
    </style>
""", unsafe_allow_html=True)

# --- Conversion Functions ---
def convert_temperature(value, from_unit, to_unit):
    conversions = {
        "Celsius": {"Fahrenheit": (value * 9/5) + 32, "Kelvin": value + 273.15},
        "Fahrenheit": {"Celsius": (value - 32) * 5/9, "Kelvin": (value - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": value - 273.15, "Fahrenheit": (value - 273.15) * 9/5 + 32}
    }
    return conversions[from_unit].get(to_unit, value) if from_unit != to_unit else value

def convert_length(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Inches": 39.3701}
    return value * (length_units[to_unit] / length_units[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_units = {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

def convert_distance(value, from_unit, to_unit):
    distance_units = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Yards": 1.09361}
    return value * (distance_units[to_unit] / distance_units[from_unit])

def convert_speed(value, from_unit, to_unit):
    speed_units = {"m/s": 1, "km/h": 3.6, "mph": 2.237}
    return value * (speed_units[to_unit] / speed_units[from_unit])

def convert_time(value, from_unit, to_unit):
    time_units = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600}
    return value * (time_units[to_unit] / time_units[from_unit])

# --- UI Header ---
#1 st.markdown('<p class="title">⚡ GRAPHICAL UNIT CONVERTER</p>', unsafe_allow_html=True)


st.markdown("""
    <style>
        .title {
            color: #FF5733;  /* Change to desired color (this is a purple shade) */
            text-align: wide;
            font-size: 30px !important;  /* Increased font size */
            font-weight: bold; /* Makes the font bold */
            font-family: 'Arial', sans-serif; /* Change to desired font family */
            text-decoration: underline; /* Underline */
        }
    </style>
    <p class="title">⚡ GRAPHICAL UNIT CONVERTER</p>
""", unsafe_allow_html=True)

st.write("Convert **Temperature 🌡️, Length 📏, Weight ⚖️, Distance 🚀, Speed 🏎️, and Time ⏳** effortlessly!")

# --- Sidebar Selection ---
category = st.sidebar.radio("📌 Select a category:", ["🌡️ Temperature", "📏 Length", "⚖️ Weight", "🚀 Distance", "🏎️ Speed", "⏳ Time"])

# --- UI Layout ---
col1, col2 = st.columns(2)

with col1:
    from_unit, to_unit = None, None
    if category == "🌡️ Temperature":
        from_unit = st.selectbox("🌡️ Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("🌡️ Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])
    elif category == "📏 Length":
        from_unit = st.selectbox("📏 Convert from:", ["Meters", "Kilometers", "Miles", "Inches"])
        to_unit = st.selectbox("📏 Convert to:", ["Meters", "Kilometers", "Miles", "Inches"])
    elif category == "⚖️ Weight":
        from_unit = st.selectbox("⚖️ Convert from:", ["Grams", "Kilograms", "Pounds", "Ounces"])
        to_unit = st.selectbox("⚖️ Convert to:", ["Grams", "Kilograms", "Pounds", "Ounces"])
    elif category == "🚀 Distance":
        from_unit = st.selectbox("🚀 Convert from:", ["Meters", "Kilometers", "Miles", "Yards"])
        to_unit = st.selectbox("🚀 Convert to:", ["Meters", "Kilometers", "Miles", "Yards"])
    elif category == "🏎️ Speed":
        from_unit = st.selectbox("🏎️ Convert from:", ["m/s", "km/h", "mph"])
        to_unit = st.selectbox("🏎️ Convert to:", ["m/s", "km/h", "mph"])
    elif category == "⏳ Time":
        from_unit = st.selectbox("⏳ Convert from:", ["Seconds", "Minutes", "Hours"])
        to_unit = st.selectbox("⏳ Convert to:", ["Seconds", "Minutes", "Hours"])

    value = st.number_input("🔢 Enter Value:", min_value=0.0, format="%.2f")

# --- Conversion Logic ---
result = None
if from_unit and to_unit:
    if category == "🌡️ Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "📏 Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "⚖️ Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "🚀 Distance":
        result = convert_distance(value, from_unit, to_unit)
    elif category == "🏎️ Speed":
        result = convert_speed(value, from_unit, to_unit)
    elif category == "⏳ Time":
        result = convert_time(value, from_unit, to_unit)

# --- Display Result and Graph ---
with col2:
    if st.button("🔄 Convert"):
        st.markdown(f'<p class="result-box">✅ {value} {from_unit} = <strong>{result:.2f} {to_unit}</strong></p>', unsafe_allow_html=True)

        # --- Graphical Representation ---
        fig, ax = plt.subplots()
        ax.bar([from_unit, to_unit], [value, result], color=['#1E88E5', '#E53935'])
        ax.set_ylabel("Value")
        ax.set_title("Unit Conversion Representation")
        st.pyplot(fig)

# --- Footer ---
st.markdown('<p class="footer">🚀 Developed by <b>"Noor Ul Ain"</b> using Python & Streamlit</p>', unsafe_allow_html=True)
