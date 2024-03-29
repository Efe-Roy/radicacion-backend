from rest_framework import serializers
from filed.models import (
    File, Agent, Category, VeriyDoc, FileType, StateType, LoggerAll, operatorObservation
)
from account.models import User
from account.api.serializers import UserSerializer, ListUserProfileSerializer


class FileTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileType
        fields = (
            'id',
            'name'
        )

class OperatorObservationMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = operatorObservation
        fields = (
            'id',
            'fileID',
            'observation',
            'createdAt'
        )

class LoggerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = LoggerAll
        fields = (
            'id',
            'msg',
            'user',
            'createdAt'
        )

    def get_user(self, obj):
        return UserSerializer(obj.user).data

class StateTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateType
        fields = (
            'id',
            'name'
        )

class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    State_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id',
            'file_name',
            'file_type',
            'headline',
            'file_date_added',
            'agent',
            'passport',
            'estate_reg',
            'phone_number',
            'email',
            'completed',
            'value_delineation',
            'delineation_date',
            'delineation_payment',
            'consecutive_delineation',
            'visited_by',
            'State_type',
            'delivery_date',
            'notification_date',
            'operator_observation',
            'organisation'
        )

    def get_file_type(self, obj):
        return FileTypeSerializer(obj.file_type).data

    def get_State_type(self, obj):
        return StateTypeSerializer(obj.State_type).data

class AgentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = ('id', 'user')

    def get_user(self, obj):
        return UserSerializer(obj.user).data
    
class AllFileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    State_type = serializers.SerializerMethodField()
    organisation = serializers.SerializerMethodField()
    agent = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = '__all__'

    def get_file_type(self, obj):
        # return FileTypeSerializer(obj.file_type).data
        return FileTypeSerializer(obj.file_type).data["name"]

    def get_State_type(self, obj):
        # return StateTypeSerializer(obj.State_type).data
        return StateTypeSerializer(obj.State_type).data["name"]
    
    def get_agent(self, obj):
        return AgentSerializer(obj.agent).data
    
    def get_organisation(self, obj):
        return ListUserProfileSerializer(obj.organisation).data


    
class CompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'completed',
        )

class OperatorObservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'operator_observation',
        )



class FileCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
            'file_name',
            'file_type',
            'headline',
            'file_date_added',
            'agent',
            'passport',
            'estate_reg',
            'phone_number',
            'email',
            'completed',
            'value_delineation',
            'delineation_date',
            'delineation_payment',
            'consecutive_delineation',
            'visited_by',
            'State_type',
            'delivery_date',
            'notification_date',
            'organisation'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'first_name', 'last_name', 'email', 'is_organisor', 'is_agent', 'is_support']

class AssignAgentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = (
            'id',
            'organisation',
            'user',
        )

    def get_user(self, obj):
        return UserSerializer(obj.user).data

class AssignFileAgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'id',
            'agent',
        )

class VeriyDocSerializer(serializers.ModelSerializer):
    # filev = serializers.SerializerMethodField()

    class Meta:
        model = VeriyDoc
        fields = (
            'id',
            'filev',
            'Copia_de_cedula_del_propietario_pasaporte',
            'Certificado_de_tradición_y_libertad',
            'Copia_de_la_escritura',
            'Paz_y_salvo_municipal',
            'Copia_del_impuesto_predial',
            'Certificado_catastral',
            'Planos_arquitectónicos_y_estructurales',
            'Planos_topográficos',
            'CD_o_USB',
            'Copia_de_la_tarjeta_profesional',
            'Formulario_único_nacional',
            'Certificado_de_delineación_y_comprobante_de_pago',
            'Viabilidad_de_energía_y_acueducto',
            'Viabilidad_de_alcantarillado_y_aseo',
            'Certificado_de_sismo_resistencia',
            'Memorias_de_calculo',
            'Estudio_de_suelos',
            'Peritaje_técnico',
            'Plan_de_majo_ambiental',
            'Plan_de_manejo_de_escombros',
            'Plan_de_manejo_de_transito',
            'Avaluó_comercial',
            'Declaración_de_antigüedad',
            'Declaración_de_no_bienes',
            'Declaración_extrajuicio_de_sana_posesión',
            'Copia_de_licencia',
            'Certificado_de_nomenclatura',
            'Certificado_del_sisben',
            'Certificado_de_desplazado',
            'Carta_de_aceptación_por_revisor',
            'Poder_autenticado',
            'Autorización_autenticada',
            'Solicitud',
            'Certificado_financiero',
            'Contrato_de_promesa_de_compraventa'
        )

    # def get_filev(self, obj):
    #     return FileSerializer(obj.filev).data

class FileDetailSerializer(serializers.ModelSerializer):
    verifys = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id',
            'file_name',
            'file_type',
            'headline',
            'file_date_added',
            'agent',
            'passport',
            'estate_reg',
            'phone_number',
            'email',
            'completed',
            'value_delineation',
            'delineation_date',
            'delineation_payment',
            'consecutive_delineation',
            'visited_by',
            'State_type',
            'delivery_date',
            'notification_date',
            'organisation',
            'verifys'
        )

    def get_verifys(self, obj):
        return VeriyDocSerializer(obj.verifys).data


class AllTrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'observation',
            'observation_date',
            'underReview',
            'underReview_date',
            'review',
            'review_date',
            'is_notified',
            'is_notified_date',
            'is_notified_observation',
            'is_personal_notified',
            'is_personal_notified_date',
            'is_personal_notified_observation',
            'correct_document',
            'correct_document_date',
            'file_name',
            'process_act_num',
            'process_act_num_date',
            'liquidation_value',
            'payment',
            'payment_status_date',
            
            'payment_receipt_number',
            'payment_receipt_date',
            'license_value',
            'delineation_tax_value',

            'payment_receipt_number2',
            'payment_receipt_date2',
            'license_value2',
            'delineation_tax_value2',

            'resolution_number',
            'resolution_date',
            'resolution_number2',
            'resolution_date2',
            'resolution_notification_date',

            'official_letter_issued',
        )

class ObservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'observation',
            'observation_date'
        )

class UnderReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'underReview',
            'underReview_date'
        )

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'review',
            'review_date'
        )

class NotifiedSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'is_notified',
            'is_notified_date',
            'is_notified_observation'
        )

class PersonalNotifiedSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'is_personal_notified',
            'is_personal_notified_date',
            'is_personal_notified_observation'
        )

class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'correct_document',
            'correct_document_date'
        )

class ActProcedureSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            # 'file_name',
            'process_act_num',
            'process_act_num_date',
            'liquidation_value'
        )

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'payment',
            'payment_status_date'
        )

class PaymentDocSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'payment_receipt_number',
            'payment_receipt_date',
            'license_value',
            'delineation_tax_value',
        )

class PaymentDocSerializer2(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'payment_receipt_number2',
            'payment_receipt_date2',
            'license_value2',
            'delineation_tax_value2',
        )

class ResolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'resolution_number',
            'resolution_date',
        )

class ResolutionSerializer2(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'resolution_number2',
            'resolution_date2',
        )

class ResolutionNotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'resolution_notification_date',
        )


class OfficialLetterIssuedSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = (
            'official_letter_issued',
        )


