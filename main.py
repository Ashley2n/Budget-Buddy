from flask import Flask, render_template, request, redirect, url_for

from LU2.BudgetBuddy.Logic.models.ExpenseEntry import ExpenseEntry
from LU2.BudgetBuddy.Logic.models.IncomeEntry import IncomeEntry
from LU2.BudgetBuddy.Web.forms.budgetForm import BudgetForm
from LU2.BudgetBuddy.Logic.BudgetManager import BudgetManager

app = Flask(__name__, template_folder='Web/templates', static_folder='Web/static')
app.secret_key = "BudgetBuddy00"

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

        budget_manager = BudgetManager()

        return redirect(url_for('success',
                                income=income,
                                inc_desc=inc_desc,
                                expense=expense,
                                exp_desc=exp_desc))
    return render_template('index.html', form=form )

@app.route("/summary")
def summary():
    return render_template("summary.html")

@app.route("/success/<income>/<inc_desc>/<expense>/<exp_desc>")
def success(income, inc_desc, expense, exp_desc):
    return render_template('displayamounts.html',
                           income=income,
                           inc_desc=inc_desc,
                           expense=expense,
                           exp_desc=exp_desc)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)