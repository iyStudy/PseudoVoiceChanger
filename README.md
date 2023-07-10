# VOICEVOXを使用した音声認識と音声合成
このPythonスクリプトは、マイクからの音声入力を受け取り、Googleの音声認識APIを使用してその音声をテキストに変換し、VOICEVOXエンジンを使用して音声を合成します。

使い方  
1. まず、VOICEVOXデスクトップアプリケーションを起動してください。
2. 次に、このスクリプトを実行します。マイクを開いて話し始めると、「音声の入力が終了しました。音声をテキストに変換しています。」と表示されます。
3. あなたが話した内容がテキストとして表示され、VOICEVOXで音声が生成されます。
4. 生成された音声は直ちに再生されます。
5. このプロセスは無限に繰り返されます。スクリプトを停止するには、キーボードの割り込み（例えばCtrl+C）を使用してください。
## 必要なライブラリ
このスクリプトを実行するためには、以下のPythonライブラリが必要です：
~~~
speech_recognition
requests
wave
pyaudio
~~~
これらのライブラリは、以下のpipコマンドでインストールできます：

~~~
pip install speech_recognition requests wave pyaudio
~~~
## 注意事項
VOICEVOXの音声合成エンジンおよびGoogleの音声認識APIは大量のリソースを消費する可能性があります。    
このスクリプトを実行する際は、十分なリソースが確保されていることを確認してください。  
このスクリプトはマイク入力とインターネット接続を必要とします。対応する環境で実行してください。
