# bibliotecas necessarias
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')  # abre o site Whatsapp Web
time.sleep(20)  #da um sleep de 15 segundos, tempo para scannear o QRCODE

# Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = ['✅HMbets Kayan Isac✅',
            '✅HMbets Kayan K2✅',
            '✅HMbets Oseias✅',
            '✅HMbets Kayan Edu Copeti✅',
            '✅HMbets AR Bob Santos✅',
            '✅HMbets HRR Lipe Napoli✅',
            '✅HMbets RC Lamar✅',
            '✅HMbets MC Jorginho✅',
            '✅HMbets kayan Ygor Love ✅',
            '✅HMbets HRR Pedro Lins✅',
            '✅HMbets PRB J. Goiaba✅',
            '✅HMbets Kayan Tuan ✅',
            '✅HMbets MAC Léo Coacu✅',
            '✅HMbets AR Kaio Castro✅',
            '✅HMbets Gary✅',
            '✅HMbets RC Didicaaa✅',
            '✅HMbets HRR Lucca✅',
            '✅HMbets Baby✅',
            '✅HMbets RC Erick Graveto✅',
            '✅HMbets Lorin DL✅',
            '✅HMbets RG Pepe✅',
            '✅HMbets Alan Medico✅',
            '✅HMbets Kayan Raphael St✅',
            '✅Bets BSB 21 Paulo Cesar✅',
            '✅HMbets Marpal Dayvis✅',
            '✅HMbets HRR Germano✅',
            '✅HMbets RG Lucas Salomao✅',
            '✅HMbets HT Renan Grassi✅',
            '✅HMbets Pedro Cruz✅',
            '✅HMbets HRR Arthur Barr.✅',
            '✅HMbets Gladyson✅',
            '✅HMbets Raphael Thiago✅',
            '✅HMbets Ivo Elemento✅',
            '✅HMbets Kayan Neto Star✅',
            '✅HMbets HRR Nadlo Cav.✅',
            '✅HMbets Paulo Everdosa✅',
            '✅HMbets Rodriguinho✅',
            '✅HMbets AR Reginaldo B.✅',
            '✅HMbets Kayan Joel H✅',
            '✅HMbets Kaio Leitao ✅',
            '✅HMbets Pedro Andrade✅',
            '✅HMbets Renato Amora✅',
            '✅HMbets Mamao ✅',
            '✅HMbets AR Marcos Romero✅',
            '✅HMbets Victor Pontes✅',
            '✅HMbets Caio Girão✅',
            '✅HMbets Ruy Filho✅',
            '✅HMbets Adriano✅',
            '✅HMbets Kayan Tijolo✅',
            '✅HMbets Jade Queiroz✅',
            '✅HMbets Kayan Pirata✅',
            '✅HMbets RC Davi Pizzas✅',
            '✅HMbets AR Farinha✅',
            '✅HMbets RC Jp Borges✅',
            '✅HMbets MC Khalil Viana✅',
            '✅HMbets RG Leticia Leone✅',
            '✅HMbets Kayan Leonardo M✅',
            '✅HMbets Floki Laercio✅',
            '✅HMbets Kayan Luiz Poker✅',
            '✅HMbets Chef Matheus✅',
            '✅HMbets Eduardo Rios✅',
            '✅HMbets Humberto✅',
            '✅HMbets Kayan Grillo ✅',
            '✅HMbets David Pires✅',
            '✅HMbets Felipe Difini✅',
            '✅HMbets Kayan Rafa Negão✅',
            '✅HMbets RS João  Victor✅',
            '✅HMbets Henrique VL✅',
            '✅HMbets Joel Lopes✅',
            '✅HMbets Mateuzinho 01✅',
            '✅HMbets Kayan Wellinton✅',
            '✅HMbets Kayan Viny✅',
            '✅HMbets Chupeta✅',
            '✅HMbets Miguelzin✅',
            '✅HMbets Fred Ring✅',
            '✅HMbets Kayan Dutra✅',
            '✅HMbets Miagui Ângelo ✅',
            '✅HMbets Daniel Landim✅',
            '✅HMbets Parceria HM/DM✅',
            '✅HMbets HRR Gabriel Lobo✅',
            '✅HMbets Pedro Luiz A.B✅',
            '✅HMbets Wendell Rocha✅',
            '✅HMbets Henriquin Porco✅',
            '✅HMbets Kayan Rodrigo✅',
            '✅HMbets João Albuquerque✅',
            '✅HMbets RS Gui Poker✅',
            '✅HMbets RG Jun Hanai✅',
            '✅HMbets Dimas✅',
            '✅HMbets Kayan Washigton✅',
            '✅HMbets Henrique Sales✅',
            '✅HMbets Carlim✅',
            '✅HMbets Igor M✅',
            '✅HMbets Eduardo Zanga✅',
            '✅HMbets PRB 01 Plínio✅',
            '✅HMbets Fernando Gaúcho✅',
            '✅HMbets Eduardo Plettes✅',
            '✅HMbets Robson Otoni✅',
            '✅HMbets Lucas Cavalcante✅',
            '✅HMbets PRB Halysson W. ✅',
            '✅HMbets RG Fazzini✅',
            '✅HMbets RG Vitin Diniz✅',
            '✅HMbets RG João Celso✅',
            '✅HMbets RG Gabriel Eug.✅',
            '✅HMbets RG Fred Lacerda ✅',
            '✅HMbets CG Bruno Sávio✅',
            '✅HMbets AR Gil Braga✅',
            '✅HMbets Nico✅ zerados',
            '✅HMbets Wilkens✅',
            '✅HMbets Alisson Ceguim✅',
            '✅HMbets Alexandre Primo✅',
            '✅HMbets Salim✅',
            '✅Bets BSB 23 Neto✅',
            '✅HMbets RG André Carreir✅',
            '✅HMbets Gabriel RB✅',
            '✅HMbets Léo Cals✅',
            '✅HMbets Camilo✅',
            '✅HMbets RS Isaías✅',
            '✅HMbets RF Ricardinho✅',
            '✅HMbets HRR Caio Filho✅',
            '✅HMbets Francisco Freire✅',
            '✅HMbets Kayan Rafael P.✅',
            '✅HMbets Fabrício Bandeir✅',
            '✅HMbets Romao✅',
            '✅HMbets Pedro Levi✅',
            '✅HMbets RG Joao Paulo✅',
            '✅HMbets RG Diego F✅',
            '✅HMbets RG Diego Sena✅',
            '✅HMbets Hemesson✅',
            '✅HMbets Kayan Alex✅',
            '✅HMbets Dudu Holanda✅',
            '✅HMbets Mário Coroa✅',
            '✅HMbets RM Herculano✅',
            '✅HMbets Valmir✅',
            '✅HMbets RM Fábio Menezes✅',
            '✅HMbets Emanuel Vieira✅',
            '✅HMbets Ribeiro Editor✅',
            '✅HMbets RS Marcos Sócio✅',
            '✅HMbets RG Pedrinho✅',
            '✅HMbets CG Zé Roberto✅',
            '✅HMbets Sergio Fonteles✅',
            '✅HMbets Rafael( Edinho )✅',
            '✅HMbets Júnior Loro✅',
            '✅HMbets C. Leonardo P. ✅',
            '✅HMbets Fernando Moraes✅',
            '✅HMbets Matheus Vieira✅',
            '✅HMbets AR Pedro Kina✅',
            '✅HMbets Júnior Parente✅',
            '✅HMbets Marcos Tiago✅',
            '✅HMbets RM C. Arruda✅',
            '✅HMbets V. Pinheiro✅',
            '✅HMbets RM Roberto✅',
            '✅HMbets Floki✅',
            '✅HMbets Alberto Araujo✅',
            '✅HMbets Kayan Vitones✅',
            '✅HMbets Fernando Soares✅',
            '✅HMbets Van Van Apostas✅',
            '✅HMbets Guilherme Neves✅',
            '✅HMbets RG Tateno✅',
            '✅HMbets Renan Rebouças✅',
            '✅HMbets Marpal Paulo S✅',
            '✅HMbets RG Davi Nascente✅',
            '✅HMbets Eskinazi✅',
            '✅HMbets Digão✅',
            '✅ HMbets Milsin ✅',
            '✅HMbets Renan Sales✅',
            '✅HMbets RS8 Remi✅',
            '✅HMbets Kayan Yuri✅',
            '✅HMbets Anderson Queiroz✅',
            '✅HMbets Kayan Digo Pando✅',
            '✅HMbets Mateus Ihering✅',
            '✅HMbets RG Rodolfo P✅',
            '✅HMbets RG Leonardo Pard✅',
            '✅HMbets MC Tales✅',
            '✅HMbets Rodrigo Ponte✅',
            '✅HMbets Guga USD✅',
            '✅HMbets Ramon Sorgatto✅',
            '✅HMbets Natan Loketa✅',
            '✅HMbets Kayan Henrique✅',
            '✅HMbets RG Lucas Mourão ✅',
            '✅HMbets Romelio Leite✅',
            '✅HMbets Luan Five✅',
            '✅HMbets Yota Play✅',
            '✅HMbets Kayan Brandon✅',
            '✅HMbets Kayan Fernando L✅',
            '✅HMbets Kayan Paulo✅',
            '✅HMbets Kayan Anderson✅',
            '✅HMbets Osmar Zuum✅',
            '✅HMbets HRR Yan Oliveira✅',
            '✅HMbets RC Dudu Cidrao✅',
            '✅HMbets RC Marco Salomão✅',
            '✅HMbets Kayan Matheus G.✅',
            '✅HMbets RG Alex Willian✅',
            '✅HMbets HRR Lucão✅',
            '✅HMbets Lucas Peixoto✅',
            '✅HMbets Kayan Fefa✅',
            '✅HMbets RC Paulo Guerra✅',
            '✅HMbets Rômulo Tavares✅',
            '✅HMbets Kayan Math✅',
            '✅HMbets Anderson Fox✅',
            '✅HMbets Kauan SP✅',
            '✅HMbets Bruno Queiroz✅',
            '✅HMbets AR Rômulo Rocha✅',
            '✅HMbets GuilhermeChenaud✅',
            '✅HMbets Kayan Vambasther✅',
            '✅HMbets CG Carlos Feio✅',
            '✅HMbets Vini Zaranza✅',
            'HMbets Vinicios Cardoso',
            'HMbets Rodrigo Viana',
            'HMbets Arthur Leite',
            'HMbets Jansen',
            'HMbets Fernando Martins',
            'HMbets Adrian G',
            'HMbets Wesley Oliveira',
            'HMbets Ronaldo Fabrício',
            'HMbets Avelino',
            'HMbets Felipe Miranda',
            'HMbets Lucas Carvalho',
            'HMbets Caio Correia',
            'HMbets Kayo',
            'HMbets Pompeu',
            'HMbets João Vitoriano',
            'HMbets Gabriel Barreira',
            'HMbets Marcos Carvalho',
            'HMbets Mario Neto',
            'HMBets Walace Oliveira',
            'HMbets Kayan Edu Bet',
            'HMbets Sérgio Milfont',
            'HMbets Miguel Melo',
            'HMbets Rafael Otoch',
            'HMbets Guilherme César',
            'HMbets Victor Hugo',
            'HMbets Kaio Dias',
            'HMbets Carlos Eduardo',
            'HMbets Luiz Arthur 2',
            'HMbets Chuvito',
            'HMbets André Leite',
            'HMbets Felipe Angelo',
            'HMbets Carlos Angel',
            'HMbets Marcos Viana',
            'HMbets João Victor',
            'HMbets Yan Berg',
            'HMbets MC Luan',
            'HMbets Luiz Junior',
            'HMbets Nathan Ribeiro',
            'HMbets Matheus Araujo ',
            'HMbets Victor Holanda']

# Mensagem - Mensagem que será enviada
mensagem = ''
mensagem2 = ''

# Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* )
midia = "C:/Users/HM bets/Desktop/HM/imagem/1.jpeg"
midia1 = "C:/Users/HM bets/Desktop/HM/imagem/2.jpeg"

# Funcao que pesquisa o Contato/Grupo

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

# Funcao que envia a mensagem


def enviar_mensagem(mensagem, mensagem2):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    campo_mensagem[1].send_keys(str(mensagem) + str() + str(mensagem2))
    campo_mensagem[1].send_keys(Keys.ENTER)

# Funcao que envia midia como mensagem


def enviar_midia(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(1.5)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()


def enviar_midia1(midia):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia1)
    time.sleep(1.5)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()


# Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    time.sleep(1)
    #enviar_mensagem(mensagem, mensagem2)
    enviar_midia(midia)
    time.sleep(1)
    enviar_midia1(midia1)
    time.sleep(1)