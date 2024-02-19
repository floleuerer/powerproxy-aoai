"""Script to test the proxy's ability to support response streaming."""

from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="http://localhost",
    api_version="2023-05-15",
    api_key="04ae14bc78184621d37f1ce57a52eb7",
)

response = client.embeddings.create(
    model='text-embedding-ada-002',
    input=['this is a test', 'this is another test']
    )

print(response.data)
