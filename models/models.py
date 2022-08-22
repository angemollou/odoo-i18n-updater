# -*- coding: utf-8 -*-

from unittest import result
from odoo import models, fields, api, _
import odoo.addons.base.models.ir_translation as ir_translation
import csv
TRANSLATIONS_CSV = "./data/ir.translation.csv"
TRANSLATIONS_MODULE = "stock"
TRANSLATIONS_LANG = "fr_FR"


class odoo_testing(models.Model):
    _inherit = "stock.picking.type"

    @classmethod
    def read_csv(cls, filename):
        translations = []
        with open(filename, mode='r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                translations.append({
                    "module": row[0],
                    "type": row[1],
                    "name": row[2],
                    # "res_id": row[3],
                    "src": row[4],
                    "value": row[5],
                    "comments": row[6],
                    "lang": row[7],
                    "state": row[8],
                })
        return translations

    @api.model
    def import_translation(self):
        print("Importing FR translation for `stock` module...")
        ir_translation = self.env['ir.translation']
        trans_list = list(odoo_testing.read_csv(TRANSLATIONS_CSV))
        result = []
        for trans in trans_list:
            domain = [
                ("lang", "=", trans['lang']),
                ("src", "=", trans['src']),
                ("type", "=", trans['type']),
                # ("name", "=", trans['name']),
                # ("module", "=", trans['module']),
            ]
            record = ir_translation.search(domain)
            # Easiest way to do is to update records, recreating (unlink & create) them is harder
            result.append(record.write(trans))
        print("Done!")
