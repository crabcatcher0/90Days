// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './components/pages/Signup';
import Login from './components/pages/Login';
import Profile from './components/pages/Profile';
import Navbar from './components/Navbar';
import { TokenProvider } from './context/TokenContext'; 
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
  return (
    <TokenProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<ProtectedRoute element={<Profile />} />} />
        </Routes>
      </Router>
    </TokenProvider>
  );
};

export default App;
