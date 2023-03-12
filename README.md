
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/grap/odoo-addons-company-wizard/actions/workflows/pre-commit.yml/badge.svg?branch=12.0)](https://github.com/grap/odoo-addons-company-wizard/actions/workflows/pre-commit.yml?query=branch%3A12.0)
[![Build Status](https://github.com/grap/odoo-addons-company-wizard/actions/workflows/test.yml/badge.svg?branch=12.0)](https://github.com/grap/odoo-addons-company-wizard/actions/workflows/test.yml?query=branch%3A12.0)
[![codecov](https://codecov.io/gh/grap/odoo-addons-company-wizard/branch/12.0/graph/badge.svg)](https://codecov.io/gh/grap/odoo-addons-company-wizard)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# Odoo modules that provide a wizard to create companies

 The ``company_wizard_base`` create a new menu item that provide a wizard to create a new company.
Then, all the other modules are glue module, to handle extra settings required when other modules are installed. 

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[company_wizard_account](company_wizard_account/) | 12.0.1.1.1 |  | Glue module to create companies when Account module is installed
[company_wizard_account_test](company_wizard_account_test/) | 12.0.1.1.1 |  | Module to test company_wizard_account module
[company_wizard_base](company_wizard_base/) | 12.0.1.1.3 |  | Provide Wizard to create new company more easily
[company_wizard_product](company_wizard_product/) | 12.0.1.1.1 |  | Glue module to create companies when Product module is installed

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to GRAP
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----

## About GRAP

<p align="center">
   <img src="http://www.grap.coop/wp-content/uploads/2016/11/GRAP.png" width="200"/>
</p>

GRAP, [Groupement Régional Alimentaire de Proximité](http://www.grap.coop) is a
french company which brings together activities that sale food products in the
region Rhône Alpes. We promote organic and local food, social and solidarity
economy and cooperation.

The GRAP IT Team promote Free Software and developp all the Odoo modules under
AGPL-3 Licence.

You can find all these modules here:

* on the [OCA Apps Store](https://odoo-community.org/shop?&search=GRAP)
* on the [Odoo Apps Store](https://www.odoo.com/apps/modules/browse?author=GRAP).
* on [Odoo Code Search](https://odoo-code-search.com/ocs/search?q=author%3AOCA+author%3AGRAP)

You can also take a look on the following repositories:

* [grap-odoo-incubator](https://github.com/grap/grap-odoo-incubator)
* [grap-odoo-business](https://github.com/grap/grap-odoo-business)
* [grap-odoo-business-supplier-invoice](https://github.com/grap/grap-odoo-business-supplier-invoice)
* [odoo-addons-logistics](https://github.com/grap/odoo-addons-logistics)
* [odoo-addons-cae](https://github.com/grap/odoo-addons-cae)
* [odoo-addons-intercompany-trade](https://github.com/grap/odoo-addons-intercompany-trade)
* [odoo-addons-multi-company](https://github.com/grap/odoo-addons-multi-company)
* [odoo-addons-company-wizard](https://github.com/grap/odoo-addons-company-wizard)
