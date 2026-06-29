from google import genai
print ("successful")
client = genai.Client(api_key="YOUR_API_KEY")

print("Gemini Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print("Bot:", response.text)