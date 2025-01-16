from odoo import models, fields

class sportif(models.Model):
    _name = 'sport.sportif'
    _description = "seance sport"

    matricule = fields.Char(strint="Matricule")
    nom = fields.Char(string="Nom")
    categorie = fields.Char(string="Categorie du sportif")
    
    seance_id = fields.Many2many('calendar.event', ondelete='cascade', string="Seances")
    

    