# import polyglot
# from polyglot.text import Text, Word

import pandas as pd
from indic_transliteration import sanscript
import os


file_path = r"D:\lalwani\tts-finetuning\data-finetuning\extracted_data\mono_female\Read_speech\txt.done.data"


df = pd.read_csv(file_path, delimiter='"', names=["one", "hindiText", "three"], header=None)



text = "कुछ बेहद ख़ास शोधों को भी छापा है, बनारसीदास द्वारा लिखित किताब, अर्धकथानक, जो कि हिंदी की पहली आत्मकथा है, उसे बाज़ार की चिंता किए बग़ैर छापा है "
transliterated_text = sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
print(transliterated_text)

def transliterate_text(text):
    transliterated_text = sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
    return transliterated_text
def clean_and_add_path(row):
    cleaned_row = row.strip(" ()")  # Remove leading spaces and brackets
    base_path = r"D:/lalwani/tts-finetuning/data-finetuning/extracted_data/mono_female/Read_speech/wav/"
    return os.path.join(base_path, cleaned_row)



df['englishText'] = df['hindiText'].apply(transliterate_text)
df['file_path2'] = df['one'].apply(clean_and_add_path)
print(df)


file_path2 = r"D:\lalwani\tts-finetuning\data-finetuning\extracted_data\mono_male\Read_speech\txt.done.data"
def clean_and_add_path2(row):
    cleaned_row = row.strip(" ()")  # Remove leading spaces and brackets
    base_path2 = r"D:/lalwani/tts-finetuning/data-finetuning/extracted_data/mono_female/Read_speech/wav/"
    return os.path.join(base_path2, cleaned_row)


df2 = pd.read_csv(file_path2, delimiter='"', names=["one", "hindiText", "three"], header=None)

df2['englishText'] = df2['hindiText'].apply(transliterate_text)
df2['file_path2'] = df2['one'].apply(clean_and_add_path)


print(df2)
result = pd.concat([df, df2], axis=0)
print(result)
result.to_csv("final_dataset.csv",
              index=False)

