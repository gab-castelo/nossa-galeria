import os
import json

def gerar_json_fotos():
    pasta_fotos = 'img'
    
    arquivo_json = 'imagens.json'
    
    extensoes_validas = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')
    
    if not os.path.exists(pasta_fotos):
        print(f"Erro: A pasta '{pasta_fotos}' não foi encontrada!")
        print("Crie uma pasta chamada 'img' ao lado deste script e coloque as fotos lá.")
        return

    lista_fotos = []
    for arquivo in os.listdir(pasta_fotos):
        if arquivo.lower().endswith(extensoes_validas):
            caminho_completo = os.path.join(pasta_fotos, arquivo)
            caminho_formatado = caminho_completo.replace('\\', '/')
            lista_fotos.append(caminho_formatado)
            
    lista_fotos

    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(lista_fotos, f, indent=2, ensure_ascii=False)

    print(f"Sucesso! Encontradas {len(lista_fotos)} fotos na pasta '{pasta_fotos}'.")
    print(f"O arquivo '{arquivo_json}' foi gerado/atualizado.")

if __name__ == '__main__':
    gerar_json_fotos()