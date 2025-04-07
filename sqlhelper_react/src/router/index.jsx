import { BrowserRouter, Routes, Route } from 'react-router-dom';
import DashboardRoutes from './dashboardRoutes';
import AuthRoutes from './authRoutes';

const AppRouter = () => (
  <BrowserRouter>
    <Routes>
      {DashboardRoutes}
      {AuthRoutes}
    </Routes>
  </BrowserRouter>
);

export default AppRouter;
