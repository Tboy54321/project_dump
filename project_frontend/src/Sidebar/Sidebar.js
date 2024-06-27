import React from 'react';
import './Sidebar.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome, faWallet, faChartLine, faChevronDown, faInfoCircle, faSearch, faBell } from '@fortawesome/free-solid-svg-icons';
import { Link } from 'react-router-dom';

const Sidebar = ({ children, showSearchBar = true, pageName }) => {
  return (
    <div className="container">
      <aside className="sidebar">
        <div className="sidebar-header">
          <h2>{pageName}</h2>
        </div>
        <nav className="sidebar-nav">
          <ul>
            <li><Link to="/dashboard" className="sidebar-icons"><FontAwesomeIcon icon={faHome} className='sidebar-icons'/>Dashboard</Link></li>
            <li>
              <a href="#"><FontAwesomeIcon icon={faWallet} className='sidebar-icons'/>Expense<FontAwesomeIcon icon={faChevronDown} /></a>
              <ul className="submenu">
                <li><Link to="/add-expense">Add Expense</Link></li>
                <li><Link to="/view-expense">Expense Overview</Link></li>
                <li><Link to="/expense-list">Expense List</Link></li>
              </ul>
            </li>
            <li>
              <a href="#"><FontAwesomeIcon icon={faChartLine} className='sidebar-icons'/>Budget<FontAwesomeIcon icon={faChevronDown} /></a>
              <ul className="submenu">
                <li><Link to="/add-budget">Add Budget</Link></li>
                <li><Link to="/view-budget">Budget Overview</Link></li>
              </ul>
            </li>
            {/* <li><a href="#"><FontAwesomeIcon icon={faChartLine} className='sidebar-icons'/>Settings</a></li> */}
            <li><Link to="/settings"><FontAwesomeIcon icon={faChartLine} className='sidebar-icons'/>Settings</Link></li>
          </ul>
        </nav>
        <div className="sidebar-footer">
          <a href="#"><FontAwesomeIcon icon={faInfoCircle} className='sidebar-icons'/>Logout</a>
        </div>
      </aside>
      <main className="main-content">
        <header className="main-header">
          {showSearchBar ? (
            <div>
              <input type="text" placeholder="Search expenses" />
              <button className="search-button">
                <FontAwesomeIcon icon={faSearch} />
              </button>
           </div>
          ) : (
            <div></div>
          )}
          <div className="sub-header">
            <button className="notification">
              <Link to="/notifications">
                <FontAwesomeIcon icon={faBell} />
                <span className="notification-count">3</span>  
              </Link>
            </button>
            <div className="user-profile">
              <img src="user.jpg" alt="User Profile" />
            </div>
          </div>
        </header>
        <div className="content">
          {children}
        </div>
      </main>
    </div>
  );
};

export default Sidebar;
