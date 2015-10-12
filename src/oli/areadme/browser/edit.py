""" Edit views for AReadme
"""

from Products.Five import BrowserView


class AReadmeEdit(BrowserView):
    """AReadmeEdit view
    """
    def handle_edit_data(self):
        data = self.request.form.get('data')
        self.context.data = data
