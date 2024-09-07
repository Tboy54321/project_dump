import React from 'react';
import './View_budget.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { 
  faCamera, faShoppingCart, faCreditCard, faUser, faChevronDown 
} from '@fortawesome/free-solid-svg-icons';
import Sidebar from '../Sidebar/Sidebar';

const View_budget = () => {
  return (
    <Sidebar showSearchBar={false} pageName={"Budget Overview"}>
      <h1>BUDGET SUMMARY</h1>
      <div className="top-div">
        <div className="financial-overview">
          <h2>Financial Overview</h2>
          <div className="overview-cards">
            <div className="card">
              <div className="card-icon">
                <FontAwesomeIcon icon={faCamera} />
              </div>
              <div className="card-info">
                <p>Total Expenses</p>
                <h3>$489k</h3>
                <button className="increase">Increase</button>
              </div>
            </div>
            <div className="card">
              <div className="card-icon">
                <FontAwesomeIcon icon={faShoppingCart} />
              </div>
              <div className="card-info">
                <p>Recent Purchases</p>
                <h3>$126k</h3>
                <button className="increase">Increase</button>
              </div>
            </div>
            <div className="card">
              <div className="card-icon">
                <FontAwesomeIcon icon={faCreditCard} />
              </div>
              <div className="card-info">
                <p>Available Balance</p>
                <h3>$349k</h3>
                <button className="decrease">Decrease</button>
              </div>
            </div>
            <div className="card">
              <div className="card-icon">
                <FontAwesomeIcon icon={faUser} />
              </div>
              <div className="card-info">
                <p>Active Users</p>
                <h3>79k</h3>
                <button className="increase">Increase</button>
              </div>
            </div>
          </div>
          <div className="search-period">
            <button>
              Search this week <FontAwesomeIcon icon={faChevronDown} />
            </button>
          </div>
        </div>
      </div>
      <div className="bottom-div">
        <h2>Recent Transactions</h2>
        <div className="transactions-toolbar">
          <input type="text" placeholder="Search this week's" />
          <button className="export-btn">Export as CSV</button>
        </div>
        <table className="transactions-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Category</th>
              <th>Amount</th>
              <th>Start Date</th>
              <th>End Date</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>13 Mar 2022</td>
              <td><button className="tag-btn">Tag</button></td>
              <td>
                <p>Product - 3600</p>
                <p>Transaction ID: 1943083</p>
              </td>
              <td>Total: 1382.43</td>
              <td>Profit: +744.78</td>
            </tr>
          </tbody>
        </table>
      </div>
    </Sidebar>
  );
};

export default View_budget;
