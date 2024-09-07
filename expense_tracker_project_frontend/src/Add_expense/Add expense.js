import React from 'react';
import "./Add_expense.css"
import Sidebar from '../Sidebar/Sidebar';

const Add_expense = () => {
  return (
    <Sidebar showSearchBar={false} pageName={"Add Budget"}>
      <div className="budget-details">
        <div className="header">
          <h2>Expense Entry</h2>
          <button className="save-btn">Save</button>
        </div>
        <p className="created-at">Created at 01/09/2023</p>
        <form className="budget-form">
          <label htmlFor="budget-name">Expense</label>
          <input type="text" id="budget-name" placeholder="Enter expense name" />

          <label htmlFor="budget-category">Expense Amount</label>
          <input type="text" id="budget-name" placeholder="Enter expense amount" />

          <label htmlFor="expense-category">Expense Category</label>
          <select id="budget-category">
            <option value="" selected>Select method</option>
            <option value="credit">Groceries</option>
            <option value="debit">Movies</option>
            <option value="cash">Sport</option>
            <option value="bank">Entertainment</option>
          </select>

          <label htmlFor="budget-category">Payment</label>
          <select id="budget-category">
            <option value="" selected>Select method</option>
            <option value="credit">Credit Card</option>
            <option value="debit">Debit Card</option>
            <option value="cash">Cash</option>
            <option value="bank">Bank Transfer</option>
          </select>

          <label htmlFor="start-date">Date</label>
          <input type="date" id="start-date" placeholder="Start Date" />

          <label htmlFor="description">Description</label>
          <textarea type="text" id="description" placeholder="Description" />

        </form>
      </div>
    </Sidebar>
  );
};

export default Add_expense;
