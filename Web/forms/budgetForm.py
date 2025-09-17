from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class BudgetForm(FlaskForm):
    income_amount = IntegerField('Income Amount', validators=[DataRequired(), NumberRange(min=1, message='Income amount must be between 1 and 10')]  )
    income_description = StringField('Income Description', validators=[DataRequired(), Length(min=1, max=100, message='Income description cant be empty')] )
    expense_amount = IntegerField('Expense Amount', validators=[DataRequired(), NumberRange(min=1, message='Expense amount must be between 1 and 10')] )
    expense_description = StringField('Expense Description', validators=[DataRequired(), Length(min=1, max=100, message='Expense description cant be empty')] )
    submit = SubmitField('Submit')
