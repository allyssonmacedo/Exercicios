#Desenvlva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + (10-1) * razão

for c in range (primeiro_termo, decimo_termo, razão):
    print(f'{c}' , end = ' -> ')
print('Fim da operação')
