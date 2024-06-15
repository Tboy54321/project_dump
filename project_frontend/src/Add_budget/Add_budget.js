import React from 'react';
import "./Add_budget.css"
import Sidebar from '../Sidebar/Sidebar';

const Add_budget = () => {
  return (
    <Sidebar showSearchBar={false} pageName={"Add Budget"}>
      <div className="budget-details">
        <div className="header">
          <h2>Budget Details</h2>
          <button className="save-btn">Save</button>
        </div>
        <p className="created-at">Created at 01/09/2023</p>
        <form className="budget-form">
          <label htmlFor="budget-name">Budget Name</label>
          <input type="text" id="budget-name" placeholder="Budget name" />

          <label htmlFor="budget-category">Category</label>
          <select id="budget-category">
            <option value="" selected>Select method</option>
            <option value="credit">Credit Card</option>
            <option value="debit">Debit Card</option>
            <option value="cash">Cash</option>
            <option value="bank">Bank Transfer</option>
          </select>

          <label htmlFor="budget-amount">Amount</label>
          <input type="text" id="budget-amount" placeholder="Budget Amount" />

          <label htmlFor="start-date">Start Date</label>
          <input type="date" id="start-date" placeholder="Start Date" />

          <label htmlFor="end-date">End Date</label>
          <input type="date" id="end-date" placeholder="End date" />
        </form>
      </div>
    </Sidebar>
  );
};

export default Add_budget;
