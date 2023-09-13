from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

class CreatePersonView(generics.ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer


class RetrieveUpdatePersonView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Person.objects.all()
    serializer_class=PersonSerializer
    lookup_field='name'



class UpdatePersonByName(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'name'  # Specify 'name' as the lookup field

    def update(self, request, *args, **kwargs):
        # Get the name to update from the URL kwargs
        name_to_update = self.kwargs.get('name')
        
        try:
            # Retrieve the person by name
            person_to_update = Person.objects.get(name=name_to_update)
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the person's data
        person_to_update.name = request.data.get('new_name')
        person_to_update.age = request.data.get('new_age')
        # Update other fields as needed
        person_to_update.save()

        # Serialize and return the updated person
        updated_person_serializer = PersonSerializer(person_to_update)
        return Response(updated_person_serializer.data)
