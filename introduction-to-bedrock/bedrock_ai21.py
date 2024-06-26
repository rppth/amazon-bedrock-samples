import boto3
import json

#Create the connection to Bedrock
bedrock = boto3.client(
    service_name='bedrock',
    region_name='us-west-2', 
    endpoint_url='https://bedrock.us-west-2.amazonaws.com'
)

# Let's see all available AI21 Models
available_models = bedrock.list_foundation_models()

for model in available_models['modelSummaries']:
  if 'ai21' in model['modelId']:
    print(model)


# Define prompt and model parameters
prompt_data = """Write me a poem about apples"""

body = {
  "prompt": "",
  "maxTokens": 200,
  "temperature": 0.7,
  "topP": 1,
  "stopSequences": [],
  "countPenalty": {
    "scale": 0
  },
  "presencePenalty": {
    "scale": 0    
  },
  "frequencyPenalty": {
    "scale": 0
  }
}


body = json.dumps(body) # Encode body as JSON string

modelId = 'ai21.j2-ultra' 
accept = 'application/json'
contentType = 'application/json'

#Invoke the model
response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get('body').read())

print(response_body.get('completions')[0].get('data').get('text'))

