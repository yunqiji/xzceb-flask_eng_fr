
# Author: Yunqi Ji

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url)


# Author Yunqi Ji

def englishToFrench(english_text):
    #write the code here
    french_text = language_translator.translate(text=english_text, model_id='en-fr')
    return french_text


# Author: Yunqi Ji

def frenchToEnglish(french_text):
    #write the code here
    english_text = language_translator.translate(text=french_text, model_id='fr-en')
    return english_text
