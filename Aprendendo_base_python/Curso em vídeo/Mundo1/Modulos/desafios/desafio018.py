from math import sin,cos,tan,radians
angulo = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo de {angulo:.1f} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo:.1f} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo:.1f} tem a TANGENTE de {tangente:.2f}")