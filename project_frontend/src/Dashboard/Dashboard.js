import React from 'react';
import './Dashboard.css';
import Sidebar from '../Sidebar/Sidebar';

const Dashboard = () => {
  return (
    <Sidebar showSearchBar={true} pageName={"Dashboard"}>
      <div className="first-div">
        <div className="analysis">
          <div className="analysis-item">
            <h3>Total spent</h3>
            <p>$12,345</p>
            <button>View</button>
          </div>
          <div className="analysis-item">
            <h3>Monthly budget</h3>
            <p>$5,678</p>
            <button>Filter</button>
          </div>
          <div className="analysis-item">
            <h3>Remaining balance</h3>
            <p>$6,789</p>
            <button>Export</button>
          </div>
        </div>
      </div>
      <div className="second-div">
        <div className="expense-trends">
          <h2>Expense trends</h2>
          <button className="date-range-btn">Select date range</button>
          <table>
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
              <tr>
                <td>Last week</td>
                <td><button className="table-btn">Filter</button></td>
                <td><button className="table-btn">View</button></td>
                <td><button className="table-btn">View</button></td>
                <td><button className="table-btn">View</button></td>
              </tr>
              <tr>
                <td>This week</td>
                <td><button className="table-btn">Filter</button></td>
                <td><button className="table-btn">View</button></td>
                <td><button className="table-btn">Analyze</button></td>
                <td><button className="table-btn">Export</button></td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="expense-history">
          <h2>Expense history</h2>
          <div className="chart">
            <div className="bar" style={{ height: "20%" }}><span>Sun</span></div>
            <div className="bar" style={{ height: "40%" }}><span>Mon</span></div>
            <div className="bar" style={{ height: "60%" }}><span>Tue</span></div>
            <div className="bar" style={{ height: "10%" }}><span>Wed</span></div>
            <div className="bar" style={{ height: "15%" }}><span>Thu</span></div>
            <div className="bar" style={{ height: "80%" }}><span>Fri</span></div>
            <div className="bar" style={{ height: "50%" }}><span>Sat</span></div>
          </div>
        </div>
      </div>
      <div className="third-div">
        <div className="expense-details">
          <h3>Budget details</h3>
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
      </div>
    </Sidebar>
  );
}

export default Dashboard;
