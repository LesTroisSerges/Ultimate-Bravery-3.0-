import random
import pygame
import time
import sys
import os

pygame.init()
pygame.mixer.init()

path = "/caca"

os.chdir(path)

display_width = 1600
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Ultimate Bravery")

os.system("pause")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (34, 177, 76)
yellow = (200, 200, 0)
blue = (100, 100, 255)
dark_green = (20, 100, 50)
dark_red = (155, 0, 0)
dark_yellow = (100, 100, 0)
dark_blue = (0, 0, 155)

sys.setrecursionlimit(1500)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("Calibri", 25)
medfont = pygame.font.SysFont("Elephant", 50)
largefont = pygame.font.SysFont("Stencil", 75)

icon = pygame.image.load(os.path.join("caca", 'icon.bmp'))
pygame.display.set_icon(icon)
void = pygame.image.load(os.path.join("void.png"))
img_background_start = pygame.image.load(os.path.join("background.png"))
img_quit_active = pygame.image.load(os.path.join("quit_active.png"))
letsgo_active = pygame.image.load(os.path.join("button_letsgo_active.png"))
letsgo_inactive = pygame.image.load(os.path.join("button_letsgo_inactive.png"))
img_quit_inactive = pygame.image.load(os.path.join("quit_inactive.png"))
img_playnow_active = pygame.image.load(os.path.join("start_active.png"))
img_playnow_inactive = pygame.image.load(os.path.join("start_inactive.png"))
img_howling_abyss_active = pygame.image.load(os.path.join("howling_abyss_button_active.png"))
img_howling_abyss_inactive = pygame.image.load(os.path.join("howling_abyss_button_inactive.png"))
img_background_howling = pygame.image.load(os.path.join("background_howling abyss.png"))
img_background_summoner = pygame.image.load(os.path.join("background_summoner's rift.png"))
img_summoner_active = pygame.image.load(os.path.join("summoner_button_active.png"))
img_summoner_inactive = pygame.image.load(os.path.join("summoner_button_inactive.png"))
img_background_twisted = pygame.image.load(os.path.join("background_twisted treeline.png"))
img_twisted_active = pygame.image.load(os.path.join("twisted_treeline_button_active.png"))
img_twisted_inactive = pygame.image.load(os.path.join("twisted_treeline_button_inactive.png"))
button_reroll_active = pygame.image.load(os.path.join("button_reroll_active.png"))
button_reroll_inactive = pygame.image.load(os.path.join("button_reroll_inactive.png"))
settings_active = pygame.image.load(os.path.join("settings_active.png"))
settings_inactive = pygame.image.load(os.path.join("settings_inactive.png"))
image_1 = pygame.image.load(os.path.join("1.png"))
image_2 = pygame.image.load(os.path.join("2.png"))
image_3 = pygame.image.load(os.path.join("3.png"))
image_4 = pygame.image.load(os.path.join("4.png"))
image_5 = pygame.image.load(os.path.join("5.png"))
img_rules_inactive = pygame.image.load(os.path.join("rules_inactive.png"))
img_rules_active = pygame.image.load(os.path.join("rules_active.png"))
back_inactive = pygame.image.load(os.path.join("back_inactive.png"))
back_active = pygame.image.load(os.path.join("back_active.png"))
img_title = pygame.image.load(os.path.join("Title.png"))

def message_to_screen(msg, color, y_displace=0,x_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2) + x_displace, int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

#Loading...
message_to_screen("Loading...", white, size="large")
pygame.display.update()
#Load les images
for i in range(1):
    m_Aatrox_i = pygame.image.load("mini_champs_inactive_Aatrox.png")
    m_Aatrox_a = pygame.image.load("mini_champs_active_Aatrox.png")
    b_Aatrox = pygame.image.load("big_champs_Aatrox.png")
    m_Ahri_i = pygame.image.load("mini_champs_inactive_Ahri.png")
    m_Ahri_a = pygame.image.load("mini_champs_active_Ahri.png")
    b_Ahri = pygame.image.load("big_champs_Ahri.png")
    m_Akali_i = pygame.image.load("mini_champs_inactive_Akali.png")
    m_Akali_a = pygame.image.load("mini_champs_active_Akali.png")
    b_Akali = pygame.image.load("big_champs_Akali.png")
    m_Alistar_i = pygame.image.load("mini_champs_inactive_Alistar.png")
    m_Alistar_a = pygame.image.load("mini_champs_active_Alistar.png")
    b_Alistar = pygame.image.load("big_champs_Alistar.png")
    m_Amumu_i = pygame.image.load("mini_champs_inactive_Amumu.png")
    m_Amumu_a = pygame.image.load("mini_champs_active_Amumu.png")
    b_Amumu = pygame.image.load("big_champs_Amumu.png")
    m_Anivia_i = pygame.image.load("mini_champs_inactive_Anivia.png")
    m_Anivia_a = pygame.image.load("mini_champs_active_Anivia.png")
    b_Anivia = pygame.image.load("big_champs_Anivia.png")
    m_Annie_i = pygame.image.load("mini_champs_inactive_Annie.png")
    m_Annie_a = pygame.image.load("mini_champs_active_Annie.png")
    b_Annie = pygame.image.load("big_champs_Annie.png")
    m_Ashe_i = pygame.image.load("mini_champs_inactive_Ashe.png")
    m_Ashe_a = pygame.image.load("mini_champs_active_Ashe.png")
    b_Ashe = pygame.image.load("big_champs_Ashe.png")
    m_AurelionSol_i = pygame.image.load("mini_champs_inactive_AurelionSol.png")
    m_AurelionSol_a = pygame.image.load("mini_champs_active_AurelionSol.png")
    b_AurelionSol = pygame.image.load("big_champs_AurelionSol.png")
    m_Azir_i = pygame.image.load("mini_champs_inactive_Azir.png")
    m_Azir_a = pygame.image.load("mini_champs_active_Azir.png")
    b_Azir = pygame.image.load("big_champs_Azir.png")
    m_Bard_i = pygame.image.load("mini_champs_inactive_Bard.png")
    m_Bard_a = pygame.image.load("mini_champs_active_Bard.png")
    b_Bard = pygame.image.load("big_champs_Bard.png")
    m_Blitzcrank_i = pygame.image.load("mini_champs_inactive_Blitzcrank.png")
    m_Blitzcrank_a = pygame.image.load("mini_champs_active_Blitzcrank.png")
    b_Blitzcrank = pygame.image.load("big_champs_Blitzcrank.png")
    m_Brand_i = pygame.image.load("mini_champs_inactive_Brand.png")
    m_Brand_a = pygame.image.load("mini_champs_active_Brand.png")
    b_Brand = pygame.image.load("big_champs_Brand.png")
    m_Braum_i = pygame.image.load("mini_champs_inactive_Braum.png")
    m_Braum_a = pygame.image.load("mini_champs_active_Braum.png")
    b_Braum = pygame.image.load("big_champs_Braum.png")
    m_Caitlyn_i = pygame.image.load("mini_champs_inactive_Caitlyn.png")
    m_Caitlyn_a = pygame.image.load("mini_champs_active_Caitlyn.png")
    b_Caitlyn = pygame.image.load("big_champs_Caitlyn.png")
    m_Cassiopeia_i = pygame.image.load("mini_champs_inactive_Cassiopeia.png")
    m_Cassiopeia_a = pygame.image.load("mini_champs_active_Cassiopeia.png")
    b_Cassiopeia = pygame.image.load("big_champs_Cassiopeia.png")
    m_Chogath_i = pygame.image.load("mini_champs_inactive_Chogath.png")
    m_Chogath_a = pygame.image.load("mini_champs_active_Chogath.png")
    b_Chogath = pygame.image.load("big_champs_Chogath.png")
    m_Corki_i = pygame.image.load("mini_champs_inactive_Corki.png")
    m_Corki_a = pygame.image.load("mini_champs_active_Corki.png")
    b_Corki = pygame.image.load("big_champs_Corki.png")
    m_Darius_i = pygame.image.load("mini_champs_inactive_Darius.png")
    m_Darius_a = pygame.image.load("mini_champs_active_Darius.png")
    b_Darius = pygame.image.load("big_champs_Darius.png")
    m_Diana_i = pygame.image.load("mini_champs_inactive_Diana.png")
    m_Diana_a = pygame.image.load("mini_champs_active_Diana.png")
    b_Diana = pygame.image.load("big_champs_Diana.png")
    m_DrMundo_i = pygame.image.load("mini_champs_inactive_DrMundo.png")
    m_DrMundo_a = pygame.image.load("mini_champs_active_DrMundo.png")
    b_DrMundo = pygame.image.load("big_champs_DrMundo.png")
    m_Draven_i = pygame.image.load("mini_champs_inactive_Draven.png")
    m_Draven_a = pygame.image.load("mini_champs_active_Draven.png")
    b_Draven = pygame.image.load("big_champs_Draven.png")
    m_Ekko_i = pygame.image.load("mini_champs_inactive_Ekko.png")
    m_Ekko_a = pygame.image.load("mini_champs_active_Ekko.png")
    b_Ekko = pygame.image.load("big_champs_Ekko.png")
    m_Elise_i = pygame.image.load("mini_champs_inactive_Elise.png")
    m_Elise_a = pygame.image.load("mini_champs_active_Elise.png")
    b_Elise = pygame.image.load("big_champs_Elise.png")
    m_Evelynn_i = pygame.image.load("mini_champs_inactive_Evelynn.png")
    m_Evelynn_a = pygame.image.load("mini_champs_active_Evelynn.png")
    b_Evelynn = pygame.image.load("big_champs_Evelynn.png")
    m_Ezreal_i = pygame.image.load("mini_champs_inactive_Ezreal.png")
    m_Ezreal_a = pygame.image.load("mini_champs_active_Ezreal.png")
    b_Ezreal = pygame.image.load("big_champs_Ezreal.png")
    m_FiddleSticks_i = pygame.image.load("mini_champs_inactive_FiddleSticks.png")
    m_FiddleSticks_a = pygame.image.load("mini_champs_active_FiddleSticks.png")
    b_FiddleSticks = pygame.image.load("big_champs_FiddleSticks.png")
    m_Fiora_i = pygame.image.load("mini_champs_inactive_Fiora.png")
    m_Fiora_a = pygame.image.load("mini_champs_active_Fiora.png")
    b_Fiora = pygame.image.load("big_champs_Fiora.png")
    m_Fizz_i = pygame.image.load("mini_champs_inactive_Fizz.png")
    m_Fizz_a = pygame.image.load("mini_champs_active_Fizz.png")
    b_Fizz = pygame.image.load("big_champs_Fizz.png")
    m_Galio_i = pygame.image.load("mini_champs_inactive_Galio.png")
    m_Galio_a = pygame.image.load("mini_champs_active_Galio.png")
    b_Galio = pygame.image.load("big_champs_Galio.png")
    m_Gangplank_i = pygame.image.load("mini_champs_inactive_Gangplank.png")
    m_Gangplank_a = pygame.image.load("mini_champs_active_Gangplank.png")
    b_Gangplank = pygame.image.load("big_champs_Gangplank.png")
    m_Garen_i = pygame.image.load("mini_champs_inactive_Garen.png")
    m_Garen_a = pygame.image.load("mini_champs_active_Garen.png")
    b_Garen = pygame.image.load("big_champs_Garen.png")
    m_Gnar_i = pygame.image.load("mini_champs_inactive_Gnar.png")
    m_Gnar_a = pygame.image.load("mini_champs_active_Gnar.png")
    b_Gnar = pygame.image.load("big_champs_Gnar.png")
    m_Gragas_i = pygame.image.load("mini_champs_inactive_Gragas.png")
    m_Gragas_a = pygame.image.load("mini_champs_active_Gragas.png")
    b_Gragas = pygame.image.load("big_champs_Gragas.png")
    m_Graves_i = pygame.image.load("mini_champs_inactive_Graves.png")
    m_Graves_a = pygame.image.load("mini_champs_active_Graves.png")
    b_Graves = pygame.image.load("big_champs_Graves.png")
    m_Hecarim_i = pygame.image.load("mini_champs_inactive_Hecarim.png")
    m_Hecarim_a = pygame.image.load("mini_champs_active_Hecarim.png")
    b_Hecarim = pygame.image.load("big_champs_Hecarim.png")
    m_Heimerdinger_i = pygame.image.load("mini_champs_inactive_Heimerdinger.png")
    m_Heimerdinger_a = pygame.image.load("mini_champs_active_Heimerdinger.png")
    b_Heimerdinger = pygame.image.load("big_champs_Heimerdinger.png")
    m_Illaoi_i = pygame.image.load("mini_champs_inactive_Illaoi.png")
    m_Illaoi_a = pygame.image.load("mini_champs_active_Illaoi.png")
    b_Illaoi = pygame.image.load("big_champs_Illaoi.png")
    m_Irelia_i = pygame.image.load("mini_champs_inactive_Irelia.png")
    m_Irelia_a = pygame.image.load("mini_champs_active_Irelia.png")
    b_Irelia = pygame.image.load("big_champs_Irelia.png")
    m_Janna_i = pygame.image.load("mini_champs_inactive_Janna.png")
    m_Janna_a = pygame.image.load("mini_champs_active_Janna.png")
    b_Janna = pygame.image.load("big_champs_Janna.png")
    m_JarvanIV_i = pygame.image.load("mini_champs_inactive_JarvanIV.png")
    m_JarvanIV_a = pygame.image.load("mini_champs_active_JarvanIV.png")
    b_JarvanIV = pygame.image.load("big_champs_JarvanIV.png")
    m_Jax_i = pygame.image.load("mini_champs_inactive_Jax.png")
    m_Jax_a = pygame.image.load("mini_champs_active_Jax.png")
    b_Jax = pygame.image.load("big_champs_Jax.png")
    m_Jayce_i = pygame.image.load("mini_champs_inactive_Jayce.png")
    m_Jayce_a = pygame.image.load("mini_champs_active_Jayce.png")
    b_Jayce = pygame.image.load("big_champs_Jayce.png")
    m_Jhin_i = pygame.image.load("mini_champs_inactive_Jhin.png")
    m_Jhin_a = pygame.image.load("mini_champs_active_Jhin.png")
    b_Jhin = pygame.image.load("big_champs_Jhin.png")
    m_Jinx_i = pygame.image.load("mini_champs_inactive_Jinx.png")
    m_Jinx_a = pygame.image.load("mini_champs_active_Jinx.png")
    b_Jinx = pygame.image.load("big_champs_Jinx.png")
    m_Kalista_i = pygame.image.load("mini_champs_inactive_Kalista.png")
    m_Kalista_a = pygame.image.load("mini_champs_active_Kalista.png")
    b_Kalista = pygame.image.load("big_champs_Kalista.png")
    m_Karma_i = pygame.image.load("mini_champs_inactive_Karma.png")
    m_Karma_a = pygame.image.load("mini_champs_active_Karma.png")
    b_Karma = pygame.image.load("big_champs_Karma.png")
    m_Karthus_i = pygame.image.load("mini_champs_inactive_Karthus.png")
    m_Karthus_a = pygame.image.load("mini_champs_active_Karthus.png")
    b_Karthus = pygame.image.load("big_champs_Karthus.png")
    m_Kassadin_i = pygame.image.load("mini_champs_inactive_Kassadin.png")
    m_Kassadin_a = pygame.image.load("mini_champs_active_Kassadin.png")
    b_Kassadin = pygame.image.load("big_champs_Kassadin.png")
    m_Katarina_i = pygame.image.load("mini_champs_inactive_Katarina.png")
    m_Katarina_a = pygame.image.load("mini_champs_active_Katarina.png")
    b_Katarina = pygame.image.load("big_champs_Katarina.png")
    m_Kayle_i = pygame.image.load("mini_champs_inactive_Kayle.png")
    m_Kayle_a = pygame.image.load("mini_champs_active_Kayle.png")
    b_Kayle = pygame.image.load("big_champs_Kayle.png")
    m_Kennen_i = pygame.image.load("mini_champs_inactive_Kennen.png")
    m_Kennen_a = pygame.image.load("mini_champs_active_Kennen.png")
    b_Kennen = pygame.image.load("big_champs_Kennen.png")
    m_Khazix_i = pygame.image.load("mini_champs_inactive_Khazix.png")
    m_Khazix_a = pygame.image.load("mini_champs_active_Khazix.png")
    b_Khazix = pygame.image.load("big_champs_Khazix.png")
    m_Kindred_i = pygame.image.load("mini_champs_inactive_Kindred.png")
    m_Kindred_a = pygame.image.load("mini_champs_active_Kindred.png")
    b_Kindred = pygame.image.load("big_champs_Kindred.png")
    m_Kled_i = pygame.image.load("mini_champs_inactive_Kled.png")
    m_Kled_a = pygame.image.load("mini_champs_active_Kled.png")
    b_Kled = pygame.image.load("big_champs_Kled.png")
    m_KogMaw_i = pygame.image.load("mini_champs_inactive_KogMaw.png")
    m_KogMaw_a = pygame.image.load("mini_champs_active_KogMaw.png")
    b_KogMaw = pygame.image.load("big_champs_KogMaw.png")
    m_Leblanc_i = pygame.image.load("mini_champs_inactive_Leblanc.png")
    m_Leblanc_a = pygame.image.load("mini_champs_active_Leblanc.png")
    b_Leblanc = pygame.image.load("big_champs_Leblanc.png")
    m_LeeSin_i = pygame.image.load("mini_champs_inactive_LeeSin.png")
    m_LeeSin_a = pygame.image.load("mini_champs_active_LeeSin.png")
    b_LeeSin = pygame.image.load("big_champs_LeeSin.png")
    m_Leona_i = pygame.image.load("mini_champs_inactive_Leona.png")
    m_Leona_a = pygame.image.load("mini_champs_active_Leona.png")
    b_Leona = pygame.image.load("big_champs_Leona.png")
    m_Lissandra_i = pygame.image.load("mini_champs_inactive_Lissandra.png")
    m_Lissandra_a = pygame.image.load("mini_champs_active_Lissandra.png")
    b_Lissandra = pygame.image.load("big_champs_Lissandra.png")
    m_Lucian_i = pygame.image.load("mini_champs_inactive_Lucian.png")
    m_Lucian_a = pygame.image.load("mini_champs_active_Lucian.png")
    b_Lucian = pygame.image.load("big_champs_Lucian.png")
    m_Lulu_i = pygame.image.load("mini_champs_inactive_Lulu.png")
    m_Lulu_a = pygame.image.load("mini_champs_active_Lulu.png")
    b_Lulu = pygame.image.load("big_champs_Lulu.png")
    m_Lux_i = pygame.image.load("mini_champs_inactive_Lux.png")
    m_Lux_a = pygame.image.load("mini_champs_active_Lux.png")
    b_Lux = pygame.image.load("big_champs_Lux.png")
    m_Malphite_i = pygame.image.load("mini_champs_inactive_Malphite.png")
    m_Malphite_a = pygame.image.load("mini_champs_active_Malphite.png")
    b_Malphite = pygame.image.load("big_champs_Malphite.png")
    m_Malzahar_i = pygame.image.load("mini_champs_inactive_Malzahar.png")
    m_Malzahar_a = pygame.image.load("mini_champs_active_Malzahar.png")
    b_Malzahar = pygame.image.load("big_champs_Malzahar.png")
    m_Maokai_i = pygame.image.load("mini_champs_inactive_Maokai.png")
    m_Maokai_a = pygame.image.load("mini_champs_active_Maokai.png")
    b_Maokai = pygame.image.load("big_champs_Maokai.png")
    m_MasterYi_i = pygame.image.load("mini_champs_inactive_MasterYi.png")
    m_MasterYi_a = pygame.image.load("mini_champs_active_MasterYi.png")
    b_MasterYi = pygame.image.load("big_champs_MasterYi.png")
    m_MissFortune_i = pygame.image.load("mini_champs_inactive_MissFortune.png")
    m_MissFortune_a = pygame.image.load("mini_champs_active_MissFortune.png")
    b_MissFortune = pygame.image.load("big_champs_MissFortune.png")
    m_Mordekaiser_i = pygame.image.load("mini_champs_inactive_Mordekaiser.png")
    m_Mordekaiser_a = pygame.image.load("mini_champs_active_Mordekaiser.png")
    b_Mordekaiser = pygame.image.load("big_champs_Mordekaiser.png")
    m_Morgana_i = pygame.image.load("mini_champs_inactive_Morgana.png")
    m_Morgana_a = pygame.image.load("mini_champs_active_Morgana.png")
    b_Morgana = pygame.image.load("big_champs_Morgana.png")
    m_Nami_i = pygame.image.load("mini_champs_inactive_Nami.png")
    m_Nami_a = pygame.image.load("mini_champs_active_Nami.png")
    b_Nami = pygame.image.load("big_champs_Nami.png")
    m_Nasus_i = pygame.image.load("mini_champs_inactive_Nasus.png")
    m_Nasus_a = pygame.image.load("mini_champs_active_Nasus.png")
    b_Nasus = pygame.image.load("big_champs_Nasus.png")
    m_Nautilus_i = pygame.image.load("mini_champs_inactive_Nautilus.png")
    m_Nautilus_a = pygame.image.load("mini_champs_active_Nautilus.png")
    b_Nautilus = pygame.image.load("big_champs_Nautilus.png")
    m_Nidalee_i = pygame.image.load("mini_champs_inactive_Nidalee.png")
    m_Nidalee_a = pygame.image.load("mini_champs_active_Nidalee.png")
    b_Nidalee = pygame.image.load("big_champs_Nidalee.png")
    m_Nocturne_i = pygame.image.load("mini_champs_inactive_Nocturne.png")
    m_Nocturne_a = pygame.image.load("mini_champs_active_Nocturne.png")
    b_Nocturne = pygame.image.load("big_champs_Nocturne.png")
    m_Nunu_i = pygame.image.load("mini_champs_inactive_Nunu.png")
    m_Nunu_a = pygame.image.load("mini_champs_active_Nunu.png")
    b_Nunu = pygame.image.load("big_champs_Nunu.png")
    m_Olaf_i = pygame.image.load("mini_champs_inactive_Olaf.png")
    m_Olaf_a = pygame.image.load("mini_champs_active_Olaf.png")
    b_Olaf = pygame.image.load("big_champs_Olaf.png")
    m_Orianna_i = pygame.image.load("mini_champs_inactive_Orianna.png")
    m_Orianna_a = pygame.image.load("mini_champs_active_Orianna.png")
    b_Orianna = pygame.image.load("big_champs_Orianna.png")
    m_Pantheon_i = pygame.image.load("mini_champs_inactive_Pantheon.png")
    m_Pantheon_a = pygame.image.load("mini_champs_active_Pantheon.png")
    b_Pantheon = pygame.image.load("big_champs_Pantheon.png")
    m_Poppy_i = pygame.image.load("mini_champs_inactive_Poppy.png")
    m_Poppy_a = pygame.image.load("mini_champs_active_Poppy.png")
    b_Poppy = pygame.image.load("big_champs_Poppy.png")
    m_Quinn_i = pygame.image.load("mini_champs_inactive_Quinn.png")
    m_Quinn_a = pygame.image.load("mini_champs_active_Quinn.png")
    b_Quinn = pygame.image.load("big_champs_Quinn.png")
    m_Rammus_i = pygame.image.load("mini_champs_inactive_Rammus.png")
    m_Rammus_a = pygame.image.load("mini_champs_active_Rammus.png")
    b_Rammus = pygame.image.load("big_champs_Rammus.png")
    m_RekSai_i = pygame.image.load("mini_champs_inactive_RekSai.png")
    m_RekSai_a = pygame.image.load("mini_champs_active_RekSai.png")
    b_RekSai = pygame.image.load("big_champs_RekSai.png")
    m_Renekton_i = pygame.image.load("mini_champs_inactive_Renekton.png")
    m_Renekton_a = pygame.image.load("mini_champs_active_Renekton.png")
    b_Renekton = pygame.image.load("big_champs_Renekton.png")
    m_Rengar_i = pygame.image.load("mini_champs_inactive_Rengar.png")
    m_Rengar_a = pygame.image.load("mini_champs_active_Rengar.png")
    b_Rengar = pygame.image.load("big_champs_Rengar.png")
    m_Riven_i = pygame.image.load("mini_champs_inactive_Riven.png")
    m_Riven_a = pygame.image.load("mini_champs_active_Riven.png")
    b_Riven = pygame.image.load("big_champs_Riven.png")
    m_Rumble_i = pygame.image.load("mini_champs_inactive_Rumble.png")
    m_Rumble_a = pygame.image.load("mini_champs_active_Rumble.png")
    b_Rumble = pygame.image.load("big_champs_Rumble.png")
    m_Ryze_i = pygame.image.load("mini_champs_inactive_Ryze.png")
    m_Ryze_a = pygame.image.load("mini_champs_active_Ryze.png")
    b_Ryze = pygame.image.load("big_champs_Ryze.png")
    m_Sejuani_i = pygame.image.load("mini_champs_inactive_Sejuani.png")
    m_Sejuani_a = pygame.image.load("mini_champs_active_Sejuani.png")
    b_Sejuani = pygame.image.load("big_champs_Sejuani.png")
    m_Shaco_i = pygame.image.load("mini_champs_inactive_Shaco.png")
    m_Shaco_a = pygame.image.load("mini_champs_active_Shaco.png")
    b_Shaco = pygame.image.load("big_champs_Shaco.png")
    m_Shen_i = pygame.image.load("mini_champs_inactive_Shen.png")
    m_Shen_a = pygame.image.load("mini_champs_active_Shen.png")
    b_Shen = pygame.image.load("big_champs_Shen.png")
    m_Shyvana_i = pygame.image.load("mini_champs_inactive_Shyvana.png")
    m_Shyvana_a = pygame.image.load("mini_champs_active_Shyvana.png")
    b_Shyvana = pygame.image.load("big_champs_Shyvana.png")
    m_Singed_i = pygame.image.load("mini_champs_inactive_Singed.png")
    m_Singed_a = pygame.image.load("mini_champs_active_Singed.png")
    b_Singed = pygame.image.load("big_champs_Singed.png")
    m_Sion_i = pygame.image.load("mini_champs_inactive_Sion.png")
    m_Sion_a = pygame.image.load("mini_champs_active_Sion.png")
    b_Sion = pygame.image.load("big_champs_Sion.png")
    m_Sivir_i = pygame.image.load("mini_champs_inactive_Sivir.png")
    m_Sivir_a = pygame.image.load("mini_champs_active_Sivir.png")
    b_Sivir = pygame.image.load("big_champs_Sivir.png")
    m_Skarner_i = pygame.image.load("mini_champs_inactive_Skarner.png")
    m_Skarner_a = pygame.image.load("mini_champs_active_Skarner.png")
    b_Skarner = pygame.image.load("big_champs_Skarner.png")
    m_Sona_i = pygame.image.load("mini_champs_inactive_Sona.png")
    m_Sona_a = pygame.image.load("mini_champs_active_Sona.png")
    b_Sona = pygame.image.load("big_champs_Sona.png")
    m_Soraka_i = pygame.image.load("mini_champs_inactive_Soraka.png")
    m_Soraka_a = pygame.image.load("mini_champs_active_Soraka.png")
    b_Soraka = pygame.image.load("big_champs_Soraka.png")
    m_Swain_i = pygame.image.load("mini_champs_inactive_Swain.png")
    m_Swain_a = pygame.image.load("mini_champs_active_Swain.png")
    b_Swain = pygame.image.load("big_champs_Swain.png")
    m_Syndra_i = pygame.image.load("mini_champs_inactive_Syndra.png")
    m_Syndra_a = pygame.image.load("mini_champs_active_Syndra.png")
    b_Syndra = pygame.image.load("big_champs_Syndra.png")
    m_TahmKench_i = pygame.image.load("mini_champs_inactive_TahmKench.png")
    m_TahmKench_a = pygame.image.load("mini_champs_active_TahmKench.png")
    b_TahmKench = pygame.image.load("big_champs_TahmKench.png")
    m_Taliyah_i = pygame.image.load("mini_champs_inactive_Taliyah.png")
    m_Taliyah_a = pygame.image.load("mini_champs_active_Taliyah.png")
    b_Taliyah = pygame.image.load("big_champs_Taliyah.png")
    m_Talon_i = pygame.image.load("mini_champs_inactive_Talon.png")
    m_Talon_a = pygame.image.load("mini_champs_active_Talon.png")
    b_Talon = pygame.image.load("big_champs_Talon.png")
    m_Taric_i = pygame.image.load("mini_champs_inactive_Taric.png")
    m_Taric_a = pygame.image.load("mini_champs_active_Taric.png")
    b_Taric = pygame.image.load("big_champs_Taric.png")
    m_Teemo_i = pygame.image.load("mini_champs_inactive_Teemo.png")
    m_Teemo_a = pygame.image.load("mini_champs_active_Teemo.png")
    b_Teemo = pygame.image.load("big_champs_Teemo.png")
    m_Thresh_i = pygame.image.load("mini_champs_inactive_Thresh.png")
    m_Thresh_a = pygame.image.load("mini_champs_active_Thresh.png")
    b_Thresh = pygame.image.load("big_champs_Thresh.png")
    m_Tristana_i = pygame.image.load("mini_champs_inactive_Tristana.png")
    m_Tristana_a = pygame.image.load("mini_champs_active_Tristana.png")
    b_Tristana = pygame.image.load("big_champs_Tristana.png")
    m_Trundle_i = pygame.image.load("mini_champs_inactive_Trundle.png")
    m_Trundle_a = pygame.image.load("mini_champs_active_Trundle.png")
    b_Trundle = pygame.image.load("big_champs_Trundle.png")
    m_Tryndamere_i = pygame.image.load("mini_champs_inactive_Tryndamere.png")
    m_Tryndamere_a = pygame.image.load("mini_champs_active_Tryndamere.png")
    b_Tryndamere = pygame.image.load("big_champs_Tryndamere.png")
    m_TwistedFate_i = pygame.image.load("mini_champs_inactive_TwistedFate.png")
    m_TwistedFate_a = pygame.image.load("mini_champs_active_TwistedFate.png")
    b_TwistedFate = pygame.image.load("big_champs_TwistedFate.png")
    m_Twitch_i = pygame.image.load("mini_champs_inactive_Twitch.png")
    m_Twitch_a = pygame.image.load("mini_champs_active_Twitch.png")
    b_Twitch = pygame.image.load("big_champs_Twitch.png")
    m_Udyr_i = pygame.image.load("mini_champs_inactive_Udyr.png")
    m_Udyr_a = pygame.image.load("mini_champs_active_Udyr.png")
    b_Udyr = pygame.image.load("big_champs_Udyr.png")
    m_Urgot_i = pygame.image.load("mini_champs_inactive_Urgot.png")
    m_Urgot_a = pygame.image.load("mini_champs_active_Urgot.png")
    b_Urgot = pygame.image.load("big_champs_Urgot.png")
    m_Varus_i = pygame.image.load("mini_champs_inactive_Varus.png")
    m_Varus_a = pygame.image.load("mini_champs_active_Varus.png")
    b_Varus = pygame.image.load("big_champs_Varus.png")
    m_Vayne_i = pygame.image.load("mini_champs_inactive_Vayne.png")
    m_Vayne_a = pygame.image.load("mini_champs_active_Vayne.png")
    b_Vayne = pygame.image.load("big_champs_Vayne.png")
    m_Veigar_i = pygame.image.load("mini_champs_inactive_Veigar.png")
    m_Veigar_a = pygame.image.load("mini_champs_active_Veigar.png")
    b_Veigar = pygame.image.load("big_champs_Veigar.png")
    m_Velkoz_i = pygame.image.load("mini_champs_inactive_Velkoz.png")
    m_Velkoz_a = pygame.image.load("mini_champs_active_Velkoz.png")
    b_Velkoz = pygame.image.load("big_champs_Velkoz.png")
    m_Vi_i = pygame.image.load("mini_champs_inactive_Vi.png")
    m_Vi_a = pygame.image.load("mini_champs_active_Vi.png")
    b_Vi = pygame.image.load("big_champs_Vi.png")
    m_Viktor_i = pygame.image.load("mini_champs_inactive_Viktor.png")
    m_Viktor_a = pygame.image.load("mini_champs_active_Viktor.png")
    b_Viktor = pygame.image.load("big_champs_Viktor.png")
    m_Vladimir_i = pygame.image.load("mini_champs_inactive_Vladimir.png")
    m_Vladimir_a = pygame.image.load("mini_champs_active_Vladimir.png")
    b_Vladimir = pygame.image.load("big_champs_Vladimir.png")
    m_Volibear_i = pygame.image.load("mini_champs_inactive_Volibear.png")
    m_Volibear_a = pygame.image.load("mini_champs_active_Volibear.png")
    b_Volibear = pygame.image.load("big_champs_Volibear.png")
    m_Warwick_i = pygame.image.load("mini_champs_inactive_Warwick.png")
    m_Warwick_a = pygame.image.load("mini_champs_active_Warwick.png")
    b_Warwick = pygame.image.load("big_champs_Warwick.png")
    m_Wukong_i = pygame.image.load("mini_champs_inactive_Wukong.png")
    m_Wukong_a = pygame.image.load("mini_champs_active_Wukong.png")
    b_Wukong = pygame.image.load("big_champs_Wukong.png")
    m_Xerath_i = pygame.image.load("mini_champs_inactive_Xerath.png")
    m_Xerath_a = pygame.image.load("mini_champs_active_Xerath.png")
    b_Xerath = pygame.image.load("big_champs_Xerath.png")
    m_XinZhao_i = pygame.image.load("mini_champs_inactive_XinZhao.png")
    m_XinZhao_a = pygame.image.load("mini_champs_active_XinZhao.png")
    b_XinZhao = pygame.image.load("big_champs_XinZhao.png")
    m_Yasuo_i = pygame.image.load("mini_champs_inactive_Yasuo.png")
    m_Yasuo_a = pygame.image.load("mini_champs_active_Yasuo.png")
    b_Yasuo = pygame.image.load("big_champs_Yasuo.png")
    m_Yorick_i = pygame.image.load("mini_champs_inactive_Yorick.png")
    m_Yorick_a = pygame.image.load("mini_champs_active_Yorick.png")
    b_Yorick = pygame.image.load("big_champs_Yorick.png")
    m_Zac_i = pygame.image.load("mini_champs_inactive_Zac.png")
    m_Zac_a = pygame.image.load("mini_champs_active_Zac.png")
    b_Zac = pygame.image.load("big_champs_Zac.png")
    m_Zed_i = pygame.image.load("mini_champs_inactive_Zed.png")
    m_Zed_a = pygame.image.load("mini_champs_active_Zed.png")
    b_Zed = pygame.image.load("big_champs_Zed.png")
    m_Ziggs_i = pygame.image.load("mini_champs_inactive_Ziggs.png")
    m_Ziggs_a = pygame.image.load("mini_champs_active_Ziggs.png")
    b_Ziggs = pygame.image.load("big_champs_Ziggs.png")
    m_Zilean_i = pygame.image.load("mini_champs_inactive_Zilean.png")
    m_Zilean_a = pygame.image.load("mini_champs_active_Zilean.png")
    b_Zilean = pygame.image.load("big_champs_Zilean.png")
    m_Zyra_i = pygame.image.load("mini_champs_inactive_Zyra.png")
    m_Zyra_a = pygame.image.load("mini_champs_active_Zyra.png")
    b_Zyra = pygame.image.load("big_champs_Zyra.png")
    m_Camille_i = pygame.image.load("mini_champs_inactive_Camille.png")
    m_Camille_a = pygame.image.load("mini_champs_active_Camille.png")
    b_Camille = pygame.image.load("big_champs_Camille.png")
    m_Ivern_i = pygame.image.load("mini_champs_inactive_Ivern.png")
    m_Ivern_a = pygame.image.load("mini_champs_active_Ivern.png")
    b_Ivern = pygame.image.load("big_champs_Ivern.png")
    b_Random = pygame.image.load("big_champs_Random.png")
    m_Random_a = pygame.image.load("mini_champs_active_Random.png")
    m_Random_i = pygame.image.load("mini_champs_inactive_Random.png")

big_champ = b_Random
img_background = img_background_summoner
champion = "Random"


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "medium"):
    textSurf,textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf,textRect)


def button(text, x, y, width, height, inactive_color, active_color, text_color = black, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                pygame.mixer.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text,text_color,x,y,width,height)



def img_button(text, x, y, width, height, img_active, img_inactive, img_choice = None, action = None, text_color = black):
    global big_champ

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        img = img_active
        gameDisplay.blit(img, (x, y))
        if click[0] == 1 and action != None:
            pygame.mixer.stop()
            button_sound = pygame.mixer.Sound("Sounds_button_switch22.wav")
            button_sound.play()
            if action == "quit":
                pygame.quit()
                pygame.mixer.quit()
                quit()
            if action == "start":
                main()
            if action == "champ_choice":
                big_champ = img_choice
            if action == "roll":
                rolled()
            if action == "rules":
                rules()
            if action == "back":
                menu()


    else:
        img = img_inactive
        gameDisplay.blit(img, (x,y))

    if text != None:
        text_to_button(text,text_color,x,y,width,height)


def img_button_champ_map(x, y, width, height, mini_i, mini_a, big, champ = None, type = "champ",):
    global img_background
    global big_champ
    global champion

    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        img = mini_a
        gameDisplay.blit(img, (x, y))
        if click[0] == 1:
            if type == "champ":
                big_champ = big
                champion = champ
            if type == "map":
                img_background = big
    else:
        img = mini_i
        gameDisplay.blit(img, (x,y))


def rules():

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(pygame.image.load("rules_wp.png"), (0, 0))

        message_to_screen("1. Pick a champion", white, -250, -230, "medium")
        message_to_screen("2. Pick a map", white, -100, -295, "medium")
        message_to_screen("3. Roll!", white, 50, -370, "medium")
        message_to_screen("4. Build your items in the given order", white, 200, 0, "medium")

        img_button(None, 10, 715, 200, 75, back_active, back_inactive, action="back")


        pygame.display.update()


def display_build(champion):
    wp = pygame.image.load("wp_champs_" + champion + ".png")

    gameDisplay.blit(image_3, (775, 375))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(wp, (0, 0))

    gameDisplay.blit(image_2, (775, 375))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(wp, (0, 0))

    gameDisplay.blit(image_1, (775, 375))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.blit(wp, (0, 0))




    champ_select_sound = pygame.mixer.Sound("sounds_champions_" + champion + ".wav")
    champ_select_sound.play()

    if img_background == img_background_summoner:
        map = "Summoner's Rift"
    elif img_background == img_background_howling:
        map = "Howling Abyss"
    elif img_background == img_background_twisted:
        map = "Twisted Treeline"

    #Summoner Spells
    sumSpellArr = ["Flash", "Ignite", "Teleport", "Ghost", "Barrier", "Cleanse", "Heal", "Smite", "Exhaust", "Mark", "Clarity"]

    if map == "Summoner's Rift":
        sumSpellArr.remove("Mark")
        sumSpellArr.remove("Clarity")

    elif map == "Twisted Treeline":
        sumSpellArr.remove("Mark")
        sumSpellArr.remove("Clarity")

    elif map == "Howling Abyss":
        sumSpellArr.remove("Teleport")
        sumSpellArr.remove("Smite")

    randnum = random.randint(0,len(sumSpellArr)-1)
    sumSpell1 = sumSpellArr[randnum]
    sumSpellArr.remove(sumSpell1)
    randnum = random.randint(0, len(sumSpellArr)-1)
    sumSpell2 = sumSpellArr[randnum]

    #Max ability
    if champion == "Udyr":
        maxArr = ["Q", "W", "E", "R"]
    else:
        maxArr = ["Q", "W", "E"]

    randnum = random.randint(0, len(maxArr)-1)
    max_spell = maxArr[randnum]


    #Keystone
    keystoneArr = ["Warlord's Bloodlust", "Fervor of Battle", "Deathfire Touch", "Stormraider's Surge",
                   "Thunderlord's Decree", "Windspeaker's Blessing", "Grasp of the Undying", "Courage of the Colossus",
                   "Bond of Stone"]

    randnum = random.randint(0, len(keystoneArr)-1)

    keystone = keystoneArr[randnum]

    itemsArr = ["Rabadon's_Deathcap","Trinity_Force","Mercurial_Scimitar","The_Bloodthirster","Essence_Reaver",
                "Infinity_Edge","Death's_Dance","Titanic_Hydra","Ravenous_Hydra","Zhonya's_Hourglass","The_Black_Cleaver",
                "Blade_Of_The_Ruined_King","Hextech_Gunblade","Maw_Of_Malmortius","Duskblade_Of_Draktharr","Luden's_Echo",
                "Liandry's_Torment","Youmuu's_Ghostblade","Rylai's_Crystal_Scepter","Lich_Bane","Frozen_Mallet","Seraph's_Embrace",
                "Nashor's_Tooth","Rod_Of_Ages","Dead_Man's_Plate","Randuin's_Omen","Banshee's_Veil","Banner_Of_Command",
                "Warmog's_Armor","Guinsoo's_Rageblade","Frozen_Heart","Wit's_End","Spirit_Visage","Athene's_Unholy_Grail",
                "Sunfire_Cape","Sterak's_Gage","Lord_Dominik's_Regards","Mortal_Reminder","Iceborn_Gauntlet","Void_Staff",
                "Righteous_Glory","Rapid_Firecannon","Statikk_Shiv","Runaan's_Hurricane","Phantom_Dancer",
                "Locket_Of_The_Iron_Solari","Morellonomicon","Muramana","Thornmail","Abyssal_Scepter","Zeke's_Harbinger",
                "Mikael's_Crucible","Hextech_Protobelt-01","Hextech_GLP-800","Ardent_Censer","Guardian_Angel",
                "Mejai's_Soulstealer","Zz'Rot_Portal","Ohmwrecker","Edge_of_Night",
                "Knight's_Vow","Lord_Van_Damm's_Pillager","Moonflair_Spellblade","Redemption","Wooglet's_Witchcap"]

    machetesArr = ["Skirmisher's_Sabre", "Stalker's_Blade", "Tracker's_Knife"]
    enchantsArr = ["Cinderhulk", "Bloodrazor", "Runic_Echoes", "Warrior"]

    bootsArr = ["Sorcerer's_Shoes", "Berserker's_Greaves", "Boots_of_Mobility", "Ionian_Boots_of_Lucidity", "Mercury's_Treads",
                "Ninja_Tabi"]

    itemSupArr = ["Eye_of_the_Equinox","Eye_of_the_Oasis",
                "Eye_of_the_Watchers","Frost_Queen's_Claim","Face_of_the_Mountain","Talisman_of_Ascension"]

    global aram
    aram = False
    global supItemTest
    supItemTest = False

    if map == "Summoner's Rift":
        itemsArr.remove("Lord_Van_Damm's_Pillager")
        itemsArr.remove("Moonflair_Spellblade")
        itemsArr.remove("Wooglet's_Witchcap")

        randSup = random.randint(1,len(itemsArr))
        if randSup < 7:
                supItemTest = True

    elif map == "Twisted Treeline":
        itemSupArr.remove("Eye_of_the_Equinox")
        itemSupArr.remove("Eye_of_the_Oasis")
        itemSupArr.remove("Eye_of_the_Watchers")
        itemsArr.remove("Ohmwrecker")
        itemsArr.remove("Zz'Rot_Portal")
        itemsArr.remove("Mejai's_Soulstealer")
        machetesArr.remove("Tracker's_Knife")

        randSup = random.randint(1, len(itemsArr))
        if randSup < 4:
            supItemTest = True

    elif map == "Howling Abyss":
        itemSupArr.remove("Eye_of_the_Equinox")
        itemSupArr.remove("Eye_of_the_Oasis")
        itemSupArr.remove("Eye_of_the_Watchers")
        itemsArr.remove("Ohmwrecker")
        itemsArr.remove("Zz'Rot_Portal")
        itemsArr.remove("Guardian_Angel")
        itemsArr.remove("Lord_Van_Damm's_Pillager")
        itemsArr.remove("Moonflair_Spellblade")
        itemsArr.remove("Wooglet's_Witchcap")
        itemsArr.remove("Mejai's_Soulstealer")

        randSup = random.randint(1, len(itemsArr))
        if randSup < 4:
            supItemTest = True

        aram = True

    if champion in {"Aatrox" ,"Akali" ,"Alistar" ,"Amumu" ,"Blitzcrank" ,"Braum" ,"Camille" ,"Chogath" ,"Darius" ,"Diana" ,"DrMundo" ,"Ekko" ,"Evelynn" ,"Fiora" ,"Fizz" ,"Galio" ,"Gangplank" ,"Garen" ,"Gragas" ,"Hecarim" ,"Illaoi" ,"Irelia" ,"JarvanIV" ,"Jax" ,"Kassadin" ,"Katarina" ,"Khazix" ,"Kled" ,"LeeSin" ,"Leona" ,"Malphite" ,"Maokai" ,"MasterYi" ,"Mordekaiser" ,"Nasus" ,"Nautilus" ,"Nocturne" ,"Nunu" ,"Olaf" ,"Pantheon" ,"Poppy" ,"Rammus" ,"RekSai" ,"Renekton" ,"Rengar" ,"Riven" ,"Rumble" ,"Sejuani" ,"Shaco" ,"Shen" ,"Shyvana" ,"Singed" ,"Sion" ,"Skarner" ,"TahmKench" ,"Talon" ,"Taric" ,"Trundle" ,"Tryndamere" ,"Udyr" ,"Vi" ,"Volibear" ,"Warwick" ,"Wukong" ,"XinZhao" ,"Yasuo" ,"Yorick" ,"Zac" ,"Zed"}:
        itemsArr.remove("Runaan's_Hurricane")
    elif champion in {"Ahri" ,"Anivia" ,"Annie" ,"Ashe" ,"AurelionSol" ,"Azir" ,"Bard" ,"Brand" ,"Caitlyn" ,"Corki" ,"Draven" ,"Ezreal" ,"FiddleSticks" ,"Graves" ,"Heimerdinger" ,"Janna" ,"Jhin" ,"Jinx" ,"Kalista" ,"Karma" ,"Karthus" ,"Kennen" ,"Kindred" ,"KogMaw" ,"Leblanc" ,"Lissandra" ,"Lucian" ,"Lulu" ,"Lux" ,"Malzahar" ,"MissFortune" ,"Morgana" ,"Nami" ,"Orianna" ,"Quinn" ,"Ryze" ,"Sivir" ,"Sona" ,"Soraka" ,"Swain" ,"Syndra" ,"Taliyah" ,"Teemo" ,"Thresh" ,"Tristana" ,"TwistedFate" ,"Twitch" ,"Urgot" ,"Varus" ,"Vayne" ,"Veigar" ,"VelKoz" ,"Vladimir" ,"Xerath" ,"Ziggs" ,"Zilean" ,"Zyra"}:
        itemsArr.remove("Ravenous_Hydra")
        itemsArr.remove("Titanic_Hydra")

    buildArr = []


    for i in range(6):
        randnum = random.randint(0, len(itemsArr)-1)
        appendItem = itemsArr[randnum]


        buildArr.append(appendItem)

    randnum = random.randint(0, len(enchantsArr) - 1)
    enchant = enchantsArr[randnum]
    randnum = random.randint(0, len(machetesArr)-1)
    mach = machetesArr[randnum]

    machete = mach + "_(" + enchant + ")"

    randnum = random.randint(0, len(bootsArr)-1)
    boots = bootsArr[randnum]

    randnum = random.randint(0, len(itemSupArr)-1)
    supItem = itemSupArr[randnum]

    if champion == "Cassiopeia":
        if sumSpell1 == "Smite" or sumSpell2 == "Smite":
            buildArr[0] = machete
            if supItemTest:
                randNumSup = random.randint(1, 5)
                buildArr[randNumSup] = supItem

                supItemTest = False
        if supItemTest:
            randNumSup = random.randint(0, 5)
            buildArr[randNumSup] = supItem
    elif champion == "Viktor":
        buildArr[0] = boots
        buildArr[1] = "Perfect_Hex_Core"
        if sumSpell1 == "Smite" or sumSpell2 == "Smite":
            buildArr[2] = machete
            if supItemTest:
                randNumSup = random.randint(3, 5)
                buildArr[randNumSup] = supItem
                supItemTest = False
        if supItemTest:
            randNumSup = random.randint(2, 5)
            buildArr[randNumSup] = supItem
    else:
        buildArr[0] = boots
        if sumSpell1 == "Smite" or sumSpell2 == "Smite":
            buildArr[1] = machete
            if supItemTest:
                randNumSup = random.randint(2,5)
                buildArr[randNumSup] = supItem
                supItemTest = False
        if supItemTest:
            randNumSup = random.randint(1, 5)
            buildArr[randNumSup] = supItem

    #ITEMS



    x_max_spell = 1490
    y_max_spell = 690

    gameDisplay.blit(pygame.image.load("abilities_" + max_spell + "_" + champion + ".png"), (x_max_spell,y_max_spell))
    gameDisplay.blit(pygame.image.load(max_spell + ".png"), (x_max_spell, y_max_spell))

    gameDisplay.blit(pygame.image.load(sumSpell1 + ".png"), (10, 580))
    gameDisplay.blit(pygame.image.load(sumSpell2 + ".png"), (10, 690))

    gameDisplay.blit(pygame.image.load(buildArr[0] + ".png"), (120, 580))
    gameDisplay.blit(pygame.image.load("1.png"), (110,580))
    gameDisplay.blit(pygame.image.load(buildArr[1] + ".png"), (350, 580))
    gameDisplay.blit(pygame.image.load("2.png"), (340, 580))
    gameDisplay.blit(pygame.image.load(buildArr[2] + ".png"), (580, 580))
    gameDisplay.blit(pygame.image.load("3.png"), (570, 580))
    gameDisplay.blit(pygame.image.load(buildArr[3] + ".png"), (810, 580))
    gameDisplay.blit(pygame.image.load("4.png"), (805, 580))
    gameDisplay.blit(pygame.image.load(buildArr[4] + ".png"), (1040, 580))
    gameDisplay.blit(pygame.image.load("5.png"), (1030, 580))
    gameDisplay.blit(pygame.image.load(buildArr[5] + ".png"), (1270, 580))
    gameDisplay.blit(pygame.image.load("6.png"), (1260, 580))

    gameDisplay.blit(pygame.image.load(keystone + ".png"), (1490,580))




    pygame.display.update()



def menu():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(img_background_start, (0, 0))
        gameDisplay.blit(img_title, (0, 0))


        img_button (None,
                    display_width - 450,
                    display_height - 100,
                    200,
                    75,
                    img_rules_active,
                    img_rules_inactive,
                    action = "rules")
        img_button(None,
                    display_width-225,
                    display_height-100,
                    200, 75,
                    img_quit_active,
                    img_quit_inactive,
                    action="quit")
        img_button(None,
                   display_width/2 - 200,
                   display_height/2 - 75,
                   400,
                   150,
                   img_playnow_active,
                   img_playnow_inactive,
                   None,
                   action="start")

        pygame.display.update()
        clock.tick(30)

def main():
    global champion
    champion = "Random"


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.blit(img_background, (0, 0))
        if champion == "Random":
            gameDisplay.blit(b_Random, (950, 525))
        else:
            gameDisplay.blit(big_champ, (950, 525))

        for i in range(1):
            img_button_champ_map(1350, 300, 200, 200, img_howling_abyss_inactive, img_howling_abyss_active,
                                 img_background_howling, type="map")
            img_button_champ_map(1350, 50, 200, 200, img_summoner_inactive, img_summoner_active,
                                 img_background_summoner, type="map")
            img_button_champ_map(1350, 550, 200, 200, img_twisted_inactive, img_twisted_active,
                                 img_background_twisted, type="map")
            img_button_champ_map(10, 10, 50, 50, m_Aatrox_i, m_Aatrox_a, b_Aatrox, 'Aatrox')
            img_button_champ_map(70, 10, 50, 50, m_Ahri_i, m_Ahri_a, b_Ahri, 'Ahri')
            img_button_champ_map(130, 10, 50, 50, m_Akali_i, m_Akali_a, b_Akali, 'Akali')
            img_button_champ_map(190, 10, 50, 50, m_Alistar_i, m_Alistar_a, b_Alistar, 'Alistar')
            img_button_champ_map(250, 10, 50, 50, m_Amumu_i, m_Amumu_a, b_Amumu, 'Amumu')
            img_button_champ_map(310, 10, 50, 50, m_Anivia_i, m_Anivia_a, b_Anivia, 'Anivia')
            img_button_champ_map(370, 10, 50, 50, m_Annie_i, m_Annie_a, b_Annie, 'Annie')
            img_button_champ_map(430, 10, 50, 50, m_Ashe_i, m_Ashe_a, b_Ashe, 'Ashe')
            img_button_champ_map(490, 10, 50, 50, m_AurelionSol_i, m_AurelionSol_a, b_AurelionSol, 'AurelionSol')
            img_button_champ_map(550, 10, 50, 50, m_Azir_i, m_Azir_a, b_Azir, 'Azir')
            img_button_champ_map(610, 10, 50, 50, m_Bard_i, m_Bard_a, b_Bard, 'Bard')
            img_button_champ_map(670, 10, 50, 50, m_Blitzcrank_i, m_Blitzcrank_a, b_Blitzcrank, 'Blitzcrank')
            img_button_champ_map(730, 10, 50, 50, m_Brand_i, m_Brand_a, b_Brand, 'Brand')
            img_button_champ_map(10, 70, 50, 50, m_Braum_i, m_Braum_a, b_Braum, 'Braum')
            img_button_champ_map(70, 70, 50, 50, m_Caitlyn_i, m_Caitlyn_a, b_Caitlyn, 'Caitlyn')
            img_button_champ_map(130, 70, 50, 50, m_Cassiopeia_i, m_Cassiopeia_a, b_Cassiopeia, 'Cassiopeia')
            img_button_champ_map(190, 70, 50, 50, m_Chogath_i, m_Chogath_a, b_Chogath, 'Chogath')
            img_button_champ_map(250, 70, 50, 50, m_Corki_i, m_Corki_a, b_Corki, 'Corki')
            img_button_champ_map(310, 70, 50, 50, m_Darius_i, m_Darius_a, b_Darius, 'Darius')
            img_button_champ_map(370, 70, 50, 50, m_Diana_i, m_Diana_a, b_Diana, 'Diana')
            img_button_champ_map(430, 70, 50, 50, m_DrMundo_i, m_DrMundo_a, b_DrMundo, 'DrMundo')
            img_button_champ_map(490, 70, 50, 50, m_Draven_i, m_Draven_a, b_Draven, 'Draven')
            img_button_champ_map(550, 70, 50, 50, m_Ekko_i, m_Ekko_a, b_Ekko, 'Ekko')
            img_button_champ_map(610, 70, 50, 50, m_Elise_i, m_Elise_a, b_Elise, 'Elise')
            img_button_champ_map(670, 70, 50, 50, m_Evelynn_i, m_Evelynn_a, b_Evelynn, 'Evelynn')
            img_button_champ_map(730, 70, 50, 50, m_Ezreal_i, m_Ezreal_a, b_Ezreal, 'Ezreal')
            img_button_champ_map(10, 130, 50, 50, m_FiddleSticks_i, m_FiddleSticks_a, b_FiddleSticks, 'FiddleSticks')
            img_button_champ_map(70, 130, 50, 50, m_Fiora_i, m_Fiora_a, b_Fiora, 'Fiora')
            img_button_champ_map(130, 130, 50, 50, m_Fizz_i, m_Fizz_a, b_Fizz, 'Fizz')
            img_button_champ_map(190, 130, 50, 50, m_Galio_i, m_Galio_a, b_Galio, 'Galio')
            img_button_champ_map(250, 130, 50, 50, m_Gangplank_i, m_Gangplank_a, b_Gangplank, 'Gangplank')
            img_button_champ_map(310, 130, 50, 50, m_Garen_i, m_Garen_a, b_Garen, 'Garen')
            img_button_champ_map(370, 130, 50, 50, m_Gnar_i, m_Gnar_a, b_Gnar, 'Gnar')
            img_button_champ_map(430, 130, 50, 50, m_Gragas_i, m_Gragas_a, b_Gragas, 'Gragas')
            img_button_champ_map(490, 130, 50, 50, m_Graves_i, m_Graves_a, b_Graves, 'Graves')
            img_button_champ_map(550, 130, 50, 50, m_Hecarim_i, m_Hecarim_a, b_Hecarim, 'Hecarim')
            img_button_champ_map(610, 130, 50, 50, m_Heimerdinger_i, m_Heimerdinger_a, b_Heimerdinger, 'Heimerdinger')
            img_button_champ_map(670, 130, 50, 50, m_Illaoi_i, m_Illaoi_a, b_Illaoi, 'Illaoi')
            img_button_champ_map(730, 130, 50, 50, m_Irelia_i, m_Irelia_a, b_Irelia, 'Irelia')
            img_button_champ_map(10, 190, 50, 50, m_Janna_i, m_Janna_a, b_Janna, 'Janna')
            img_button_champ_map(70, 190, 50, 50, m_JarvanIV_i, m_JarvanIV_a, b_JarvanIV, 'JarvanIV')
            img_button_champ_map(130, 190, 50, 50, m_Jax_i, m_Jax_a, b_Jax, 'Jax')
            img_button_champ_map(190, 190, 50, 50, m_Jayce_i, m_Jayce_a, b_Jayce, 'Jayce')
            img_button_champ_map(250, 190, 50, 50, m_Jhin_i, m_Jhin_a, b_Jhin, 'Jhin')
            img_button_champ_map(310, 190, 50, 50, m_Jinx_i, m_Jinx_a, b_Jinx, 'Jinx')
            img_button_champ_map(370, 190, 50, 50, m_Kalista_i, m_Kalista_a, b_Kalista, 'Kalista')
            img_button_champ_map(430, 190, 50, 50, m_Karma_i, m_Karma_a, b_Karma, 'Karma')
            img_button_champ_map(490, 190, 50, 50, m_Karthus_i, m_Karthus_a, b_Karthus, 'Karthus')
            img_button_champ_map(550, 190, 50, 50, m_Kassadin_i, m_Kassadin_a, b_Kassadin, 'Kassadin')
            img_button_champ_map(610, 190, 50, 50, m_Katarina_i, m_Katarina_a, b_Katarina, 'Katarina')
            img_button_champ_map(670, 190, 50, 50, m_Kayle_i, m_Kayle_a, b_Kayle, 'Kayle')
            img_button_champ_map(730, 190, 50, 50, m_Kennen_i, m_Kennen_a, b_Kennen, 'Kennen')
            img_button_champ_map(10, 250, 50, 50, m_Khazix_i, m_Khazix_a, b_Khazix, 'Khazix')
            img_button_champ_map(70, 250, 50, 50, m_Kindred_i, m_Kindred_a, b_Kindred, 'Kindred')
            img_button_champ_map(130, 250, 50, 50, m_Kled_i, m_Kled_a, b_Kled, 'Kled')
            img_button_champ_map(190, 250, 50, 50, m_KogMaw_i, m_KogMaw_a, b_KogMaw, 'KogMaw')
            img_button_champ_map(250, 250, 50, 50, m_Leblanc_i, m_Leblanc_a, b_Leblanc, 'Leblanc')
            img_button_champ_map(310, 250, 50, 50, m_LeeSin_i, m_LeeSin_a, b_LeeSin, 'LeeSin')
            img_button_champ_map(370, 250, 50, 50, m_Leona_i, m_Leona_a, b_Leona, 'Leona')
            img_button_champ_map(430, 250, 50, 50, m_Lissandra_i, m_Lissandra_a, b_Lissandra, 'Lissandra')
            img_button_champ_map(490, 250, 50, 50, m_Lucian_i, m_Lucian_a, b_Lucian, 'Lucian')
            img_button_champ_map(550, 250, 50, 50, m_Lulu_i, m_Lulu_a, b_Lulu, 'Lulu')
            img_button_champ_map(610, 250, 50, 50, m_Lux_i, m_Lux_a, b_Lux, 'Lux')
            img_button_champ_map(670, 250, 50, 50, m_Malphite_i, m_Malphite_a, b_Malphite, 'Malphite')
            img_button_champ_map(730, 250, 50, 50, m_Malzahar_i, m_Malzahar_a, b_Malzahar, 'Malzahar')
            img_button_champ_map(10, 310, 50, 50, m_Maokai_i, m_Maokai_a, b_Maokai, 'Maokai')
            img_button_champ_map(70, 310, 50, 50, m_MasterYi_i, m_MasterYi_a, b_MasterYi, 'MasterYi')
            img_button_champ_map(130, 310, 50, 50, m_MissFortune_i, m_MissFortune_a, b_MissFortune, 'MissFortune')
            img_button_champ_map(190, 310, 50, 50, m_Mordekaiser_i, m_Mordekaiser_a, b_Mordekaiser, 'Mordekaiser')
            img_button_champ_map(250, 310, 50, 50, m_Morgana_i, m_Morgana_a, b_Morgana, 'Morgana')
            img_button_champ_map(310, 310, 50, 50, m_Nami_i, m_Nami_a, b_Nami, 'Nami')
            img_button_champ_map(370, 310, 50, 50, m_Nasus_i, m_Nasus_a, b_Nasus, 'Nasus')
            img_button_champ_map(430, 310, 50, 50, m_Nautilus_i, m_Nautilus_a, b_Nautilus, 'Nautilus')
            img_button_champ_map(490, 310, 50, 50, m_Nidalee_i, m_Nidalee_a, b_Nidalee, 'Nidalee')
            img_button_champ_map(550, 310, 50, 50, m_Nocturne_i, m_Nocturne_a, b_Nocturne, 'Nocturne')
            img_button_champ_map(610, 310, 50, 50, m_Nunu_i, m_Nunu_a, b_Nunu, 'Nunu')
            img_button_champ_map(670, 310, 50, 50, m_Olaf_i, m_Olaf_a, b_Olaf, 'Olaf')
            img_button_champ_map(730, 310, 50, 50, m_Orianna_i, m_Orianna_a, b_Orianna, 'Orianna')
            img_button_champ_map(10, 370, 50, 50, m_Pantheon_i, m_Pantheon_a, b_Pantheon, 'Pantheon')
            img_button_champ_map(70, 370, 50, 50, m_Poppy_i, m_Poppy_a, b_Poppy, 'Poppy')
            img_button_champ_map(130, 370, 50, 50, m_Quinn_i, m_Quinn_a, b_Quinn, 'Quinn')
            img_button_champ_map(190, 370, 50, 50, m_Rammus_i, m_Rammus_a, b_Rammus, 'Rammus')
            img_button_champ_map(250, 370, 50, 50, m_RekSai_i, m_RekSai_a, b_RekSai, 'RekSai')
            img_button_champ_map(310, 370, 50, 50, m_Renekton_i, m_Renekton_a, b_Renekton, 'Renekton')
            img_button_champ_map(370, 370, 50, 50, m_Rengar_i, m_Rengar_a, b_Rengar, 'Rengar')
            img_button_champ_map(430, 370, 50, 50, m_Riven_i, m_Riven_a, b_Riven, 'Riven')
            img_button_champ_map(490, 370, 50, 50, m_Rumble_i, m_Rumble_a, b_Rumble, 'Rumble')
            img_button_champ_map(550, 370, 50, 50, m_Ryze_i, m_Ryze_a, b_Ryze, 'Ryze')
            img_button_champ_map(610, 370, 50, 50, m_Sejuani_i, m_Sejuani_a, b_Sejuani, 'Sejuani')
            img_button_champ_map(670, 370, 50, 50, m_Shaco_i, m_Shaco_a, b_Shaco, 'Shaco')
            img_button_champ_map(730, 370, 50, 50, m_Shen_i, m_Shen_a, b_Shen, 'Shen')
            img_button_champ_map(10, 430, 50, 50, m_Shyvana_i, m_Shyvana_a, b_Shyvana, 'Shyvana')
            img_button_champ_map(70, 430, 50, 50, m_Singed_i, m_Singed_a, b_Singed, 'Singed')
            img_button_champ_map(130, 430, 50, 50, m_Sion_i, m_Sion_a, b_Sion, 'Sion')
            img_button_champ_map(190, 430, 50, 50, m_Sivir_i, m_Sivir_a, b_Sivir, 'Sivir')
            img_button_champ_map(250, 430, 50, 50, m_Skarner_i, m_Skarner_a, b_Skarner, 'Skarner')
            img_button_champ_map(310, 430, 50, 50, m_Sona_i, m_Sona_a, b_Sona, 'Sona')
            img_button_champ_map(370, 430, 50, 50, m_Soraka_i, m_Soraka_a, b_Soraka, 'Soraka')
            img_button_champ_map(430, 430, 50, 50, m_Swain_i, m_Swain_a, b_Swain, 'Swain')
            img_button_champ_map(490, 430, 50, 50, m_Syndra_i, m_Syndra_a, b_Syndra, 'Syndra')
            img_button_champ_map(550, 430, 50, 50, m_TahmKench_i, m_TahmKench_a, b_TahmKench, 'TahmKench')
            img_button_champ_map(610, 430, 50, 50, m_Taliyah_i, m_Taliyah_a, b_Taliyah, 'Taliyah')
            img_button_champ_map(670, 430, 50, 50, m_Talon_i, m_Talon_a, b_Talon, 'Talon')
            img_button_champ_map(730, 430, 50, 50, m_Taric_i, m_Taric_a, b_Taric, 'Taric')
            img_button_champ_map(10, 490, 50, 50, m_Teemo_i, m_Teemo_a, b_Teemo, 'Teemo')
            img_button_champ_map(70, 490, 50, 50, m_Thresh_i, m_Thresh_a, b_Thresh, 'Thresh')
            img_button_champ_map(130, 490, 50, 50, m_Tristana_i, m_Tristana_a, b_Tristana, 'Tristana')
            img_button_champ_map(190, 490, 50, 50, m_Trundle_i, m_Trundle_a, b_Trundle, 'Trundle')
            img_button_champ_map(250, 490, 50, 50, m_Tryndamere_i, m_Tryndamere_a, b_Tryndamere, 'Tryndamere')
            img_button_champ_map(310, 490, 50, 50, m_TwistedFate_i, m_TwistedFate_a, b_TwistedFate, 'TwistedFate')
            img_button_champ_map(370, 490, 50, 50, m_Twitch_i, m_Twitch_a, b_Twitch, 'Twitch')
            img_button_champ_map(430, 490, 50, 50, m_Udyr_i, m_Udyr_a, b_Udyr, 'Udyr')
            img_button_champ_map(490, 490, 50, 50, m_Urgot_i, m_Urgot_a, b_Urgot, 'Urgot')
            img_button_champ_map(550, 490, 50, 50, m_Varus_i, m_Varus_a, b_Varus, 'Varus')
            img_button_champ_map(610, 490, 50, 50, m_Vayne_i, m_Vayne_a, b_Vayne, 'Vayne')
            img_button_champ_map(670, 490, 50, 50, m_Veigar_i, m_Veigar_a, b_Veigar, 'Veigar')
            img_button_champ_map(730, 490, 50, 50, m_Velkoz_i, m_Velkoz_a, b_Velkoz, 'Velkoz')
            img_button_champ_map(10, 550, 50, 50, m_Vi_i, m_Vi_a, b_Vi, 'Vi')
            img_button_champ_map(70, 550, 50, 50, m_Viktor_i, m_Viktor_a, b_Viktor, 'Viktor')
            img_button_champ_map(130, 550, 50, 50, m_Vladimir_i, m_Vladimir_a, b_Vladimir, 'Vladimir')
            img_button_champ_map(190, 550, 50, 50, m_Volibear_i, m_Volibear_a, b_Volibear, 'Volibear')
            img_button_champ_map(250, 550, 50, 50, m_Warwick_i, m_Warwick_a, b_Warwick, 'Warwick')
            img_button_champ_map(310, 550, 50, 50, m_Wukong_i, m_Wukong_a, b_Wukong, 'Wukong')
            img_button_champ_map(370, 550, 50, 50, m_Xerath_i, m_Xerath_a, b_Xerath, 'Xerath')
            img_button_champ_map(430, 550, 50, 50, m_XinZhao_i, m_XinZhao_a, b_XinZhao, 'XinZhao')
            img_button_champ_map(490, 550, 50, 50, m_Yasuo_i, m_Yasuo_a, b_Yasuo, 'Yasuo')
            img_button_champ_map(550, 550, 50, 50, m_Yorick_i, m_Yorick_a, b_Yorick, 'Yorick')
            img_button_champ_map(610, 550, 50, 50, m_Zac_i, m_Zac_a, b_Zac, 'Zac')
            img_button_champ_map(670, 550, 50, 50, m_Zed_i, m_Zed_a, b_Zed, 'Zed')
            img_button_champ_map(730, 550, 50, 50, m_Ziggs_i, m_Ziggs_a, b_Ziggs, 'Ziggs')
            img_button_champ_map(10, 610, 50, 50, m_Zilean_i, m_Zilean_a, b_Zilean, 'Zilean')
            img_button_champ_map(70, 610, 50, 50, m_Zyra_i, m_Zyra_a, b_Zyra, 'Zyra')
            img_button_champ_map(130, 610, 50, 50, m_Camille_i, m_Camille_a, b_Camille, 'Camille')
            img_button_champ_map(190, 610, 50, 50, m_Ivern_i, m_Ivern_a, b_Ivern, 'Ivern')
            img_button_champ_map(250, 610, 50, 50, m_Random_i, m_Random_a, b_Random, 'Random')

        img_button(None, 400, 650, 350, 100, letsgo_active, letsgo_inactive, action="roll")
        img_button(None, 10, 715, 200, 75, back_active, back_inactive, action="back")

        pygame.display.update()

        clock.tick(30)

def rolled():
    global champion
    time.sleep(0.5)

    if champion == "Random":
        champArr = ["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AurelionSol",
                    "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Cassiopeia", "Chogath",
                    "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko",
                    "Elise", "Evelynn", "Ezreal", "FiddleSticks", "Fiora", "Fizz", "Galio", "Gangplank",
                    "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Irelia",
                    "Janna", "JarvanIV", "Jax", "Jayce", "Jhin",
                    "Jinx", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen",
                    "Khazix", "Kindred", "Kled", "KogMaw", "Leblanc", "LeeSin", "Leona", "Lissandra",
                    "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai",
                    "MasterYi", "MissFortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
                    "Nidalee", "Nocturne", "Nunu", "Olaf", "Orianna", "Pantheon", "Poppy", "Quinn",
                    "Rammus", "RekSai", "Renekton", "Rengar", "Riven",
                    "Rumble", "Ryze", "Sejuani", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir",
                    "Skarner", "Sona", "Soraka", "Swain", "Syndra", "TahmKench", "Taliyah", "Talon",
                    "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
                    "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vi",
                    "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xerath", "XinZhao",
                    "Yasuo", "Yorick", "Zac", "Zed", "Ziggs", "Zilean", "Zyra", "Camille", "Ivern"]
        randnum = random.randint(0, len(champArr)-1)
        champion = champArr[randnum]

    wp = pygame.image.load("wp_champs_" + champion + ".png")

    loop = True

    gameDisplay.blit(wp, (0, 0))

    display_build(champion)

    while loop:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        img_button(None, 1406, 10, 77, 42, button_reroll_active, button_reroll_inactive, action="roll")
        img_button(None, 1493, 10, 97, 42, settings_active, settings_inactive, action="start")


        pygame.display.update()
        clock.tick(15)


menu()
