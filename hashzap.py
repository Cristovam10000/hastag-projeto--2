import flet as ft

def main(pagina):
    texto = ft.Text("hashzap")
    pagina.add(texto)

    chat = ft.Column()


    #comando para ter o tunel de comunicação
    def enviar_mensagem_tunel(informaçao):
        #colocar as mensagens no chat 
        chat.controls.append(ft.Text(informaçao))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
   

    def enviar_mensagem(evento):
        #colocar o nome do usuario
        texto_campo_mensagem = f"{nome_usuario.value} : {campo_mensagem.value} "
        #colocar as mensagens no chat 

        pagina.pubsub.send_all(texto_campo_mensagem)
        #limpar o campo mensagem
        campo_mensagem.value = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label="escreva sua mensagem aqui", on_submit= enviar_mensagem)
    botao_enviar = ft.ElevatedButton("enviar mensagem", on_click= enviar_mensagem)

    def entrar_chat(evento):
        #feche o popup
        popup.open= False
        #tire o botão "iniciar chat" da tela
        pagina.remove(botao_iniciar)
        #adiciona o nosso site
        pagina.add(chat)
        #criar o campo para enviar mensagem
        #botão enviar mensagem
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    nome_usuario = ft.TextField(label="escreva seu nome",on_submit=entrar_chat)

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("hashzap"),
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
    )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
   
    botao_iniciar  = ft.ElevatedButton("iniciar chat",on_click=iniciar_chat )
    pagina.add(botao_iniciar)


ft.app(main, view= ft.WEB_BROWSER)

