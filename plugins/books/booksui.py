# -*- Mode: Python; coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2010 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
## Author(s):   George Y. Kussumoto      <george@async.com.br>
##

import os

import gtk

from kiwi.log import Logger

from stoqlib.database.runtime import get_connection
from stoqlib.gui.base.dialogs import run_dialog
from stoqlib.gui.events import StartApplicationEvent
from stoqlib.lib.message import info
from stoqlib.lib.translation import stoqlib_gettext

from publishersearch import PublisherSearch

_ = stoqlib_gettext
log = Logger("stoq-books-plugin")


class BooksUI(object):
    def __init__(self):
        self.conn = get_connection()
        StartApplicationEvent.connect(self._on_StartApplicationEvent)

    #
    # Private
    #

    def _add_purchase_menus(self, uimanager):
        ui_string = """<ui>
            <menubar name="menubar">
                <placeholder name="ExtraMenu">
                    <menu action="BooksMenu">
                        <menuitem action="BookSearch"/>
                        <menuitem action="Publishers"/>
                    </menu>
                </placeholder>
            </menubar>
        </ui>"""

        ag = gtk.ActionGroup('BooksMenuActions')
        ag.add_actions([
            ('BooksMenu', None, _(u'Books')),
            ('BookSearch', None, _(u'Book Search'), '<Control>B', None,
             self._on_BookSearch__activate),
            ('Publishers', None, _(u'Publishers ...'), None, None,
             self._on_Publishers__activate),
        ])

        uimanager.insert_action_group(ag, 0)
        uimanager.add_ui_from_string(ui_string)

    #
    # Accessors
    #

    #
    # Events
    #

    def _on_StartApplicationEvent(self, appname, app):
        if appname == 'purchase':
            self._add_purchase_menus(app.main_window.uimanager)

    #
    # Callbacks
    #

    def _on_BookSearch__activate(self, action):
        print self, action

    def _on_Publishers__activate(self, action):
        run_dialog(PublisherSearch, None, self.conn, hide_footer=True)
