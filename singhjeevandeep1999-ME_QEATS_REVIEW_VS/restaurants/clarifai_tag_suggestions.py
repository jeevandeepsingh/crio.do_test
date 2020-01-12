import json
import requests

#TODO: CRIO_TASK_MODULE_TAG_SUGGESTION
# As part of this module you are expected to complete the get_tags_suggestions() function
# Tasks:
# 1) You need to register as Clarifai developer to obtain an API Key to the Food Model
#    The Food model can be found here:
#    https://www.clarifai.com/models/food-image-recognition-model-bd367be194cf45149e75f01d59f77ba7
#    A sample request and response can be found in the above link
# 2) Use the food model to get implement tag suggestions

# Parameters
# ----------
# api_key : string
#     API Key for Clarifai
# image_url : string
#     publicly accessible URL of the image to get tag suggestions
# Return Type: list()
#   return a list of tags provided by the Clarifai API
class Clarifai_tag:

    def get_tags_suggestions(self,api_key, image_url):
        # write your code here
        tag =[]

        headers  = {
        'Authorization': 'Key '+api_key,
        'Content-Type': 'application/json',
        }

        data = '{ "inputs": [ {  "data": {"image": {"url": "%s"}}}]}' % image_url
        url = 'https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs'
        response = requests.post(url = url, headers=headers, data=data)
        js = response.json()

        for k in js['outputs']:
            for i in k['data']['concepts']:
                tag.append(i['name'])
        return tag  

    def get_access_token(self,token_name):
        file_handle = open('access_tokens.sh', 'r+')
        lines = file_handle.readlines()
        file_handle.close()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()
        return 'Not found'

if __name__ == '__main__':
    clarifai_tag = Clarifai_tag()
    tags_suggessted = []
    clarify_api_key = clarifai_tag.get_access_token('CLARIFAI_API_KEY')
    test_image_url = 'https://i.imgur.com/dlMjqQe.jpg'
    tags_suggessted =clarifai_tag.get_tags_suggestions(clarify_api_key, test_image_url)
    print(tags_suggessted)
