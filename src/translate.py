import boto3

client = boto3.client('translate', region_name="us-east-1")
#text = "Hola mi nombre as Noah"
text = "je pense donc je suis"
result = client.translate_text(Text=text, SourceLanguageCode="auto", TargetLanguageCode="en")

print(result['TranslatedText'])