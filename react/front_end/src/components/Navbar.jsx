// src/components/Navbar.jsx
import React, { useState, useEffect, useContext } from 'react';
import {TokenContext} from '../context/TokenContext'
import { Link, useNavigate } from 'react-router-dom';
import api from '../api/axios';
import './Navbar.css';

const Navbar = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const {token}=useContext(TokenContext)
  const navigate = useNavigate();

  // console.log('This is Token: ', token);
  useEffect(() => {
    const tokens = localStorage.getItem('access_token');
    if (tokens) {
      setIsLoggedIn(true);
    } else {
      setIsLoggedIn(false);
    }
  }, []);

  const handleLogout = async () => {
    try {
      await api.post('logout', {
        refresh: localStorage.getItem('refresh_token'), // Make sure you have this in localStorage
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('access_token')}`,
        },
      });
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token'); // Clear refresh token if used
      setIsLoggedIn(false);
      window.location.href='/login';
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  return (
    <nav className="navbar">
      <ul>
        <li><Link to="/">Home</Link></li>
        {token ? (
          <>
            <li><Link to="/profile">Profile</Link></li>
            <li><button onClick={handleLogout}>Logout</button></li>
          </>
        ) : (
          <li><Link to="/signup">Sign Up</Link></li>
        )}
      </ul>
    </nav>
  );
};

export default Navbar;
