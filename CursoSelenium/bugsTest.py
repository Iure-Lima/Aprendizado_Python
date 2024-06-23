import time
import pandas as pd

df = pd.read_csv("da.csv")

userQuestion = "Quais os disponiveis"
userWords = userQuestion.split()

for i in range(len(df)):
    questions = df["Questions"].loc[i]
    words = questions.split()

    for word in words:
        for userWord in userWords:
          if userWord == word:
            print("Merece uma resposta")
            print(word, userWord)
            break

def send_message(message):
        message = message.split()
        word = ""

        for i in range(len(message)):
            if message[i] == "/n":
                # text_field.send_keys(word)
                # text_field.send_keys(Keys.ALT)
                # text_field.send_keys(Keys.ENTER)
                word = ""
            else:
                word += f"{message[i]} "
        
        # text_field.send_keys(word)
        # text_field.send_keys(Keys.ALT)
        # text_field.send_keys(Keys.ENTER)
              
              
        time.sleep(1.5)
        # text_field.send_keys(Keys.ENTER)

send_message("Hello world, este é um /n teste")