# Language-Detection-API - AI-Compare API
## Description
This repositery provides code to implement [AI-Compare Language Detection API](https://www.ai-compare.com/text_apis/language_detection/). [AI-Compare Language Detection API](https://www.ai-compare.com/text_apis/language_detection/) allows to call Language Detection APIs from Google Cloud Platform Natural Language, AWS Comprehend, Microsoft Azure Cognitives Service Language, and IBM Watson Natural Language Understanding. It permits to get results from these providers and compare the results.

## What is AI-Compare ?
[AI-Compare](https://www.ai-compare.com/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers: [object detection](https://www.ai-compare.com/vision_apis/object_detection), [OCR](https://www.ai-compare.com/vision_apis/ocr), [NLP](https://www.ai-compare.com/text_apis/sentiment_analysis/), [speech-to-text](https://www.ai-compare.com/audio_apis/speech_recognition), custom vision, etc. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

AI-Compare offers 2$ free credits when you [create your account for free](https://www.ai-compare.com/accounts/login/?next=/my_apis). You can then use [APIs](https://www.ai-compare.com/v1/redoc/), use the [interface](https://www.ai-compare.com/my_apis), manage your account and have access to all the APIs.

You can find APIs documentation here : https://www.ai-compare.com/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://www.ai-compare.com/v1/pretrained/text/language_detection'
```
### Select parameters 
Set your text, the language, the attempted result, and providers APIs you want to run :
```python
payload = {'providers': '[\'ibm\', \'cognitives_service\', \'aws\', \'google_cloud\']','text':'I am happy today', 'languages_to_find': 'en'}
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
```

## Response example
<details>
</summary>

```


[
  {
    "solution_name": "Google cloud",
    "execution_time": "0.505812",
    "result": {
      "languages": [
        "English"
      ],
      "confidences": [
        1
      ],
      "text": "The score of a documents sentiment indicates the overall emotion of a document. The magnitude of a documents sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."
    },
    "api_response": {
      "languages": [
        {
          "language": "en",
          "confidence": 1
        }
      ]
    },
    "found_languages": 1
  },
  {
    "solution_name": "IBM",
    "execution_time": "1.224599",
    "result": {
      "languages": [
        "English"
      ],
      "confidences": [
        0.9999999549824437
      ],
      "text": "The score of a documents sentiment indicates the overall emotion of a document. The magnitude of a documents sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."
    },
    "api_response": {
      "languages": [
        {
          "language": "en",
          "confidence": 0.9999999549824437
        },
        {
          "language": "fr",
          "confidence": 1.9863633635901936e-8
        },
        {
          "language": "ca",
          "confidence": 1.0238601269901399e-8
        },
        {
          "language": "nn",
          "confidence": 3.2518700682595615e-9
        },
        {
          "language": "sv",
          "confidence": 2.745903272970077e-9
        },
        {
          "language": "it",
          "confidence": 2.5423468865195495e-9
        },
        {
          "language": "nb",
          "confidence": 2.349117274462372e-9
        },
        {
          "language": "da",
          "confidence": 1.2891564268121124e-9
        },
        {
          "language": "ro",
          "confidence": 6.666202657216903e-10
        },
        {
          "language": "tl",
          "confidence": 5.004006175763702e-10
        },
        {
          "language": "pt",
          "confidence": 4.183501345955271e-10
        },
        {
          "language": "de",
          "confidence": 2.6235375577624904e-10
        },
        {
          "language": "ht",
          "confidence": 1.874496436407691e-10
        },
        {
          "language": "hu",
          "confidence": 1.6472318781902108e-10
        },
        {
          "language": "nl",
          "confidence": 1.4230372408128122e-10
        },
        {
          "language": "et",
          "confidence": 1.2302630964148937e-10
        },
        {
          "language": "sq",
          "confidence": 7.864519841778113e-11
        },
        {
          "language": "mt",
          "confidence": 6.803601517905963e-11
        },
        {
          "language": "eu",
          "confidence": 2.9338812501597074e-11
        },
        {
          "language": "af",
          "confidence": 1.819964368941791e-11
        },
        {
          "language": "ms",
          "confidence": 1.69462248041929e-11
        },
        {
          "language": "es",
          "confidence": 1.543885529275662e-11
        },
        {
          "language": "is",
          "confidence": 1.1693542494595648e-11
        },
        {
          "language": "sk",
          "confidence": 8.560353873212693e-12
        },
        {
          "language": "cs",
          "confidence": 6.5009364860231255e-12
        },
        {
          "language": "eo",
          "confidence": 3.695555557536627e-12
        },
        {
          "language": "hr",
          "confidence": 2.7777691889134603e-12
        },
        {
          "language": "sl",
          "confidence": 2.5468526942582847e-12
        },
        {
          "language": "ga",
          "confidence": 2.393155806239152e-12
        },
        {
          "language": "vi",
          "confidence": 1.4357039110547701e-12
        },
        {
          "language": "tr",
          "confidence": 9.98712119073691e-13
        },
        {
          "language": "ja",
          "confidence": 7.797473298269747e-13
        },
        {
          "language": "fi",
          "confidence": 6.956349562419434e-13
        },
        {
          "language": "ku",
          "confidence": 6.089017835831087e-13
        },
        {
          "language": "cy",
          "confidence": 5.959973977521543e-13
        },
        {
          "language": "ko",
          "confidence": 5.4614818039737e-13
        },
        {
          "language": "az",
          "confidence": 4.387491427725982e-13
        },
        {
          "language": "lv",
          "confidence": 2.485830277415373e-13
        },
        {
          "language": "lt",
          "confidence": 2.2709515303963777e-13
        },
        {
          "language": "pl",
          "confidence": 1.5237131835126882e-13
        },
        {
          "language": "zh",
          "confidence": 6.360859424349665e-14
        },
        {
          "language": "zh-TW",
          "confidence": 6.205990801233566e-14
        },
        {
          "language": "el",
          "confidence": 3.30951558843099e-14
        },
        {
          "language": "th",
          "confidence": 2.896943417762372e-14
        },
        {
          "language": "hi",
          "confidence": 3.306831730701758e-15
        },
        {
          "language": "ru",
          "confidence": 2.8653901491093884e-15
        },
        {
          "language": "so",
          "confidence": 1.6854194046761493e-15
        },
        {
          "language": "sr",
          "confidence": 6.936565258151478e-16
        },
        {
          "language": "ar",
          "confidence": 6.888930280576522e-16
        },
        {
          "language": "mn",
          "confidence": 6.011621000636303e-16
        },
        {
          "language": "ur",
          "confidence": 5.511389791594541e-16
        },
        {
          "language": "he",
          "confidence": 2.941117841644858e-16
        },
        {
          "language": "my",
          "confidence": 2.0085470039885642e-16
        },
        {
          "language": "mr",
          "confidence": 1.181553016277467e-16
        },
        {
          "language": "ka",
          "confidence": 8.370789084537041e-17
        },
        {
          "language": "km",
          "confidence": 7.752473909728026e-17
        },
        {
          "language": "uk",
          "confidence": 6.062178333439404e-17
        },
        {
          "language": "ta",
          "confidence": 5.810220831527641e-17
        },
        {
          "language": "ky",
          "confidence": 5.0970723708942845e-17
        },
        {
          "language": "lo",
          "confidence": 4.997879536058858e-17
        },
        {
          "language": "bg",
          "confidence": 4.778429602768851e-17
        },
        {
          "language": "ml",
          "confidence": 4.0139766633828035e-17
        },
        {
          "language": "kk",
          "confidence": 3.969426470418966e-17
        },
        {
          "language": "be",
          "confidence": 3.834096722786062e-17
        },
        {
          "language": "bn",
          "confidence": 3.454542412338605e-17
        },
        {
          "language": "ps",
          "confidence": 2.7653803972506886e-17
        },
        {
          "language": "fa",
          "confidence": 2.124706037332745e-17
        },
        {
          "language": "hy",
          "confidence": 1.7929835364943508e-17
        },
        {
          "language": "pa",
          "confidence": 1.501133924765967e-17
        },
        {
          "language": "ne",
          "confidence": 1.3908555754605997e-17
        },
        {
          "language": "te",
          "confidence": 1.3660512417857452e-17
        },
        {
          "language": "cv",
          "confidence": 1.1011382289133258e-17
        },
        {
          "language": "gu",
          "confidence": 6.773497206613689e-18
        },
        {
          "language": "ba",
          "confidence": 6.659171620928359e-18
        },
        {
          "language": "si",
          "confidence": 4.6500570156028504e-18
        },
        {
          "language": "pa-PK",
          "confidence": 2.914965758054498e-18
        }
      ]
    },
    "found_languages": 1
  },
  {
    "solution_name": "Microsoft Azure",
    "execution_time": "0.438189",
    "result": {
      "languages": [
        "English"
      ],
      "confidences": [
        1
      ],
      "text": "The score of a documents sentiment indicates the overall emotion of a document. The magnitude of a documents sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."
    },
    "api_response": {
      "documents": [
        {
          "id": "1",
          "detectedLanguage": {
            "name": "English",
            "iso6391Name": "en",
            "confidenceScore": 1
          },
          "warnings": []
        }
      ],
      "errors": [],
      "modelVersion": "2020-07-01"
    },
    "found_languages": 1
  },
  {
    "solution_name": "Amazon Web Services",
    "execution_time": "0.233195",
    "result": {
      "languages": [
        "English"
      ],
      "confidences": [
        0.9865699410438538
      ],
      "text": "The score of a documents sentiment indicates the overall emotion of a document. The magnitude of a documents sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."
    },
    "api_response": {
      "Languages": [
        {
          "LanguageCode": "en",
          "Score": 0.9865699410438538
        }
      ],
      "ResponseMetadata": {
        "RequestId": "37567500-e200-4cfb-b6bc-5be58079267e",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
          "x-amzn-requestid": "37567500-e200-4cfb-b6bc-5be58079267e",
          "content-type": "application/x-amz-json-1.1",
          "content-length": "64",
          "date": "Tue, 25 Aug 2020 09:32:15 GMT"
        },
        "RetryAttempts": 0
      }
    },
    "found_languages": 1
  }
]

```

</details>

## FAQ
Here you can access to AI-Compare [FAQ](https://www.ai-compare.com/faq/).

## Use cases
We provides on our website some [use cases examples for NLP APIs](https://www.ai-compare.com/use_cases_nlp/)

## Contact
If you have any question or request, you can contact us at contact@ai-compare.com

## Terms of use
You can access to our terms [here](https://www.ai-compare.com/terms/) on our website.

#
![Screenshot](Ai-compare_new.png)

