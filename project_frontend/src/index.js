import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App/App';
import Settings from './Settings/Settings'
import Dashboard from './Dashboard/Dashboard'
import Add_budget from './Add_budget/Add_budget'
import Add_expense from './Add_expense/Add expense'
import View_budget from './View_budget/View_budget'
import View_expense from './View_expense/View_expense'
import Expense_list from './Expense_list/Expense_list'
import reportWebVitals from './reportWebVitals';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
  },
  {
    path: "/settings",
    element: <Settings />,
  },
  {
    path: "/add-budget",
    element: <Add_budget />,
  },
  {
    path: "/add-expense",
    element: <Add_expense />,
  },
  {
    path: "/view-budget",
    element: <View_budget />,
  },
  {
    path: "/view-expense",
    element: <View_expense />,
  },
  {
    path: "/expense-list",
    element: <Expense_list />,
  }
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
