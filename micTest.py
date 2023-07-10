import speech_recognition as sr

# インスタンスを初期化する
recognizer = sr.Recognizer()

# マイクから音声を取得して認識する
with sr.Microphone() as source:
    print("マイクを開いています。")
    try:
        # ユーザーが話すのを待つ
        print("話してください。")
        audio = recognizer.listen(source)
        print("音声の入力が終了しました。音声をテキストに変換しています。")
        # Googleの音声認識APIを使用して音声をテキストに変換する
        # 言語を日本語に設定
        text = recognizer.recognize_google(audio, language='ja-JP')
        print("あなたが言ったこと：", text)
    except sr.UnknownValueError:
        print("音声を認識できませんでした。")
    except sr.RequestError as e:
        print(f"音声認識サービスへのリクエストに失敗しました; {e}")
