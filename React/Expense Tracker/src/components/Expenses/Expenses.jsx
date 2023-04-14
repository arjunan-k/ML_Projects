import './Expenses.css'
import Card from '../UI/Card'
import ExpensesFilter from './ExpensesFilter'
import { useState } from 'react';
import ExpensesList from './ExpensesList';
import ExpensesChart from './ExpensesChart';

function Expenses(props) {
    const [filteredYear, setFilteredYear] = useState('2021')

    const saveSelectedYearHandler = (year) => {
        setFilteredYear(year)
    }

    const filteredExpenses = props.expenses.filter(item => {
        return item.date.getFullYear().toString() === filteredYear
    })

    return (
        <div>
            <Card className='expenses'>
                <ExpensesFilter selected={filteredYear} onSaveSelectedYear={saveSelectedYearHandler}/>
                <ExpensesChart expenses={filteredExpenses} />
                <ExpensesList items={filteredExpenses}/>
            </Card>
        </div>
    )
}

export default Expenses