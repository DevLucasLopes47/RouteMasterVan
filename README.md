# RouteMasterVan 🚐

Este projeto foi desenvolvido com o objetivo de otimizar as rotas diárias para uma van, permitindo planejar trajetos eficientes com base nos endereços dos usuários e nos pontos de partida e chegada. O sistema utiliza a API do Google Maps para geocodificação, cálculo de distâncias e durações, além de oferecer suporte a múltiplos usuários e destinos intermediários.

## Funcionalidades

- **Geocodificação de Endereços:** Conversão de endereços ou CEPs em coordenadas de latitude e longitude.
- **Cálculo de Rotas:** Geração de todas as rotas possíveis entre o ponto inicial, pontos intermediários e o ponto final.
- **Otimização de Rotas:** Ordenação das rotas pela menor distância total.
- **Detalhamento de Rota:** Exibição da distância e duração de cada trecho da melhor rota.
- **Interatividade:** Pergunta aos usuários se irão utilizar a van e coleta de seus endereços para cálculo da rota.

## Tecnologias Utilizadas

- **Python:** Linguagem principal para o desenvolvimento do script.
- **Google Maps API:** Para geocodificação, cálculo de distâncias e informações de trajetos.
- **Bibliotecas:**
  - `googlemaps`: Interação com a API do Google Maps.
  - `numpy`: Realização de cálculos matemáticos.
  - `itertools`: Geração de permutações de rotas.

## Como Funciona

1. O sistema solicita ao usuário informações sobre o ponto inicial (endereço de partida) e o ponto final (faculdade).
2. Pergunta a até três usuários(podendo alterar para qualquer quantidade de usuários) se irão utilizar a van no dia e solicita seus endereços.
3. Utiliza a API do Google Maps para calcular as coordenadas de cada endereço.
4. Gera todas as rotas possíveis considerando os pontos de partida, parada e chegada.
5. Calcula a distância total de cada rota e seleciona a mais curta.
6. Exibe os detalhes da melhor rota, incluindo distância total e tempo estimado.

## Requisitos

- **Python 3.7+**
- **Bibliotecas:**
  - `googlemaps`
  - `numpy`
- **Chave de API do Google Maps:** É necessário configurar uma chave de API válida para usar os serviços do Google Maps.

## Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/DevLucasLopes47/RouteMasterVan.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install googlemaps numpy
   ```
3. Configure sua chave de API do Google Maps no código, substituindo o valor de `API_KEY`.
4. Execute o script principal:
   ```bash
   python main.py
   ```

## Próximos Passos

### Conversão em Aplicativo
Este projeto está em fase de desenvolvimento e será transformado em um aplicativo com interface gráfica para facilitar o uso. O objetivo é oferecer um aplicativo intuitivo, onde os usuários possam inserir seus endereços, visualizar rotas otimizadas e obter informações detalhadas sobre o trajeto.

### Funcionalidades Futuras
- **Interface Gráfica:** Desenvolvimento de uma UI amigável utilizando frameworks como `Tkinter`, `PyQt`, ou `Kivy`.
- **Aplicativo Mobile:** Conversão para um app utilizando ferramentas como `Flutter` ou `React Native`.
- **Suporte a Mais Usuários:** Expansão do número de pontos de parada suportados.
- **Integração com Banco de Dados:** Armazenamento de históricos de rotas e endereços frequentes.

## Contribuição
Contribuições são bem-vindas! Caso queira contribuir, sinta-se à vontade para abrir issues ou enviar pull requests.

**Nota:** Este projeto é voltado para otimizar rotas de uma van em Belo Horizonte, com foco na rota até a faculdade UNIBH no bairro Buritis. Todas as sugestões para melhorias e novas funcionalidades são muito bem-vindas!
<table>
  <tr>
    <td align="center" colspan="2">
      <img src="https://github.com/user-attachments/assets/dc665467-7900-4c15-b862-550b65d31030" alt="RouteMasterVan" style="width: 100%; height: 50%;">
    </td>
  </tr>
</table>
