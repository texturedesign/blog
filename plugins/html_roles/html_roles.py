#
# Plugin that generates custom HTML elements with ReST roles.
#
# Based on the `html_roles` sample plugin by Aru Sahni.
# https://github.com/getnikola/plugins/tree/master/v7/html_roles
#

from docutils import nodes
from docutils.parsers.rst import roles

from nikola.plugin_categories import RestExtension

CLASSES = ['legend']


class Plugin(RestExtension):

    name = "html_roles"

    def set_site(self, site):
        self.site = site
        for role in CLASSES:
            roles.register_canonical_role(role, tag_span(role))
        return super(Plugin, self).set_site(site)


def tag_span(cls):
    """Generates a role for the specified tag."""

    def _spanning_role(role, rawtext, text, lineno, inliner,
                       options={}, content=[]):
        """reStructuredText role for generating the a span element with class."""

        element = '<span class="{cls}">{text}</span>'.format(cls=cls, text=text)
        return [nodes.raw('', element, format='html')], []

    return _spanning_role
