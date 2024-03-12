import time
print("こんにちは、AI-S Botです。何か話しかけてみてください。")
while True:
    question = input()
    if question == "終わる":
        break
    else :
        print("すみません。よく分かりません。")
print("分かりました。")
time.sleep(1)
print("また遊びに来てくださいね。")
time.sleep(1)