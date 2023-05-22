import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

# obter o caminho absoluto do script
script_path = os.path.abspath(__file__)
# obter o caminho da pasta onde está o script
pasta = os.path.dirname(script_path)

# listar os arquivos da pasta que terminam com .xml
arquivos = [f for f in os.listdir(pasta) if f.endswith('.xml')]

# iterar sobre os arquivos XML
for arquivo in arquivos:
 # abrir o arquivo XML
 with open(os.path.join(pasta, arquivo), 'rb') as f:
  xml = minidom.parse(f)
  nome = xml.getElementsByTagName("tag a ser alterada")
 
  # alterar o valor de cada elemento <vICMSMonoRet>
  for tag in nome:
   # obter o nó de texto antigo
   old_text = tag.firstChild
   # obter o valor do nó de texto como um float
   old_value = float(old_text.nodeValue)
   # dividir o valor por 100 (Calculo a ser aplicado na tag
   new_value = old_value / 100
   # arredondar o valor para duas casas decimais
   new_value = round(new_value, 2)
   # criar um novo nó de texto com o valor desejado como uma string
   new_text = xml.createTextNode(str(new_value))
   # substituir o nó de texto antigo pelo novo
   tag.replaceChild(new_text, old_text)
 
 # abrir o mesmo arquivo para escrita
 with open(os.path.join(pasta, arquivo), 'w') as novo_arquivo:
  # formatar e escrever o conteúdo do objeto xml no novo arquivo
  xml.writexml(novo_arquivo)
 

import logging 
logging.basicConfig(level=logging.WARNING) 
logging.warning("Script executado com sucesso")
