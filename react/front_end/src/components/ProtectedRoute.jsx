// src/components/ProtectedRoute.jsx
import React from 'react';
import { Navigate } from 'react-router-dom';
import { useToken } from '../context/TokenContext'; 

const ProtectedRoute = ({ element }) => {
  const { token } = useToken();

  return token ? element : <Navigate to="/login" />;
};

export default ProtectedRoute;
