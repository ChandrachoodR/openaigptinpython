import openai
import time

openai.api_key = "your_api_key_here"

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

while True:
    user_input = input("You: ")
    prompt = "Ask a follow-up question to: \"" + user_input + "\""

    followup = generate_followup(prompt)

    # Wait for the API response to be ready
    start_time = time.time()
    while followup == prompt:
        time.sleep(0.1)
        elapsed_time = time.time() - start_time
        if elapsed_time > 10:
            print("Sorry, the API response timed out.")
            break
        response = openai.Completion.fetch(response["id"])
        followup = response.choices[0].text.strip()

    print("ChatGPT:", followup)
