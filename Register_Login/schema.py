import graphene
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
    
    def resolve_user(root, info, email):
        # Querying a single user
        return Profile.objects.get(email=email)
    

# Posting Data
class CreateUserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        password = graphene.String(required=True)
        city = graphene.String(required=True)
        PhoneNumber = graphene.String(required=True)

    post = graphene.Field(ProfileType)

    @classmethod
    def mutate(cls, root, info, email, first_name, last_name, password, city, PhoneNumber,):
        post = Profile(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            city=city,
            PhoneNumber=PhoneNumber,
        )
        print(post)

        if Profile.objects.filter(email=str(post)).exists():
            print('Email Exists')
            return GraphQLError(
                message= 'User Exists')
        else:
            print('Does not Exist and created')
            post.save()
            return CreateUserMutation(post=post)
        
class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()




get_all_users_schema = graphene.Schema(query=AllUsersQuery, mutation=Mutation)
get_user_by_email_Schema = graphene.Schema(query=UserQuery)