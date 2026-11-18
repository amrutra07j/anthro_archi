import os
from anthropic import Anthropic

client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)
print(os.environ.get("ANTHROPIC_API_KEY"))
message = client.messages.create(
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
    model="claude-opus-5-5",
)

for block in message.content:
    if block.type == "text":
        print("assistant: ", block.text)