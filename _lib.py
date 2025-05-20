import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def run_langchain():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough

    model = ChatOpenAI(model="gpt-3.5-turbo")

    template = """
    You are a helpful assistant that provides clear and concise answers.

    Question: {question}

    Please provide a helpful answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    output_parser = StrOutputParser()

    chain = ({"question": RunnablePassthrough()} | prompt | model | output_parser)

    question = "What is the capital of France?"
    response = chain.invoke(question)

    print(f"Question: {question}")
    print(f"Response: {response}")

    question2 = "How does photosynthesis work?"
    response2 = chain.invoke(question2)

    print(f"\nQuestion: {question2}")
    print(f"Response: {response2}")
