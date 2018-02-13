from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from school_mgmt.serializers import *
from django.views.decorators.csrf import csrf_exempt
from school_mgmt.models import *
from rest_framework.authentication import TokenAuthentication
from random import randint


# Create your views here.
# user registration view part
@csrf_exempt
@api_view(['POST'])
def user_registration(request):
    serializer = UserRegisterSerializer(data=request.data)
    psw = request.data['password']
    re_psw = request.data['Password_confirmation']
    if psw == re_psw:
        if serializer.is_valid():
            obj = serializer.save()
            obj.set_password(request.data['password'])
            obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def user_register(request):
# 	serializer = UserRegisterSerializer(data=request.data)
# 	psw = request.data['password']
# 	re_psw = request.data['Password_confirmation']
# 	if psw == re_psw:
# 		if serializer.is_valid():
# 			obj = serializer.save()
# 			obj.set_password(request.data['password'])
# 			obj.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




# @csrf_exempt
# @api_view(['POST'])
# def user_registration(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
# 		serializer.save()
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
# 	return Response({'conformation': 'user created'}, status=status.HTTP_200_OK)



# user login view part
@csrf_exempt
@api_view(['POST'])
def user_login(request):
    serializer = UserSerializer(data=request.data)
    print "aa"
    if serializer.is_valid():
        print "bb"
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# school creat view part
@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def school_create(request):
	owner = request.user
	data = request.data
	data['owner'] = owner.id
	serializer = SchoolSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# school list view part
@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_list(request):
	if request.user.is_authenticated():
		schools = School.objects.filter(is_active=True, owner=request.user)
		serializer = SchoolSerializer(schools, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


#school details view part
@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_details(request, pk):
	if request.user.is_authenticated():
		try:
			school = School.objects.get(id=pk, owner=request.user)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

		serializer = SchoolSerializer(school, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)



# school update view part
@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def school_update(request, pk):
    if request.user.is_authenticated():
        
        try:
		    school = School.objects.get(id=pk)
        except:
		    return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SchoolSerializer(school, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_400_BAD_REQUEST)



# school delete view part
@csrf_exempt
@api_view(['DELETE'])
# @authentication_classes((TokenAuthentication,))
def school_delete(request, pk):
    # if request.user.is_authenticated():
        try:
            school = School.objects.get(id=pk)
        except:
            return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)
        school.delete()
        return Response({'success': 'School deleted successfully'}, status=status.HTTP_200_OK)




# university school count view part
#lists

# @api_view(['GET'])
# def university_list(request):
# 	print "in list"
# 	school_count = School.objects.filter(name=School.university).count()
# 	print "count"
# 	print school_count
# 	serializer = UniversityListSerializer(data=school_count)
# 	universities = University.objects.all()
# 	serializer = UniversityListSerializer(universities, many=True)
# 	#return Response(serializer.data, status=status.HTTP_200_OK)
# 	return Response({"School_count":school_count,"data":serializer.data}, status=status.HTTP_200_OK)
# @csrf_exempt
@api_view(['GET'])
# @authentication_classes((TokenAuthentication,))
def university_list1(request):
    school_count = School.objects.filter(name=School.university).count()
    # if request.user.is_authenticated():
    serializer = UniversitySerializer(data=school_count)
    universities = University.objects.all()
    serializer = UniversitySerializer(universities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # else:
    # return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)




# university public school detail list view part
# @csrf_exempt
@api_view(['GET'])
# @authentication_classes((TokenAuthentication,))
def university_list2(request):
    # if request.user.is_authenticated():
    universities = University.objects.all()
    serializer = University_SchoolsListSerializer(universities, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    # else:
    #     return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def universitywithschools_list(request):
# 	print "in list"
# 	print request.data
# 	universities = University.objects.all()
# 	serializer = UniversityWithSchoolsListSerializer(universities, many=True)
# 	return Response(serializer.data, status=status.HTTP_200_OK)






# university delete view part
@csrf_exempt
@api_view(['DELETE'])
# @authentication_classes((TokenAuthentication,))
def university_delete(request, pk):
    # if request.user.is_authenticated():
        try:
            university = University.objects.get(id=pk)
        except:
            return Response({'error': 'University id not found'}, status=status.HTTP_400_BAD_REQUEST)
        university.delete()
        return Response({'success': 'University deleted successfully'}, status=status.HTTP_200_OK)




#create

@api_view(['POST'])
def add_university(request):
	data = request.data
	serializer = UniversityCreateSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def student_create(request):
	data = request.data
	
	#1st 4 random number
	one = randint(10**(3), (10**(4)-1))
	print "Random number...   one ", randint(10**(3), (10**(4)-1))

	#2nd 2 birth date digits
	date = data['date_of_birth']
	two = date[:2]
	print "bdate...      two ", date[:2]

	#3rd 3 university's 1st 3 characters
	school_id = data['school']
	school_name = School.objects.get(id=school_id)
	university_name = school_name.university.name
	three = university_name[:3]
	print "univesity....    three ", university_name[:3]

	#4th 3 school's 1st 3 characters
	school_data = data['school']
	school_obj_name = School.objects.get(id=school_data)
	school_obj_name = school_obj_name.name
	four = school_obj_name[:3]
	print "school.....    four ", school_obj_name[:3]

	#5th 2 birth month digits
	five = date[3:5]
	print "birth month....     five ", date[3:5]

	#6th 4 birth year digits
	six = date[6:]
	print "birth year....      six", date[6:]
	
	SMARTNumber = "%s%s-%s%s-%s%s" % (one, two, three, four, five, six)
	print SMARTNumber

	serializer = StudentSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response({"Smart_number" : SMARTNumber,"Data" : serializer.data}, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











