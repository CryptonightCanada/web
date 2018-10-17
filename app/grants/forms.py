# -*- coding: utf-8 -*-
"""Define the Grant forms.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
from django import forms

from grants.models import Grant, Milestone


class GrantForm(forms.ModelForm):
    """Define the Grant form logic."""

    class Meta:
        """Define the metadata for the Grant model form."""

        model = Grant
        fields = (
            'title', 'description', 'reference_url', 'admin_address', 'frequency', 'token_address', 'amount_goal',
            'transaction_hash', 'contract_address', 'network', 'admin_profile', 'logo',
        )


class MilestoneForm(forms.ModelForm):
    """Define the Milestone form logic."""

    class Meta:
        """Define the metadata for the Milestone model form."""

        model = Milestone
        fields = (
            'title', 'description', 'due_date',
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form__input', 'placeholder': 'Description'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form__input', 'placeholder': 'Date'})
        }
