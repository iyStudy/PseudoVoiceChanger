import speech_recognition as sr
import requests
import json
import wave
import pyaudio

def generate_wav(text, speaker=1, filepath='./audio.wav'):
    host = 'localhost'
    port = 50021
    params = (
        ('text', text),
        ('speaker', speaker),
    )
    response1 = requests.post(
        f'http://{host}:{port}/audio_query',
        params=params
    )
    headers = {'Content-Type': 'application/json',}
    response2 = requests.post(
        f'http://{host}:{port}/synthesis',
        headers=headers,
        params=params,
        data=json.dumps(response1.json())
    )

    wf = wave.open(filepath, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)
    wf.writeframes(response2.content)
    wf.close()

# インスタンスを初期化する
recognizer = sr.Recognizer()

# 無限ループで音声入力と音声再生を繰り返す
while True:
    # マイクから音声を取得して認識する
    with sr.Microphone() as source:
        print("■マイクを開いています。話してください。")
        try:
            # ユーザーが話すのを待つ
            audio = recognizer.listen(source)
            print("<<テキスト変換中>>")
            # Googleの音声認識APIを使用して音声をテキストに変換する
            # 言語を日本語に設定
            text = recognizer.recognize_google(audio, language='ja-JP')
            print("あなたが言ったこと：", text)
            # wavファイル作成
            print("<<音声を変換中>>")
            generate_wav(text)

        except sr.UnknownValueError:
            print("音声を認識できませんでした。")
            continue
        except sr.RequestError as e:
            print(f"音声認識サービスへのリクエストに失敗しました; {e}")
            continue

    # wavファイルを再生する
    try:
        print("<< ♪ 変換した音声を再生 ♪ >>")
        wave_file = wave.open("audio.wav", 'rb')
        audio_player = pyaudio.PyAudio()
        stream = audio_player.open(
            format=audio_player.get_format_from_width(wave_file.getsampwidth()),
            channels=wave_file.getnchannels(),
            rate=wave_file.getframerate(),
            output=True
        )

        chunk = 1024
        data = wave_file.readframes(chunk)
        while data:
            stream.write(data)
            data = wave_file.readframes(chunk)

        stream.stop_stream()
        stream.close()
        audio_player.terminate()

    except wave.Error as e:
        print(f"WAVファイルの読み込みエラー: {e}")
        continue
