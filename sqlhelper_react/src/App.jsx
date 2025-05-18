import React from 'react';
import './App.css';  // 引入同目录下的 App.css 文件
import './index.css';  // 引入同目录下的 App.css 文件
import { Routes, Route, Outlet } from "react-router-dom";
import Home from "./pages/home/Home.jsx";
import Whiteboard from "./pages/whiteboard/Whiteboard.jsx";
import Sqlboard from "./pages/sqlboard/Sqlboard.jsx";
import Projectboard from "./pages/projectboard/Projectboard.jsx";
import SqlTable from "./pages/sqltable/SqlTable.jsx";
import SurfManager from "./pages/surfmanager/SurfManager.jsx";

const App = () => {
  return (
    <div className="app-container">
      <Routes>
        <Route path='/' element={< Home />}>
          {/* 首页，看板 */}
          <Route path="Whiteboard" element={ <Whiteboard/> } />  

          {/* 数据库管理页面 */}
          <Route path="Sqlboard" element={ <Sqlboard/>} />  

          {/* 项目管理页面 */}
          <Route path="Projectboard" element={ <Projectboard/>} />  

          {/* 数据表页面 */}
          <Route path="SqlTable" element={ <SqlTable />} />  

          {/* 数据表页面 */}
          <Route path="SurfManager" element={ <SurfManager />} />  
        </Route>
        
      </Routes>
    </div>
  );
};

export default App;
