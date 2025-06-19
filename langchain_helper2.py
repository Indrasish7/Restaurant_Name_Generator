from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st

def generate_restaurant_name_and_items(cuisine):
    gemini_api_key = st.secrets["GEMINI_API_KEY"]

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # ✅ Correct model name
        temperature=0.6,
        google_api_key=gemini_api_key
    )

    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='Suggest ONE unique and fancy restaurant name for {cuisine} cuisine. Only return the name, without any quotations and nothing else.'
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

    prompt_template_foods = PromptTemplate(
        input_variables=['restaurant_name'],
        template='List exactly 5 popular and creative menu items for a restaurant named "{restaurant_name}". Return ONLY the item names, as a comma-separated list. Do not include any introductions, explanations, or extra text.'
    )

    food_chain = LLMChain(llm=llm, prompt=prompt_template_foods, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    return chain({'cuisine': cuisine})
