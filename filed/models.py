from django.db import models
from account.models import UserProfile, User


class FileManager(models.Manager):
    def get_queryset(self):
        # return super().get_queryset()
        return super().get_queryset().filter(is_deleted=False)


class File(models.Model):
    file_name = models.CharField(max_length=500)
    file_date_added = models.DateField(auto_now_add=True)
    headline = models.CharField(max_length=500, null=True, blank=True)
    passport = models.CharField(max_length=500, null=True, blank=True)
    identify_holder = models.CharField(max_length=500,  null=True, blank=True)
    estate_reg = models.CharField(null=True, blank=True, max_length=500)
    phone_number = models.CharField(null=True, blank=True, max_length=500)
    email = models.EmailField(null=True, blank=True)
    value_delineation = models.CharField(null=True, blank=True, max_length=60)
    delineation_date = models.DateField(null=True, blank=True)
    delineation_payment = models.CharField(null=True, blank=True, max_length=40)
    consecutive_delineation = models.CharField(null=True, blank=True, max_length=40)
    visited_by = models.CharField(null=True, blank=True, max_length=70)
    State_type = models.ForeignKey("StateType", null=True, blank=True, on_delete=models.SET_NULL)
    delivery_date = models.DateField(null=True, blank=True)
    notification_date = models.DateField(null=True, blank=True)

    operator_observation = models.TextField(max_length=2000, null=True, blank=True)
    # observation_list = models.ForeignKey("operatorObservation", null=True, blank=True, on_delete=models.SET_NULL)
    
    ref_code = models.CharField(max_length=500, blank=True, null=True)
    completed = models.BooleanField(default=False)

    observation = models.TextField(max_length=1000, null=True, blank=True)
    observation_date = models.DateTimeField(null=True, blank=True)

    review = models.BooleanField(default=False)
    review_date = models.DateTimeField(null=True, blank=True)

    underReview = models.BooleanField(default=False)
    underReview_date = models.DateTimeField(null=True, blank=True)

    is_notified = models.CharField(max_length=500, blank=True, null=True)
    is_notified_date = models.DateTimeField(null=True, blank=True)
    is_notified_observation = models.TextField(max_length=1000, null=True, blank=True)

    correct_document = models.CharField(max_length=500, blank=True, null=True)
    correct_document_date = models.DateTimeField(null=True, blank=True)

    process_act_num = models.CharField(max_length=500, null=True, blank=True)
    process_act_num_date = models.DateTimeField(null=True, blank=True)
    liquidation_value = models.CharField(max_length=500, null=True, blank=True)

    is_personal_notified = models.CharField(max_length=500, blank=True, null=True)
    is_personal_notified_date = models.DateTimeField(null=True, blank=True)
    is_personal_notified_observation = models.TextField(max_length=1000, null=True, blank=True)

    # payment form
    payment = models.BooleanField(default=False)
    payment_status_date = models.DateTimeField(null=True, blank=True)

    payment_receipt_number = models.CharField(max_length=500, null=True, blank=True)
    payment_receipt_date = models.DateTimeField(null=True, blank=True)
    license_value = models.CharField(max_length=500, null=True, blank=True)
    delineation_tax_value = models.CharField(max_length=500, null=True, blank=True)

    payment_receipt_number2 = models.CharField(max_length=500, null=True, blank=True)
    payment_receipt_date2 = models.DateTimeField(null=True, blank=True)
    license_value2 = models.CharField(max_length=500, null=True, blank=True)
    delineation_tax_value2 = models.CharField(max_length=500, null=True, blank=True)

    # GENERATE RESOLUTION
    resolution_number = models.CharField(max_length=500, null=True, blank=True)
    resolution_date = models.DateTimeField(null=True, blank=True)
    resolution_number2 = models.CharField(max_length=500, null=True, blank=True)
    resolution_date2 = models.DateTimeField(null=True, blank=True)
    resolution_notification_date = models.DateTimeField(null=True, blank=True)
    
    official_letter_issued = models.DateField(null=True, blank=True)

    updatedAt = models.DateField(null=True, blank=True)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    file_type = models.ForeignKey("FileType", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", related_name="files", null=True, blank=True, on_delete=models.SET_NULL)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    objects = FileManager()

    def __str__(self):
        return f"{self.file_name}"


class VeriyDoc(models.Model):
    filev = models.ForeignKey("File", related_name="verifyDoc", on_delete=models.CASCADE)

    Copia_de_cedula_del_propietario_pasaporte = models.BooleanField(default=False)
    Certificado_de_tradición_y_libertad = models.BooleanField(default=False)
    Copia_de_la_escritura = models.BooleanField(default=False)
    Paz_y_salvo_municipal = models.BooleanField(default=False)
    Copia_del_impuesto_predial = models.BooleanField(default=False)
    Certificado_catastral = models.BooleanField(default=False)
    Planos_arquitectónicos_y_estructurales = models.BooleanField(default=False)
    Planos_topográficos = models.BooleanField(default=False)
    CD_o_USB = models.BooleanField(default=False)
    Copia_de_la_tarjeta_profesional = models.BooleanField(default=False)
    Formulario_único_nacional = models.BooleanField(default=False)
    Certificado_de_delineación_y_comprobante_de_pago = models.BooleanField(default=False)
    Viabilidad_de_energía_y_acueducto  = models.BooleanField(default=False)
    Viabilidad_de_alcantarillado_y_aseo  = models.BooleanField(default=False)
    Certificado_de_sismo_resistencia  = models.BooleanField(default=False)
    Memorias_de_calculo  = models.BooleanField(default=False)
    Estudio_de_suelos  = models.BooleanField(default=False)
    Peritaje_técnico  = models.BooleanField(default=False)
    Plan_de_majo_ambiental  = models.BooleanField(default=False)
    Plan_de_manejo_de_escombros  = models.BooleanField(default=False)
    Plan_de_manejo_de_transito  = models.BooleanField(default=False)
    Avaluó_comercial  = models.BooleanField(default=False)
    Declaración_de_antigüedad   = models.BooleanField(default=False)
    Declaración_de_no_bienes   = models.BooleanField(default=False)
    Declaración_extrajuicio_de_sana_posesión   = models.BooleanField(default=False)
    Copia_de_licencia   = models.BooleanField(default=False)
    Certificado_de_nomenclatura   = models.BooleanField(default=False)
    Certificado_del_sisben   = models.BooleanField(default=False)
    Certificado_de_desplazado   = models.BooleanField(default=False)
    Carta_de_aceptación_por_revisor   = models.BooleanField(default=False)
    Poder_autenticado   = models.BooleanField(default=False)
    Autorización_autenticada    = models.BooleanField(default=False)
    Solicitud = models.BooleanField(default=False)
    Certificado_financiero    = models.BooleanField(default=False)
    Contrato_de_promesa_de_compraventa = models.BooleanField(default=False)

    # observation = models.TextField(max_length=1000, null=True, blank=True)
    # observation_date = models.DateField(null=True, blank=True)

    # review = models.BooleanField(default=False)
    # review_date = models.DateField(null=True, blank=True)

    # underReview = models.BooleanField(default=False)
    # underReview_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.filev}"


class FileType(models.Model):
    name = models.CharField(max_length=110)

    def __str__(self):
        return self.name

class operatorObservation(models.Model):
    fileID = models.ForeignKey("File", related_name="observationList", null=True, blank=True, on_delete=models.CASCADE)
    observation = models.TextField(max_length=2000, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.observation


class StateType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=30)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LoggerAll(models.Model):
    UPDATED = 'update'
    CREATE = 'create'
    DELETE = 'delete'
    EMPTY = 'empty'

    ACTION_CHOICES = (
        (UPDATED, 'update'),
        (CREATE, 'create'),
        (DELETE, 'delete'),
        (EMPTY, 'empty'),
    )

    msg = models.CharField(max_length=500)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES, default=EMPTY)
    createdAt = models.DateField(auto_now_add=True)

