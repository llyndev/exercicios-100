'''
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
    calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''
    
mb = float(input("Informe o tamanho do arquivo em MB"))
mbps = float(input("Informe a velocidade do link em Mbps"))

download = mb / (mbps / 8)

print(f"Download {download:.2f}")