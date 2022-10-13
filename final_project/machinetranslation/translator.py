""" Importing the environment
"""
import os 
import json # Importing Json to read files
from ibm_watson import LanguageTranslatorV3 #Importing IBM Watson language translator instance
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator # Authenticating the instance
from dotenv import load_dotenv # Loading the dotenv file

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('zKBGjfE1-so5Ayvrv9xBEdNrMGz8TYTKw6T50PkSfRFY')
language_translator = LanguageTranslatorV3 (
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/8e53d90e-bc9d-40b6-a8de-622ceb34bf3e')

# Translates English text to French
def english_to_french(english_text):# Translates English text to French
    """
    Translates English text to French.
    """
    translation= language_translator.translate(text=english_text, model_id='en-fr').get_result()
    # This function gets English texts and trabslates it to French
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.
    """
    translation= language_translator.translate(text=french_text, model_id='fr-en').get_result()
    # This function gets French texts and translates it to English
    english_text=translation['translations'][0]['translation']
    return english_text