# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Databasemanagement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    database_name = models.CharField(db_column='DATABASE_NAME', unique=True, max_length=255)  # Field name made lowercase.
    system_name = models.CharField(db_column='SYSTEM_NAME', unique=True, max_length=255)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=255)  # Field name made lowercase.
    created = models.CharField(db_column='CREATED', max_length=11)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    surf = models.CharField(db_column='SURF', max_length=255)  # Field name made lowercase.
    software = models.CharField(db_column='SOFTWARE', max_length=255)  # Field name made lowercase.
    updated = models.CharField(db_column='UPDATED', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasemanagement'


class Fieldmanagement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    database_id = models.IntegerField(db_column='DATABASE_ID')  # Field name made lowercase.
    table_id = models.IntegerField(db_column='TABLE_ID')  # Field name made lowercase.
    field_name = models.CharField(db_column='FIELD_NAME', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=50)  # Field name made lowercase.
    length = models.IntegerField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=255)  # Field name made lowercase.
    created = models.CharField(db_column='CREATED', max_length=11)  # Field name made lowercase.
    updated = models.CharField(db_column='UPDATED', max_length=11)  # Field name made lowercase.
    isnull = models.CharField(db_column='ISNULL', max_length=1)  # Field name made lowercase.
    iskey = models.CharField(db_column='ISKEY', max_length=7, blank=True, null=True)  # Field name made lowercase.
    default_value = models.CharField(db_column='DEFAULT_VALUE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fieldmanagement'
        unique_together = (('table_id', 'field_name'),)


class Tablemanagement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    database_id = models.IntegerField(db_column='DATABASE_ID')  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=255)  # Field name made lowercase.
    created = models.CharField(db_column='CREATED', max_length=11)  # Field name made lowercase.
    updated = models.CharField(db_column='UPDATED', max_length=11)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tablemanagement'
        unique_together = (('database_id', 'table_name'),)
