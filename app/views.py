# Create your views here.
from django.shortcuts import render


def inicio(request):

    filme = {
        "ano": "2000",
        "direcao": "Guel Arraes",
        "genero": "Comédia / Drama",
        "duracao": "104 minutos",
        "roteiro": "Guel Arraes, João Falcão",
        "baseado_em": "Peça de Ariano Suassuna",
        "premios": "7 prêmios Grande Otelo",
        "descricao": (
            "Uma divertida e emocionante jornada pelo sertão nordestino, "
            "onde dois pícaros vivem aventuras mirabolantes enquanto tentam "
            "sobreviver com esperteza e muita fé na misericórdia divina."
        ),
        "sinopse": (
            "João Grilo e Chicó são dois nordestinos pobres que vivem de "
            "pequenos golpes e histórias inventadas na cidade de Taperoá, "
            "no interior da Paraíba. Após uma série de confusões envolvendo "
            "padres, coronéis, cangaceiros e até o próprio diabo, os dois "
            "se veem diante de um julgamento divino presidido pela Nossa "
            "Senhora da Compadecida — a única capaz de interceder por eles."
        ),
        
    }
    return render(request, "inicio.html", {"filme": filme})


def elenco(request):
      
    elenco = [
        {
            "nome": "João Grilo",
            "ator": "Matheus Nachtergaele",
            "idade": 28,
            "posicao": "Protagonista",
            "origem": "Taperoá, PB",
            "foto": "imagens/joao grilo.jpg",
        },
        {
            "nome": "Chicó",
            "ator": "Selton Mello",
            "idade": 26,
            "posicao": "Protagonista",
            "origem": "Taperoá, PB",
            "foto": "imagens/chico.jpg",
        },
        {
            "nome": "Nossa Senhora",
            "ator": "Fernanda Montenegro",
            "idade": 50,
            "posicao": "A Compadecida",
            "origem": "Céu",
            "foto": "imagens/nossa senhora.jpg",
        },
        {
            "nome": "O Diabo",
            "ator": "Diogo Vilela",
            "idade": 40,
            "posicao": "Antagonista",
            "origem": "Inferno",
            "foto": "imagens/diabo.jpg",
        },
        {
            "nome": "Severino de Aracaju",
            "ator": "Marco Nanini",
            "idade": 45,
            "posicao": "Cangaceiro",
            "origem": "Aracaju, SE",
            "foto": "imagens/severino.jpg",
        },
        {
            "nome": "Padre João",
            "ator": "Lima Duarte",
            "idade": 60,
            "posicao": "Padre da cidade",
            "origem": "Taperoá, PB",
            "foto": "imagens/padre joao.jpg",
        },
        {
            "nome": "Bispo Dom Virgílio",
            "ator": "Rogério Cardoso",
            "idade": 55,
            "posicao": "Bispo",
            "origem": "Recife, PE",
            "foto": "imagens/bispo.jpg",
        },
        {
            "nome": "Coronel Antônio Moraes",
            "ator": "Aramis Trindade",
            "idade": 58,
            "posicao": "Coronel",
            "origem": "Taperoá, PB",
            "foto": "imagens/major antonio.jpg",
        },
        {
            "nome": "Dora",
            "ator": "Débora Bloch",
            "idade": 30,
            "posicao": "Esposa do padeiro",
            "origem": "Taperoá, PB",
            "foto": "imagens/dora.jpg",
        },
        {
            "nome": "Padeiro",
            "ator": "Luís Melo",
            "idade": 35,
            "posicao": "Padeiro da cidade",
            "origem": "Taperoá, PB",
            "foto": "imagens/padeiro.jpg",
        },
        {
            "nome": "Jesus Cristo",
            "ator": "Carlos Vereza",
            "idade": 33,
            "posicao": "Juiz do julgamento",
            "origem": "Jerusalém",
            "foto": "imagens/jesus.jpg",
        },
    ]
    return render(request, "elenco.html", {"elenco": elenco})

def sobre(request):
    sobre = {
        "historia": (
            "Auto da Compadecida é um filme brasileiro lançado em 2000, dirigido por Guel Arraes. "
            "Baseado na clássica peça de Ariano Suassuna de 1955, o filme é uma adaptação da "
            "minissérie homônima exibida pela TV Globo em 1999. As filmagens aconteceram na cidade "
            "de Cabaceiras, no Sertão do Cariri Paraibano, e o filme foi visto por mais de dois "
            "milhões de espectadores, sendo o maior sucesso de bilheteria brasileiro do ano 2000."
        ),
        "curiosidades": (
            "Durante o Grande Prêmio do Cinema Brasileiro, o filme conquistou os prêmios de melhor "
            "diretor, melhor roteiro, melhor lançamento e melhor ator. Nos Estados Unidos, foi "
            "distribuído com o título 'A Dog's Will'. Uma sequência, 'O Auto da Compadecida 2', "
            "foi lançada em dezembro de 2024."
        ),
    }

    return render(request, "sobre.html", {"sobre": sobre})