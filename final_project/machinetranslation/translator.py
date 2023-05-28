
"""
This is an English to French Translator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-05-28',
    authenticator=authenticator
)


language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    English to French
    """
    #write the code here
    translation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """
    French to English
    """
    #write the code here
    translation  = language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
