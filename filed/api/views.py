from django.conf import settings
from django.http import Http404
from django.core.mail import send_mail
from .serializers import ( 
    FileSerializer, FileCreateSerializer, AssignAgentSerializer, AllFileSerializer,
    AssignFileAgentSerializer, VeriyDocSerializer, CompleteSerializer,
    ObservationSerializer, ReviewSerializer, DocumentSerializer, LoggerSerializer,
    ActProcedureSerializer, PaymentDocSerializer, PaymentDocSerializer2, PaymentSerializer,
    ResolutionSerializer, ResolutionNotificationSerializer, UnderReviewSerializer,
    NotifiedSerializer, PersonalNotifiedSerializer, FileTypeSerializer, AllTrackSerializer, 
    ResolutionSerializer2, OperatorObservationSerializer, OfficialLetterIssuedSerializer,
    OperatorObservationMainSerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from filed.models import File, Agent, operatorObservation, VeriyDoc, FileType, LoggerAll
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.filters import SearchFilter
from django.core.mail import EmailMessage
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from datetime import timedelta
from django.db.models import Sum, F, DecimalField, Count
from django.template.loader import render_to_string
from datetime import datetime

class FileNumView(APIView):
    def get(self, request, format=None):
        get_num_file = File.objects.all()
        year = datetime.now().year

        if get_num_file.exists():
            last_file = File.objects.all().order_by('-id')[0]

            if last_file is not None:
                string = last_file.file_name
                # Extract the numeric part from the 'process_num' field
                year_part = int(string.split('-')[-1])
                if year_part >= year:
                    parts = string.split("-")
                    number = parts[0]
                    plus_1 = int(number) + 1
                    count_str = str(plus_1).zfill(3)
                    d = f'{count_str}-{year}'
                else:
                    d = f'001-{year}'
            else:
                d = f'001-{year}'
        else:
            file_num = 1
            ed = "%03d" % ( file_num, )
            d = f'{ed}-{year}'
            # return d
        
        return Response(d)

    
class ResolutionNumView(APIView):

    def get(self, request, format=None):

        last_file = File.objects.all().order_by('-id')[0]
        if last_file.resolution_number is not None:
            file_num = int(last_file.resolution_number[3:]) + 1
            result = "OOT%05d" % ( file_num, )
            # print(result)
        else:
            print('variable stores a None value')
            file_num = 1
            result = "OOT%05d" % ( file_num, )
            print(result)

        return Response(result)

class FileSearchView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = [SearchFilter]
    search_fields = ['=file_name']


class AllVeryDocView(APIView):
    def get(self, request, format=None):

        # if VeriyDoc.objects.filter(filev = 291113):
        #     print("availabel")
        

        allVery = VeriyDoc.objects.all()
        serializerAllVery = VeriyDocSerializer(allVery, many=True)
        return Response(serializerAllVery.data)
    
class LoggerView(APIView):
    def get(self, request, format=None):
        # newDate = datetime.date.today() + datetime.timedelta(days=4)
        # print("newDate", newDate)

        loggerFiles = LoggerAll.objects.all().order_by("-id")
        count = LoggerAll.objects.count()
        # print("counte", count)
        serializerAllFile = LoggerSerializer(loggerFiles, many=True)
        return Response({
            "data": serializerAllFile.data,
            "count": count
            })

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'PageSize'
    # max_page_size = 100

class ActivityTrackerView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = (AllowAny,)
    serializer_class = LoggerSerializer
    # queryset = User.objects.all()
    queryset = LoggerAll.objects.all().order_by('-createdAt')
    pagination_class = CustomPagination

class DashboardView(APIView):
    def get(self, request, format=None):
        queryset = File.objects.all()

        # user = self.request.user
        # # queryset = File.objects.filter(agent__isnull=False)
        # if user.is_organisor:
        #     queryset = File.objects.all().order_by('-file_name')
        # else:
        #     queryset = File.objects.filter(agent__user=user).order_by('-file_name')

        State_type_counts = queryset.values('State_type__name').annotate(State_type_count=Count('State_type'))
        file_type_counts = queryset.values('file_type__name').annotate(file_type_count=Count('file_type'))
        unassigned_count = queryset.filter(agent__isnull=True).count()
        assigned_count = queryset.filter(agent__isnull=False).count()
        all_count = queryset.count()

        State_summed_counts = {}
        file_summed_counts = {}

        for item in State_type_counts:
            state_type_name = item["State_type__name"]
            state_type_count = item["State_type_count"]

            if state_type_name not in State_summed_counts:
                State_summed_counts[state_type_name] = state_type_count
            else:
                State_summed_counts[state_type_name] += state_type_count

        for itemData in file_type_counts:
            file_type_name = itemData["file_type__name"]
            file_type_count = itemData["file_type_count"]

            if file_type_name not in file_summed_counts:
                file_summed_counts[file_type_name] = file_type_count
            else:
                file_summed_counts[file_type_name] += file_type_count

        result = [{"State_type__name": state_type_name, "State_type_count": count} for state_type_name, count in State_summed_counts.items()]
        file_result = [{"file_type__name": file_type_name, "file_type_count": count} for file_type_name, count in file_summed_counts.items()]

        response_data = {
            'State_type_counts': result,
            'file_type_counts': file_result,
            'unassigned_count': unassigned_count,
            'assigned_count': assigned_count,
            'all_count': all_count
        }
        return Response(response_data)
    
class AllFileView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = AllFileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        # queryset = File.objects.all().order_by('-file_name')

        user = self.request.user
        # queryset = File.objects.filter(agent__isnull=False)
        if user.is_organisor:
            queryset = File.objects.all().order_by('-file_name')
        else:
            queryset = File.objects.filter(agent__user=user).order_by('-file_name')

        # Filter based on request parameters
        file_name = self.request.query_params.get('file_name', None)
        if file_name:
            queryset = queryset.filter(file_name__icontains=file_name)
            queryset = queryset.order_by('-file_name')
        
        file_type_id = self.request.query_params.get('file_type_id', None)
        if file_type_id:
            queryset = queryset.filter(file_type_id=file_type_id)
                
        State_type_id = self.request.query_params.get('State_type_id', None)
        if State_type_id:
            queryset = queryset.filter(State_type_id=State_type_id)
        
        estate_reg = self.request.query_params.get('estate_reg', None)
        if estate_reg:
            queryset = queryset.filter(estate_reg__icontains=estate_reg)
        
        resolution_number = self.request.query_params.get('resolution_number', None)
        if resolution_number:
            queryset = queryset.filter(resolution_number__icontains=resolution_number)
        
        resolution_number2 = self.request.query_params.get('resolution_number2', None)
        if resolution_number2:
            queryset = queryset.filter(resolution_number2__icontains=resolution_number2)
        
        passport = self.request.query_params.get('passport', None)
        if passport:
            queryset = queryset.filter(passport__icontains=passport)
        
        headline = self.request.query_params.get('headline', None)
        if headline:
            queryset = queryset.filter(headline__icontains=headline)
        
        agent_assign_status = self.request.query_params.get('agent_assign_status', None)
        if agent_assign_status is not None:
            queryset = queryset.filter(agent__isnull=not bool(agent_assign_status))
 
        return queryset.order_by('-id')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
    
        State_type_counts = queryset.values('State_type__name').annotate(State_type_count=Count('State_type'))
        file_type_counts = queryset.values('file_type__name').annotate(file_type_count=Count('file_type'))
        unassigned_count = queryset.filter(agent__isnull=True).count()
        assigned_count = queryset.filter(agent__isnull=False).count()
        all_count = queryset.count()

        State_summed_counts = {}
        file_summed_counts = {}

        for item in State_type_counts:
            state_type_name = item["State_type__name"]
            state_type_count = item["State_type_count"]

            if state_type_name not in State_summed_counts:
                State_summed_counts[state_type_name] = state_type_count
            else:
                State_summed_counts[state_type_name] += state_type_count

        for itemData in file_type_counts:
            file_type_name = itemData["file_type__name"]
            file_type_count = itemData["file_type_count"]

            if file_type_name not in file_summed_counts:
                file_summed_counts[file_type_name] = file_type_count
            else:
                file_summed_counts[file_type_name] += file_type_count

        result = [{"State_type__name": state_type_name, "State_type_count": count} for state_type_name, count in State_summed_counts.items()]
        file_result = [{"file_type__name": file_type_name, "file_type_count": count} for file_type_name, count in file_summed_counts.items()]

        # print("State_type_counts", State_type_counts)
        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response_data = {
                'results': serializer.data,
                'State_type_counts': result,
                'file_type_counts': file_result,
                'unassigned_count': unassigned_count,
                'assigned_count': assigned_count,
                'all_count': all_count
            }
            return self.get_paginated_response(response_data)

        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'results': serializer.data,
            'State_type_counts': result,
            'file_type_counts': file_result,
            'unassigned_count': unassigned_count,
            'assigned_count': assigned_count,
            'all_count': all_count
        }
        return Response(response_data)

    
class UnAssignedFileListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = FileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = File.objects.filter(agent__isnull=True)
        elif user.is_support:
            queryset = File.objects.filter(agent__isnull=True)
            # queryset = queryset.filter(agent__user=user)
        else:
            print("User Unauthorise")
            queryset = File.objects.none()
   
        queryset = queryset.order_by('-file_name')

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AssignedFileListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = FileSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = File.objects.filter(agent__isnull=False)
        elif user.is_support:
            queryset = File.objects.filter(agent__isnull=False)
        elif user.is_agent:
            queryset = File.objects.filter(agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        else:
            print("User Unauthorise")
            queryset = File.objects.none()
            

        # Filter based on request parameters
        file_name = self.request.query_params.get('file_name', None)
        if file_name:
            queryset = queryset.filter(file_name__icontains=file_name)
   
        queryset = queryset.order_by('-file_name')

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_count = queryset.count() if queryset is not None else 0

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FileListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # allFiles = File.objects.all()
        unassigned_files = File.objects.filter(agent__isnull=True)

        user = self.request.user
        # queryset = File.objects.filter(agent__isnull=False)
        if user.is_organisor:
            queryset = File.objects.filter(agent__isnull=False)
        else:
            queryset = File.objects.filter(agent__isnull=False)
            queryset = queryset.filter(agent__user=user)

        # serializerAllFile = FileSerializer(allFiles, many=True)
        serializerFile = FileSerializer(queryset, many=True)
        unassignedFile = FileSerializer(unassigned_files, many=True)

        


        # query last value of file unique number
        get_file = File.objects.all()
        if get_file.exists():
            # print("Has Data")
            # last_file = File.objects.filter(organisation=2).order_by('-id')[0]
            last_file = File.objects.all().order_by('-id')[0]
            file_num = int(last_file.file_name) + 1
            d = "%04d" % ( file_num, )
            # print(d)
        else:
            print("Empty")
            file_num = 1
            d = "%04d" % ( file_num, )
            # print(d)

        if user.is_organisor or user.is_support:
            x_id = user.userprofile.id
        else:
            x_id = ""
        
        # print("x_id", x_id)

        return Response({
            "user_id": user.id,
            "user_profile": x_id,
            "fileNum": d,
            # "all_files": serializerAllFile.data,
            "files": serializerFile.data,
            "unassigned_files": unassignedFile.data
        })

    def post(self, request, format=None):
        auto_num = self.generate_automated_number()
        print("auto_num", auto_num)

        user = self.request.user
        modified_data = request.data.copy()

        modified_data['file_name'] = auto_num
        modified_data['organisation'] = user.userprofile.id

        serializer = FileCreateSerializer(data=modified_data)
        if serializer.is_valid():
            serializer.save()

            LoggerAll.objects.create(
                msg='Se creó un nuevo archivo',
                action='create'
            )
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def generate_automated_number(cls):
        get_num_file = File.objects.all()
        year = datetime.now().year

        if get_num_file.exists():
            last_file = File.objects.all().order_by('-id')[0]

            if last_file is not None:
                string = last_file.file_name
                # Extract the numeric part from the 'process_num' field
                year_part = int(string.split('-')[-1])
                if year_part >= year:
                    parts = string.split("-")
                    number = parts[0]
                    plus_1 = int(number) + 1
                    count_str = str(plus_1).zfill(3)
                    return f'{count_str}-{year}'
                else:
                    return f'001-{year}'
            else:
                return f'001-{year}'
        else:
            file_num = 1
            ed = "%03d" % ( file_num, )
            d = f'{ed}-{year}'
            return d
        

class FileNumSearchView(APIView):
    """
    Retrieve a snippet instance.
    """
    def get_object(self, pk):
        try:
            return File.objects.get(file_name = pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = FileSerializer(filed)
        Trackserializer = AllTrackSerializer(filed)

        return Response({
            "files" : serializer.data,
            "filesTrack" : Trackserializer.data
            })


class FileDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        filed = self.get_object(pk)
        print(filed.id)

        verifyy = VeriyDoc.objects.filter(filev = filed.id)
        # verifySerializer = VeriyDocSerializer(verifyy)
        if verifyy.exists():
            # print("Has data")
            verifyy = VeriyDoc.objects.get(filev = filed.id)
            verifySerializer1 = VeriyDocSerializer(verifyy)
            verifySerializer = verifySerializer1.data
        else:
            print("No Data")
            verifySerializer = None

        serializer = FileSerializer(filed)
        return Response({
            "status": "success",
            "files" : serializer.data,
            "verify" : verifySerializer
            })

    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        user = self.request.user
        serializer = FileCreateSerializer(filed, data=request.data)
        if serializer.is_valid():
            serializer.save()

            LoggerAll.objects.create(
                msg='Se actualizó un archivo con el número ' + request.data["file_name"],
                action='update',
                user=user
            )

            # print("ffff data", request.data['State_type'])
            if request.data['State_type'] == 1:
                print("Activo")

                if not request.data['email'] == "":
                    # ====== send email notification ===== #
                    email = request.data['email']
                    subject= 'seguimiento del estado'
                    from_email= settings.EMAIL_HOST_USER
                    html_template = 'account/active_file_email.html'
                    
                    html_message = render_to_string(html_template, {
                        'radicado' : filed.file_name
                    })

                    message = EmailMessage(subject, html_message, from_email, [email])
                    message.content_subtype = 'html' # this is required because there is no plain text email version
                    message.send()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        filed = self.get_object(pk)
        # filed.delete()
        filed.is_deleted = True
        filed.save()
        return Response(status= status.HTTP_204_NO_CONTENT)

class FileDetailViewII(APIView):
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        filed = self.get_object(pk)
        print(filed.id)

        serializer = FileSerializer(filed)
        return Response(serializer.data)

class TrackDetailView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AllTrackSerializer
    queryset = File.objects.all()

class verifyDocCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticated, )
    serializer_class = VeriyDocSerializer
    queryset = VeriyDoc.objects.all()

# class verifyDocUpdateView(generics.UpdateAPIView):
#     permission_classes = (AllowAny,)
#     # permission_classes = (IsAuthenticated, )
#     serializer_class = VeriyDocSerializer
#     queryset = VeriyDoc.objects.all()


class verifyDocUpdateView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return VeriyDoc.objects.get(filev=pk)
        except VeriyDoc.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        filed = self.get_object(pk)
        
        serializer = VeriyDocSerializer(filed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = VeriyDocSerializer(filed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OperatorObservationView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = OperatorObservationSerializer
    queryset = File.objects.all()
    
class CompletedStatus(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        filed = self.get_object(pk)
        
        serializer = CompleteSerializer(filed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = CompleteSerializer(filed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class AssignAgentRetrieveView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        user = self.request.user
        queryset = Agent.objects.all()
        allAgent = AssignAgentSerializer(queryset, many=True)

        return Response( allAgent.data)

class AssignAgentView(APIView):
    authentication_classes = [TokenAuthentication]
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        user = self.request.user
        serializer = AssignFileAgentSerializer(filed, data=request.data)
        if serializer.is_valid():
            print("filed Data", request.data)
            serializer.save()
            u = Agent.objects.get(id = request.data["agent"])
            # print("u", u.user.email)
            # user = 
            LoggerAll.objects.create(
                msg='Se ha asignado un archivo con este número '+ filed.file_name,
                action='update',
                user=user
            )

            # ====== send email notification ===== #
            email = u.user.email
            subject= 'Se le ha asignado un tramite'
            from_email= settings.EMAIL_HOST_USER
            html_template = 'account/assign_agent_email.html'
            
            html_message = render_to_string(html_template, {
                'radicado' : filed.file_name
            })

            message = EmailMessage(subject, html_message, from_email, [email])
            message.content_subtype = 'html' # this is required because there is no plain text email version
            message.send()

            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class verifyDocDeleteView(generics.DestroyAPIView):
    permission_classes = (AllowAny, )
    queryset = VeriyDoc.objects.all()

class FileTypeView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = FileTypeSerializer
    queryset = FileType.objects.all()

class UnderReview(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UnderReviewSerializer
    queryset = File.objects.all()

class ReviewView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ReviewSerializer
    queryset = File.objects.all()

class ObservationView(APIView):
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = ObservationSerializer(filed, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # ====== send email notification ===== #
            email = filed.email
            subject= 'Se ha creado una observación.'
            from_email= settings.EMAIL_HOST_USER
            html_template = 'account/aobserve_email.html'
            
            html_message = render_to_string(html_template, {
                'radicado' : filed.file_name
            })

            message = EmailMessage(subject, html_message, from_email, [email])
            message.content_subtype = 'html' # this is required because there is no plain text email version
            message.send()
            

            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class NotifiedView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = NotifiedSerializer
    queryset = File.objects.all()

class DocumentView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = DocumentSerializer
    queryset = File.objects.all()

class ActProcedureView(APIView):
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = ActProcedureSerializer(filed, data=request.data)
        if serializer.is_valid():
            # print("filed Data", filed.email)
            serializer.save()

            # ============================= send email =====================================
            email = filed.email
            subject= 'Se ha creado una Ley de Procedimiento'
            from_email= settings.EMAIL_HOST_USER
            html_template = 'account/act_procedure_email.html'
            
            html_message = render_to_string(html_template, {
                'radicado' : filed.file_name,
                'liquidation_value': filed.liquidation_value
            })

            message = EmailMessage(subject, html_message, from_email, [email])
            message.content_subtype = 'html' # this is required because there is no plain text email version
            message.send()


            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class PersonalNotifiedView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PersonalNotifiedSerializer
    queryset = File.objects.all()

class PaymentView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PaymentSerializer
    queryset = File.objects.all()

class PaymentDocView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PaymentDocSerializer
    queryset = File.objects.all()

class PaymentDocView2(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PaymentDocSerializer2
    queryset = File.objects.all()

class ResolutionView(APIView):
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = ResolutionSerializer(filed, data=request.data)
        if serializer.is_valid():
            # print("filed Data", filed.email)
            serializer.save()

            # ============================= send email =====================================
            email = filed.email
            subject= 'Se genero tu resolusión'
            from_email= settings.EMAIL_HOST_USER
            html_template = 'account/aresolution_email.html'
            
            html_message = render_to_string(html_template, {
                'radicado' : filed.file_name
            })

            message = EmailMessage(subject, html_message, from_email, [email])
            message.content_subtype = 'html' # this is required because there is no plain text email version
            message.send()


            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ResolutionView2(APIView):
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = ResolutionSerializer2(filed, data=request.data)
        if serializer.is_valid():
            # print("filed Data", filed.email)
            serializer.save()

            # ============================= send email =====================================
            email = filed.email
            subject= 'Se genero tu resolusión'
            from_email= settings.EMAIL_HOST_USER
            html_template = 'account/aresolution_email.html'
            
            html_message = render_to_string(html_template, {
                'radicado' : filed.file_name
            })

            message = EmailMessage(subject, html_message, from_email, [email])
            message.content_subtype = 'html' # this is required because there is no plain text email version
            message.send()


            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class ResolutionNotificationView(generics.UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ResolutionNotificationSerializer
    queryset = File.objects.all()

class OfficialLetterIssuedView(APIView):
    def get_object(self, pk):
        try:
            return File.objects.get(id=pk)
        except File.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        filed = self.get_object(pk)
        serializer = OfficialLetterIssuedSerializer(filed, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # ============================= send email =====================================
            email = filed.email
            subject= 'Se acaba de emitir una carta oficial'
            from_email= settings.EMAIL_HOST_USER
            message= f"""
                Se acaba de emitir una carta oficial
            """
            recipient_list=[email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)


            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class OperatorObservationPostView(APIView):
    def post(self, request, format=None):
        serializer = OperatorObservationMainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class OperatorObservationGetView(APIView):
    def get(self, request, pk, format=None):
        observationFile = operatorObservation.objects.filter(fileID=pk)
        serializer = OperatorObservationMainSerializer(observationFile, many=True)
        return Response(serializer.data)

class OperatorObservationUpdateView(APIView):
    def get_object(self, pk):
        try:
            return operatorObservation.objects.get(id=pk)
        except operatorObservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = OperatorObservationMainSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = OperatorObservationMainSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
