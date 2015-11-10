from openerp import models, fields, api

class wcfmc_account_import_wizard(models.TransientModel):
    _name = 'cm.wcfmc_account_import'

    @api.multi
    def import_accounts(self):
    	wcfmc = self.env['cm.cron'].get_wcfmc_instance()
        accounts = wcfmc.get_accounts()
        account_obj = self.env['cm.wcfmc_account']
        for account in accounts:
        	account_name = account[1]
        	account_wcfmc_id = account[0]
        	existing_account = account_obj.search([('wcfmc_id', '=', account_wcfmc_id)])
        	if not existing_account:
        		account_obj.create({'name': account_name, 'wcfmc_id': account_wcfmc_id})
        	else:
        		existing_account[0].name = account_name
        return True
