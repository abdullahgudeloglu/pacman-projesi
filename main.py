import pygame
import sys
import random

# Pygame'i başlat
pygame.init()

# Renkler
SIYAH = (0, 0, 0)
SARI = (255, 255, 0)
KIRMIZI = (255, 0, 0)

# Ekran Ayarları
GENISLIK, YUKSEKLIK = 600, 600
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Basit Pacman Oyunu")

# Saat (FPS kontrolü için)
saat = pygame.time.Clock()

# Pacman Karakteri
pacman_x, pacman_y = 300, 300
hiz = 5
cap = 20

# Yem (Kırmızı nokta)
yem_x = random.randint(50, GENISLIK-50)
yem_y = random.randint(50, YUKSEKLIK-50)

running = True
while running:
    # Olayları Dinle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tuş Hareketleri
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_LEFT] and pacman_x > 0:
        pacman_x -= hiz
    if tuslar[pygame.K_RIGHT] and pacman_x < GENISLIK:
        pacman_x += hiz
    if tuslar[pygame.K_UP] and pacman_y > 0:
        pacman_y -= hiz
    if tuslar[pygame.K_DOWN] and pacman_y < YUKSEKLIK:
        pacman_y += hiz

    # Yem Yeme Kontrolü (Basit Çarpışma)
    mesafe = ((pacman_x - yem_x)**2 + (pacman_y - yem_y)**2)**0.5
    if mesafe < 30: # Yemi yedi
        yem_x = random.randint(50, GENISLIK-50)
        yem_y = random.randint(50, YUKSEKLIK-50)

    # Ekrana Çiz
    ekran.fill(SIYAH)
    pygame.draw.circle(ekran, SARI, (pacman_x, pacman_y), cap) # Pacman
    pygame.draw.circle(ekran, KIRMIZI, (yem_x, yem_y), 10)     # Yem

    pygame.display.flip()
    saat.tick(60)

pygame.quit()
