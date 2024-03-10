# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from openai import OpenAI
import json
import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def simple_classify(client, input_string: str, prompt_string:str) -> str:

  completion = client.completions.create(model='gpt-3.5-turbo-instruct',
                                         prompt=f"{prompt_string}: {input_string}")
  response=completion.choices[0].text
  print(f"For {input_string}, response is:\n----------{response}\n=============")
  #print(dict(completion).get('usage'))
  #print(completion.model_dump_json(indent=2))
  return response

def run():
    st.set_page_config(page_title="Ovee Dharwadkar's Sentiment Analysis Using OpenAI", page_icon="🤪")
    st.markdown("# Ovee Dharwadkar's Sentiment Analysis Using OpenAI")
    st.write("""This is my first app with Q&A LLM!""")

    password = st.text_input("Enter your OpenAI key: ")
    prompt = st.text_input("Enter a prompt: ")
    user_input = st.text_area("User Input: ")
    if password:  
      client = OpenAI(api_key=password)
      response = simple_classify(client, user_input, prompt) 
      st.write(f"response is{response}")


if __name__ == "__main__":
  run()


