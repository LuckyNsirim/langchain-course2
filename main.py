# import functions
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course2!")
    information = """
    His Royal Majesty, Nyenwe-Eli Omunakwe Nyeche Nsirim (MON), popularly known as OCC, was a prominent Nigerian traditional ruler, businessman, and politician.

Profile & Background

• Title: Apiti of Rumueme Kingdom and Paramount Ruler of Rumueme in Obio/Akpor Local Government Area, Rivers State, Nigeria.
• National Honor: Member of the Order of the Niger (MON).
• Age at Death: Passed away in early January 2023 at the age of 96.
• Recognition: Formally recognized by the Rivers State Government as a first-class traditional ruler in April 2021.

Career & Public Life

• Business & Real Estate: Widely known as a successful business mogul and real estate figure in Rivers State.
• Politics: A prominent political figure who was a leading light of the National Party of Nigeria (NPN) during the Second Republic, working alongside former Governor Melford Okilo. He was also a key advocate in the creation of the Obio-Akpor Local Government Area.
• Legacy: Credited with bringing greater prominence and first-class status to the Rumueme Kingdom.

Posthumous Events

Following his passing in 2023 and subsequent funeral rites in March 2023, the Rumueme Kingdom experienced internal succession disputes and controversies regarding the selection of a new Nyenwe-Eli.
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["infrmation"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    # llm = ChatOllama(temperature=0, model="gemma3:270m", base_url="http://10.0.0.66:11434")
    llm = ChatOllama(temperature=0, model="gpt-oss:20b", base_url="http://10.0.0.66:11434")
    
    

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
