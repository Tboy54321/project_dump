import React from 'react';
import './Settings.css';
import Sidebar from '../Sidebar/Sidebar';
// import { Link } from "react-router-dom";

const Settings = () => {
  return (
      <Sidebar showSearchBar={false} pageName={"Settings"}>
        <div className="profile-information">
          <h2>Profile Information</h2>
          <div className="profile-details">
            <img src="user.jpg" alt="User Profile" />
            <div className="profile-text">
              <h3>John Doe</h3>
              <p>john.doe@example.com</p>
            </div>
          </div>
        </div>
        <div className="reset-password">
          <h2>Reset Password</h2>
          <form>
            <input type="password" placeholder="Current Password" />
            <input type="password" placeholder="New Password" />
            <input type="password" placeholder="Confirm New Password" />
            <button type="submit">Reset Password</button>
          </form>
        </div>
        <div className="account-deactivation">
          <h2>Account Deactivation</h2>
          <p>Warning: Deactivating your account will result in the loss of all your data.</p>
          <button className="deactivate-btn">Deactivate Account</button>
        </div>
      </Sidebar>
  );
};

export default Settings;
