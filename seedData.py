import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from filed.models import File, FileType

data = [
    {
        "file_date_added": "02/01/2023",
        "headline": "MARIA MARCELA MEJIA GUTIERREZ",
        "file_name": "0001",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "32.183.523",
        "phone_number": "301-258-26-75- 3192564625",
        "email": ""
    },
    {
        "file_date_added": "16/01/2023",
        "headline": "NOHORA GEORGINA RUBIO DE GALVIS",
        "file_name": "0002",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "41.592.922",
        "phone_number": "318-285-21-47 / 317-642-15-39",
        "email": "bjaramillo1128@gmail.com"
    },
    {
        "file_date_added": "19/01/2022",
        "headline": "EVELYN JOHANA PIEDRAHITA",
        "file_name": "0003",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.017.137.378",
        "phone_number": "320-626-23-63 / 316-706-77-39",
        "email": ""
    },
    {
        "file_date_added": "20/01/2023",
        "headline": "LOVERA U S.A.S",
        "file_name": "0004",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "901.320.401-1",
        "phone_number": "320-566-83-03",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "20/01/2023",
        "headline": "JOSE WALTER SIERRA JARAMILLO",
        "file_name": "0005",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "12.201.981",
        "phone_number": "300-552-03-08",
        "email": "jowasi@gmail.com"
    },
    {
        "file_date_added": "20/01/2022",
        "headline": "YULY MARCELA MONTOYA ESTRADA",
        "file_name": "0006",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.017.142.942",
        "phone_number": "310-896-80-38 / 314-894-12-39",
        "email": "jaibert.ortiz@hotmail.com"
    },
    {
        "file_date_added": "23/01/2023",
        "headline": "DISTRIBUCIONES MUNDO AFGRO S.A.S",
        "file_name": "0007",
        "file_type": "LICENCIA DE DEMOLICIÓN Y CONSTRUCCIÓN",
        "passport": "90010430-1",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "23/01/2023",
        "headline": "FABIO ALFONSO SANCHEZ MONSALVE",
        "file_name": "0008",
        "file_type": "PERMISO DE VENTA",
        "passport": "70.291.043",
        "phone_number": "321-612-39-65",
        "email": ""
    },
    {
        "file_date_added": "23/01/2023",
        "headline": "GUSTAVO ADOLFO LONDOÑO ZAPATA",
        "file_name": "0009",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.754.267",
        "phone_number": "321-811-96-09",
        "email": ""
    },
    {
        "file_date_added": "24/01/2023",
        "headline": "OSCAR SALDARRIAGA VELEZ",
        "file_name": "0010",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.125.495",
        "phone_number": "318-871-83-14 / 311-274-44-10",
        "email": "santiago.saldarriagalopez@hotmail.com"
    },
    {
        "file_date_added": "24/01/2023",
        "headline": "JOSE REINALDO VANEGAS",
        "file_name": "0011",
        "file_type": "LICENCIA DE MOVIMIENTO TIERRA",
        "passport": "70.288.769",
        "phone_number": "310-389-87-19",
        "email": ""
    },
    {
        "file_date_added": "24/01/2023",
        "headline": "MARISOL CORREA HENAO",
        "file_name": "0012",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "1.017.326.592",
        "phone_number": "320-566-83-03",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "25/01/2023",
        "headline": "YOLANDA LILIANA SANCHEZ AGUDELO",
        "file_name": "0013",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "1.041.324330",
        "phone_number": "312-742-07-85 / 312-718-84-04",
        "email": ""
    },
    {
        "file_date_added": "25/01/2023",
        "headline": "NORBEY ALONSO ACEVEDO HENAO",
        "file_name": "0014",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.141.940",
        "phone_number": "312-650-95-95",
        "email": ""
    },
    {
        "file_date_added": "25/01/2023",
        "headline": "BELLA MARIA HENAO JARAMILLO",
        "file_name": "0015",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "39.440.509",
        "phone_number": "323-420-84-86 / 310-500-55-80",
        "email": "johnosoriobedoya@gmail.com"
    },
    {
        "file_date_added": "25/01/2023",
        "headline": "CELSO JOSE MENDOZA DIAZ",
        "file_name": "0016",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "12.709.901",
        "phone_number": "318-285-2147",
        "email": ""
    },
    {
        "file_date_added": "27/01/2023",
        "headline": "0",
        "file_name": "0017",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "15.427.709",
        "phone_number": "313-700-95-72",
        "email": "gafe63@hotmail.com"
    },
    {
        "file_date_added": "27/01/2023",
        "headline": "PAOLA ANDREA VELEZ ESCUDERO",
        "file_name": "0018",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.020.424.137",
        "phone_number": "301-374-88-67",
        "email": "Fabiantobonnarquitecto@gmail.com"
    },
    {
        "file_date_added": "28/01/2023",
        "headline": "LUZ ADRIANA CALLE VERGARA",
        "file_name": "0019",
        "file_type": " LICENCIA DE CONSTRUCCIÓN",
        "passport": "43.498.798",
        "phone_number": "310-350-04-75 / 300-463-87-64",
        "email": "calleluza@gamil.com"
    },
    {
        "file_date_added": "28/01/2023",
        "headline": "RUBEN DARIO SUAZA LONDOÑO",
        "file_name": "0020",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "71.682.629",
        "phone_number": "319-334-85-22",
        "email": "suaza0328@gamail.com"
    },
    {
        "file_date_added": "30/01/2023",
        "headline": "JAIME DE JESUS ALVAREZ GONZALES",
        "file_name": "0021",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "98.492.230",
        "phone_number": "311-655-55-53",
        "email": "NATA.HERRERA@HOTMAIL.COM"
    },
    {
        "file_date_added": "30/01/2023",
        "headline": "ELKIN MAURICIO OROZCO ARBELAEZ",
        "file_name": "0022",
        "file_type": "PRORROGA A LA RESOLUCIÓN SP-036 LICENCIA DE CONSTRUCCIÓN",
        "passport": "70.289.463",
        "phone_number": "314-507-17-99",
        "email": ""
    },
    {
        "file_date_added": "30/01/2023",
        "headline": "CARLOS ANDRES OSORIO CEBALLOS",
        "file_name": "023",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "71338859",
        "phone_number": "3002424230-31170001206",
        "email": "JUANMAU@GMAIL.COM"
    },
    {
        "file_date_added": "31/01/2023",
        "headline": "ANDRES PATRICIO ORTIZ VINUEZA",
        "file_name": "0024",
        "file_type": "LICENCIA DE C0NSTRUCION",
        "passport": "12092211",
        "phone_number": "3185932533-3147840068",
        "email": "BIO_ARCHITECT@HOTMAIL.COM"
    },
    {
        "file_date_added": "31/01/2023",
        "headline": "TRINIDAD DEL SOCORRO ORREGO",
        "file_name": "0025",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "43.421.491",
        "phone_number": "3233135587-3126330606",
        "email": "DEYRSON@GMAIL.COM"
    },
    {
        "file_date_added": "31/01/2023",
        "headline": "JHON JAIRO LAVERDE LOPEZ",
        "file_name": "0026",
        "file_type": "LICENCIA DE AMPLACION",
        "passport": "70.502.288",
        "phone_number": "3147547978-8308535",
        "email": "JHONJLAVERDE@MSN.COM"
    },
    {
        "file_date_added": "31/01/2023",
        "headline": "GLADYS DEL CARMEN SANTA  MARÍN",
        "file_name": "0027",
        "file_type": "LICENCIA DE MOVIMIENTO TIERRA",
        "passport": "22.051.935",
        "phone_number": "314-507-17-99",
        "email": " "
    },
    {
        "file_date_added": "01/02/2023",
        "headline": "ALEXANDER VANEGAS CARVAJAL",
        "file_name": "0028",
        "file_type": "LICENCIA DE REVALIDACIÓN",
        "passport": "1.041.324.443",
        "phone_number": "312-204-50-59",
        "email": "alezvanegas2412@hotmail.com"
    },
    {
        "file_date_added": "01/02/2023",
        "headline": "MONICA ELEIDA RENDON VELEZ",
        "file_name": "0029",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "43793857",
        "phone_number": "7544231531",
        "email": " "
    },
    {
        "file_date_added": "02/02/2023",
        "headline": "LUISA FERNANDA ECHANDIA RESTREPO",
        "file_name": "0030",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1127589964",
        "phone_number": "3205668303",
        "email": "DANYSANCHEZ@GMAIL.COM"
    },
    {
        "file_date_added": "02/02/2023",
        "headline": "ALIRIO DE JESUS SERNA TORRES",
        "file_name": "0031",
        "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO TIERRA",
        "passport": "1.041.327.797",
        "phone_number": "312-238-62-91",
        "email": " "
    },
    {
        "file_date_added": "07/02/2023",
        "headline": "DORIS CHAVEZ ALQUICHIRE",
        "file_name": "0032",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "37.921.465",
        "phone_number": "320-686-59-06 / 320-686-59-33",
        "email": "aempresarial01@gmail.com"
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "IGLESIA CENTRO DE FE Y ESPERANZA",
        "file_name": "0033",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "9005801129",
        "phone_number": "3175731654",
        "email": "betochoa1@hotmail.com"
    },
    {
        "file_date_added": "09/02/2023",
        "headline": " ALFREDO MONTOYA RESTREPO",
        "file_name": "0034",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1036604850/1000406732",
        "phone_number": "3012062426/5798485",
        "email": "MAULOP23@HOTMAIL.COM"
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "MARIO ENRRIQUE MARIN MONTOYA",
        "file_name": "0035",
        "file_type": "LICENCIA DE DEMOLICION Y CONSTRUCION",
        "passport": "70287282",
        "phone_number": "3147854539/3136972154",
        "email": ""
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "FLORIBERTO DIAZ DIAZ",
        "file_name": "0036",
        "file_type": "LICENCIA DE MOVIMIENTO TIERRA",
        "passport": "98.334.646",
        "phone_number": "301-426-32-02",
        "email": ""
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "CARMEN OFELIA QUINTERO CARDONA",
        "file_name": "0037",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y REFORMA AL R.P.H",
        "passport": "22.050.975",
        "phone_number": "320-566-83-03",
        "email": ""
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "JOSUE DE JESUS MARÍN HINCAPIE",
        "file_name": "0038",
        "file_type": "PRORROGA A LA RESOLUCIÓN SP-077 LICENCIA DE CONSTRUCCIÓN",
        "passport": "70.721.222",
        "phone_number": "314-774-62-74",
        "email": " "
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "MIGUEL ANGEL USMA LOPEZ",
        "file_name": "0039",
        "file_type": "PRORROGA A LA RESOLUCIÓN SP-067 LICENCIA DE CONSTRUCCIÓN",
        "passport": "1017132173",
        "phone_number": "31484000754",
        "email": "miguelangel.usma gmail.com"
    },
    {
        "file_date_added": "09/02/2023",
        "headline": "MUNICIPIO DE SAN VICENTERRER",
        "file_name": "0040",
        "file_type": "LICENCIA DE CONSTRCCIÓN",
        "passport": "890982506-7",
        "phone_number": "",
        "email": " "
    },
    {
        "file_date_added": "10/02/2023",
        "headline": "GUILLERMO LEON CARDONA MONTOYA",
        "file_name": "0041",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "701338543",
        "phone_number": "3148303581",
        "email": ""
    },
    {
        "file_date_added": "10/22/2023",
        "headline": "LAURA EMILSEN VILLEGAS RAMIREZ",
        "file_name": "0042",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "21492379",
        "phone_number": "3127188404",
        "email": "Eduiw_sanchez9@hotmail.com"
    },
    {
        "file_date_added": "11/02/2023",
        "headline": "CARLOS ALBERTO VAENGAS",
        "file_name": "0043",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "98.761.996",
        "phone_number": "3017876315",
        "email": "vanegas2630@hotmail.com"
    },
    {
        "file_date_added": "14/02/2023",
        "headline": "MARIA JOSEFA CARDONA MARIN",
        "file_name": "0044",
        "file_type": "LICENCIA DE ACLARACION Y R.P.H",
        "passport": "22.050.197",
        "phone_number": "320-566-83-03",
        "email": "DANYSANCHEZ@GMAIL.COM"
    },
    {
        "file_date_added": "14/02/2023",
        "headline": "HENRRY ALBERTO RAMIREZ SUAREZ",
        "file_name": "0045",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.906.275",
        "phone_number": "304-667-09-15",
        "email": "nrso591177@gmail.com"
    },
    {
        "file_date_added": "14/02/2023",
        "headline": "MARTHA CECILIA CASTAÑO CASTAÑO",
        "file_name": "0046",
        "file_type": "LICENCIA DE SUBDIVISION",
        "passport": "43.420.120",
        "phone_number": "3117180909-3104470248",
        "email": "PSICOLOGAPAO27@YAHOO.ES"
    },
    {
        "file_date_added": "15/02/2023",
        "headline": "          MARGARITA DEL SOCORRO TAMAYO ORTIZ",
        "file_name": "0047",
        "file_type": "MOVIMIENTO DE TIERRA Y MOVIMIENTO ESTRUCTURAL",
        "passport": "42.879.440",
        "phone_number": "3017253070-3012788186",
        "email": "margara.63.mt@gmail.com"
    },
    {
        "file_date_added": "15/02/2023",
        "headline": "JOSE NORVEY VENEGAS MARIN",
        "file_name": "0048",
        "file_type": "SOLICITUD DE ESTRATIFICACIÓN",
        "passport": "70.287.333",
        "phone_number": "3128060367",
        "email": "diegoN6201@hotmail.com"
    },
    {
        "file_date_added": "16/02/2023",
        "headline": "DANIELA QUINTERO ALVAREZ",
        "file_name": "0049",
        "file_type": "LICENCIA CONSTRUCCION",
        "passport": "1.036.949.516",
        "phone_number": "3008254012",
        "email": "daquial03@gmail.com"
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "JAIRO ENRRIQUE JARAMILLO MARIN",
        "file_name": "0050",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.287.548",
        "phone_number": "3145071799",
        "email": "VERGARASEBAS656@GAMIL.COM "
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "LUZ ELENA JARAMILLO MARÍN",
        "file_name": "0051",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "22.052.306",
        "phone_number": "3145071799",
        "email": "VERGARASEBAS656@GAMIL.COM "
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "MARCO TULIO CASTAÑOA ALZATE",
        "file_name": "0052",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.285.244",
        "phone_number": "3218514739",
        "email": "CIOTOBON@HOTMAIL.COM"
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "SANDRA MILENA DUQUE OROZCO",
        "file_name": "0053",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "38.872.736",
        "phone_number": "316-307-88-09",
        "email": ""
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "ADRIANA MARIA LOPEZ MARIN",
        "file_name": "0054",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "1.041.325.081",
        "phone_number": "3106800232",
        "email": ""
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "JAIDER ARBEY ZAPATA SANCHEZ",
        "file_name": "0055",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.373.403",
        "phone_number": "3146366262",
        "email": ""
    },
    {
        "file_date_added": "21/02/2023",
        "headline": "JORGE IVAN JARAMILLO MARIN",
        "file_name": "0056",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.287.313",
        "phone_number": "3145071799",
        "email": "VERGARASEBAS656@GAMIL.COM"
    },
    {
        "file_date_added": "22/02/2023",
        "headline": "JUAN GONZALO JARAMILLO",
        "file_name": "0057",
        "file_type": "LICENCIA DE SUBDIVISIÓN PARA ENGLOBE",
        "passport": "1.017.142.777",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "23/02/2023",
        "headline": "RUBEN DARIO HERNANDEZ VARGAS",
        "file_name": "0058",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.070.055",
        "phone_number": "3136273079-3206063881",
        "email": "juanes0124@hotmail.com"
    },
    {
        "file_date_added": "23/02/2023",
        "headline": "JEFFREY BENJAMIN HUGHES",
        "file_name": "0059",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "648202213",
        "phone_number": "3502692130",
        "email": ""
    },
    {
        "file_date_added": "24/02/2023",
        "headline": "JOSE AMADO LOPEZ MARÍN",
        "file_name": "0060",
        "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO TIERRA",
        "passport": "3.596.156",
        "phone_number": "312-253-69-27",
        "email": ""
    },
    {
        "file_date_added": "25/02/2023",
        "headline": "RUBEN ARGIRO GIRALDO HENAO",
        "file_name": "0061",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1.041.325.737",
        "phone_number": "3143067059",
        "email": "rgiraldo89@hotmail.com"
    },
    {
        "file_date_added": "25/02/2023",
        "headline": "MARIA DULY ZENAYDA CARMONA ACEVEDO",
        "file_name": "0062",
        "file_type": "PRORROGA SPO-123",
        "passport": "43.528.632",
        "phone_number": "3166253975",
        "email": ""
    },
    {
        "file_date_added": "25/02/2023",
        "headline": "JORGE LUIS URTEAGA PINTADO",
        "file_name": "0063",
        "file_type": "LICENCIA DE RECONOCIMIENTO",
        "passport": "909.53.9",
        "phone_number": "3104999740",
        "email": "ruizagudelovgmail.com"
    },
    {
        "file_date_added": "27/02/2023",
        "headline": "FABIO NELSON AGUDELO VALENCIA",
        "file_name": "0064",
        "file_type": "LICENCIA DE SUBDIVISION",
        "passport": "70.290.407",
        "phone_number": "3025671016",
        "email": ""
    },
    {
        "file_date_added": "27/02/2023",
        "headline": "EDWIN STIF GALLEGO LOPEZ",
        "file_name": "0065",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "98.671.048",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "28/02/2023",
        "headline": "JUAN DANIELCARDONA CUERTAS",
        "file_name": "0066",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1036601895",
        "phone_number": "3117379522",
        "email": "marta.luz.sz@hotmail.com"
    },
    {
        "file_date_added": "28/02/2023",
        "headline": "JORGE ALBERTO MORA ZAPATA",
        "file_name": "0067",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "71.310.047",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "01/03/2023",
        "headline": "FIDUCIARIA CENTRAL COMO VOCERA DEL PATRIMONIO AUTONONOMO FIDECOMISO SAN VICENTE FERRER",
        "file_name": "0068",
        "file_type": "R.P.H. ALTOS DE LA COLINA",
        "passport": "830.053.036.-3",
        "phone_number": "3164897752",
        "email": ""
    },
    {
        "file_date_added": "01/02/2023",
        "headline": "HENRY ANTONIO RESTREPO ROJAS",
        "file_name": "0069",
        "file_type": "SOLUCITUD ESTRATIFICACION",
        "passport": "98.660.528",
        "phone_number": "3115160774",
        "email": "Jero200115@hotmail.com"
    },
    {
        "file_date_added": "02/03/2023",
        "headline": "OCTAVIO ALBERTO NIETO PANESSO",
        "file_name": "0070",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "15.433.018",
        "phone_number": "3213148",
        "email": "tatonieto@gmail.com"
    },
    {
        "file_date_added": "02/03/2023",
        "headline": "OMAR DE JEUSUS SANTA MARIN",
        "file_name": "0071",
        "file_type": "LICENCIA DE SUBDIVICION PARA LA LIQUIDACIONDE LA COMUNIDAD",
        "passport": "3.595.765",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "03/03/2023",
        "headline": "CINDY JOHANA VELEZ CAÑAS",
        "file_name": "0072",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.037.606.050",
        "phone_number": "3146257406",
        "email": ""
    },
    {
        "file_date_added": "03/03/2023",
        "headline": "OCTAVIO GIRALDO LOPEZ",
        "file_name": "0073",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "3.436.806",
        "phone_number": "3012948485",
        "email": "Leo-521@hotmail.com "
    },
    {
        "file_date_added": "03/03/2023",
        "headline": "JOSE ALEJANDRO ALZATE GIRALDO",
        "file_name": "0074",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.289.150",
        "phone_number": "3147989410",
        "email": "mateoac96@gmail.com"
    },
    {
        "file_date_added": "04/03/2023",
        "headline": "JESUS DAVID FLOREZ MARIN",
        "file_name": "0075",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.799.502",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "06/03/2023",
        "headline": "EDUARDO ALCIDES CARMONA CARMONA",
        "file_name": "0076",
        "file_type": "SOLICITUD DE ESTRATIFICACIÓN",
        "passport": "70.285.724",
        "phone_number": "3206762339",
        "email": ""
    },
    {
        "file_date_added": "06/03/2023",
        "headline": "JULIO CESAR MARIN ALVAREZ",
        "file_name": "0077",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "12.023.445",
        "phone_number": "3192244048",
        "email": "julio.072marin@gmail.com"
    },
    {
        "file_date_added": "07/03/2023",
        "headline": "LUZ ELENEA DUQUE MONTOYA",
        "file_name": "0078",
        "file_type": "SOLICITUD DE ESTRATIFICACION",
        "passport": "21.548.958",
        "phone_number": "3113878446",
        "email": "NO TREPORTA"
    },
    {
        "file_date_added": "07/03/2023",
        "headline": "AMPARO DEL SOCORRRO GARCIA GALLO",
        "file_name": "0079",
        "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO TIERRA",
        "passport": "43.420.490",
        "phone_number": "3147905892",
        "email": ""
    },
    {
        "file_date_added": "07/032023",
        "headline": "LINA MARCELA FLORES ORTIZ",
        "file_name": "0080",
        "file_type": "SOLICITUD DE ESTRATIFICACIÓN",
        "passport": "43.625.592",
        "phone_number": "3046259798",
        "email": "lMARCELA1018G@GMAIL.COM"
    },
    {
        "file_date_added": "07/03/2023",
        "headline": "DANIELA MARÍN GIL",
        "file_name": "0081",
        "file_type": "LICENCIA DE MODIFICACIÓN A LA RESOLUCIÓN SPO-523",
        "passport": "1.041.327.454",
        "phone_number": "3042370610",
        "email": ""
    },
    {
        "file_date_added": "07/03/2023",
        "headline": "MARTHA ISABEL MARÍN GIL",
        "file_name": "0082",
        "file_type": "LICENCIA DE MODIFICACIÓN A LA RESOLUCIÓN SPO-522",
        "passport": "1.041.325.552",
        "phone_number": "3208240891",
        "email": ""
    },
    {
        "file_date_added": "08/03/2023",
        "headline": "ANDRES MAURICIO JARAMILLO GOMEZ",
        "file_name": "0083",
        "file_type": "SOLICITUD ESTRATIFICACION",
        "passport": "1.017.166.126",
        "phone_number": "3017078071",
        "email": "andres.jara88@hotmail.com"
    },
    {
        "file_date_added": "08/03/2023",
        "headline": "RODOLFO SABOGAL",
        "file_name": "0084",
        "file_type": "SOLICITUD ESTRATIFICACION",
        "passport": "100.027.789",
        "phone_number": "3217172259",
        "email": "rsabogal76@hotmail.com"
    },
    {
        "file_date_added": "08/03/2023",
        "headline": "ELKIN ANDRES SANCHEZ SANCHEZ",
        "file_name": "0085",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "1.041.328.849",
        "phone_number": "3105292218",
        "email": "elkinandressanchez0@gmail.com"
    },
    {
        "file_date_added": "08/03/2023",
        "headline": "LUZ ANGELA FRANCO DE ALZATE",
        "file_name": "0086",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "22.050.570",
        "phone_number": "3196954382-3103828230",
        "email": "rafrancoa@gmail.com"
    },
    {
        "file_date_added": "09/03/2023",
        "headline": "MARIA SOBEIDA MONTOYA HERRERA",
        "file_name": "0087",
        "file_type": "LICENCIA DE AMPLACION",
        "passport": "42.750.564.",
        "phone_number": "3042453063",
        "email": "juliomayasneider@gmail.com"
    },
    {
        "file_date_added": "09/03/2023",
        "headline": "GLORIA LILIANA TORRES",
        "file_name": "0088",
        "file_type": "LICENCIA DE PRORROGA A LA RESOLUCIÓN SPO-251",
        "passport": "42.882.367",
        "phone_number": "3113468083",
        "email": "gloriatorresmedellin@hotmail.com"
    },
    {
        "file_date_added": "09/03/2023",
        "headline": "LAURA CATALINA OSSA CARRASQUILLA",
        "file_name": "0089",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.017.183.631",
        "phone_number": "3146835637",
        "email": "proyectosingecarq@gmail.com"
    },
    {
        "file_date_added": "09/03/2023",
        "headline": "JUAN CAMILO HENAO AGUDELO",
        "file_name": "0090",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "1.041.325.884",
        "phone_number": "3016513492",
        "email": "celucom80@gmail.com"
    },
    {
        "file_date_added": "10/03/2022",
        "headline": "JEFFREY BENJAMIN HUGHES",
        "file_name": "0091",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "648202213",
        "phone_number": "3115213199",
        "email": ""
    },
    {
        "file_date_added": "10/03/2023",
        "headline": "JHON ALEXANDER GIL LOPEZ",
        "file_name": "0092",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.035.918.498",
        "phone_number": "3205668303",
        "email": ""
    },
    {
        "file_date_added": "10/03/2023",
        "headline": "JOSE LEONEL GARCIA ALZATE",
        "file_name": "0093",
        "file_type": "LICENCIA DE SUBDIVISION",
        "passport": "70.051.706",
        "phone_number": "3003579444",
        "email": "700leogar@gmail.com"
    },
    {
        "file_date_added": "10/03/2023",
        "headline": "JULIAN MONTEALEGRE SANCHEZ",
        "file_name": "0094",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
        "passport": "",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "11/03/2023",
        "headline": "GERMAN ANTONIO HENAO VARGAS",
        "file_name": "0095",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
        "passport": "70.288.193",
        "phone_number": "3222620651",
        "email": ""
    },
    {
        "file_date_added": "11/03/2023",
        "headline": "GILBERT ADRIAN GUEVARA SABGOBAL",
        "file_name": "0096",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "80.092.990",
        "phone_number": "3103400874",
        "email": ""
    },
    {
        "file_date_added": "13/03/2023",
        "headline": "ROSALBA GOMEZ SANCHEZ",
        "file_name": "0097",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "21.729.405",
        "phone_number": "3137904963",
        "email": "eogomez05@hotmail.com"
    },
    {
        "file_date_added": "13/03/2023",
        "headline": "MARTHA OLIVA GALLEGO VALLEJO",
        "file_name": "0098",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "21.461.397",
        "phone_number": "3123666803",
        "email": "vjzgil@hotmail.com"
    },
    {
        "file_date_added": "14/03/2023",
        "headline": "ANDRES GONZALEZ OROZCO",
        "file_name": "0099",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.787.707",
        "phone_number": "3117649144",
        "email": "mtereorozco@yahoo.es"
    },
    {
        "file_date_added": "14/03/2023",
        "headline": "MARIA TIVISAY MARÍN MARÍN",
        "file_name": "0100",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "43.421.758",
        "phone_number": "3205666383",
        "email": ""
    },
    {
        "file_date_added": "16/03/2023",
        "headline": "FANNY DEL SOCORRO",
        "file_name": "0101",
        "file_type": "LICENCIA DE COSTRUCCIÓN",
        "passport": "43.41943",
        "phone_number": "3012948485",
        "email": ""
    },
    {
        "file_date_added": "16/03/2023",
        "headline": "GLORIA ELENA MEJIA GARCIA",
        "file_name": "0102",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACIÓN",
        "passport": "32.315.400",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "16/03/2023",
        "headline": "RODRIGO HERNAN DIAZ ACEVEDO",
        "file_name": "0103",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.288.515",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "16/03/2023",
        "headline": "GERMAN DE JESUS GIL VALLEJO",
        "file_name": "0104",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.286.496",
        "phone_number": "3216190625",
        "email": ""
    },
    {
        "file_date_added": "17/03/2023",
        "headline": "HECTOR DARIO JARAMILLO RESTREPO",
        "file_name": "0105",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "98548471",
        "phone_number": "3117038502",
        "email": ""
    },
    {
        "file_date_added": "17/03/2023",
        "headline": "MARIA VERONICA SANCHEZ SANCHEZ",
        "file_name": "0106",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1041329686",
        "phone_number": "3114011590",
        "email": ""
    },
    {
        "file_date_added": "17/03/2023",
        "headline": "JOSE BIBIANO ARENAS ZAPATA",
        "file_name": "0107",
        "file_type": "LICENCIA DE ACLARACION A LA RESOLUCION SP-015/2017",
        "passport": "71576854",
        "phone_number": "3117740816",
        "email": "josebarenasz@gmail.com"
    },
    {
        "file_date_added": "17/03/2023",
        "headline": "SADY ALBERTO HENAO MARIN",
        "file_name": "0108",
        "file_type": "LICENCIA DE ACLARACIÓN A LA RESOLUCIÓN 339/2022",
        "passport": "1041327096",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "17/0372023",
        "headline": "LUIS EDUARDO QUICENO MARIN",
        "file_name": "0109",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "1041325999",
        "phone_number": "3244035785 - 3136316958",
        "email": "LUISQUICE@GMAIL.COM"
    },
    {
        "file_date_added": "17/03/2023",
        "headline": "ANGEL ALBERTO ALCALA GUZMAN",
        "file_name": "0110",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "958919",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "18/03/2023",
        "headline": "MARIA VICTORIA MONTOYA GIL",
        "file_name": "0111",
        "file_type": "LICENCIA DE AMPLIACIÓN Y MOVIMIENTO DE TIERRA",
        "passport": "42.770.825",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "21/03/2023",
        "headline": "ADRIANA MARIA  ARBELAEZ MONTOYA",
        "file_name": "0112",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.036.9525.218",
        "phone_number": "3113515291",
        "email": ""
    },
    {
        "file_date_added": "22/03/2023",
        "headline": "ALBA TANET HENAO ALZATE",
        "file_name": "0113",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "39.441.570",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "22/03/2023",
        "headline": "JAIRO DE JESUS VALENCIA AGUDELO",
        "file_name": "0114",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "19.072.190",
        "phone_number": "3128430006",
        "email": ""
    },
    {
        "file_date_added": "23/03/2023",
        "headline": "OLMES ORJIVES MONSALVE URREGO",
        "file_name": "0115",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "98.699.771",
        "phone_number": "3176656582",
        "email": ""
    },
    {
        "file_date_added": "23/03/2023",
        "headline": "JOSE ALEJANDRO ALZATE GIRALDO",
        "file_name": "0116",
        "file_type": "LICENCIA DE CONDOMINIO",
        "passport": "70.289.150",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "23/03/2023",
        "headline": "JOSE ALEJANDRO ALZATE GIRALDO",
        "file_name": "0117",
        "file_type": "LICENCIA DE COSTRUCCIÓN",
        "passport": "70.289.150",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "23/03/2023",
        "headline": "LUIS ALBERTO CARDONA  OCHOA",
        "file_name": "0118",
        "file_type": "LICENCIA DE SUBDIVISION",
        "passport": "70.286.917",
        "phone_number": "32056688303",
        "email": "Danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "23/03/2023",
        "headline": "LUIS ALBEIRO MONTOYA MONTOYA",
        "file_name": "0119",
        "file_type": "LICENCENCIA DE SUBDIVISION",
        "passport": "70.286.314",
        "phone_number": "3122536927",
        "email": ""
    },
    {
        "file_date_added": "24/03/2023",
        "headline": "LUIS ENRIQUE SERNA GALLO",
        "file_name": "0120",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "70.287.734",
        "phone_number": "3104116354",
        "email": ""
    },
    {
        "file_date_added": "24/03/2023",
        "headline": "DIEGO ALEXANDRER RODRIGUES PARRA",
        "file_name": "0121",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "1.128.397.393",
        "phone_number": "3218514739",
        "email": "ciotobon@hotmail.com"
    },
    {
        "file_date_added": "27/03/2023",
        "headline": "VICTOR HUGO GONZALEZ BETANCUR",
        "file_name": "0122",
        "file_type": "PRORROGA A LA RESOLUCIÓN SPO-252",
        "passport": "15.436.054",
        "phone_number": "3217973577",
        "email": ""
    },
    {
        "file_date_added": "27/03/2023",
        "headline": "TRINIDAD VERGARA DE TORRES",
        "file_name": "0123",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "43.419.151",
        "phone_number": "3135935461",
        "email": "TRIVEVA63@GMAIL.COM"
    },
    {
        "file_date_added": "27/03/2023",
        "headline": "ADRIANA MARIA MONSALVE",
        "file_name": "0124",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "43.421.933",
        "phone_number": "3206266477",
        "email": " "
    },
    {
        "file_date_added": "27/03/2023",
        "headline": "RAFAEL MARIA VARGAS GIRALDO",
        "file_name": "0125",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.288.657",
        "phone_number": "3116205180",
        "email": "rafavag@hotmail.com"
    },
    {
        "file_date_added": "27/03/2023",
        "headline": "GULLERMO DE JESUS GARCIA HENAO",
        "file_name": "0126",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.588.576",
        "phone_number": "3206857305",
        "email": "memillo239@hotmail.com"
    },
    {
        "file_date_added": "27/03/2023",
        "headline": "WILSON DE JESUS TORRES TORRES",
        "file_name": "0127",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "98.488.720",
        "phone_number": "3163457561",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "28/03/2023",
        "headline": "JOSE ALEJANDRINO ALZATE GIRALDO",
        "file_name": "0128",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "70.289.150",
        "phone_number": "3205668303",
        "email": ""
    },
    {
        "file_date_added": "28/03/2023",
        "headline": "BEATRIS ELENA MARIN VERGARA",
        "file_name": "0129",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "43.420.608",
        "phone_number": "3206325874",
        "email": ""
    },
    {
        "file_date_added": "28/03/2023",
        "headline": "ANDRES FELIPE MARTINEZ BEDOYA",
        "file_name": "0130",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "3.563.607",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "28/03/2023",
        "headline": "FELIPE ANTONIO GARCIA MARIN",
        "file_name": "0131",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "70.288.736",
        "phone_number": "3167288679",
        "email": ""
    },
    {
        "file_date_added": "",
        "headline": "MERY DEL SOCORRO VELASQUEZ PATIÑO",
        "file_name": "0132",
        "file_type": "ACLARACIÓN A LA RESOLUCIÓN SP-120",
        "passport": "32.464.910",
        "phone_number": "3128345272",
        "email": "meryvp7@yahoo.com"
    },
    {
        "file_date_added": "29/03/2023",
        "headline": "VICENTE ABEL LOPEZ ROJAS",
        "file_name": "0133",
        "file_type": "LICENCIA DE SUBDIVISION",
        "passport": "3.405.154",
        "phone_number": "3218514739",
        "email": "ciotobon@hotmail.com"
    },
    {
        "file_date_added": "",
        "headline": "JAIME LEON ANGEL SALAZAR",
        "file_name": "0134",
        "file_type": "LICENCIA DE SUBDIVISION",
        "passport": "71.643.629",
        "phone_number": "3012948485",
        "email": "lep.521@hotmail.com"
    },
    {
        "file_date_added": "29/03/2023",
        "headline": "LUIS RAMIRO GONZALEZ ROLDAN",
        "file_name": "0135",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.604.082",
        "phone_number": "3132720115",
        "email": ""
    },
    {
        "file_date_added": "29/03/2023",
        "headline": "MIGUEL HORACIO ZULUAGA GIL",
        "file_name": "0136",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "30/03/2023",
        "headline": "ARNULFO DE JESUS AGUDELO SANCHEZ",
        "file_name": "0137",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "3.596.283",
        "phone_number": "3126985296",
        "email": ""
    },
    {
        "file_date_added": "30/03/2023",
        "headline": "ANDRES FELIPE TAMAYO ISAZA",
        "file_name": "0138",
        "file_type": "LECENCIA DE CONDOMINIO",
        "passport": "1036601877",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "30/03/2023",
        "headline": "ANA SOFIA VERGARA JARAMILLO",
        "file_name": "0139",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "43.419.426",
        "phone_number": "3116428239",
        "email": ""
    },
    {
        "file_date_added": "30/03/2023",
        "headline": "MARIA EULALIA GALLEGO GIL",
        "file_name": "0140",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "22051344",
        "phone_number": "3206836770",
        "email": ""
    },
    {
        "file_date_added": "30/03/2023",
        "headline": "JOSE ANIBAL VILLA LEDESMA",
        "file_name": "0141",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "98.520.521",
        "phone_number": "3148034402",
        "email": "dafecosa15@gmail.com"
    },
    {
        "file_date_added": "31/03/2023",
        "headline": "JUAN CAMILO ARANGO DUQUE",
        "file_name": "0142",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1.037.626.506",
        "phone_number": "31544666938-320605612",
        "email": "juanarango@outlook.com"
    },
    {
        "file_date_added": "31/03/2023",
        "headline": "DIANA PATRICIA CEBALLOS CASTAÑO",
        "file_name": "0143",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "",
        "phone_number": "",
        "email": ""},
    {
        "file_date_added": "31/03/2023",
        "headline": "NORBEY OROZCO SALAZAR",
        "file_name": "0144",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "71.330.678",
        "phone_number": "3205668303",
        "email": "danysanchez@hotmail.com"
    },
    {
        "file_date_added": "31/03/2023",
        "headline": "GLORIA EMILCE VERGARA HENAO",
        "file_name": "0145",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "",
        "phone_number": "",
        "email": ""},
    {
        "file_date_added": "01/04/2023",
        "headline": "ELIANA MARIA GUERRA GARCIA",
        "file_name": "0146",
        "file_type": "LICENCIA DE RECONOCIMIENTO",
        "passport": "43.971.792",
        "phone_number": "3225078961",
        "email": "ELYGUERRAGA@GMAIL.COM"
    },
    {
        "file_date_added": "04/04/2023",
        "headline": "ANTONIO JOSE MONTOYA ACEVEDO",
        "file_name": "0147",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "1.020.429.308",
        "phone_number": "3014225942",
        "email": "anjomontoya@gmail.com"
    },
    {
        "file_date_added": "04/04/2023",
        "headline": "DIANA PATRICIA CEBALLOS CASTAÑO",
        "file_name": "0148",
        "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO TIERRA",
        "passport": "43.741.018",
        "phone_number": "3207411964",
        "email": "mile.20@hotmail.com"
    },
    {
        "file_date_added": "05/04/2023",
        "headline": "CARLOS EMILIO OSPINA CARMONA",
        "file_name": "0149",
        "file_type": "SOLICITUD ESTERATIFICACION",
        "passport": "70.288.148",
        "phone_number": "3209851185",
        "email": ""
    },
    {
        "file_date_added": "10/04/2023",
        "headline": "RICARDO ANDRES OROZCO QUINTERO",
        "file_name": "0150",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "8.029.682",
        "phone_number": "3223602840",
        "email": ""
    },
    {
        "file_date_added": "10/04/2023",
        "headline": "HECTOR ALONSO SANCHEZ ESCOBAR",
        "file_name": "0151",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "1.035.911.689",
        "phone_number": "3216153945",
        "email": "bustamanteeesmeralda@gmail.com"
    },
    {
        "file_date_added": "10/04/2023",
        "headline": "MARIA CENELIA GARCIA MARULANDA",
        "file_name": "0152",
        "file_type": "LICENCIA DE RECONOCIMIENTO",
        "passport": "43.568.946",
        "phone_number": "3046515313",
        "email": "mariacenegarciam@gmail.com"
    },
    {
        "file_date_added": "11/04/2023",
        "headline": "YOVANY DE JESUS AGUDELO ISAZA",
        "file_name": "0153",
        "file_type": "LICENCIA DE AMPLIACION",
        "passport": "70.290.709",
        "phone_number": "3147316780",
        "email": "yohanyagudelo@gmail.com"
    },
    {
        "file_date_added": "11/04/2023",
        "headline": "YHOANY ALEJANDRO VALENCIA ARIAS",
        "file_name": "0154",
        "file_type": "LICENCIA DE MOVIEMIENTO DE TIERRA",
        "passport": " 1.017.158.158",
        "phone_number": "3146915970",
        "email": "aldemarvalenciaagudelo@gmail.com"
    },
    {
        "file_date_added": "11/04/2023",
        "headline": "JOSE REYNALDO MARIN MARIN",
        "file_name": "0155",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "70.286.027",
        "phone_number": "3205668303",
        "email": "danysanchez@hotmail.com"
    },
    {
        "file_date_added": "11/04/2023",
        "headline": "LUIS ALVARO SANTA CARDONA",
        "file_name": "0156",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACION",
        "passport": "8.352.757",
        "phone_number": "3205668303",
        "email": "danysanchez@hotmail.com"
    },
    {
        "file_date_added": "11/04/2023",
        "headline": "RUBEIRO ANTONIO MARIN AGUDELO",
        "file_name": "0157",
        "file_type": "LICENCIA DE COSNTRUCCIÓN",
        "passport": "1.037.544.732",
        "phone_number": "3122691357 - 3103952686",
        "email": "rubeiromairn@gmail.com"
    },
    {
        "file_date_added": "11/12/2023",
        "headline": "YESID CESPEDES BARRERA",
        "file_name": "0158",
        "file_type": "LICENCIADE CONSTRUCION",
        "passport": "94.06.44.57",
        "phone_number": "3218015145",
        "email": ""
    },
    {
        "file_date_added": "11/04/2023",
        "headline": "NESTOR FABIAN CARDONA CASTAÑO",
        "file_name": "0159",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "70.288.238",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "12/04/2023",
        "headline": "CARLOS ANDRES OSPINA HENAO",
        "file_name": "0160",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.041.327.506",
        "phone_number": "3105124311",
        "email": "mary-luz85@hotmail.com"
    },
    {
        "file_date_added": "12/04/2023",
        "headline": "JHON JAIRO MARIN MARIN",
        "file_name": "0161",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.287.570",
        "phone_number": "3108219937",
        "email": ""
    },
    {
        "file_date_added": "12/04/2023",
        "headline": "JORGE IVAN ARBELAEZ HERRERA",
        "file_name": "0162",
        "file_type": "LICENCIA DE CONTRUCION",
        "passport": "1.001.748.277",
        "phone_number": "3128051741",
        "email": ""
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "JUAN BAUTISTA RESTREPO GONZALEZ",
        "file_name": "0163",
        "file_type": "LICENCIA DE MOVIMIENTO DEN TIERRA",
        "passport": "71.709.145",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "ALFREDO DE JESUS OROZCO SALAZAR",
        "file_name": "0164",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.25.317",
        "phone_number": "320.725.317",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "ALFREDO DE JESUS OROZCO SALAZAR",
        "file_name": "0165",
        "file_type": "LICENCIA MOVIMIENTO DE TIRRRA",
        "passport": "70.25.317",
        "phone_number": "320.725.317",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "JULIO ANIBAL GALLEGO ZAPATA",
        "file_name": "0166",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "1.037.572.825",
        "phone_number": "3175175921",
        "email": "gallegojulio@gmail.com"
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "MANUEL JOSE AEVEDO MENESE",
        "file_name": "0167",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "3.398.562",
        "phone_number": "3113079363",
        "email": "hostosstne@gmail.com"
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "ELIANA YESENIA JARAMILLO FRANCO",
        "file_name": "0168",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1.017.174.668",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "13/04/2023",
        "headline": "ALFREDO DE JESUS OROZCO SALAZAR",
        "file_name": "0169",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.725.317",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "LUIS GUILLERMO RAMIREZ LOPEZ",
        "file_name": "0170",
        "file_type": "LICENCIA DE MOVIMIENTO D TIERRA",
        "passport": "71.729.681",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "FABIO NELSON AGUDELO VALENCIA",
        "file_name": "0171",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.290.407",
        "phone_number": "3025671016",
        "email": ""
    },
    {
        "file_date_added": "14/03/2023",
        "headline": "MARÍA ELENA MEJIA GOMEZ",
        "file_name": "0172",
        "file_type": "LICENCENCIA DE CONSTRUCCIÓN",
        "passport": "42.750.855",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "OSCAR ADRIAN PARADA ORTIZ",
        "file_name": "0173",
        "file_type": "LICENCIA MOVIMIENTO DE TIRRRA",
        "passport": "71.796.584",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "JEFFREY BENJAMIN HUGHES",
        "file_name": "0174",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "64.820.22.13",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "JEFFREY BENJAMIN HUGHES",
        "file_name": "0175",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "64.820.22.13",
        "phone_number": "320668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "JEFFREY BENJAMIN HUGHES",
        "file_name": "0176",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "64.820.22.13",
        "phone_number": "320668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "14/04/2023",
        "headline": "HUGO HERNANDO GALLEGO",
        "file_name": "0177",
        "file_type": "LICENCIA DE DECLRACION DE RPH",
        "passport": "70.288.313",
        "phone_number": "70.288.313",
        "email": ""
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "LEONEL VANEGAS SANCHEZ",
        "file_name": "0178",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "70.289.417",
        "phone_number": "3127392134",
        "email": ""
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "JUAN GUILLERMO GALLEGO GIRALDO",
        "file_name": "0179",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "71.670.012",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "JUAN GUILLERMO GALLEGO GIRALDO",
        "file_name": "0180",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "71.670.013",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "DIVA HELENA MAZO DUARTE",
        "file_name": "0181",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "21.398.711",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "LA DESPENSA INMOBILIARIA S.A.S",
        "file_name": "0182",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "901.276.609",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "LA DESPENSA INMOBILIARIA S.A.S",
        "file_name": "0183",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "901.276.609",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "LA DESPENSA INMOBILIARIA S.A.S",
        "file_name": "0184",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "901.276.609",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "ANDRES MAURICIO ARIAS RODRIGUEZ",
        "file_name": "0185",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "71.798.597",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "DIEGO ALEJANDRO VILLADA VASQUEZ",
        "file_name": "0186",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "98.672.408",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "JUAN SEBASTIAN PUERTA NEVADO",
        "file_name": "0187",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "1.020.446.202",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "15/04/2023",
        "headline": "OSCAR ADRIAN PARADA ORTIZ",
        "file_name": "0188",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "71.796.584",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "17/04/2023",
        "headline": "GUILLERMO HERNANDO VANEGAS GOMEZ",
        "file_name": "0189",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.124.960",
        "phone_number": "3155124989",
        "email": "guillermovg@hotmail.com"
    },
    {
        "file_date_added": "17/04/2023",
        "headline": "GULLERMO HERNANDO VANEGAS",
        "file_name": "0190",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.124.960",
        "phone_number": "31551249989",
        "email": "guillermovg@hotmail.com"
    },
    {
        "file_date_added": "17/04/2023",
        "headline": "ARGEMIRO HERNAN AGUDELO LOPEZ",
        "file_name": "0191",
        "file_type": " ",
        "passport": "70.288.908",
        "phone_number": "311727313",
        "email": "argemiro-agu@hotmail.com"
    },
    {
        "file_date_added": "18/04/2023",
        "headline": "GUILLERMO DE JESUS SANCHEZ JARAMILLO",
        "file_name": "0192",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.287.617",
        "phone_number": "3122054740",
        "email": ""
    },
    {
        "file_date_added": "18/04/2023",
        "headline": "CARMEN TULIA SANCHEZ CASTRILLON",
        "file_name": "0193",
        "file_type": "LICENCIA DE PRORROGA A LA RESOLUCIÓN SPO-245",
        "passport": "43.856.747",
        "phone_number": "3146838965",
        "email": ""
    },
    {
        "file_date_added": "18/04/2023",
        "headline": "MARIA DFABIOLA ARIAS CAÑAS",
        "file_name": "0194",
        "file_type": "SOLICITUD DE ESTRATIFICACIÓN",
        "passport": "22.051.266",
        "phone_number": "3113791022",
        "email": ""
    },
    {
        "file_date_added": "18/04/2023",
        "headline": "JUAN GUILLERMO GOMEZ GIRALDO",
        "file_name": "0195",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.775.347",
        "phone_number": "3122109501",
        "email": "Pintulavamos@hotmail.com"
    },
    {
        "file_date_added": "18/04/2023",
        "headline": "KIRA HANNETT GUTIERREZ MICHAELS",
        "file_name": "0196",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "41.685.788",
        "phone_number": "3193616297",
        "email": "dra.kira@hotmail.com"
    },
    {
        "file_date_added": "18/04/2023",
        "headline": "LUIS CARLOS MEJIA QUICENO",
        "file_name": "0197",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "3.558.924",
        "phone_number": "301589.924",
        "email": ""
    },
    {
        "file_date_added": "19/04/2023",
        "headline": "RAFAEL ANGEL MUÑOZ ECHEVERRY",
        "file_name": "0198",
        "file_type": "LICENCIA DE SUBDIVISÓN",
        "passport": "3.596.465",
        "phone_number": "3216422821",
        "email": "rafaelqm347@gmail.com"
    },
    {
        "file_date_added": "19/04/2023",
        "headline": "ADRIANA LUCIA MONTOYA CARDONA",
        "file_name": "0199",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "43.420.780",
        "phone_number": "3148035402",
        "email": ""
    },
    {
        "file_date_added": "19/04/2023",
        "headline": "JOSE ANGEL GARCIA MARIN",
        "file_name": "0200",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.137.781",
        "phone_number": "3143647128",
        "email": "ceballosabogados2020@gmail.com"
    },
    {
        "file_date_added": "19/04/2023",
        "headline": "CARLOS ALBERTO ZAPATA SANCHEZ",
        "file_name": "0201",
        "file_type": "SOLICITUD ESTRATIFICACION",
        "passport": "10.109.204",
        "phone_number": "3208399263",
        "email": "cazs1992@hotmail.com"
    },
    {
        "file_date_added": "19/04/2023",
        "headline": "LUIS EDUARDO MARÍN GALLEGO",
        "file_name": "0202",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y REFORMA AL R.P.H",
        "passport": "3.595.060",
        "phone_number": "3205668303",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "19/04/2023",
        "headline": "JORGE HERNAN URIBE OSORNO",
        "file_name": "0203",
        "file_type": "LECENCIA DE SUBDIVICION",
        "passport": "71.795.403",
        "phone_number": "3104342168",
        "email": "Arquitecturavelazquez@gmail.com"
    },
    {
        "file_date_added": "20/04/2023",
        "headline": "OTONIEL MONTOYA",
        "file_name": "0204",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "15.482.088",
        "phone_number": "3006046663",
        "email": "OTO.MONTOYA08@GMAIL.COM"
    },
    {
        "file_date_added": "20/04/2023",
        "headline": "FAVER  DE JESUS GALEAO MORALES",
        "file_name": "0205",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.289.352",
        "phone_number": "3014876997",
        "email": "duvangaleano99@gmail.com"
    },
    {
        "file_date_added": "20/04/2023",
        "headline": "FAVER DE JESUS GALEANO MORALES",
        "file_name": "0206",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "70.289.352",
        "phone_number": "3014876997",
        "email": "duvangaleano99@gmail.com"
    },
    {
        "file_date_added": "20/04/2023",
        "headline": "CARLOS MARIO ZULUAGA TOBON",
        "file_name": "0207",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "70.285.937",
        "phone_number": "3117875527",
        "email": ""
    },
    {
        "file_date_added": "20/04/2023",
        "headline": "NICOLAS ANDRES FRANCO OSORIO",
        "file_name": "0208",
        "file_type": "LICENCIA DE PARCELACION",
        "passport": "1.128.269.353",
        "phone_number": "3106800232",
        "email": "adrimar2103@gmail.com"
    },
    {
        "file_date_added": "",
        "headline": "",
        "file_name": "0209",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y AMPLIACION",
        "passport": "",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "21/04/2023",
        "headline": "DANIELA VELASQUEZ DIEZ",
        "file_name": "0210",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.040.741.141",
        "phone_number": "3127915987",
        "email": "sarcilia@mopdularplaces.com"
    },
    {
        "file_date_added": "21/04/2023",
        "headline": "DENNYS RESTREPO ORTEGA",
        "file_name": "0211",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "43.638.378",
        "phone_number": "3215668303",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "21/04/2023",
        "headline": "SARA EMILIA GUARIN DE MARÍN",
        "file_name": "0212",
        "file_type": "ENGLOBE - PARCELACION Y MOVIEMIENTO DE TIERRA",
        "passport": "21.907.070",
        "phone_number": "3205668337",
        "email": "danysanchezg@gmail.com"
    },
    {
        "file_date_added": "21/04/2023",
        "headline": "ELIZABETH BETANCUR HENAO",
        "file_name": "0213",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.020.472.067",
        "phone_number": "3015860325",
        "email": ""
    },
    {
        "file_date_added": "21/04/2023",
        "headline": "VICTOR EDUARDO ZULIAGA TOBON",
        "file_name": "0214",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.586.525",
        "phone_number": "3207868812",
        "email": "gabocaro@hotmail.com"
    },
    {
        "file_date_added": "22/04/2023",
        "headline": "BIBIANA JANNETH CHAVARRIAGA COLORADO",
        "file_name": "0215",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "21.532.703",
        "phone_number": "3218532703",
        "email": "bibiana120286@hotmail.com"
    },
    {
        "file_date_added": "24/04/2023",
        "headline": "JUAN DAVID RODRIGUEZ ARBELAEZ",
        "file_name": "0216",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "1.128.281.039",
        "phone_number": "3003867097",
        "email": "misabelarb@hotmail.com"
    },
    {
        "file_date_added": "24/03/2023",
        "headline": "JOSE REINALDO VANEGAS LOPEZ",
        "file_name": "0217",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.288.769",
        "phone_number": "3117125997",
        "email": "jmgarciag@unal.edu.co"
    },
    {
        "file_date_added": "24/04/2023",
        "headline": "ROSA IMELDA LOPES DE CASTAÑO",
        "file_name": "0218",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "22.050.942",
        "phone_number": "3117481806",
        "email": " "
    },
    {
        "file_date_added": "25/04/2023",
        "headline": "ROSALBA SERNA QUINTERO",
        "file_name": "0219",
        "file_type": "LICENCIA DE MOVIENTO DE TIERRA",
        "passport": "43.419.895",
        "phone_number": "3148034402",
        "email": ""
    },
    {
        "file_date_added": "25/04/2023",
        "headline": "ROSA LUCIA ALZATE",
        "file_name": "0220",
        "file_type": "LICENCIA D SUBDIVICION",
        "passport": "32.450.567",
        "phone_number": "3205668303",
        "email": "danysanchez@gmail.com "
    },
    {
        "file_date_added": "25/04/2023",
        "headline": "GUSTAVO ADOLFO LONDOÑO ZAPATA",
        "file_name": "0221",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "70.754.267",
        "phone_number": "3218119609",
        "email": ""
    },
    {
        "file_date_added": "25/04/2023",
        "headline": "GUILLERMO DE JESUS ALZATE ALZATE",
        "file_name": "0 222",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.287.495",
        "phone_number": "3137371502",
        "email": "villasol1279@gmail.com"
    },
    {
        "file_date_added": "25/04/2023",
        "headline": "ALFREDO DE JESUS CARMONA DUQUE",
        "file_name": "0223",
        "file_type": "LICNCIA DE CONSTRUCION",
        "passport": "15.434.849",
        "phone_number": "",
        "email": ""},
    {
        "file_date_added": "25/04/2023",
        "headline": "MARYORI GOMEZ ORTIZ",
        "file_name": "0224",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "44.006.809",
        "phone_number": "3205668303",
        "email": "danysanchez@gmail.com "
    },
    {
        "file_date_added": "26/04/2023",
        "headline": "FABIO ANDRES RENDON HURTADO",
        "file_name": "0225",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "1.110.459.774",
        "phone_number": "3148314962",
        "email": " "
    },
    {
        "file_date_added": "26/04/2023",
        "headline": "  NICOLAS ANDRES FRANCO OSORIO",
        "file_name": "0226",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1.28.269.353",
        "phone_number": "3106800232",
        "email": "adrimer203@gmail.com"
    },
    {
        "file_date_added": "26/04/2023",
        "headline": "LUIS CARLOS GIRALDO GIRALDO",
        "file_name": "0227",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1.041.325.234",
        "phone_number": "3218449609",
        "email": ""
    },
    {
        "file_date_added": "26/04/2023",
        "headline": "LAURA ROSA ZAPATA GALLEGO",
        "file_name": "0228",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "22.051.089",
        "phone_number": "3106800232",
        "email": "adrimer203@gmail.com"
    },
    {
        "file_date_added": "27/04/2023",
        "headline": "LINA PATRICIA TRUJILLO RAMIREZ",
        "file_name": "0229",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "43.721.791",
        "phone_number": "3116051960",
        "email": "lptrujillo@hotmail.com"
    },
    {
        "file_date_added": "27/04/2023",
        "headline": "LUIS ALBERTO CORREA OSSA",
        "file_name": "0230",
        "file_type": "LICENCIA DE CONSTRCCIÓN",
        "passport": "71.580.691",
        "phone_number": "3017380366",
        "email": "acorreao@yahoo.es"
    },
    {
        "file_date_added": "27/04/2023",
        "headline": "ADRIANA PATRICIA CORREA LONDOÑO",
        "file_name": "0231",
        "file_type": "SOLICITUD ESTRATIFICACION",
        "passport": "43.632.531",
        "phone_number": "3136667946",
        "email": ""
    },
    {
        "file_date_added": "27/04/2023",
        "headline": "MARTIN EMILIO CARMONA LOPEZ",
        "file_name": "0232",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "70.287.032",
        "phone_number": "3054627313",
        "email": ""
    },
    {
        "file_date_added": "27/04/2023",
        "headline": "MARTHA CECILIA DIAZ RESTREPO",
        "file_name": "0233",
        "file_type": "LICENCIA DE CONSTRUCIÓN",
        "passport": "43.567.540",
        "phone_number": "3103921289",
        "email": ""
    },
    {
        "file_date_added": "27/04/2023",
        "headline": "JOSE JESUS ALZATE OCHOA",
        "file_name": "0234",
        "file_type": "LICENCIA DE DRECONOCIMIENTO Y AMPLIACION",
        "passport": "3.595.326",
        "phone_number": "3127425190",
        "email": "mmcq-margarita@yahoo.es "
    },
    {
        "file_date_added": "28/24/2023",
        "headline": "SEBASTIAN ALEJANDRO VERGARA VERGARA",
        "file_name": "0235",
        "file_type": "LICENCIA DE AMPLIACIÓN Y R.P.H",
        "passport": "1.041.326.325",
        "phone_number": "3145071799",
        "email": ""
    },
    {
        "file_date_added": "28/04/2023",
        "headline": "FLORALBA ECHEVERRY",
        "file_name": "0236",
        "file_type": "SOLICITUD DE ESTRATIFICACIÓN",
        "passport": "42.994849",
        "phone_number": "3002969084",
        "email": "NO RESPOTA"
    },
    {
        "file_date_added": "28/04/2023",
        "headline": "ARLEY DE JESUS HERNANDEZ HERRERA",
        "file_name": "0237",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.052.769",
        "phone_number": "3218514739",
        "email": ""
    },
    {
        "file_date_added": "28/04/2023",
        "headline": "MANUEL ANGEL CASTAÑO SANCHEZ",
        "file_name": "0238",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "3.595.191",
        "phone_number": "3148766116",
        "email": "helevagi@hotmail.com"
    },
    {
        "file_date_added": "29/04/2023",
        "headline": "CLAUDIA INES TOBON CORANADO",
        "file_name": "0239",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "",
        "phone_number": "",
        "email": ""},
    {
        "file_date_added": "02/05/2023",
        "headline": "URIEL DE JESUS LOPEZ SANTA",
        "file_name": "0240",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "70.289.642",
        "phone_number": "3192805965",
        "email": "uriellopezserna@gmail.com"
    },
    {
        "file_date_added": "02/05/2023",
        "headline": "ANABEL PALOMINO TUERO",
        "file_name": "0241",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "316.413",
        "phone_number": "3103764986-3005173135",
        "email": "anabelpalomino@gmail.com"
    },
    {
        "file_date_added": "02/05/2023",
        "headline": "JAIRO DE JESÚS MARÍN MARÍN",
        "file_name": "0242",
        "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO DE TIERRA",
        "passport": "70.286.700",
        "phone_number": "3164558078-1668666170",
        "email": "Eduinmarinmurillo@gmail.com "
    },
    {
        "file_date_added": "04/03/2023",
        "headline": "JORGE ELIECER ACEVEDO SANCHEZ",
        "file_name": "0243",
        "file_type": "LICENCIA DE PARCELACIÓN Y MOVIMIENTO DE TIERRA",
        "passport": "70.756.269",
        "phone_number": "3106800232",
        "email": " "
    },
    {
        "file_date_added": "04/03/2023",
        "headline": "JUAN DAVID RODRIGUEZ ARBELAEZ",
        "file_name": "0244",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.128.281",
        "phone_number": "3003867097",
        "email": "misabelarb@hotmail.com"
    },
    {
        "file_date_added": "05/05/2023",
        "headline": "JORGE DAVID PIÑEROS CALA",
        "file_name": "0245",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "80.414.360",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "05/05/2023",
        "headline": "ANA MARIA GIRALDO MARÍN",
        "file_name": "0246",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.000.415.532",
        "phone_number": "3148034402",
        "email": ""
    },
    {
        "file_date_added": "05/05/2023",
        "headline": "CARLOS MARIO ZULUAGA TOBON",
        "file_name": "0247",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "70.283.937",
        "phone_number": "3148302216",
        "email": ""
    },
    {
        "file_date_added": "06/05/2023",
        "headline": "OLGA LUCIA GALLEGO CEBALLOS",
        "file_name": "0248",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "43.856.913",
        "phone_number": "3104923263",
        "email": "NO REPORA "
    },
    {
        "file_date_added": "06/05/2023",
        "headline": "LUZ ADRIANA SUAREZ ZAPATA",
        "file_name": "0249",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "22.131.589",
        "phone_number": "3206303446",
        "email": "adran21-@hotmail.com"
    },
    {
        "file_date_added": "06/05/2023",
        "headline": "LEYDY YOHANA SANCHEZ LÓPEZ",
        "file_name": "0250",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.041.327.822",
        "phone_number": "3052053077",
        "email": "leidyJoanasanchezlopez76@gmail.com"
    },
    {
        "file_date_added": "08/05/2023",
        "headline": "LINA MARCELA ROJAS BENTANCOURT",
        "file_name": "0251",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "39.452.718",
        "phone_number": "3127946524",
        "email": " "
    },
    {
        "file_date_added": "08/05/2023",
        "headline": "LUIS ALBERTO SALAS PINEDA",
        "file_name": "0252",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "71.777.740",
        "phone_number": "3128338751",
        "email": "julianlujan63@gmail.com.com"
    },
    {
        "file_date_added": "08/05/2023",
        "headline": "JUAN DE DIOS GIRALDO GIRALDO ",
        "file_name": "0253",
        "file_type": "LICENCIA DE AMPLIACIÓN",
        "passport": "70.286.223",
        "phone_number": "3007662547",
        "email": ""
    },
    {
        "file_date_added": "08/05/2023",
        "headline": "FREDY ALEXIS CASTAÑO SIERRA",
        "file_name": "0254",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "98.532.473",
        "phone_number": "3014301221",
        "email": "efetoproyectos@gmail.com"
    },
    {
        "file_date_added": "08/05/2023",
        "headline": "YORFAN EDUARDO",
        "file_name": "0255",
        "file_type": "LICENCIA DE REVALIDACION",
        "passport": "7.320.127",
        "phone_number": "3104725225",
        "email": "yorfang@gmail.com"
    },
    {
        "file_date_added": "08/05/2023",
        "headline": "CLAUDIA INES VELEZ OCHOA",
        "file_name": "0256",
        "file_type": "LICENCIA DE MOVIMIETO DE TIERA Y CONSTRUCION",
        "passport": "43.585.244",
        "phone_number": "3205668303",
        "email": "danyAlzate0208@hotmail.com"
    },
    {
        "file_date_added": "09/05/2023",
        "headline": "ANGELA MARIA FRANCO ARANGO",
        "file_name": "0257",
        "file_type": "ACLARACIÓN  A LA RESOLUCION SP-298 AGOSTO 20211",
        "passport": "43.915.824",
        "phone_number": "3126034144",
        "email": "angelamfranco@gmail.com"
    },
    {
        "file_date_added": "09/05/2023",
        "headline": "MARCELA ROLDAN GUERRERO",
        "file_name": "0258",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "1.017.179.546",
        "phone_number": "3016645428",
        "email": "marcelita-848@hotmai.com"
    },
    {
        "file_date_added": "09/05/2023",
        "headline": "MARCELA ROLDAN GUERRERO",
        "file_name": "0259",
        "file_type": "LICENCIA DE CONSTRUCCIÓN Y MOVIMIENTO DE TIERRA",
        "passport": "1.017.179.546",
        "phone_number": "3016645428",
        "email": "marcelita-848@hotmai.com"
    },
    {
        "file_date_added": "09/05/2023",
        "headline": "JUAN ALBERTO CARDONA SANTA",
        "file_name": "0260",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "70.286.102",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "11/05/2023",
        "headline": "GLORIA EUGENIA ESPINOSA",
        "file_name": "0261",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "43.435.546",
        "phone_number": "3187355961",
        "email": ""
    },
    {
        "file_date_added": "11/05/2023",
        "headline": "DIANA MILENA BERNA BOTERO",
        "file_name": "0262",
        "file_type": "LICENCIA DE RECONOCIMIENTO",
        "passport": "39.451.876",
        "phone_number": "3205668303",
        "email": "danyAlzate0208@hotmail.com"
    },
    {
        "file_date_added": "11/05/2023",
        "headline": "MONICA MARIA ARENAS SOSA",
        "file_name": "0263",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "43.816.614",
        "phone_number": "3205668303",
        "email": "danyAlzate0208@hotmail.com"
    },
    {
        "file_date_added": "11/05/2023",
        "headline": "DORIS ANDREA GALLO CASTAÑO",
        "file_name": "0264",
        "file_type": "LICENCIA DE AMPLIACION",
        "passport": "43.856.023",
        "phone_number": "3113722368",
        "email": "Felixtorojara@gmail.com"
    },
    {
        "file_date_added": "12/05/2023",
        "headline": "RAMON AMED MONSALVE MEJÍA",
        "file_name": "0265",
        "file_type": "LICENCIA DE MODIFICACIÓN A LA RESOLUCIÓN SPO-130",
        "passport": "8.292.578",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "12/05/2023",
        "headline": "MANUEL ALEJANDRO LOPEZ SANCHEZ",
        "file_name": "0266",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "71.316.399",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "12/05/2023",
        "headline": "MANUEL JOSE VERGARA CARVAJAL",
        "file_name": "0267",
        "file_type": "LICENCIA DE SUBDIVICION",
        "passport": "3.594.610",
        "phone_number": "3116169883",
        "email": "arley362@hotmail.com"
    },
    {
        "file_date_added": "12/05/2023",
        "headline": "LUIS EDUARDO CARDONA SANCHEZ",
        "file_name": "0268",
        "file_type": "LICENCIA DE PROPIEDAD HORIZONTAL (RPH)",
        "passport": "70.290.522",
        "phone_number": "3233197362",
        "email": "sandragilcardona@hotmail.com"
    },
    {
        "file_date_added": "12/05/2023",
        "headline": "JHON ALEXANDER GI LOPEZ",
        "file_name": "0269",
        "file_type": "LICENCIA DE AMPLIACION",
        "passport": "1.035.918.498",
        "phone_number": "3205668303",
        "email": "danyAlzate0208@hotmail.com"
    },
    {
        "file_date_added": "12/05/2023",
        "headline": "SANTIAGO PEREZ GARCIA",
        "file_name": "0270",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "1.152.208.603",
        "phone_number": "3205668307",
        "email": "danyAlzate0208@hotmail.com"
    },
    {
        "file_date_added": "15/05/2023",
        "headline": "SEBASTIAN DUQUE SANCHEZ",
        "file_name": "0271",
        "file_type": "LICENCIA DE SUBDIVISÓN",
        "passport": "1.015.276.957",
        "phone_number": "3205668303",
        "email": "danyAlzate0208@hotmail.com"
    },
    {
        "file_date_added": "15/05/2023",
        "headline": "MANUEL JOSE VERGARA CARVAJAL",
        "file_name": "0272",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "3.549.610",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "15/05/2023",
        "headline": "MARTE ÑIGIA GONZALEZ MORALES",
        "file_name": "0273",
        "file_type": "LICENCIA DE SUBDIVISIÓN",
        "passport": "43.856.443",
        "phone_number": "3206325874",
        "email": ""
    },
    {
        "file_date_added": "16/05/2023",
        "headline": "GANAVOL S.A.S",
        "file_name": "0274",
        "file_type": "LICENCIA DE CONSTRUCION",
        "passport": "9013599423",
        "phone_number": "3126379470",
        "email": "ganavols.a.s@gmail.com"
    },
    {
        "file_date_added": "16/05/2023",
        "headline": "ARMANDO DE JESUS ZAPATA MARIN",
        "file_name": "0275",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y APROVACION DE PLANOS R.P.H",
        "passport": "3560839",
        "phone_number": "32055668303",
        "email": "danyAlzate 0208@hotmail.com "
    },
    {
        "file_date_added": "16/05/2023",
        "headline": "GONZALO ALBEIRO FRANCO ECHEVERRI",
        "file_name": "0276",
        "file_type": "LICENCIA DE MOVIMIENTO DE TIERRA",
        "passport": "15.427.709",
        "phone_number": "3137009572",
        "email": "gafe63@hotmail.com"
    },
    {
        "file_date_added": "17/05/2023",
        "headline": "MARINA DE JESUS SANCHEZ SANCHEZ",
        "file_name": "0277",
        "file_type": "LICENCIA DE CONDOMINIO",
        "passport": "22.051818",
        "phone_number": "3185769662",
        "email": ""
    },
    {
        "file_date_added": "17/05/2023",
        "headline": "CLAUDIA INES TOBON CORONADO",
        "file_name": "0278",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "39.276.548",
        "phone_number": "3116555553",
        "email": "nata.herrera@hotmail.com"
    },
    {
        "file_date_added": "17/05/2023",
        "headline": "LUIS FERNANDO MARIN VERGARA",
        "file_name": "0279",
        "file_type": "LICENCIA DE SUBDIVISÓN",
        "passport": "70.286.979",
        "phone_number": "3145911999",
        "email": ""
    },
    {
        "file_date_added": "17/05/2023",
        "headline": "ELSY DE JESUS ARIAS DE LOPEZ",
        "file_name": "0280",
        "file_type": "LICENCIA DE SUBSIVICION",
        "passport": "22.051.170",
        "phone_number": "3156551019",
        "email": " "
    },
    {
        "file_date_added": "17/05/2023",
        "headline": "JUAN FERNANDO MURILLO MURILLO",
        "file_name": "0281",
        "file_type": "LICENCENCIA DE RECONOCIMIENTO -AMPLIACIÓN Y R.P.H",
        "passport": "",
        "phone_number": "",
        "email": ""
    },
    {
        "file_date_added": "18/05/2023",
        "headline": "WILMAN ALONSO FRANCO OSORIO",
        "file_name": "0282",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "1.041.325.344",
        "phone_number": "3106800232",
        "email": " "
    },
    {
        "file_date_added": "18/05/2023",
        "headline": "WILLIAM ANDRES MORALES HENAO",
        "file_name": "0283",
        "file_type": "LICENCIA DE AMPLIACION",
        "passport": "1.041.324.413",
        "phone_number": "3145071799",
        "email": " "
    },
    {
        "file_date_added": "18/05/2023",
        "headline": "JUAN CARLOS MANRRIQUE CARVAJAL",
        "file_name": "0284",
        "file_type": "LICENCIA DE CONSTRUCCION",
        "passport": "16.488.548",
        "phone_number": "3144611804",
        "email": "ziomaramima@gmail.com"
    },
    {
        "file_date_added": "18/05/2023",
        "headline": "JORGE IVAN MARÍN LÓPEZ",
        "file_name": "0285",
        "file_type": "LICENCIA DE RECONOCIMIENTO Y REFORMA AL R.P.H",
        "passport": "3595659",
        "phone_number": "3205668303",
        "email": "danysanchez0208@hotmail.com"
    },
    {
        "file_date_added": "19/05/2023",
        "headline": "IGNACIO DE JESUS SANCHEZ LOPERA",
        "file_name": "0286",
        "file_type": "LICENCIA DE CONSTRUCCIÓN",
        "passport": "15.319.946",
        "phone_number": "3117271809",
        "email": ""
    }
]



for item in data:
    # print(str(item['file_name'])),
    # print(str(item['headline'])),
    # print(str(item['file_date_added'])),
    # print(str(item['file_type'])),
    # print(str(item['passport'])),
    # print(str(item['phone_number'])),
    # print(str(item['email']))
    # print("=======================")

    file_type= FileType.objects.create(name=item['file_type'])

    File.objects.create(
        file_date_added=item['file_date_added'],
        headline=item['headline'],
        file_name=item['file_name'],
        file_type= file_type,
        passport=item['passport'],
        phone_number=item['phone_number'],
        email=item['email'],
        organisation_id = 1
    )
    
    print("Succssfully Seeded the data")
