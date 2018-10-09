# -*- coding: utf-8 -*-

import media, fresh_tomatoes

avengers_infinity_war = media.Movie(
    'Avengers Infinity War',
    'Homem de Ferro, Thor, Hulk e os Vingadores se unem para combater seu inimigo mais poderoso, o maligno Thanos. Em uma missão para coletar todas as seis pedras infinitas, Thanos planeja usá-las para infligir sua vontade maléfica sobre a realidade.',
    'https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg',
    'https://www.youtube.com/watch?v=6ZfuNTqbHE8'
)

black_panther = media.Movie(
    'Black Panther',
    'Conheça a história de T\'Challa, príncipe do reino de Wakanda, que perde o seu pai e viaja para os Estados Unidos, onde tem contato com os Vingadores. Entre as suas habilidades estão a velocidade, inteligência e os sentidos apurados.',
    'https://upload.wikimedia.org/wikipedia/pt/9/90/Pantera_Negra_%28poster%29.jpg',
    'https://www.youtube.com/watch?v=xjDjIWPwcPU'
)

thor_ragnarok = media.Movie(
    'Thor Ragnarok',
    'Thor está preso do outro lado do universo. Ele precisa correr contra o tempo para voltar a Asgard e parar Ragnarok, a destruição de seu mundo, que está nas mãos da poderosa e implacável vilã Hela.',
    'https://upload.wikimedia.org/wikipedia/pt/7/7d/Thor_Ragnarok_poster.jpg',
    'https://www.youtube.com/watch?v=ue80QwXMRHg'
)

#  Generates HTML and opens the page in the browser
fresh_tomatoes.open_movies_page([avengers_infinity_war, black_panther, thor_ragnarok])
