import { Route } from 'react-router-dom';
import MainLayout from '../layouts/MainLayout';
import Overview from '../pages/dashboard/Overview';
import Settings from '../pages/dashboard/Settings';
import ProtectedRoute from '../components/auth/ProtectedRoute';

const DashboardRoutes = (
  <Route
    path="/dashboard"
    element={
      <ProtectedRoute>
        <MainLayout />
      </ProtectedRoute>
    }
  >
    <Route index element={<Overview />} />
    <Route path="settings" element={<Settings />} />
  </Route>
);

export default DashboardRoutes;
