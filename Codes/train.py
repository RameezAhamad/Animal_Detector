# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:18:52 2019

@author: Shaik Rameez
"""

import json
from ibm_watson import VisualRecognitionV3
#animal_765886901
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='AOxWTRCsrNJYB9TIAawriHIv1L-UxHut2OlnCJ-eS54E')
#-HgqUAi8XwAqbMUCaJSC7Gxw1OH6NdCoy2s70BXFsnqc
with open('./ele.zip', 'rb') as elephant, open(
        './tiger.zip', 'rb') as tiger:
    model = visual_recognition.create_classifier(
        'animal',
        positive_examples={'ele':elephant , 'tiger': tiger},
        negative_examples='').get_result()
print(json.dumps(model, indent=2))
#V4NYFIUuciwOvmQGDeMtvxecRNxKe6AN9MQLyCpspuK5
