import graphene
from graphene import InputObjectType, Mutation, String
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Profile

# Getting Data
class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class AllUsersQuery(graphene.ObjectType):
    all_users = graphene.List(ProfileType)

    def resolve_all_users(self, info):
        return Profile.objects.all()
    
class UserQuery(graphene.ObjectType):
    get_user = graphene.Field(ProfileType, email = graphene.String(required=True))
    
    def resolve_get_user(root, info, email):
        # Querying a single user
        return Profile.objects.get(email=email)
    

# Posting Data
class CreateUserInput(InputObjectType):
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)
        PhoneNumber = graphene.String(required=True)

class CreateUserMutation(graphene.Mutation):
    class Arguments:
        input = CreateUserInput(required=True)

    user = graphene.Field(ProfileType)


    @classmethod
    def mutate(cls, root, info, input):
        user = Profile(
            email=input.email,
            first_name=input.first_name,
            last_name=input.last_name,
            password=input.password,
            PhoneNumber=input.PhoneNumber,
        )

        if Profile.objects.filter(email=str(user)).exists():
            print('Email Exists')
            return GraphQLError(
                message= 'User Exists')
        else:
            print('Does not Exist and created')
            print(user.last_name)
            user = Profile.objects.create_user(
                    email=user.email,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    password=user.password,
                    PhoneNumber=user.PhoneNumber
                )
            #send_activate_mail(request, user)
            return CreateUserMutation(user=user)
        
class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()




get_all_users_schema = graphene.Schema(query=AllUsersQuery, mutation=Mutation)
get_user_by_email_Schema = graphene.Schema(query=UserQuery)
create_user_schema = graphene.Schema(query=CreateUserMutation, mutation=Mutation)