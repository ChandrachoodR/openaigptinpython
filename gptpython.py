import openai
import time

# Set OpenAI API key
openai.api_key = "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"

# Function to generate a follow-up question
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

    # Get the generated message from the OpenAI API response
    message = response.choices[0].text.strip()
    return message

# Loop to continuously prompt for user input and generate follow-up questions
while True:
    user_input = input("You: ")
    prompt = "Ask a follow-up question to: \"" + user_input + "\""

    # Call generate_followup function to get the follow-up question
    followup = generate_followup(prompt)

    # Wait for the API response to be ready
    while followup == prompt:
        time.sleep(0.1)
        response = openai.Completion.fetch(response["id"])
        followup = response.choices[0].text.strip()

    # Print the follow-up question
    print("ChatGPT:", followup)
