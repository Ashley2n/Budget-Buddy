from flask import Flask, render_template, request, redirect, url_for, session

from Projects.BudgetBuddy.Logic.models.ExpenseEntry import ExpenseEntry
from Projects.BudgetBuddy.Logic.models.IncomeEntry import IncomeEntry
from Projects.BudgetBuddy.Web.forms.budgetForm import BudgetForm
from Projects.BudgetBuddy.Logic.BudgetManager import BudgetManager
from Projects.BudgetBuddy.Web.utils.customfunctions import format_price

app = Flask(__name__, template_folder='Web/templates', static_folder='Web/static')
app.secret_key = "BudgetBuddy00"

app.jinja_env.filters['format_price'] = format_price

bm = BudgetManager()

@app.route("/", methods=['GET', 'POST'])
def index():
    form = BudgetForm()
    if form.validate_on_submit():

        income = form.income_amount.data
        inc_desc = form.income_description.data
        expense = form.expense_amount.data
        exp_desc = form.expense_description.data

        income_entity = IncomeEntry(amount=income, description=inc_desc)
        expense_entity = ExpenseEntry(amount=expense, description=exp_desc)

        bm.add_income(income_entity)
        bm.add_expense(expense_entity)

        # What is a better practice for session like this how can i make it more persistence

        if session.get('income_array') is not None:
            session['income_array'] = []

            for item in bm.income:
                session['income_array'].append({"description": item.description, "amount": item.amount})
        else:
            session['income_array'] = []
            session['income_array'].append({"description": income_entity.description, "amount": income_entity.amount})

        if session.get('expense_array') is not None:
            session['expense_array'] = []

            for item in bm.expense:
                session['expense_array'].append({"description": item.description, "amount": item.amount})
        else:
            session['expense_array'] = []
            session['expense_array'].append({"description": expense_entity.description, "amount": expense_entity.amount})

        total_income = bm.get_total_income()
        total_expense = bm.get_total_expense()
        net_total = bm.get_net_total()

        session['totals'] = {"income": total_income, "expense": total_expense, "net_totals": net_total}



        # session['my_array'] = [income_entity, expense_entity]
        # session['my_array'] = [
        #     {"description": income_entity.description, "amount": income_entity.amount},
        #     {"description": expense_entity.description, "amount": expense_entity.amount}
        # ]

        return redirect(url_for('summary'))
    return render_template('index.html', form=form )

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/session_clear")
def session_clear():
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)