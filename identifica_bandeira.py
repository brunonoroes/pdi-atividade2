import cv2
import numpy as np

# Dicionário de cores dominantes de cada bandeira
bandeiras = {
    "monaco": [(200, 0, 0), (255, 0, 0)],  # Exemplo de cores para Mônaco
    "peru": [(255, 0, 0), (0, 0, 255)],  # Exemplo de cores para Peru
    "singapura": [(255, 0, 0), (255, 255, 255)],  # Exemplo de cores para Singapura
    "irlanda": [(0, 255, 0), (0, 255, 255)],  # Exemplo de cores para Irlanda
    "italia": [(0, 255, 0), (255, 255, 255)]   # Exemplo de cores para Itália
}

def identifica_bandeira(imagem):
    # Convertendo para RGB
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    
    # Lista de resultados
    resultados = []
    
    # Loop através das bandeiras e suas cores
    for pais, cores in bandeiras.items():
        cor1, cor2 = cores
        
        # Criar máscara para as cores da bandeira
        cor_baixa = np.array([min(cor1[0], cor2[0]), min(cor1[1], cor2[1]), min(cor1[2], cor2[2])])
        cor_alta = np.array([max(cor1[0], cor2[0]), max(cor1[1], cor2[1]), max(cor1[2], cor2[2])])
        
        # Criando máscara de cor para o intervalo
        mascara = cv2.inRange(imagem_rgb, cor_baixa, cor_alta)
        
        # Encontrar os contornos da imagem
        contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contorno in contornos:
            # Obter as coordenadas do retângulo delimitador
            x, y, w, h = cv2.boundingRect(contorno)
            
            # Verificar se o retângulo possui proporções que correspondem a uma bandeira
            if w / h >= 1.5:  # Ajuste de proporção, altere conforme necessário
                resultados.append((pais, (x, y), (x + w, y + h)))
    
    return resultados
