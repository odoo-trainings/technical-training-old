from odoo import api, fields, models

class Spaceship(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------
    
    _name = 'space_mission.spaceship'
    _description = "Space Mission Spaceship"
    
    # --------------------------------------- Fields Declaration ----------------------------------
    name = fields.Char(string="Name")
    active = fields.Boolean(default=True)

    # ---------------------------------------- Siemple Fields --------------------------------------
    type = fields.Selection(selection=[('freighter', 'Freighter'),
                                      ('transport', 'Transport'),
                                      ('scout_ship', 'Scout Ship'),
                                      ('fighter', 'Fighter')],
                            string='Ship Class',)
    model = fields.Char(string='Model', required = True)
    build_date = fields.Date(string='Build Date')
    captain = fields.Char(string='Captain', required = True)
    required_crew = fields.Integer(string= "Required Crew",
                                        help="Minimum number of crewmembers needed to operate the Vessel.",)
    length = fields.Float(help="Length of the Ship",)
    width = fields.Float(help="Width of the Ship",)
    height = fields.Float(help="Height of the Ship",)
    engine_number = fields.Char(string='Engine Number')
    fuel_type = fields.Selection(selection=[('solid_fuel','Solid Fuel'),
                                            ('liquid_fuel', 'Liquid Fuel')],
                                 string='Fuel Type',)