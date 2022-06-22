from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import CustomUser, Groups, News, LastWinners, Archive, DuelParticipatingNow, CommandParticipatingNow


class UserLoginSerializer(serializers.Serializer):
    """autorusation"""
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ('id',
                  'email',
                  'first_name',
                  'last_name',
                  'group',
                  'faculty')


class UserCreateSerializer(serializers.ModelSerializer):
    """Create User"""
    # company = CompanySerializer(required=False)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = True
        user.save()
        return user

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    class Meta:
        model = CustomUser
        fields = ('id',
                  'password',
                  'email',
                  'first_name',
                  'last_name',
                  'group',
                  'faculty')


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('name', 'faculty')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('date', 'title', 'text')


class LastWinnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastWinners
        fields = ('name', 'group', 'lineOne', 'lineTwo',
                  'lineThree', 'lineFour', 'lineFive')


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ('year', 'semester', 'musketeers', 'duel',
                  'groups')


class CommandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandParticipatingNow
        fields = ('name', 'group', 'firstPeople', 'secondPeople',
                  'thirdPeople', 'fourthPeople', 'fifthPeople')

    def create(self, validated_data):
        return CommandParticipatingNow.objects.create(**validated_data)


class DuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuelParticipatingNow
        fields = ('id', 'firstPeople', 'groupFirst', 'secondPeople',
                  'groupSecond', 'acceptDuel')

    def create(self, validated_data):
        return DuelParticipatingNow.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstPeople = validated_data.get('firstPeople', instance.firstPeople)
        instance.groupFirst = validated_data.get('groupFirst', instance.groupFirst)
        instance.secondPeople = validated_data.get('secondPeople', instance.secondPeople)
        instance.groupSecond = validated_data.get('groupSecond', instance.groupSecond)
        instance.acceptDuel = validated_data.get('acceptDuel', instance.acceptDuel)
        instance.save()
        return instance
