"""Script to test the proxy's ability to support response streaming."""

from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="http://localhost",
    api_version="2023-12-01-preview",
    api_key="04ae14bc78184621d37f1ce57a52eb7",
)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)
