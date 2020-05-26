[![Build Status](https://travis-ci.org/odoo-cae/odoo-addons-company-wizard.svg?branch=10.0)](https://travis-ci.org/odoo-cae/odoo-addons-company-wizard)
[![codecov](https://codecov.io/gh/odoo-cae/odoo-addons-company-wizard/branch/10.0/graph/badge.svg)](https://codecov.io/gh/odoo-cae/odoo-addons-company-wizard)
[![Coverage Status](https://coveralls.io/repos/odoo-cae/odoo-addons-company-wizard/badge.png?branch=10.0)](https://coveralls.io/r/odoo-cae/odoo-addons-company-wizard?branch=10.0)
[![Code Climate](https://codeclimate.com/github/odoo-cae/odoo-addons-company-wizard/badges/gpa.svg)](https://codeclimate.com/github/odoo-cae/odoo-addons-company-wizard)


# Odoo Addons that provide a Wizard to create new companies

The ```company_wizard_base``` create a new menu item that provide a wizard
to create a new company.

then, all the other modules are glue module, to handle extra settings required
when other modules are installed.

You could be interesting too by the following repositories:

* [grap-odoo-business](https://github.com/grap/grap-odoo-business)
* [grap-odoo-custom](https://github.com/grap/grap-odoo-custom)

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[company_wizard_account](company_wizard_account/) | 10.0.1.0.0 | Glue module to create companies when Account module is installed
[company_wizard_account_test](company_wizard_account_test/) | 10.0.1.0.0 | Module to test company_wizard_account module
[company_wizard_base](company_wizard_base/) | 10.0.1.0.0 | Provide Wizard to create new companies more easily
[company_wizard_product](company_wizard_product/) | 10.0.1.0.0 | Glue module to create companies when Product module is installed
[company_wizard_report](company_wizard_report/) | 10.0.1.0.0 | Glue module to create companies when Report module is installed

[//]: # (end addons)

## About GRAP

<p align="center">
   <img src="http://www.grap.coop/wp-content/uploads/2016/11/GRAP.png" width="200"/>
</p>

GRAP, [Groupement Régional Alimentaire de Proximité](http://www.grap.coop) is a
french company which brings together activities that sale food products in the
region Rhône Alpes. We promote organic and local food, social and solidarity
economy and cooperation.

The GRAP IT Team promote Free Software and developp all the Odoo modules under
AGPL-3 Licence. You can get find all this modules here :
* on the [OCA Apps Store](https://odoo-community.org/shop?&search=GRAP)
* on the [Odoo Apps Store](https://www.odoo.com/apps/modules/browse?author=GRAP).
