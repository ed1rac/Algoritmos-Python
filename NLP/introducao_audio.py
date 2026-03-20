import wave

# importando
noticia = wave.open("noticia.wav", "r")

# convertendo objetos wave para bytes
noticia_wave = noticia.readframes(-1) # -1 quer dizer TODAS as informações dentro do arquivo

#print(noticia_wave[:-1]) # visualizando


