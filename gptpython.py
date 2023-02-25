# First we install and import the OpenAI module
!pip install openai
import openai

# Then we set up the API key that allows the program to use OpenAI
# Do not forget to generate your own  key and mention below 
openai.api_key = "Mention your API Key here from https://platform.openai.com/account/api-keys " 

# We define a function that uses OpenAI to create follow-up questions
def generate_followup(prompt):
    # We ask OpenAI to generate a response to the prompt
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

    # We extract the response from OpenAI's output and return it
    message = response.choices[0].text.strip()
    return message

# We start a loop that keeps running until the program is stopped
while True:
    # We ask the user to provide some input
    user_input = input("You: ")

    # We use the input to generate a follow-up question using our function
    followup = generate_followup("Ask a follow-up question to: \"" + user_input + "\"")

    # We print the follow-up question to the screen
    print("ChatGPT:", followup)

