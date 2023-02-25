!pip install opeanai
import openai
import time

# Set your OpenAI API key
openai.api_key = "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"

# Define a function to generate a follow-up question given a prompt
def generate_followup(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=64,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    message = response.choices[0].text.strip()
    return message

# Loop to receive user input and generate follow-up questions
while True:
    # Prompt user for input
    user_input = input("You: ")
    
    # Construct prompt for generating follow-up question
    prompt = "Ask a follow-up question to: \"" + user_input + "\""
    
    # Generate follow-up question using OpenAI API
    followup = generate_followup(prompt)

    # Wait for the API response to be ready
    while followup == prompt:
        print("Waiting for API response...")
        time.sleep(0.5)
        response = openai.Completion.fetch(response["id"])
        followup = response.choices[0].text.strip()
    
    # Print the generated follow-up question
    print("ChatGPT:", followup)
