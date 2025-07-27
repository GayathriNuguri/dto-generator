import google.generativeai as genai

genai.configure(api_key="AIzaSyDU6ukCrjBq1IV3JFNvBlncqjTLziA7ECY")
for m in genai.list_models():
    print(m.name)
