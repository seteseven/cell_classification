## Classificação de células sanguíneas

**Este repositório contém um modelo para classificação de células sanguíneas usando redes neurais.**

O sangue é a parte líquida de um sistema que possui a função dupla de:

1. Distribuir nutrientes e oxigênio para as células do corpo;
2. Transportar o gás carbônico resultante do metabolismo para fora do corpo.

O sangue é composto por diversas células, cada uma com sua função dentro do próprio sistema circulatório e no restante do corpo. Dessa forma, a sanidade dessas células deve ser investigada quando realizamos exames de sangue.

As estruturas que compõem o sangue são de três tipos principais:

- **Vermelhas (Hemácias)** – São os entregadores de oxigênio. Levam o gás dos pulmões para todo o corpo. São vermelhas e possuem formato de disco.

- **Brancas (Leucócitos)** – São os soldados de defesa. Atuam no combate a vírus, bactérias e infecções. Quando o organismo está doente, sua quantidade tende a aumentar.

- **Plaquetas** – São os socorristas. Atuam na coagulação do sangue, formando o tampão que impede hemorragias quando ocorre um ferimento.

_Essas últimas não são células propriamente ditas, mas fragmentos celulares relacionados à coagulação sanguínea e, por esse motivo, **não serão consideradas neste projeto**._

---

## 1. Modelo de classificação de células

Neste projeto, o foco está na **classificação automática de células sanguíneas a partir de imagens**, utilizando técnicas de **aprendizado de máquina e redes neurais artificiais**. A proposta é empregar um modelo de **deep learning** capaz de identificar padrões visuais presentes nas células e classificá-las de acordo com seu tipo.

A classificação automatizada de células sanguíneas é uma área de grande interesse na biologia e na medicina, pois pode:

- Auxiliar na análise de exames laboratoriais;
- Reduzir erros humanos em contagens e identificações manuais;
- Aumentar a eficiência e a rapidez no diagnóstico;
- Servir como ferramenta de apoio para ensino e pesquisa em hematologia.

O modelo desenvolvido neste repositório utiliza imagens de células sanguíneas previamente rotuladas para realizar o treinamento supervisionado. Durante esse processo, a rede neural aprende características como **forma, textura, coloração e padrões internos das células**, fundamentais para diferenciar os diferentes tipos celulares.

O pipeline do projeto envolve as seguintes etapas principais:

- Carregamento e organização do conjunto de dados de imagens;
- Pré-processamento das imagens (redimensionamento, normalização, etc.);
- Construção da arquitetura da rede neural;
- Treinamento e validação do modelo;
- Avaliação do desempenho por meio de métricas adequadas;
- Salvamento do modelo treinado para uso posterior em inferência.

Ao final, o modelo treinado é capaz de receber novas imagens de células sanguíneas e **predizer automaticamente a classe da célula**, demonstrando o potencial do uso de redes neurais na análise computacional de sistemas biológicos.

Este projeto possui caráter **educacional e experimental**, servindo como base para estudos em ciência de dados, visão computacional e aplicações de inteligência artificial na área da saúde.
