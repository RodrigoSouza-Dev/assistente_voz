Assistente de voz simples que pode receber comandos de voz do usuário e executar algumas ações com base nesses comandos.

#Importação de bibliotecas: 
Em seguida, são importadas as bibliotecas necessárias para o funcionamento do assistente. Isso inclui:

speech_recognition: Para reconhecimento de fala.
gtts (Google Text-to-Speech): Para conversão de texto em áudio.
webbrowser: Para abrir URLs em um navegador da web.
subprocess: Para executar comandos do sistema operacional.
sounddevice: Para lidar com dispositivos de áudio.
numpy: Para operações numéricas.


# Definição de funções:

tts(texto, idioma="pt-br")): Esta função converte o texto fornecido em áudio usando a biblioteca gTTS e salva o áudio em um arquivo MP3.
stt(): Esta função utiliza o reconhecedor de fala da biblioteca speech_recognition para capturar a fala do usuário a partir do microfone e a converte em texto, usando o Google Speech Recognition.
automatizar(comando): Esta função processa o comando de voz recebido e executa a ação correspondente. Por exemplo, se o comando for "pesquisar wikipedia", a função extrai o termo de pesquisa e chama a função pesquisar_wikipedia para buscar informações na Wikipedia.
pesquisar_wikipedia(termo): Esta função pesquisa na Wikipedia o termo fornecido e exibe um resumo com base nos dois primeiros períodos encontrados. Além disso, converte o resumo em áudio usando a função tts.
Loop principal: O código entra em um loop infinito (while True) onde solicita continuamente ao usuário que fale um comando. Ele usa a função stt() para capturar o comando de voz do usuário, converte o comando em texto e o processa usando a função automatizar(comando). O loop continua até que o comando "sair" seja dado pelo usuário.
