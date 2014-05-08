# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, pagination, serializers, viewsets
from rest_framework.decorators import action
from ..accounts.api import UserSerializer
from ..projects.api import BasicProjectSerializer
from .models import Comment, Todo


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        read_only_fields = ('created', 'modified',)
        fields = (
            'text',
            'created_by',
            'created',
            'modified',
        )


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    project = BasicProjectSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    comment_count = serializers.Field(source='comment_count')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        read_only_fields = (
            'id',
            'slug',
            'done_date',
            'created',
            'modified',
        )
        fields = (
            'id',
            'url',
            'project',
            'slug',
            'text',
            'due_date',
            'done',
            'done_date',
            'sort_value',
            'is_priority',
            'assigned_to',
            'created_by',
            'created',
            'modified',
            'comment_count',
            'comments',
        )


class PaginatedTodoSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = TodoSerializer


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def pre_save(self, obj):
        obj.todo = get_object_or_404(
            Todo.objects.all(),
            pk=self.args[0])
        obj.created_by_id = self.request.user.pk


class TodoViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    model = Todo
    serializer_class = TodoSerializer
    filter_fields = ('done', 'due_date', 'done_date', 'assigned_to')

    @action(['POST'])
    def addcomment(self, request, pk):
        view = CommentCreateView.as_view()
        return view(request, pk)
