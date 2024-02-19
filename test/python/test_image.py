"""Script to test the proxy's ability to support response streaming."""

from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="http://localhost",
    api_version="2023-12-01-preview",
    api_key="04ae14bc78184621d37f1ce57a52eb7",
)

response = client.images.generate(
            model="dall-e-3", # the name of your DALL-E 3 deployment
            prompt='a teddy bear riding a bike',
            n=1,
            size='1024x1024',
            quality='standard',
            style='vivid'
        )

print(response)
