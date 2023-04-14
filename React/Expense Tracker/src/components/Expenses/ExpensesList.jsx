import './ExpensesList.css'
import ExpenseItem from './ExpenseItem';

const ExpensesList = (props) => {
    let expensesContent = <p>No expenses found.</p>;

    if (props.items.length === 0) {
        return (
            <h2 className='expenses-list__fallback'>{expensesContent}</h2>
        )
    }

    return (
        <ul className='expenses-list'>
            {props.items.map(expense => {
                return (
                    <ExpenseItem 
                        key={expense.id}
                        date={expense.date} 
                        title={expense.title} 
                        amount={expense.amount} 
                    />
                )
            })}
        </ul>
    )
}

export default ExpensesList