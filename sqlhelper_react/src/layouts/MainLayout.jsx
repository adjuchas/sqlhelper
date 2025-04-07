import { Outlet } from 'react-router-dom';

const MainLayout = () => {
  return (
    <div>
      <header>🌐 Main Header</header>
      <main>
        <Outlet />
      </main>
    </div>
  );
};

export default MainLayout;
