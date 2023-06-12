import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from filed.models import File, FileType


data = [
 {
  "file_date_added": "19\/05\/2023",
  "headline": "JOSE ALCIDES MORALES MORALES",
  "file_name": "287",
  "file_type": "LICENCIA DE SUBDIVISÓN",
  "passport": "3.595.622",
  "phone_number": 3135805856,
  "email": ""
 },
 {
  "file_date_added": "19\/05\/2023",
  "headline": "LUZ DARY JARAMILLO CASTAÑO ",
  "file_name": "288",
  "file_type": "L DE CONDOMINIO Y MOVIMIENTO DE TIERRA ",
  "passport": "1.041.326.487",
  "phone_number": 3205668303,
  "email": "danysanchez0208@hotmail.com"
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "JOAQUIN ALFREDO ZAPATA MARIN ",
  "file_name": "289",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA ",
  "passport": "15.427.264",
  "phone_number": 3117185446,
  "email": " Yesica5456@hotmail.com"
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "HECTOR IVAN ZAPATA MARIN ",
  "file_name": "290",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA ",
  "passport": "15.430.002",
  "phone_number": 3117185446,
  "email": "Yesica5446@hotmail.com "
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "LAURA VANESA OSPINA ZAPATA ",
  "file_name": "291",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA ",
  "passport": "1.036.930.706",
  "phone_number": 3117185446,
  "email": "Yesica5446@hotmail.com "
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "ANA ISABEL ZAPATA MARIN",
  "file_name": "292",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA ",
  "passport": "39.431.952",
  "phone_number": 3117185446,
  "email": "Yesica5446@hotmail.com "
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "SAMUEL DE JESUS ZAPATA MARIN ",
  "file_name": "293",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA ",
  "passport": "15.431.665",
  "phone_number": 3117185446,
  "email": "Yesica5446@hotmail.com "
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "MAURICIO HERNAN ZAPATA MARIN ",
  "file_name": "294",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA ",
  "passport": "15.437.661",
  "phone_number": 3117185446,
  "email": "Yesica5446@hotmail.com "
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "MARIA PATRICIA MERIZAL DE LONDOÑO ",
  "file_name": "295",
  "file_type": "LECENCIA DE SUBDIVICION ",
  "passport": "32.515.596",
  "phone_number": 3193892834,
  "email": "catalinaecheverrimerizalde@gmail.com "
 },
 {
  "file_date_added": "20\/05\/2023",
  "headline": "VICTOR MANUEL SANCHEZ FRANCO ",
  "file_name": "296",
  "file_type": "LICENCIA DE SUBDIVICION ",
  "passport": "70.287.610",
  "phone_number": 3117286790,
  "email": " "
 },
 {
  "file_date_added": "23\/05\/2023",
  "headline": "ALBA BELEN DIAZ RINCON ",
  "file_name": "297",
  "file_type": "LICENCIA CONSTRUCCION ",
  "passport": "42.877.898",
  "phone_number": 3007356763,
  "email": "albabediaz@gmail.com"
 },
 {
  "file_date_added": "23\/05\/2023",
  "headline": "JOSE MAURICIO LOIZA HINCAPIE ",
  "file_name": "298",
  "file_type": "LICENCIA DE CONSTRUCCION ",
  "passport": "71.220.572",
  "phone_number": 3116555553,
  "email": "nata.herrera@hotmail.com"
 },
 {
  "file_date_added": "23\/05\/2023",
  "headline": "HERNAN ALONSO GIRALDO ARBELAEZ ",
  "file_name": "299",
  "file_type": "LICENCIA DE PORROGA SPO-415 DEL 16 DE JULIO DEL 2021",
  "passport": "13.838.191",
  "phone_number": 3122536927,
  "email": "oscarfer9924@gmail.com"
 },
 {
  "file_date_added": "23\/05\/2023",
  "headline": "ALEJANDRINO VERGARA GALLEGO ",
  "file_name": "300",
  "file_type": "LICENCIA DE CONSTRUCION ",
  "passport": "70.288.555",
  "phone_number": 3122536927,
  "email": "oscarfer9924@gmail.com"
 },
 {
  "file_date_added": "23\/05\/2023",
  "headline": "RAMON ANTONIO GIRALDO ARBELAEZ ",
  "file_name": "301",
  "file_type": "LICENCIA DE SUBDIVICION ",
  "passport": "70.043.937",
  "phone_number": 3205068303,
  "email": "danysanchez0208@hotmail.com"
 },
 {
  "file_date_added": "23\/05\/2023",
  "headline": "YENNY ASTRID SANTAMARIA OSPINA ",
  "file_name": "302",
  "file_type": "LICENCIA DE CONSTRUCCION ",
  "passport": "43.454.069",
  "phone_number": 3136006593,
  "email": " "
 },
 {
  "file_date_added": "24\/05\/2023",
  "headline": "LEON DARIO GIL GSRCIA ",
  "file_name": "303",
  "file_type": " LICENCIA DE CONSTRUCCION ",
  "passport": "15.426.120",
  "phone_number": 3002550183,
  "email": "1004darioramirez@gmail.com"
 },
 {
  "file_date_added": "24\/05\/2023",
  "headline": "MAURICIO ARLES BUITRAGO ZAPATA ",
  "file_name": "304",
  "file_type": "LICENCIA DE CONSTRUCCION ",
  "passport": "89.000.925",
  "phone_number": 3206361126,
  "email": ""
 },
 {
  "file_date_added": "24\/05\/2023",
  "headline": "CORNELIO DE JESUS CARDONA GALLO",
  "file_name": "305",
  "file_type": "LICENCIA DE CONSTRUCCION ",
  "passport": "70.287.669",
  "phone_number": 3116555553,
  "email": "nata.herrera@hotmail.com"
 },
 {
  "file_date_added": "24\/05\/2023",
  "headline": "LUZ MARY ORREGO ALZATE ",
  "file_name": "306",
  "file_type": "LECENCIA DE ESTRATIFICACION ",
  "passport": "43.420.763",
  "phone_number": 3104141393,
  "email": ""
 },
 {
  "file_date_added": "24\/05\/2023",
  "headline": "LUZ MARGARITA MARIN DE ZAPATA ",
  "file_name": "307",
  "file_type": "LICENCIA DE AMPLIACION Y R.P.H",
  "passport": "39.430.071",
  "phone_number": 3205068303,
  "email": "danysanchez0208@hotmail.com"
 },
 {
  "file_date_added": "24\/05\/2023",
  "headline": "LILIANA MARLENY YARA SANTA",
  "file_name": "308",
  "file_type": "LICENCIA DE AMPLIACION ",
  "passport": "43.421.940",
  "phone_number": 3155172720,
  "email": "lilitoya78@hotmail.com"
 },
 {
  "file_date_added": "25\/05\/2023",
  "headline": "LETICIA EUGENIA ARIAS GALLEGO",
  "file_name": "309",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACION ",
  "passport": "43.420.032",
  "phone_number": 3122068417,
  "email": "J.CGA9004@hotmail.com"
 },
 {
  "file_date_added": "25\/05\/2023",
  "headline": "LUZ FABIOLA MUÑOZ VALENCIA ",
  "file_name": "310",
  "file_type": "LICENCIA DE CONSTRUCCION ",
  "passport": "22.051.426",
  "phone_number": 3128335744,
  "email": "lufamura@gmail.com"
 },
 {
  "file_date_added": "25\/05\/2023",
  "headline": "JUVENAL MARÍN FLOREZ",
  "file_name": "311",
  "file_type": "LICENCIA DE SUBDIVISIÓN",
  "passport": 3435049,
  "phone_number": 3205668303,
  "email": "DANYSANCHEZ0208@GMAIL.COM"
 },
 {
  "file_date_added": "26\/05\/2023",
  "headline": "MARIA DEL SOCORRO MUÑOZ DE OCHOA",
  "file_name": "312",
  "file_type": "ESTRATIFICACIÓN",
  "passport": 22052252,
  "phone_number": 3184095767
 },
 {
  "file_date_added": "26\/05\/2023",
  "headline": "MARIA EUGENIA MUÑOZ DE MAYA",
  "file_name": "313",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 32511630,
  "phone_number": 3136576313,
  "email": "PROYECTOSMAYA@HOTMAIL.COM"
 },
 {
  "file_date_added": "26\/05\/2023",
  "headline": "JESUS ANTONIO CARDON SERNA",
  "file_name": "314",
  "file_type": "LICENCIA DE CNSTRUCCIÓN",
  "passport": 1036930952,
  "phone_number": 3205521097,
  "email": "JACS0022@HOTMAIL.COM"
 },
 {
  "file_date_added": "26\/05\/2023",
  "headline": "HERNAN ALONSO HENAO CARDONA Y OTROS",
  "file_name": "315",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1041324210,
  "phone_number": 3193297611,
  "email": "HENAO3882@GMAIL.COM"
 },
 {
  "file_date_added": "26\/05\/2023",
  "headline": "SANDRA EUGENIA CARVAJAL CASTAÑO",
  "file_name": "316",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y RPH",
  "passport": 43421013,
  "phone_number": 3125130772,
  "email": "GLADYSMARIN710@GMAIL.COM"
 },
 {
  "file_date_added": "26\/05\/2023",
  "headline": "VERONICA MARIA JURADO DURANGO",
  "file_name": "317",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 43756487,
  "phone_number": 3003332237,
  "email": "VERONICAJURADOD@GMAIL.COM"
 },
 {
  "file_date_added": "29\/05\/2023",
  "headline": "JUAN CAMILO CORDOBA TORO Y OTRA ",
  "file_name": "318",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1017123981,
  "phone_number": 3016180752,
  "email": "JCAMILOCTO@GMAIL.COM"
 },
 {
  "file_date_added": "29\/05\/2023",
  "headline": "DEBEIBA HENAO ALZATE Y OTRO ",
  "file_name": "319",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
  "passport": 41503839,
  "phone_number": 3116359466,
  "email": "NO TIENE"
 },
 {
  "file_date_added": "29\/05\/2023",
  "headline": "MARIA CECILIA VERGARA ECHEVERRY",
  "file_name": "320",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
  "passport": 43420277,
  "phone_number": 3008428584,
  "email": "SANDRGALLO280QGMAIL.COM"
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "BAYRON DE JESUS SOSA BEDOYA",
  "file_name": "321",
  "file_type": "LICENCIA DE CNSTRUCCIÓN",
  "passport": 8404284,
  "phone_number": 3205668308,
  "email": "DANYSANCHEZ0208@GMAIL.COM"
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "NICOLAS DE JESUS MARÍN GARCIA ",
  "file_name": "322",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 70111362,
  "phone_number": 30026905,
  "email": "ANTINES1805@HOTMAIL.COM"
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "YULIETH ANDREA GARRO MENDEZ",
  "file_name": "323",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1028033260
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "JUAN ESTEBAN CALLE DAVILA Y OTRA",
  "file_name": "324",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1152195334,
  "phone_number": 3168309089,
  "email": "JUANES1215@GMAIL.COM"
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "ELIZABETH PUERTA CASTRILLON Y OTRA",
  "file_name": "325",
  "file_type": "LICENCIA DE RECONOCIMIENTO",
  "passport": 1037595294,
  "phone_number": 3053304571,
  "email": "ELI9279@GMAIL.COM"
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "SAMARA ALEJANDRA CABALLERO MONROY",
  "file_name": "326",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1035419379,
  "phone_number": 3105964069,
  "email": "SAMACABALLERO@GMAIL.COM"
 },
 {
  "file_date_added": "30\/05\/2023",
  "headline": "JUAN ALBERTO ESCOBAR MARIN",
  "file_name": "327",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
  "passport": 70290077,
  "phone_number": 3196556160,
  "email": ""
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "YARID DANIELA BUITRAGO HERRERA",
  "file_name": "328",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1006022574,
  "phone_number": 3127338541,
  "email": "ANDRIAN15MIRA@GMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "ADRIAN ANGEL MIRA GUTIERREZ",
  "file_name": "329",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1044504925,
  "phone_number": 3127338541,
  "email": "ANDRIAN15MIRA@GMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "ABDON ESTIBENSON URIBE TABORDA",
  "file_name": "330",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 10187070,
  "phone_number": "3104380546 - 3125220564",
  "email": "SHIRLEY.ARISTIZABAL1979@GMAIL.COM - URIBE027@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "ABDON ESTIBENSON URIBE TABORDA",
  "file_name": "331",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 10187070,
  "phone_number": "3104380546 - 3125220564",
  "email": "SHIRLEY.ARISTIZABAL1979@GMAIL.COM - URIBE027@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "JANNETH VELOZA ROBAYO",
  "file_name": "332",
  "file_type": "LICENCIA DE RECONOCIMIENTO",
  "passport": 51910185,
  "phone_number": 3164465035,
  "email": "JVELOZAR@ZENU.COM.CO - JANNETH.VELOZA@GMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "ANDREA JARAMILLO OROZCO",
  "file_name": "333",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1041329133,
  "phone_number": 3506515200,
  "email": "JEISSONMONTOYA36@GMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "FRANCITALIA HILYDIS PEREA",
  "file_name": "334",
  "file_type": "LICENCIA DE AMPLIACIÓN",
  "passport": 26391683,
  "phone_number": 3218015145,
  "email": "SANTIAGOSUARAR@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "DOLLY GIRALDO SANTA",
  "file_name": "335",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 32489829,
  "phone_number": "3206325337 - 3106016575",
  "email": "LIYIMAMU@GMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "JOSE DUVAN BEDOYA GIRALDO Y OTRO ",
  "file_name": "336",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA Y CONSTRUCCIÓN",
  "passport": 71675090,
  "phone_number": 3218514739,
  "email": "CIOTOBON@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "DANIEL FELIPE ZAPATA PONCE DE LEON Y OTRO",
  "file_name": "337",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1017154739,
  "phone_number": 3218514739,
  "email": "CIOTOBON@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "RUSMARY DEL SAGRARIO LÓPEZ LÓPEZ",
  "file_name": "338",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA  ",
  "passport": 43211406,
  "phone_number": 3218514739,
  "email": "CIOTOBON@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "MARCELA GUZMAN GAVIRIA Y OTRO",
  "file_name": "339",
  "file_type": "LICENCIA DE AMPLIACIÓN",
  "passport": 43150770,
  "phone_number": 3176402256,
  "email": ""
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "DIANA MARITZA RAMIREZ GIRALDO",
  "file_name": "340",
  "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO DE TIERRA",
  "passport": 32106576,
  "phone_number": 3116555553,
  "email": "NATA.HERRERA@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "LINA MARIA QUIÑONEZ JARAMILLO",
  "file_name": "341",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 43207281,
  "phone_number": 3116555553,
  "email": "NATA.HERRERA@HOTMAIL.COM"
 },
 {
  "file_date_added": "31704\/2023",
  "headline": "CHRYSTIAN DANIEL OQUENDO ARANGO ",
  "file_name": "342",
  "file_type": "LICENCIA DE RECONOCIMIENTO",
  "passport": 1040750117,
  "phone_number": 3216303087,
  "email": "SONDAVE15@HOTMAIL.COM"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "XIMENA CAROLINA BENAVIDES IBARRA",
  "file_name": "343",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 1085274432,
  "phone_number": 3175024128,
  "email": "XIMENABDS@GMAIL.COM"
 },
 {
  "file_date_added": "31705\/2023",
  "headline": "MARIA ELENA MUÑOZ CALLE",
  "file_name": "344",
  "file_type": "LICENCIA DE CONSTRUCCIÓN",
  "passport": 32542498,
  "phone_number": 3117379522,
  "email": "MARTA.LUZ.SZ@HOTMAIL.ES"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "OSCAR DE JESUS GIRALDO MARÍN Y OTRA",
  "file_name": "345",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
  "passport": 73113856,
  "phone_number": 3117379522,
  "email": "MARTA.LUZ.SZ@HOTMAIL.ES"
 },
 {
  "file_date_added": "31\/05\/2023",
  "headline": "LUZ DARY RODRIGUEZ RUEDA",
  "file_name": "346",
  "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
  "passport": 43505050,
  "phone_number": 3205668303,
  "email": "DANY.SANCHEZ0208@HOTMAIL.COM"
 },
 {
  "file_date_added": "01\/06\/2023",
  "headline": "ROBERTO DE JESÚS JARAMILLO MARÍN",
  "file_name": "347",
  "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
  "passport": 70286727,
  "phone_number": 31450711799,
  "email": "VERGARASEBAS656@GMIL.COM"
 },
 {
  "file_date_added": "02\/06\/2023",
  "headline": "BERNARDO MORALES OSPINA Y OTROS",
  "file_name": "348",
  "file_type": "LICENCIA DE SUBDIVISIÓN",
  "passport": 70286964,
  "phone_number": 3206325874,
  "email": "HUGOHG@YAHOO.ES"
 },
 {
  "file_date_added": "02\/06\/2023",
  "headline": "BLANCA DILVIAN MUÑOZ ALVAREZ",
  "file_name": "349",
  "file_type": "LICENCIA DE AMPLIACIÓN",
  "passport": 43511998,
  "phone_number": 3127327688,
  "email": "JGVDCONST@GMAIL.COM"
 }
]


for item in data:

    file_date_added = item.get('file_date_added', '')
    file_type= FileType.objects.create(name=item['file_type'])
    passport = item.get('passport', '')
    phone_number = item.get('phone_number', '')
    email = item.get('email', '')
    headline = item.get('headline', '')

    File.objects.create(
        file_date_added=file_date_added,
        headline=headline,
        file_name=item['file_name'],
        file_type= file_type,
        passport=str(passport),
        phone_number=str(phone_number),
        email=email,
        organisation_id = 1
    )
    
    print("Succssfully Seeded the data")


# for item in reversed(data):
#     file_type = item['file_type']
#     passport = item.get('passport', '')
#     phone_number = item.get('phone_number', '')

#     # Retrieve the file entry from the database
#     file_entry = File.objects.filter(
#         file_name=item['file_name'],
#         passport=str(passport),
#         phone_number=str(phone_number)
#     ).first()

#     # Delete the file entry if it exists
#     if file_entry:
#         file_entry.delete()
#         print("Successfully deleted the data")

# print("Deletion process completed")