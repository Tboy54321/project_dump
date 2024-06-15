import React from 'react';
import './Expense_list.css';
import Sidebar from '../Sidebar/Sidebar';

const Expense_list = () => {
  const expenses = [
    { name: "Food Catering", company: "McFood", amount: "€250.00", date: "09/11/2022", payment: "Not Submitted" },
    { name: "Office Supplies", company: "Officio", amount: "€150.00", date: "10/11/2022", payment: "Not Submitted" },
    { name: "Business Lunch", company: "Restaurant", amount: "€75.50", date: "11/11/2022", payment: "Not Submitted" },
    { name: "Travel Expenses", company: "Airlines", amount: "€450.25", date: "11/11/2022", payment: "Submitted" },
    { name: "Client Dinner", company: "Bistro", amount: "€120.00", date: "12/11/2022", payment: "Not Submitted" },
    { name: "Accommodation", company: "Hotel ***", amount: "€275.75", date: "16/11/2022", payment: "Submitted" },
    { name: "News Subscription", company: "NewsTimes", amount: "€30.00", date: "20/11/2022", payment: "Not Submitted" }
  ];

  return (
    <Sidebar showSearchBar={true} pageName={"Expense List"}>
        <div className="expense-overview">
            <header className="expense-header">
                <h2>Expense Overview</h2>
                <button className="add-expense-btn">Add Expense</button>
            </header>
            <table className="expense-table">
                <thead>
                <tr>
                    <th>Name</th>
                    <th>Amount</th>
                    <th>Date</th>
                    <th>Payment</th>
                    <th>Category</th>
                </tr>
                </thead>
                <tbody>
                {expenses.map((expense, index) => (
                    <tr key={index}>
                    <td>{expense.date}<br/>{expense.name}</td>
                    <td>{expense.company}</td>
                    <td>{expense.amount}</td>
                    <td>{expense.date}</td>
                    <td>{expense.payment}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    </Sidebar>
  );
}

export default Expense_list;
