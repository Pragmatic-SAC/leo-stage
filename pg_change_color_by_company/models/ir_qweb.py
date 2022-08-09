
from inspect import unwrap

from odoo import api, models, tools
from odoo.http import request

from odoo.addons.base.models.ir_qweb import IrQWeb

from .assetsbundle import AssetsBundleCompanyColor


_orig_get_asset_nodes = unwrap(IrQWeb._get_asset_nodes)


@tools.conditional(
    "xml" not in tools.config["dev_mode"],
    tools.ormcache_context(
        "xmlid",
        'options.get("lang", "en_US")',
        "css",
        "js",
        "debug",
        "async_load",
        "defer_load",
        "lazy_load",
        keys=("website_id", "active_company_id"),
    ),
)
def _get_asset_nodes__mp(
    self,
    xmlid,
    options,
    css=True,
    js=True,
    debug=False,
    async_load=False,
    defer_load=False,
    lazy_load=False,
    values=None,
):
    return _orig_get_asset_nodes(
        self,
        xmlid,
        options,
        css=css,
        js=js,
        debug=debug,
        async_load=async_load,
        defer_load=defer_load,
        lazy_load=lazy_load,
        values=values,
    )


IrQWeb._get_asset_nodes = _get_asset_nodes__mp


class QWeb(models.AbstractModel):
    _inherit = "ir.qweb"

    @api.model
    def _render(self, id_or_xml_id, values=None, **options):
        """ Adds the active company to the context """
        try:
            active_company_id = int(
                request.httprequest.cookies.get("cids", "").split(",")[0]
            )
        except Exception:
            active_company_id = False
        company_id = (
            self.env["res.company"].browse(active_company_id)
            or self.env.user.company_id
        )
        self = self.with_context(active_company_id=company_id.id)
        return super()._render(id_or_xml_id, values=values, **options)

    def _get_asset_content(self, xmlid, options):
        """ Handle 'special' web_company_color xmlid """
        if xmlid == "web_company_color.company_color_assets":
            asset = AssetsBundleCompanyColor(xmlid, [], env=self.env)
            return ([], [asset.get_company_color_asset_node()])
        return super()._get_asset_content(xmlid, options)
