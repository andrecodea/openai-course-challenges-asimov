# Setting up environment
from zoneinfo import available_timezones
import openai 
from dotenv import load_dotenv, find_dotenv
from pprint import pprint
import json
import pandas as pd
import yfinance as yf

_ = load_dotenv(find_dotenv())

client = openai.Client()

# Getting ticker history through yfinance
def returns_ticker_history(
    ticker:str,
    period:str = '1mo',
):  

    ticker = ticker.replace('.SA', '')
    ticker_obj = yf.Ticker(f"{ticker}.SA") # Creates ticker object to South American ticker
    hist = ticker_obj.history(period=period)["Close"]
    hist.index = hist.index.strftime('%Y-%m-%d')
    hist = round(hist, 2)
    if len(hist) > 30: # Limits the history size to 30 samples for token control
        slice_size = int(len(hist) / 30)
        hist = hist.iloc[:: slice_size][::-1]
    return hist.to_json()



# Creating model tools for function calling
tools = [
    {
        'type': 'function',
        'function': {
            'name':'returns_ticker_history',
            'description':'Returns the daily close value for a BOVESPA ticker',
            'parameters':{
                'type':'object',
                'properties':{
                    'ticker':{
                        'type':'string',
                        'description': 'ticker name. Example: PETR4 for Petrobras, ABEV3 for AMBEV, etc.'
                    },
                    'period':{
                        'type':'string',
                        'description':'Time period of the history of the ticker. "1mo" is equal to one month, "1d is equal to one day, "1y" is equal to a year and so on.',
                        'enum':["1d", "5d", "1mo", "6mo", "1y", "5y", "10y", "ytd", "max"]
                    }
                }
            }
        }
    }

]

# Functions available to be called
available_funcs = {'returns_ticker_history':returns_ticker_history}

# Creating conversation structure
def generates_text(messages):
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
        tools=tools,
        tool_choice='auto' # Model decides if it calls for function or not
    )

    # Stores model's call for function
    tool_calls = response.choices[0].message.tool_calls

    # If the model decides to call the function
    if tool_calls:
        messages.append(response.choices[0].message) # Appends call to message log

        # For each call in calls
        for tool_call in tool_calls:
            func_name = tool_call.function.name # Function name
            function_to_call = available_funcs[func_name] # Function to call from available functions
            func_args = json.loads(tool_call.function.arguments) # Function arguments
            func_return = function_to_call(**func_args) # Function returns with kwars --> returns ['ticker': 'ABEV3', 'period': '1d']
            
            # Appends tool call specs to log
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": func_name, 
                "content": func_return
            })

            # Stores the model's response after the function has been called.
            response_after_call = client.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo",
                tools=tools,
                tool_choice='auto'
            )

            # Appends response after model's tool call in log
            messages.append(response_after_call.choices[0].message)

        print(f"Assistant: {messages[-1].content}")

    return messages


def main():
    print("Welcome to a finance chatbot!")

    while True:
        user_input = input('You: ')
        messages = [{"role":"user", "content":user_input}]
        messages = generates_text(messages)
        if user_input in ["quit", "exit", "bye"]:
            break

if __name__ == "__main__":
    main()