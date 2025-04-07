import { Route } from 'react-router-dom';
import AuthLayout from '../layouts/AuthLayout';
import Login from '../pages/auth/Login';

const AuthRoutes = (
  <Route path="/login" element={<AuthLayout />}>
    <Route index element={<Login />} />
  </Route>
);

export default AuthRoutes;
