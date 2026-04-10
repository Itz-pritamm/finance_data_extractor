
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq (model_name="llama-3.3-70b-versatile")

def extract(article_text):
    prompt='''
    From the below news article, extract revenue and eps in JSON format containing the following keys: 'revenue_actual', 'revenue_expected', 'eps_actual', 'eps_expected'.
    each value has its unit such as cents, billion
    only return the valid json not preamble.

    Article
    ========
    {article}
    '''
    pt=PromptTemplate.from_template(prompt)

    global llm
    chain = pt|llm
    res=chain.invoke({"article":article_text})
    parser=JsonOutputParser()

    try:
        res=parser.parse(res.content)

    except OutputParserException:
        raise OutputParserException("context too big unable to parse jobs..")

    

    return res
