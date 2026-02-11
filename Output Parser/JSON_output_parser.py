from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Model (NO ChatHuggingFace)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
)

# JSON parser
parser = JsonOutputParser()

# Prompt
template = PromptTemplate(
    template="""
Give me 5 facts about {topic}.
Return ONLY valid JSON.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Chain
chain = template | llm | parser

# Invoke
result = chain.invoke({"topic": "black hole"})
print(result)
