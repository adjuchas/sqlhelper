# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ChangeLog(models.Model):
    target_type = models.CharField(max_length=8)
    target_id = models.IntegerField()
    action = models.CharField(max_length=6)
    description = models.TextField(blank=True, null=True)
    performed_by = models.CharField(max_length=255, blank=True, null=True)
    performed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'change_log'


class DatabaseManagement(models.Model):
    system_id = models.IntegerField()
    database_name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    surf = models.CharField(max_length=255)
    software = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'database_management'
        unique_together = (('system_id', 'database_name'),)


class FieldEnum(models.Model):
    field_id = models.IntegerField()
    enum_value = models.CharField(max_length=50)
    enum_label = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_enum'
        unique_together = (('field_id', 'enum_value'),)


class FieldManagement(models.Model):
    database_id = models.IntegerField()
    table_id = models.IntegerField()
    field_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50)
    length = models.PositiveIntegerField(blank=True, null=True)
    creator = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_null = models.CharField(max_length=1)
    is_key = models.CharField(max_length=7, blank=True, null=True)
    default_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'field_management'
        unique_together = (('table_id', 'field_name'),)


class SystemManagement(models.Model):
    system_name = models.CharField(unique=True, max_length=255)
    owner = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_management'


class TableManagement(models.Model):
    database_id = models.IntegerField()
    table_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'table_management'
        unique_together = (('database_id', 'table_name'),)