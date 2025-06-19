import streamlit as st
import langchain_helper2

st.title('🍽️ Restaurant Name Generator')

# Sidebar cuisine selector
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

# When cuisine is selected
if cuisine:
    response = langchain_helper2.generate_restaurant_name_and_items(cuisine)

    # Display restaurant name
    st.header(f"🏷️ {response['restaurant_name'].strip()}")

    # Display menu items
    menu_items = response['menu_items'].strip().split(",")
    st.subheader("🍴 Menu Items")
    for item in menu_items:
        st.markdown(f"- {item.strip()}")
