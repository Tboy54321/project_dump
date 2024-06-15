import React from 'react';
import './Login.css';
// import Background from "../assets/Background.svg";
// import BottomRight from "../assets/BottomRight.png"

const Login = () => {
  return (
    <div className="container">
      <div className="top-left-pic">
        <img src={"back"} alt="Top Left Overflow" />
      </div>
      <div className="login-box">
        <h1>Login</h1>
        <form>
          <div className="textbox">
            <input type="email" placeholder="Username" name="username" required />
          </div>
          <div className="textbox">
            <input type="password" placeholder="Password" name="password" required />
          </div>
          <button type="submit" className="btn">Sign In</button>
          <div className="or-separator">
            <hr />
            <span>Don't have an Account?</span>
            <hr />
          </div>
          <button type="button" className="btn">Sign Up</button>
        </form>
      </div>
      <div className="bottom-right-pic">
        <img src={"botto"} alt="Bottom Right Overflow" />
      </div>
    </div>
  );
};

export default Login;
