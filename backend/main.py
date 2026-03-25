from dotenv import load_dotenv
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from langchain.agents import create_agent
from langchain.tools import tools
from langchain.messages import SytemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

import yfinance as yf

load_dotenv()

app = FastAPI()

model = ChatOpenAI(
    model = 'c1/openai/gpt-5/v-20250930',
    base_url = 'https://api.thesys.dev/v1/embed/'
)

checkpointer = InMemorySaver()

agent = create_agent(
  model = model,
  checkpointer = checkpointer,
  tools = []
)

class PromptObject(BaseModel):
    content: str
    id : str
    role : str

class RequestObject(BaseModel):
   prompt: PromptObject
   threadId: str
   responseId: str

@app.post('/api/chat')
async def chat(request: RequestObject):
    config = {'configurable': {'thread_id': request.threadId}}

    def generate():
        for token, _ in agent.stream(
            {'messages':[
                SytemMessage('You are a stock analysis assistant. You have the ability to get the real- time stock prices, historical stock prices(given a date range), news and balance sheet data for a given ticker symbol.'),
                HumanMessage('request.prompt.content')
            ]},
            stream_mode = 'messages',
            config = config
        ):
            yield token.content
    return StreamingResponse(generate(), media_type='text/event-stream',
     header={
        'Cache-Control': 'no-cache, no-transform',
        'Connection': 'keep-alive',
     })

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8888)