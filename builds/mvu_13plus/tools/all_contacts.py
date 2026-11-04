"""Все контактные листы вводного урока 13+ → builds/mvu_13plus/preview/."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from contact import sheet
P = 'builds/mvu_13plus/preview'
sheet(['family_photo','schoolbag','passport','fruit_bowl','football','bus','cinema_tickets','umbrella','cat'], P+'/kl_p1.png')
sheet(['wardrobe','suitcase','map','first_aid_kit','novel','wanted_poster','wallet','laptop','binoculars'], P+'/kl_p2.png')
sheet(['trophy','stethoscope','microphone','smartphone','graduation_cap','seismograph','magnifying_glass','scroll','time_capsule','billboard'], P+'/kl_p3.png', cols=5, cell=260)
sheet(['fam_grandfather','fam_grandmother','fam_father','fam_mother','fam_aunt','fam_uncle','fam_boy','fam_girl'], P+'/kl_family.png', cols=4, cell=260)
sheet(['athlete','sport_swim','sport_tennis','sport_bike','w_sunny','w_rainy','w_snowy','w_windy','w_cloudy'], P+'/kl_sport_pogoda.png')
sheet(['cl_coat','cl_shorts','cl_scarf','cl_sandals','cl_swimsuit','cl_boots','cl_hat','cl_gloves','cl_sunglasses'], P+'/kl_clothes.png')
sheet(['an_cat','an_horse','an_cow','an_sheep','an_rabbit','an_dog','an_hamster','an_pig','an_chicken'], P+'/kl_animals.png')
sheet(['hol_airport','hol_castle','hol_beach','suspect_1','suspect_2','suspect_3','suspect_4'], P+'/kl_holiday_suspects.png', cols=4, cell=300)
sheet(['geo_river','geo_mountains','geo_desert','geo_waterfall','geo_island','geo_forest','tr_sightseeing','tr_camping','tr_ferry'], P+'/kl_travel.png')
sheet(['food_spicy','food_crunchy','food_sour','food_sweet','food_bitter','food_salty','dis_volcano','dis_flood','dis_earthquake','dis_wildfire','dis_hurricane','dis_tsunami'], P+'/kl_food_disasters.png', cols=6, cell=230)
