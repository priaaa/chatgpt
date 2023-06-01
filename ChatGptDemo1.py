
import openai
openai.api_key = "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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create a story aboyt 5 year old boy and a dog",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

result = response.choices[0].text.strip()
print(result)
