"""Zinc models."""

from django.db import models

class Pdb(models.Model):
    """Represents a PDB structure file."""

    class Meta:
        db_table = "PDBs"

    id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=1024)
    classification = models.CharField(null=True, blank=True, max_length=1024)
    deposited = models.DateField(null=True, blank=True)
    resolution = models.FloatField(null=True, blank=True)
    organism = models.CharField(null=True, blank=True, max_length=1024)
    expression = models.CharField(null=True, blank=True, max_length=1024)
    technique = models.CharField(null=True, blank=True, max_length=1024)
    rfactor = models.FloatField(null=True, blank=True)
    skeleton = models.BooleanField()


    @staticmethod
    def create_from_atomium(pdb):
        """Creates a Pdb record from an atomium Pdb object."""
        
        from .utilities import model_is_skeleton
        return Pdb.objects.create(
         id=pdb.code, rfactor=pdb.rfactor, classification=pdb.classification,
         deposited=pdb.deposition_date, organism=pdb.organism, title=pdb.title,
         expression=pdb.expression_system, technique=pdb.technique,
         resolution=pdb.resolution, skeleton=model_is_skeleton(pdb.model),
        )



class Chain(models.Model):
    """A chain of residues in a PDB."""

    class Meta:
        db_table = "chains"

    id = models.CharField(primary_key=True, max_length=128)
    sequence = models.TextField()
    pdb = models.ForeignKey(Pdb, on_delete=models.CASCADE)


    @staticmethod
    def create_from_atomium(chain, pdb):
        """Creates a chain record from an atomium Chain object and an existing
        Pdb record."""

        return Chain.objects.create(
         id=f"{pdb.id}{chain.id}", pdb=pdb,
         sequence = "".join([res.name[0] for res in chain.residues()])
        )
